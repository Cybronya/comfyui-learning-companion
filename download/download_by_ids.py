#!/usr/bin/env python3
"""download_by_ids.py — 按 ID 清单批量下载 RunningHub 工作流 JSON（标准库版）。

流程：
    1. 读取一个或多个 ID txt（每行一个 ID）
    2. 调搜索接口建立 id -> (name, author, publishTime) 清单（manifest）
    3. 逐个 POST /api/workflow/export 下载，按 <id>.json 落盘（防同标题覆盖）
    4. 已存在的文件自动跳过（可断点续传），失败自动重试 1 次

用法:
    # 按关键词搜索建 manifest
    python download_by_ids.py <ids1.txt> [ids2.txt ...] --out <输出目录> --keyword <关键词>

    # 按分类 tag_id 搜索建 manifest（推荐，精确筛选）
    python download_by_ids.py <ids1.txt> [ids2.txt ...] --out <输出目录> --tag-id <tag_id>

产出:
    <输出目录>/<名字>_<id>.json     工作流文件（名字在前便于识别，ID 后缀保证唯一）
    <输出目录>/manifest.csv         id,name,author,publishTime,file 清单
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

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
PAGE_SIZE = 30


def api_post(url: str, body: dict, timeout: int = 15) -> dict:
    """发送 POST 请求并返回 JSON dict（搜索接口用）。"""
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", "replace")[:200]
        return {"_error": f"HTTP {e.code}: {err_body}"}
    except Exception as e:
        return {"_error": str(e)}


def api_export(wid: str, timeout: int = 30) -> tuple[bool, bytes]:
    """下载工作流 JSON（二进制）。返回 (成功?, 内容bytes)。"""
    body = json.dumps({"workflowId": wid}).encode("utf-8")
    req = urllib.request.Request(EXPORT_URL, data=body, headers=HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
            if resp.status == 200 and content:
                return True, content
            return False, b""
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", "replace")[:200]
        print(f"    export HTTP {e.code}: {err_body}")
        return False, b""
    except Exception as e:
        print(f"    export 异常: {e}")
        return False, b""


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


def build_manifest(ids: list[str], tag_id: str | None = None,
                   keyword: str = "") -> dict[str, dict]:
    """翻搜索页建立 id->meta 映射，直到目标 ID 全覆盖或翻完。

    优先用 tag_id 筛选（tags 参数），否则用 keyword 关键词搜索。
    """
    meta: dict[str, dict] = {}
    target = set(ids)
    current = 1
    max_pages = 200
    while target - set(meta) and current <= max_pages:
        if tag_id:
            body = {"size": PAGE_SIZE, "current": current, "search": "",
                    "tags": [tag_id], "sort": "NEWEST"}
        else:
            body = {"size": PAGE_SIZE, "current": current, "search": keyword,
                    "tags": [], "sort": "NEWEST"}
        r = api_post(SEARCH_URL, body)
        if "_error" in r:
            print(f"    manifest 搜索失败: {r['_error']}")
            break
        data = r.get("data") or {}
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
        ok, content = api_export(wid)
        if ok:
            try:
                data = json.loads(content)
                if not isinstance(data, dict) or "nodes" not in data:
                    return False, f"响应不是工作流 JSON（可能是错误信息: {str(data)[:80]}）", fname
                dest.write_bytes(content)
                return True, f"{len(content) // 1024} KB", fname
            except json.JSONDecodeError:
                return False, "响应不是合法 JSON", fname
        if attempt == 2:
            return False, "两次尝试均失败", fname
        time.sleep(1.5)
    return False, "两次尝试均失败", fname


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    txt_paths: list[Path] = []
    out_dir = Path("workflows-json")
    tag_id = None
    keyword = ""
    i = 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            out_dir = Path(args[i + 1])
            i += 2
        elif args[i] == "--tag-id" and i + 1 < len(args):
            tag_id = args[i + 1]
            i += 2
        elif args[i] == "--keyword" and i + 1 < len(args):
            keyword = args[i + 1]
            i += 2
        else:
            txt_paths.append(Path(args[i]))
            i += 1

    ids = load_ids(txt_paths)
    print(f"读取 {len(ids)} 个唯一 ID（来自 {len(txt_paths)} 个清单文件）")

    # 建 manifest
    if tag_id:
        print(f"建立清单映射（按分类 tag_id={tag_id} 搜索）…")
    elif keyword:
        print(f"建立清单映射（搜索关键词 {keyword!r}）…")
    else:
        # 兼容旧用法：从文件名推断关键词
        kw = "minimax h3" if any("minimax" in p.name.lower() for p in txt_paths) else txt_paths[0].stem
        print(f"建立清单映射（搜索关键词 {kw!r}）…")
        keyword = kw

    meta = build_manifest(ids, tag_id=tag_id, keyword=keyword)
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
