#!/usr/bin/env python3
"""finalize_2026-11-13.py — 2026-11-13 全平台扫描批次的收尾编排

与 digest_runner.py 的区别：本批次是**扁平目录**（平台全量），
且下载器由 collect_platform_sweep.py 拉起（不是 collect_download_*.py），
落地校验的口径也不同（清单累计 15,326 vs 本批实际下载 15,150）。

本脚本只做编排，不含业务逻辑：
    1. 等下载进程退出（含 collect_platform_sweep / download_by_ids）
    2. 落地校验（容差放宽到 5%：412/404 是站点侧永久失败，不是下载没跑完）
    3. 消化轮：入库 + 建卡 + 学习（跳过图谱，图谱留给独立进程）
    4. 全量重归纳（独立进程）
    5. 知识图谱重建（独立进程）

用法（仓库根目录）：
    python -X utf8 download/finalize_2026-11-13.py
"""
import argparse
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable
LOG = ROOT / "download" / "finalize_2026-11-13.log"

#: 本批次清单（累计口径：含历次扫描累积，去重后 15,150）
PLATFORM_IDS = "download/ids-by-tag/平台全量/平台全量_ids.txt"
#: 下载落地目录（相对 workflows-by-tag，扁平一层）
PLATFORM_TAG = "平台全量"


def log(msg: str) -> None:
    line = f"[{datetime.now():%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def heavy_pipelines() -> list:
    """正在跑的重型管线进程 pid（排除本脚本自己）。"""
    ps = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
         "Where-Object { $_.CommandLine -match "
         "'learn_pipeline|finalize_phase|consolidat|build_graph|download_by_ids|"
         "collect_platform_sweep|collect_extra|collect_download' } | "
         "ForEach-Object { $_.ProcessId }"],
        capture_output=True, text=True, timeout=30)
    pids = [int(x) for x in ps.stdout.split() if x.strip().isdigit()]
    return [p for p in pids if p != os.getpid()]


def wait_idle(what: str, deadline_s: int = 14400) -> bool:
    """等一类进程全部退出。"""
    t0 = time.time()
    waited = False
    while time.time() - t0 < deadline_s:
        others = heavy_pipelines()
        if not others:
            return True
        if not waited:
            log(f"等待 {what} 退出：{others}")
            waited = True
        time.sleep(20)
    return not heavy_pipelines()


def run_stage(name: str, log_name: str, argv: list) -> int:
    """独立进程跑一个阶段，无缓冲 UTF-8 日志；rc=0 才算成功。"""
    if not wait_idle(f"外来管线（阶段「{name}」启动前）"):
        log(f"[中止] 阶段「{name}」：门禁超时，仍有外来管线在跑")
        return 99
    log_path = ROOT / "download" / log_name
    log(f"阶段「{name}」开始 → {log_name}")
    t0 = time.time()
    with open(log_path, "w", encoding="utf-8") as fh:
        rc = subprocess.call([PY, "-X", "utf8", "-u"] + argv,
                             cwd=str(ROOT), stdout=fh, stderr=subprocess.STDOUT)
    log(f"阶段「{name}」结束 rc={rc} 耗时 {(time.time() - t0) / 60:.1f} 分钟")
    return rc


def landed_ids(tag: str) -> set:
    dl_dir = ROOT / "download" / "workflows-by-tag" / tag
    have = set()
    if dl_dir.is_dir():
        for f in os.listdir(dl_dir):
            m = re.search(r"(\d{12,})\.json$", f)
            if m:
                have.add(m.group(1))
    return have


def check_landed(rel: str, tag: str, tolerance: float) -> tuple:
    """返回 (landed, total, ratio)。"""
    txt = (ROOT / rel).resolve()
    ids = [l.strip() for l in txt.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    have = landed_ids(tag)
    landed = len([i for i in ids if i in have])
    ratio = landed / len(ids) if ids else 0.0
    return landed, len(ids), ratio


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tolerance", type=float, default=0.05,
                    help="落地率容差（默认 5%%，412/404 属站点侧永久失败）")
    ap.add_argument("--skip-consolidate", action="store_true",
                    help="跳过重归纳")
    args = ap.parse_args()

    log(f"=== 2026-11-13 批次收尾启动 {datetime.now():%m-%d %H:%M:%S} ===")
    log(f"  清单：{PLATFORM_IDS}")
    log(f"  落地目录：download/workflows-by-tag/{PLATFORM_TAG}")
    log(f"  落地率容差：{args.tolerance:.1%}")

    # 1. 等下载
    if not wait_idle("下载进程"):
        log("[中止] 下载进程长时间未退出，不启动入库（下载非原子落盘）")
        return 98
    log("下载进程已全部退出")

    # 2. 落地校验
    landed, total, ratio = check_landed(PLATFORM_IDS, PLATFORM_TAG, args.tolerance)
    log(f"落地校验：清单 {total}，落地 {landed}，落地率 {ratio:.2%}")
    if ratio < 1.0 - args.tolerance:
        log(f"[中止] 落地率 {ratio:.2%} 低于容差下限 {1 - args.tolerance:.2%}，"
            f"下载未完成，不启动入库")
        return 97

    # 未落地 ID 单独留档（412 作者导出限制 / 404 站点下架）
    txt = (ROOT / PLATFORM_IDS).resolve()
    ids = [l.strip() for l in txt.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    have = landed_ids(PLATFORM_TAG)
    failed = [i for i in ids if i not in have]
    if failed:
        out = txt.with_name(txt.stem + "_未落地.txt")
        out.write_text("\n".join(failed) + "\n", encoding="utf-8")
        log(f"未落地 {len(failed)} 个已写入 {out.name}")

    # 3. 消化轮（入库 + 建卡 + 学习，跳过图谱）
    rc = run_stage(
        "消化：入库+建卡+学习（不建图谱）", "digest_learn.log",
        [str(ROOT / "skills" / "comfyui-learning" / "tools" / "learn_pipeline.py"),
         "--tag", "图片生成/文生图", "--count", "500",
         "--skip-collect", "--skip-download", "--skip-graph"])
    if rc != 0:
        log(f"[中止] 消化轮失败 rc={rc}，不进入后续阶段")
        return rc

    # 4. 全量重归纳（独立进程）
    if not args.skip_consolidate:
        rc = run_stage(
            "全量重归纳", "digest_consolidate.log",
            [str(ROOT / "download" / "finalize_phase1_consolidate.py")])
        if rc != 0:
            log(f"[中止] 重归纳失败 rc={rc}，不进入图谱（模式卡未刷新，图谱会缺 matches）")
            return rc

    # 5. 图谱重建（独立进程）
    rc = run_stage(
        "知识图谱重建", "digest_graph.log",
        [str(ROOT / "download" / "finalize_phase2_graph.py")])
    if rc != 0:
        log(f"[警告] 图谱重建失败 rc={rc}（多为内存；重跑 download/finalize_phase2_graph.py 即可，"
            f"前面的模式卡已落盘不受影响）")
        return rc

    log(f"=== 全部完成 {datetime.now():%m-%d %H:%M:%S} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
