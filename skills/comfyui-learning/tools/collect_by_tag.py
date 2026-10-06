#!/usr/bin/env python3
"""collect_by_tag.py — 从 RunningHub 工作流市场按「功能分类」收集工作流 ID（不按搜索关键字）。

接口（2026-10-06 浏览器抓包确认，勿凭猜测修改字段名）：
    分类树:  POST https://www.runninghub.cn/api/portal/tag/tree
             body {"rang":"WORKFLOW"}
             返回两级分类树：level 1 父分类（图片生成/视频生成/数字人…），
             childTags 为 level 2 子标签（文生图/图生图/反推提示词…），均含 id 与中文名。
    列表:    POST https://www.runninghub.cn/api/portal/template/list
             body {"size":30,"current":N,"tags":["<tag_id>",...],"sort":"NEWEST"}
             tags 传父分类时传其全部子标签 id（与网页点分类行为一致）；
             sort=NEWEST 按发布时间倒序；无需登录；每条记录自带
             tags / nodeCount / owner / publishTime。

产出（--out 目录下，按「大类/小类」层级组织，反映平台分类的嵌套关系）:
    <out>/<大类>/<小类>_ids.txt      该小类已收集的全部工作流 ID（每行一个，可直接喂给 download_by_ids.py）
    <out>/<大类>/<小类>_meta.csv     id,name,author,publishTime（仅供下载解析文件名与对齐 manifest，不存其他标签）
    <out>/<大类>/<小类>_state.json   增量锚点（已见 ID 集合；重跑自动续收、跳过已见）

    同一小类的清单文件只有一份：tag id 可能随平台调整变化（如 AI漫剧 下也有名为
    「视频生成」的小类），落盘文件名一律只用小类名，靠「大类/」目录隔离歧义。
    state 里记录 tag_id_history（曾用于本文件的 tag id 集合），供 ids.txt 跨 id 去重。

用法:
    python collect_by_tag.py --list                          # 列出全部 大类/小类 结构
    python collect_by_tag.py 文生图 100 --out download/ids-by-tag
    python collect_by_tag.py 文生图 200 --out download/ids-by-tag   # 续收：补足到 200
    python collect_by_tag.py 图生图 100 --out download/ids-by-tag   # 同大类下另一个小类
    python collect_by_tag.py 风格画作/热门IP 50               # 同名歧义小类用「父/子」写法消歧
    python collect_by_tag.py 图片生成/* all                  # 通配：收集该大类全部小类（数量填 all）
    python collect_by_tag.py 图片生成/文生图 图片生成/图生图 图片生成/反推提示词 100  # 等价显式写法

说明:
    - 只按小类收集（大类是嵌套分组，不是并列分类）；单独传大类名会列出其小类并拒绝，
      同名歧义（如 风格画作/热门IP 与 二次元/热门IP）用「父/子」写法。
    - 大类名与其唯一同名小类相同（数字人/音频生成/其他）时，自动按小类处理。
    - 大类名后接 /*（如 图片生成/*）表示收集该大类下全部启用小类；
      显式列举同大类多个小类也可以（位置参数写多个「父/子」名 + 一个数量）。
"""
from __future__ import annotations

import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None  # 缺席时 _post_json 走 urllib 兜底（标准库）

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TAG_TREE_URL = "https://www.runninghub.cn/api/portal/tag/tree"
LIST_URL = "https://www.runninghub.cn/api/portal/template/list"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
    "Origin": "https://www.runninghub.cn",
    "Referer": "https://www.runninghub.cn/page-workflow",
}
PAGE_SIZE = 30
MAX_PAGES = 200
DELAY = 0.4  # 翻页间隔（秒），温和限速


def _post_json(url: str, payload: dict, timeout: int = 15):
    """POST JSON 并返回 Response-like 对象（只用到 status_code / json()）。

    优先 requests；环境没有（项目约定工具只用标准库）时用 urllib 兜底，
    接口行为与抓包事实一致。"""
    try:
        import requests
        return requests.post(url, headers=HEADERS, json=payload, timeout=timeout)
    except ImportError:
        import urllib.request
        import ssl
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")
        with urllib.request.urlopen(req, timeout=timeout,
                                    context=ssl.create_default_context()) as resp:
            body = resp.read().decode("utf-8", errors="replace")

        class _Resp:
            status_code = resp.status
            def __init__(self, body):
                self._body = body
            def json(self):
                return json.loads(self._body)
            def raise_for_status(self):
                if self.status_code >= 400:
                    raise RuntimeError(f"HTTP {self.status_code}")
        return _Resp(body)


def fetch_tree() -> list[dict]:
    """拉取工作流分类树（两级）。"""
    r = _post_json(TAG_TREE_URL, {"rang": "WORKFLOW"})
    r.raise_for_status()
    payload = r.json()
    if payload.get("code") != 0:
        raise RuntimeError(f"tag/tree 返回异常: code={payload.get('code')} msg={payload.get('msg')}")
    return payload.get("data") or []


