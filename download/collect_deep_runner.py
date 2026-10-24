"""清单深页补收 runner（2026-10-21）

为什么不用 collect_by_tag 直接跑：
- MAX_PAGES=900 顶不住 3.3 万条分类（需 ~1110 页），且单页 550 限流会
  把整轮打回零——脚本收满 target 才落盘，中途中断内存全丢。
- 2026-10-21 图生图补收连踩两次：22:10 翻到第 128 页 HTTP 550
  （EdgeOne CDN 限流），0 个新增落盘。

本 runner 复用 collect_by_tag 的接口逻辑，改三件事：
1. 单页失败指数退避重试（5/10/20/40s，共 5 次），仍失败则**先落盘再退出**；
2. 每 CHECKPOINT_EVERY 页把已收新 ID 原子写入 ids.txt + state.json（走
   engine.atomic_write，遵循 2026-10-17 原子写约定），中断不丢进度；
3. 页数上限可配（--max-pages），翻到数据尽头（空页）自动停。

断点续跑：进度记在同目录 <小类>_collect_progress.json，重跑自动从上次页码继续；
正常收满后删除该文件。

用法（仓库根）：
  python -X utf8 download/collect_deep_runner.py 图片生成/图生图 --max-pages 1200
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TOOLS = PROJECT_ROOT / "skills" / "comfyui-learning" / "tools" / "collect_by_tag.py"


def load_module():
    spec = importlib.util.spec_from_file_location("collect_by_tag", TOOLS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # 顶层无网络调用，安全
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("name", help="小类名或 父/子（同 collect_by_tag）")
    ap.add_argument("--max-pages", type=int, default=1200)
    ap.add_argument("--delay", type=float, default=0.8)
    ap.add_argument("--checkpoint-every", type=int, default=50)
    ap.add_argument("--out", default="download/ids-by-tag")
    args = ap.parse_args()

    cbt = load_module()
    sys.path.insert(0, str(PROJECT_ROOT))
    from engine.atomic_write import atomic_write_text, atomic_write_json

    tree = cbt.fetch_tree()
    items = cbt.resolve_tags(tree, args.name)
    if len(items) != 1:
        raise SystemExit(f"需要精确到单个小类，解析得到 {len(items)} 个：{items}")
    parent_name, display, tag_ids = items[0]

    base_dir = Path(args.out)
    if not base_dir.is_absolute():
        base_dir = PROJECT_ROOT / base_dir
    out_dir = base_dir / parent_name
    state_path = out_dir / f"{display}_state.json"
    ids_path = out_dir / f"{display}_ids.txt"
    meta_path = out_dir / f"{display}_meta.csv"
    prog_path = out_dir / f"{display}_collect_progress.json"

    state = cbt.load_state(state_path)
    known = set(state.get("known_ids", []))
    baseline = set(known)
    collected: dict[str, dict] = {}   # 本轮新发现（未落盘部分并入检查点）

    start_page, total = 1, int(state.get("total_on_site") or 0)
    if prog_path.exists():
        prog = json.loads(prog_path.read_text(encoding="utf-8"))
        if prog.get("tag_ids") == list(tag_ids) and prog.get("sort") == "NEWEST":
            start_page = int(prog["next_page"])
            collected = prog.get("collected", {})
            total = int(prog.get("total") or total)
            print(f"[续跑] 从第 {start_page} 页继续，已收 {len(collected)} 个新 ID", flush=True)

    def checkpoint(next_page: int, done: bool):
        all_ids = sorted(baseline | set(collected))
        atomic_write_text(ids_path, "\n".join(all_ids) + "\n")
        st = dict(state)
        st.update({"name": display, "tag_ids": tag_ids,
                   "tag_id_history": sorted(set(state.get("tag_id_history", []) or []) | set(tag_ids)),
                   "sort": "NEWEST", "total_on_site": total, "known_ids": all_ids})
        atomic_write_json(state_path, st)
        if collected:
            cbt.merge_meta_csv(meta_path, collected)
        if done:
            prog_path.unlink(missing_ok=True)
        else:
            atomic_write_json(prog_path, {"tag_ids": list(tag_ids), "sort": "NEWEST",
                                          "next_page": next_page, "total": total,
                                          "collected": collected})
        print(f"[检查点] 页 {next_page-1} 本轮累计新增 {len(collected)} 清单总量 {len(all_ids)}", flush=True)

    print(f"深页补收 {parent_name}/{display} tags={tag_ids} 从第 {start_page} 页起，"
          f"上限 {args.max_pages} 页", flush=True)
    t0 = time.time()
    current = start_page
    while current <= args.max_pages:
        body = {"size": cbt.PAGE_SIZE, "current": current, "tags": tag_ids, "sort": "NEWEST"}
        payload = None
        for attempt in range(5):
            try:
                r = cbt._post_json(cbt.LIST_URL, body, timeout=30)
                r.raise_for_status()
                payload = r.json()
                break
            except Exception as e:
                wait = 5 * (2 ** attempt)
                print(f"  第 {current} 页第 {attempt+1} 次失败：{type(e).__name__}: "
                      f"{str(e)[:100]} → 等 {wait}s 重试", flush=True)
                time.sleep(wait)
        if payload is None:
            print(f"[中止] 第 {current} 页连续 5 次失败，已落盘，可重跑续接", flush=True)
            checkpoint(current, done=False)
            return 3
        if payload.get("code") != 0:
            print(f"[中止] 接口异常 code={payload.get('code')} msg={payload.get('msg')}", flush=True)
            checkpoint(current, done=False)
            return 3
        data = payload.get("data") or {}
        recs = data.get("records") or []
        total = int(data.get("total", total) or 0)
        if not recs:
            print(f"[结束] 第 {current} 页无记录，已到达数据尽头", flush=True)
            checkpoint(current, done=True)
            print(f"本次共新增 {len(collected)} 个，耗时 {time.time()-t0:.0f}s", flush=True)
            return 0
        page_new = 0
        for rec in recs:
            rid = str(rec["id"])
            if baseline and rid in baseline or rid in collected:
                continue
            collected[rid] = {"name": rec.get("name", "") or "",
                              "author": (rec.get("owner") or {}).get("name", "")
                              if isinstance(rec.get("owner"), dict) else "",
                              "publishTime": rec.get("publishTime", "") or ""}
            page_new += 1
        if current % 20 == 0 or page_new:
            print(f"  第 {current} 页：新增 {page_new}（本轮累计 {len(collected)}）"
                  f" 平台总量 {total}", flush=True)
        if current % args.checkpoint_every == 0:
            checkpoint(current + 1, done=False)
        current += 1
        time.sleep(args.delay)

    print(f"[结束] 达到页数上限 {args.max_pages}，还有更深的页，重跑自动续接", flush=True)
    checkpoint(current, done=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
