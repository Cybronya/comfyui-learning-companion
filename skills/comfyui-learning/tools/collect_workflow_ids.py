#!/usr/bin/env python3
"""collect_workflow_ids.py — 从 RunningHub 搜索接口收集工作流 ID（支持增量续收，不进入详情页）。

原理：搜索页「工作流」标签的数据来自
    POST https://www.runninghub.cn/api/search/workflow
    body: {"size": 30, "current": N, "search": "<关键词>", "tags": [], "sort": "NEWEST"}
该接口无需登录，每页最多 30 条，sort=NEWEST 为网页端「最新」排序（按发布时间倒序）。

增量续收原理：
    最新流是动态的（新帖发布会把旧内容往后挤），固定页码会漂移漏收。
    因此用状态文件(state.json)记录所有已收集 ID 作为"位置锚点"：
    每次续收从第 1 页扫描，跳过已见 ID，只收集未见 ID，直到凑满目标数量。
    位置由 ID 集合天然精确定位，不怕新帖插入。

用法:
    # 从旧 txt 导入已知 ID，初始化状态库
    python collect_workflow_ids.py --import 旧批次.txt --state state.json

    # 首次收集 / 增量续收（同一命令，有 state 自动续收）
    python collect_workflow_ids.py "minimax h3" 50 批次输出.txt NEWEST --state state.json

输出: 批次 txt 每行一个新收集的 ID；state.json 记录全量已见 ID 与进度。
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

URL = "https://www.runninghub.cn/api/search/workflow"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
    "Origin": "https://www.runninghub.cn",
    "Referer": "https://www.runninghub.cn/search",
}
PAGE_SIZE = 30
MAX_PAGES = 100  # 安全上限


def load_state(state_path: Path) -> dict:
    if state_path.exists():
        return json.loads(state_path.read_text(encoding="utf-8"))
    return {"keyword": None, "sort": None, "total_on_site": 0,
            "collected_count": 0, "last_id": None, "last_publish_time": None,
            "known_ids": [], "updated_at": None}


def save_state(state_path: Path, state: dict):
    state["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def cmd_import(txt_path: Path, state_path: Path):
    state = load_state(state_path)
    ids = [line.strip() for line in txt_path.read_text(encoding="utf-8").splitlines()
           if line.strip()]
    known = set(state.get("known_ids", []))
    fresh = [i for i in ids if i not in known]
    state["known_ids"] = sorted(known | set(fresh))
    state["collected_count"] = len(state["known_ids"])
    state["last_id"] = state["known_ids"][-1] if state["known_ids"] else None
    save_state(state_path, state)
    print(f"导入 {len(fresh)} 个新 ID（跳过已存在 {len(ids) - len(fresh)} 个）")
    print(f"状态库现有 {state['collected_count']} 个 ID -> {state_path.resolve()}")


def collect_incremental(keyword: str, target: int, sort: str,
                        known: set[str]) -> tuple[list[str], dict[str, str], int, str]:
    """从第 1 页扫描，跳过已知 ID，收集未见 ID 至 target 数。"""
    new_ids: list[str] = []
    names: dict[str, str] = {}
    last_meta: str = ""       # 最后一条新收记录的发布时间
    total = 0
    current = 1
    while len(new_ids) < target and current <= MAX_PAGES:
        body = {"size": PAGE_SIZE, "current": current, "search": keyword,
                "tags": [], "sort": sort}
        data = requests.post(URL, headers=HEADERS, json=body, timeout=15).json().get("data") or {}
        recs = data.get("records") or []
        total = data.get("total", total)
        if not recs:
            break
        page_new = 0
        for rec in recs:
            rid = rec["id"]
            if rid in known or rid in names:
                continue
            names[rid] = rec.get("name", "")
            new_ids.append(rid)
            last_meta = str(rec.get("publishTime", ""))
            page_new += 1
            if len(new_ids) >= target:
                break
        current += 1
    return new_ids, names, total, last_meta


def cmd_collect(keyword: str, target: int, out_path: Path, sort: str, state_path: Path):
    state = load_state(state_path)
    known = set(state.get("known_ids", []))
    resuming = bool(known)
    if resuming:
        print(f"续收模式：状态库已有 {len(known)} 个 ID，从最新流扫描跳过已知…")

    t0 = time.time()
    new_ids, names, total, last_meta = collect_incremental(keyword, target, sort, known)
    elapsed = time.time() - t0

    if not new_ids:
        print("没有收集到新 ID（可能已全部收集，或接口无返回）。")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(new_ids) + "\n", encoding="utf-8")

    state["keyword"] = keyword
    state["sort"] = sort
    state["total_on_site"] = total
    state["known_ids"] = sorted(known | set(new_ids))
    state["collected_count"] = len(state["known_ids"])
    state["last_id"] = new_ids[-1]
    state["last_publish_time"] = last_meta or state.get("last_publish_time")
    save_state(state_path, state)

    mode = "续收" if resuming else "首次"
    print(f"[{mode}] 本次新增 {len(new_ids)} 个（{max(1, -(-len(new_ids) // PAGE_SIZE))} 次请求），耗时 {elapsed:.2f} 秒")
    print(f"进度: {state['collected_count']} / 平台总数 {total}")
    if state["last_publish_time"]:
        print(f"新位置锚点: 最后一个 ID {state['last_id']}（发布于 {state['last_publish_time'][:19]}）")
    print(f"批次输出: {out_path.resolve()}")
    print(f"状态更新: {state_path.resolve()}")
    print("--- 本批前 10 条 ---")
    for i, wid in enumerate(new_ids[:10], 1):
        print(f"  {i:2}. {wid}  {names.get(wid, '')[:40]}")
    if len(new_ids) > 10:
        print(f"  ... 其余 {len(new_ids) - 10} 个见文件")


def parse_args(args: list[str]) -> tuple[dict, list[str]]:
    """解析 '--key value' 标志对与位置参数。"""
    opts: dict[str, str] = {}
    positional: list[str] = []
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("--import", "--state", "--sort", "--out") and i + 1 < len(args):
            opts[a] = args[i + 1]
            i += 2
        else:
            positional.append(a)
            i += 1
    return opts, positional


def main() -> int:
    opts, positional = parse_args(sys.argv[1:])
    if not positional and "--import" not in opts:
        print(__doc__)
        return 1
    if "--import" in opts:
        state_path = Path(opts.get("--state", "workflow-ids-state.json"))
        cmd_import(Path(opts["--import"]), state_path)
        return 0
    keyword = positional[0]
    target = int(positional[1]) if len(positional) > 1 else 50
    out = Path(opts.get("--out", positional[2] if len(positional) > 2 else "workflow-ids.txt"))
    sort = opts.get("--sort", positional[3] if len(positional) > 3 else "NEWEST")
    state_path = Path(opts.get("--state", out.parent / "workflow-ids-state.json"))
    cmd_collect(keyword, target, out, sort, state_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