def resolve_tags(tree: list[dict], name: str) -> list[tuple[str, str, list[str]]]:
    """分类名 -> [(大类名, 小类显示名, tag id 列表), ...]。

    分类是嵌套关系：大类（图片生成…）下挂小类（文生图/图生图…）。
    - 「父/子」写法精确匹配单个小类；「父/*」收集该大类全部启用小类。
    - 只按小类收集；单独传大类名会列出其小类并拒绝。
    - 同名歧义（如 风格画作/热门IP 与 二次元/热门IP）用「父/子」写法消歧。
    """
    # 1) 「父/子」或「父/*」写法
    if "/" in name:
        p, c = name.split("/", 1)
        for cat in tree:
            if cat.get("name") != p:
                continue
            children = [ch for ch in (cat.get("childTags") or []) if ch.get("enable")]
            if c == "*":
                if not children:
                    raise SystemExit(f"大类「{p}」没有启用的子标签，无法收集。")
                return [(p, ch["name"], [ch["id"]]) for ch in children]
            for child in cat.get("childTags") or []:
                if child.get("name") == c:
                    return [(p, c, [child["id"]])]
        raise SystemExit(f"未找到「{name}」，用 --list 查看大类/小类结构。")

    # 2) 大类名：若其下有唯一同名小类则按小类处理（数字人/音频生成/其他），否则拒绝并提示 /*
    for cat in tree:
        if cat.get("name") == name:
            children = cat.get("childTags") or []
            same = [c for c in children if c.get("name") == name and c.get("enable")]
            if len(same) == 1:
                return [(name, name, [same[0]["id"]])]
            child_names = " / ".join(c.get("name", "") for c in children) or "（无子标签）"
            raise SystemExit(
                f"「{name}」是大类，不单独收集（大类=全部小类的并集，且无法按小类拆文件）。"
                f"可选：{name}/* 收集全部小类，或从 {child_names} 中指定其一")

    # 3) 唯一小类匹配
    hits: list[tuple[str, str, list[str]]] = []
    for cat in tree:
        for child in cat.get("childTags") or []:
            if child.get("name") == name and child.get("enable"):
                hits.append((cat["name"], name, [child["id"]]))
    if len(hits) == 1:
        return hits
    if len(hits) > 1:
        parents = "、".join(p for p, _, _ in hits)
        raise SystemExit(
            f"小类「{name}」在多个大类下存在（{parents}），"
            f"请用「父/子」写法消歧，如：{hits[0][0]}/{name}")

    raise SystemExit(f"未找到分类「{name}」，用 --list 查看大类/小类结构。")


def cmd_list(tree: list[dict]):
    print(f"{'父分类':<8} 子标签")
    for cat in tree:
        children = cat.get("childTags") or []
        names = " / ".join(c.get("name", "") for c in children) or "（无子标签）"
        print(f"{cat.get('name', ''):<8} {names}")


def load_state(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"name": None, "tag_ids": [], "tag_id_history": [], "sort": None,
            "total_on_site": 0, "known_ids": [], "updated_at": None}


def save_state(path: Path, state: dict):
    state["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def collect(tag_ids: list[str], target: int, sort: str,
            known: set[str]) -> tuple[list[str], dict[str, dict], int]:
    """翻页收集，跳过已见 ID，直到补足 target 个新 ID 或翻完。"""
    new_ids: list[str] = []
    meta: dict[str, dict] = {}
    total = 0
    current = 1
    while len(new_ids) < target and current <= MAX_PAGES:
        body = {"size": PAGE_SIZE, "current": current, "tags": tag_ids, "sort": sort}
        r = _post_json(LIST_URL, body)
        r.raise_for_status()
        payload = r.json()
        if payload.get("code") != 0:
            raise RuntimeError(f"template/list 返回异常: code={payload.get('code')} msg={payload.get('msg')}")
        data = payload.get("data") or {}
        recs = data.get("records") or []
        total = int(data.get("total", total) or 0)
        if not recs:
            break
        page_new = 0
        for rec in recs:
            rid = str(rec["id"])
            if rid in known or rid in meta:
                continue
            meta[rid] = {
                "name": rec.get("name", "") or "",
                "author": (rec.get("owner") or {}).get("name", "") if isinstance(rec.get("owner"), dict) else "",
                "publishTime": rec.get("publishTime", "") or "",
            }
            new_ids.append(rid)
            page_new += 1
            if len(new_ids) >= target:
                break
        print(f"  第 {current} 页：新增 {page_new}（累计新收 {len(new_ids)}/{target}）", flush=True)
        current += 1
        time.sleep(DELAY)
    return new_ids, meta, total


def merge_meta_csv(path: Path, new_meta: dict[str, dict]):
    """meta 表合并模式：已有行保留，同 id 用新数据覆盖，新行按收集顺序写在前面。"""
    existing: dict[str, list] = {}
    if path.exists():
        with open(path, encoding="utf-8-sig") as f:
            for row in list(csv.reader(f))[1:]:
                if row and row[0]:
                    existing[row[0]] = row
    merged: list[list] = []
    seen: set[str] = set()
    for rid, m in new_meta.items():
        merged.append([rid, m["name"], m["author"], m["publishTime"]])
        seen.add(rid)
    for rid, row in existing.items():
        if rid not in seen:
            merged.append(row)
            seen.add(rid)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "author", "publishTime"])
        w.writerows(merged)


