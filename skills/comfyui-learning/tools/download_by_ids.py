#!/usr/bin/env python3
"""download_by_ids.py — 按 ID 清单批量下载 RunningHub 工作流 JSON。

流程：
    1. 读取一个或多个 ID txt（每行一个 ID）
    2. 调搜索接口建立 id -> (name, author, publishTime) 清单（manifest）
    3. 逐个 POST /api/workflow/export 下载，按 <id>.json 落盘（防同标题覆盖）
    4. 已存在的文件自动跳过（可断点续传），失败自动重试 1 次

用法:
    python download_by_ids.py <ids1.txt> [ids2.txt ...] --out <输出目录>

产出:
    <输出目录>/<名字>_<id>.json     工作流文件（名字在前便于识别，ID 后缀保证唯一）
    <输出目录>/manifest.csv         id,name,author,publishTime,file 清单
"""
from __future__ import annotations

import csv
import re
import sys
import time
from pathlib import Path

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEARCH_URL = "https://www.runninghub.cn/api/search/workflow"
EXPORT_URL = "https://www.runninghub.cn/api/workflow/export"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
    "Origin": "https://www.runninghub.cn",
    "Referer": "https://www.runninghub.cn/search",
}
DELAY = 0.4  # 每次下载间隔（秒），温和限速


def load_ids(txt_paths: list[Path]) -> list[str]:
    ids: list[str] = []
    seen: set[str] = set()
    for p in txt_paths:
        for line in p.read_text(encoding="utf-8-sig").splitlines():
            rid = line.strip()
            if rid and rid not in seen:
                seen.add(rid)
                ids.append(rid)
    return ids


def build_manifest(ids: list[str], keyword: str) -> dict[str, dict]:
    """翻搜索页建立 id->meta 映射，直到目标 ID 全覆盖或翻完。"""
    meta: dict[str, dict] = {}
    target = set(ids)
    current = 1
    while target - set(meta) and current <= 200:
        body = {"size": 30, "current": current, "search": keyword, "tags": [], "sort": "NEWEST"}
        try:
            data = requests.post(SEARCH_URL, headers=HEADERS, json=body, timeout=15).json().get("data") or {}
        except Exception:
            break
        recs = data.get("records") or []
        if not recs:
            break
        for rec in recs:
            if rec["id"] in target and rec["id"] not in meta:
                meta[rec["id"]] = {
                    "name": rec.get("name", ""),
                    "author": (rec.get("owner") or {}).get("name", ""),
                    "publishTime": rec.get("publishTime", ""),
                }
        current += 1
    return meta


BAD_CHARS = re.compile(r'[\\/:*?"<>|\r\n\t]')


def safe_name(s: str) -> str:
    """文件名安全化：替换 Windows 非法字符，截断 80 字符（与历史批次命名规则一致）。"""
    s = BAD_CHARS.sub("_", s).strip().strip(".")
    return s[:80] if s else ""


def download_one(wid: str, name: str, out_dir: Path) -> tuple[bool, str, str]:
    """下载单个工作流。返回 (成功?, 说明, 最终文件名)。按 <名字>_<id>.json 落盘。"""
    stem = safe_name(name)
    fname = f"{stem}_{wid}.json" if stem else f"{wid}.json"
    dest = out_dir / fname
    if dest.exists() and dest.stat().st_size > 0:
        return True, "已存在，跳过", fname
    for attempt in (1, 2):
        try:
            r = requests.post(EXPORT_URL, headers=HEADERS, json={"workflowId": wid}, timeout=30)
            if r.status_code == 200 and r.content:
                data = r.json()
                if not isinstance(data, dict) or "nodes" not in data:
                    return False, f"响应不是工作流 JSON（可能是错误信息: {str(data)[:80]}）", fname
                dest.write_bytes(r.content)
                return True, f"{len(r.content) // 1024} KB", fname
        except Exception as e:
            if attempt == 2:
                return False, f"异常: {e}", fname
            time.sleep(1.5)
    return False, "两次尝试均失败", fname


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    txt_paths: list[Path] = []
    out_dir = Path("workflows-json")
    i = 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            out_dir = Path(args[i + 1])
            i += 2
        else:
            txt_paths.append(Path(args[i]))
            i += 1

    ids = load_ids(txt_paths)
    print(f"读取 {len(ids)} 个唯一 ID（来自 {len(txt_paths)} 个清单文件）")

    # 用第一个清单对应的关键词建 manifest（文件名里约定包含关键词，否则用 minimax h3）
    kw = "minimax h3" if any("minimax" in p.name.lower() for p in txt_paths) else txt_paths[0].stem
    print(f"建立清单映射（搜索关键词 {kw!r}）…")
    meta = build_manifest(ids, kw)
    print(f"清单覆盖 {len(meta)}/{len(ids)} 个 ID")

    out_dir.mkdir(parents=True, exist_ok=True)
    ok = skip = fail = 0
    failures: list[tuple[str, str]] = []
    saved_files: dict[str, str] = {}
    t0 = time.time()
    for n, wid in enumerate(ids, 1):
        success, msg, fname = download_one(wid, meta.get(wid, {}).get("name", ""), out_dir)
        saved_files[wid] = fname
        if success:
            if msg == "已存在，跳过":
                skip += 1
            else:
                ok += 1
        else:
            fail += 1
            failures.append((wid, msg))
        if n % 10 == 0 or n == len(ids):
            print(f"  进度 {n}/{len(ids)}  成功 {ok}  跳过 {skip}  失败 {fail}")
        time.sleep(DELAY)

    # 写 manifest（合并模式：保留历史记录，同 id 用新数据覆盖，新记录追加在末尾）
    mf = out_dir / "manifest.csv"
    existing: dict[str, list] = {}
    if mf.exists():
        for r in list(csv.reader(open(mf, encoding="utf-8-sig")))[1:]:
            if r and r[0]:
                existing[r[0]] = r
    merged: list[list] = []
    seen_ids: set[str] = set()
    for wid in ids:  # 先按本次顺序写本次 ID
        m = meta.get(wid, {})
        merged.append([wid, m.get("name", ""), m.get("author", ""),
                       m.get("publishTime", ""), saved_files.get(wid, f"{safe_name(m.get('name',''))}_{wid}.json")])
        seen_ids.add(wid)
    for wid, r in existing.items():  # 再追加历史中不在本次范围的记录
        if wid not in seen_ids:
            merged.append(r)
            seen_ids.add(wid)
    with mf.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "author", "publishTime", "file"])
        w.writerows(merged)
    print(f"manifest 合并后共 {len(merged)} 条 -> {mf.resolve()}")

    elapsed = time.time() - t0
    print("---")
    print(f"完成：成功 {ok} + 跳过已存在 {skip} + 失败 {fail}，耗时 {elapsed:.1f} 秒")
    print(f"输出目录: {out_dir.resolve()}")
    print(f"清单文件: {mf.resolve()}")
    if failures:
        print("失败清单:")
        for wid, msg in failures:
            print(f"  {wid}  {msg}")
    return 0 if fail == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
