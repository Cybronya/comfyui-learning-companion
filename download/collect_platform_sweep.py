#!/usr/bin/env python3
"""collect_platform_sweep.py — 全平台列表扫描收集（补分类收集的盲区）

背景（2026-11-13 发现）：
    既有收集方式 `collect_by_tag.py <大类/小类>` 是**按 tags 过滤**翻页，
    跳过本地已见 ID。长期跑下来，7 个主线分类的「已见 ID 数」已 ≥ 平台该分类
    总量（例：图生图本地 35,205 vs 平台 33,370 —— 多出的是跨标签重复）。

    但这掩盖了一个真问题：**按分类过滤会漏掉那些归类在「未收集子分类」
    下的工作流**。实测直接打平台全量列表（不带 tags）：
        扫前 1,800 条 → 本地完全没见过的 ID 有 1,022 个（57%）。

    平台全量列表接口：POST /api/portal/template/list
        body {"size":30,"current":N,"sort":"NEWEST"}（不带 tags = 全平台）
        total ≈ 91,872，无需登录。

做法：
    按 NEWEST 顺序扫全平台列表，与本地全局已知 ID 集合比对，
    把未见过的 ID 收集到 <out>/平台全量_ids.txt + _meta.csv，
    再喂给 download_by_ids.py 下载。

    已知 ID 集合来源（三者并集）：
        ① 各分类 state.json 的 known_ids
        ② 各分类 ids.txt
        ③ 下载目录里已落地的文件名（ID 后缀）
    —— 第 ③ 项很重要：有些工作流下载过但没进过任何分类清单。

只依赖标准库；断点续跑靠 --start / --max-pages。
"""
import argparse
import csv
import datetime
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

ROOT = Path(__file__).resolve().parents[1]
IDS = ROOT / "download" / "ids-by-tag"
DL = ROOT / "download" / "workflows-by-tag"
TOOLS = ROOT / "skills" / "comfyui-learning" / "tools"
PY = sys.executable

LIST_URL = "https://www.runninghub.cn/api/portal/template/list"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 Chrome/120 Safari/537.36"),
}
PAGE_SIZE = 30
DELAY = 0.4

OUT_DIR = IDS / "平台全量"
OUT_IDS = OUT_DIR / "平台全量_ids.txt"
OUT_META = OUT_DIR / "平台全量_meta.csv"


def log(msg: str) -> None:
    print(f"[{datetime.datetime.now():%m-%d %H:%M:%S}] {msg}", flush=True)


def post_json(url: str, body: dict, retries: int = 3):
    """POST 一个 JSON 接口；失败重试（指数退避）。"""
    data = json.dumps(body).encode("utf-8")
    last = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, data=data, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:      # 网络抖动 / 限流
            last = e
            if attempt < retries:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"接口请求失败（重试 {retries} 次）: {last}")


def collect_known_ids() -> set:
    """本地全局已知 ID：三来源并集。"""
    known = set()

    # ① state.json
    for st in IDS.rglob("*_state.json"):
        try:
            known |= set(
                json.loads(st.read_text(encoding="utf-8-sig"))
                .get("known_ids") or []
            )
        except (OSError, ValueError):
            continue

    # ② ids.txt
    for txt in IDS.rglob("*_ids.txt"):
        try:
            for line in txt.read_text(encoding="utf-8-sig").splitlines():
                line = line.strip()
                if line:
                    known.add(line)
        except OSError:
            continue

    # ③ 下载目录里已落地的文件名（ID 后缀）
    pat = re.compile(r"(\d{12,})\.json$")
    for f in DL.glob("*/*/*.json"):
        m = pat.search(f.name)
        if m:
            known.add(m.group(1))

    return known