def cmd_collect(parent_name: str, display: str, tag_ids: list[str],
                target: int, sort: str, base_dir: Path):
    out_dir = base_dir / parent_name          # 按「大类/小类」层级落盘
    out_dir.mkdir(parents=True, exist_ok=True)
    state_path = out_dir / f"{display}_state.json"
    ids_path = out_dir / f"{display}_ids.txt"
    meta_path = out_dir / f"{display}_meta.csv"

    state = load_state(state_path)
    known = set(state.get("known_ids", []))
    if target <= 0:  # 干跑：只验证解析与状态，不收集
        print(f"[干跑] {parent_name}/{display} tags={tag_ids}  "
              f"状态库已收集 {len(known)} 条  -> {out_dir}")
        return
    history = set(state.get("tag_id_history", []) or []) | set(state.get("tag_ids", []) or [])
    if history and not (history & set(tag_ids)):
        # 同名不同 id（如 AI漫剧 下也有「视频生成」）落到同一文件时，
        # ids.txt 必须跨 id 去重，不能清空锚点从头收。
        print(f"注意：本文件此前由 tag {sorted(history)} 收集，本次换用 {tag_ids}；"
              f"清单跨分类合并去重续收。")

    resuming = bool(known)
    if resuming:
        print(f"续收模式：状态库已有 {len(known)} 个 ID，从最新流扫描跳过已知…")

    t0 = time.time()
    new_ids, new_meta, total = collect(tag_ids, target, sort, known)
    elapsed = time.time() - t0

    if not new_ids:
        print("没有收集到新 ID（可能已全部收集，或接口无返回）。")
        return

    merge_meta_csv(meta_path, new_meta)
    all_ids = sorted(known | set(new_ids))
    ids_path.write_text("\n".join(all_ids) + "\n", encoding="utf-8")

    state.update({"name": display, "tag_ids": tag_ids,
                  "tag_id_history": sorted(history | set(tag_ids)),
                  "sort": sort,
                  "total_on_site": total, "known_ids": all_ids})
    save_state(state_path, state)

    mode = "续收" if resuming else "首次"
    print(f"[{mode}] 本次新增 {len(new_ids)} 个（{max(1, -(-len(new_ids) // PAGE_SIZE))} 次请求），耗时 {elapsed:.2f} 秒")
    print(f"进度: {len(all_ids)} / 平台总量 {total}")
    print(f"ID 清单（全量 {len(all_ids)} 条）: {ids_path.resolve()}")
    print(f"meta 表（id/名称/作者/发布时间）: {meta_path.resolve()}")
    print(f"状态: {state_path.resolve()}")
    print("--- 本批前 10 条 ---")
    for i, rid in enumerate(new_ids[:10], 1):
        m = new_meta[rid]
        print(f"  {i:2}. {rid}  {m['name'][:40]}")


def main() -> int:
    args = sys.argv[1:]
    tree = fetch_tree()
    if "--list" in args:
        cmd_list(tree)
        return 0

    opts: dict[str, str] = {}
    positional: list[str] = []
    i = 0
    while i < len(args):
        if args[i] in ("--out", "--sort") and i + 1 < len(args):
            opts[args[i]] = args[i + 1]
            i += 2
        else:
            positional.append(args[i])
            i += 1

    # 位置参数：一个或多个分类名 + 可选数量（纯数字，缺省 100；all = 全部翻完）
    names = [x for x in positional if not x.isdigit() and x.lower() != "all"]
    targets = [int(x) for x in positional if x.isdigit()]
    unlimited = any(x.lower() == "all" for x in positional)
    if not names:
        print(__doc__)
        return 1
    if len(targets) > 1:
        raise SystemExit("数量参数只能有一个。")
    if unlimited and targets:
        raise SystemExit("数量不能同时写 all 和数字，二选一（all = 全部翻完）。")
    target = -1 if unlimited else (targets[0] if targets else 100)
    sort = opts.get("--sort", "NEWEST")
    base_dir = Path(opts.get("--out", "download/ids-by-tag"))

    # 先解析全部名称并展开（大类/* → 多个小类），再按「大类+小类」去重，
    # 避免显式列举与通配混用时同一小类被收集两次
    resolved: list[tuple[str, str, list[str]]] = []
    seen_keys: set[tuple[str, str]] = set()
    for name in names:
        for item in resolve_tags(tree, name):
            key = (item[0], item[1])
            if key in seen_keys:
                continue
            seen_keys.add(key)
            resolved.append(item)

    for parent_name, display, tag_ids in resolved:
        print(f"小类「{display}」（大类「{parent_name}」）-> tags={tag_ids}")
        cmd_collect(parent_name, display, tag_ids, target, sort, base_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