def sweep(start_page: int, max_pages: int, known: set):
    """扫全平台列表，返回 (新ID列表, meta字典, 平台总量, 扫到第几页)。"""
    new_ids = []
    meta = {}
    total = 0
    page = start_page
    while page < start_page + max_pages:
        payload = post_json(LIST_URL, {
            "size": PAGE_SIZE, "current": page, "sort": "NEWEST",
        })
        if payload.get("code") != 0:
            raise RuntimeError(
                f"template/list 异常: code={payload.get('code')} "
                f"msg={payload.get('msg')}"
            )
        data = payload.get("data") or {}
        recs = data.get("records") or []
        total = int(data.get("total", total) or 0)
        if not recs:
            log(f"  第 {page} 页返回空，列表已到末尾")
            break

        added = 0
        for rec in recs:
            rid = str(rec.get("id") or "")
            if not rid or rid in known or rid in meta:
                continue
            meta[rid] = {
                "id": rid,
                "name": rec.get("name") or "",
                "author": (rec.get("owner") or {}).get("name", "")
                          if isinstance(rec.get("owner"), dict) else "",
                "publishTime": rec.get("publishTime") or "",
            }
            new_ids.append(rid)
            added += 1

        if page % 50 == 0 or added:
            log(f"  第 {page} 页：新增 {added}（累计 {len(new_ids)}）")
        page += 1
        time.sleep(DELAY)

    return new_ids, meta, total, page


def write_outputs(new_ids, meta):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # 追加到既有清单（断点续跑）
    existing = []
    if OUT_IDS.exists():
        existing = [l.strip() for l in
                    OUT_IDS.read_text(encoding="utf-8-sig").splitlines()
                    if l.strip()]
    merged = list(existing)
    seen = set(existing)
    for i in new_ids:
        if i not in seen:
            merged.append(i)
            seen.add(i)
    OUT_IDS.write_text("\n".join(merged) + "\n", encoding="utf-8")

    # meta 表：读旧 + 并入新
    old = {}
    if OUT_META.exists():
        with open(OUT_META, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                old[row.get("id", "")] = row
    for rid, m in meta.items():
        old[rid] = m
    with open(OUT_META, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "name", "author", "publishTime"])
        w.writeheader()
        for rid, m in old.items():
            w.writerow({k: m.get(k, "") for k in
                        ("id", "name", "author", "publishTime")})
    return len(merged)


def download_new(new_ids):
    """把新 ID 交给 download_by_ids.py 下载。"""
    if not new_ids:
        log("无新增，跳过下载")
        return 0
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tmp = OUT_DIR / "本次新增.txt"
    tmp.write_text("\n".join(new_ids) + "\n", encoding="utf-8")
    # 输出到 平台全量 目录，与分类目录分开，避免 manifest 混账
    out_dir = DL / "平台全量"
    out_dir.mkdir(parents=True, exist_ok=True)
    log(f"[下载] {len(new_ids)} 个新 ID → {out_dir}")
    rc = subprocess.run(
        [PY, "-X", "utf8", str(TOOLS / "download_by_ids.py"), str(tmp),
         "--meta", str(OUT_META), "--out", str(out_dir)]
    ).returncode
    return rc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=1, help="起始页（断点续跑）")
    ap.add_argument("--max-pages", type=int, default=300,
                    help="本次最多扫多少页")
    ap.add_argument("--download", action="store_true", help="扫完立即下载")
    args = ap.parse_args()

    t0 = time.time()
    known = collect_known_ids()
    log(f"本地已知唯一 ID：{len(known)} 个")
    log(f"扫描：第 {args.start} 页起，最多 {args.max_pages} 页")

    new_ids, meta, total, end_page = sweep(args.start, args.max_pages, known)
    log(f"平台总量 {total}；本次扫到第 {end_page - 1} 页，"
        f"新发现 {len(new_ids)} 个")

    total_ids = write_outputs(new_ids, meta)
    log(f"清单累计 {total_ids} 个 → {OUT_IDS}")

    if args.download:
        rc = download_new(new_ids)
        if rc != 0:
            log(f"下载阶段 rc={rc}")
            return rc

    log(f"耗时 {(time.time() - t0) / 60:.1f} 分钟")
    return 0


if __name__ == "__main__":
    sys.exit(main())
