#!/usr/bin/env python3
"""digest_runner.py — 合并消化编排（2026-10-26）

用途：把「多个标签的补下载」与「全库消化」串成一条安全的链，
避免为每个标签各跑一轮重归纳 + 图谱重建（每次 ~30 分钟 + ~30 分钟）。

流程：
    1. 等所有 download_by_ids 进程退出（下载非原子落盘，期间不并行入库）
    2. 核对各清单落地情况 → 未落地 ID 写 *_未落地.txt（412 转登录态浏览器，404 已下架）
    3. 消化轮：learn_pipeline --skip-collect --skip-download --skip-graph
       （入库 + 预建卡 + 增量学习；跳过图谱——图谱与库对账同进程会叠内存，
        10-23 崩过 0xC0000005，故图谱留给独立进程）
    4. 阶段1 全量重归纳（独立进程，写模式卡 + 回库 + 三索引 + VACUUM）
    5. 阶段2 知识图谱重建（独立进程，消费阶段1 落盘的新模式）

与 finalize_runner.py 的区别：finalize 只做「归纳 → 图谱」，
本脚本前面多了「等下载 + 消化」，是完整的数据层收尾链。

门禁：每阶段启动前等外来 learn_pipeline / consolidation / graph 进程退出
    （两条同写 sqlite 会互相覆盖，AGENTS.md 2026-10-19 禁令）。
    WMI 检测，Git Bash 下 pgrep 不可用。

用法（仓库根目录）：
    python -X utf8 download/digest_runner.py \
        --plan "数字人/数字人=download/ids-by-tag/数字人/数字人_missing_2026-10-26.txt" \
        --plan "图片生成/反推提示词=download/ids-by-tag/图片生成/反推提示词_missing_2026-10-26.txt"
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
LOG = ROOT / "download" / "digest_runner.log"


def log(msg: str) -> None:
    line = f"[{datetime.now():%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def wmi_count(pattern: str) -> int:
    """命令行匹配 pattern 的 python 进程数（WMI；pgrep 在 Git Bash 不可用）。"""
    ps = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" "
         f"| Where-Object {{ $_.CommandLine -like '*{pattern}*' }} "
         "| Measure-Object | ForEach-Object { $_.Count }"],
        capture_output=True, text=True)
    try:
        return int(ps.stdout.strip())
    except ValueError:
        return 0


def heavy_pipelines() -> list:
    """正在跑的重型管线进程 pid（排除本脚本自己）。"""
    ps = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
         "Where-Object { $_.CommandLine -match "
         "'learn_pipeline|finalize_phase|consolidat|build_graph|download_by_ids' } | "
         "ForEach-Object { $_.ProcessId }"],
        capture_output=True, text=True, timeout=30)
    pids = [int(x) for x in ps.stdout.split() if x.strip().isdigit()]
    return [p for p in pids if p != os.getpid()]


def wait_idle(what: str, deadline_s: int = 7200) -> bool:
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
    log(f"阶段「{name}」结束 rc={rc} 耗时 {(time.time()-t0)/60:.1f} 分钟")
    return rc


def check_all_landed(plans: list, tolerance: float = 0.02) -> list:
    """校验每个清单的落地率；返回未完成的清单列表。

    容差 2%：站点偶发 404 下架属正常（会写进 _未落地.txt），
    但如果落地率明显偏低，说明下载环节根本没跑完。
    """
    bad = []
    for tag, rel in plans:
        fam, t = tag.split("/")
        dl_dir = ROOT / "download" / "workflows-by-tag" / fam / t
        have = set()
        if dl_dir.is_dir():
            for f in os.listdir(dl_dir):
                m = re.search(r"(\d{12,})\.json$", f)
                if m:
                    have.add(m.group(1))
        txt = (ROOT / rel).resolve()
        if not txt.exists():
            bad.append((tag, rel, 0, 0))
            continue
        ids = [l.strip() for l in txt.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        landed = len([i for i in ids if i in have])
        ratio = landed / len(ids) if ids else 0.0
        if ratio < 1.0 - tolerance:
            bad.append((tag, rel, landed, len(ids)))
    return bad


def verify(plans: list) -> None:
    """核对各清单落地情况，未落地的写 *_未落地.txt。"""
    for tag, rel in plans:
        fam, t = tag.split("/")
        dl_dir = ROOT / "download" / "workflows-by-tag" / fam / t
        have = set()
        if dl_dir.is_dir():
            for f in os.listdir(dl_dir):
                m = re.search(r"(\d{12,})\.json$", f)
                if m:
                    have.add(m.group(1))
        txt = (ROOT / rel).resolve()
        ids = [l.strip() for l in txt.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        landed = [i for i in ids if i in have]
        failed = [i for i in ids if i not in have]
        log(f"下载核对 {tag}：清单 {len(ids)}，落地 {len(landed)}，未落地 {len(failed)}")
        if failed:
            out = txt.with_name(txt.stem + "_未落地.txt")
            out.write_text("\n".join(failed) + "\n", encoding="utf-8")
            log(f"  未落地 {len(failed)} 个已写入 {out.name}"
                f"（412 作者导出限制转登录态浏览器补，404 为站点下架，不无限重试）")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="append", required=True,
                    help="标签=清单路径，可重复")
    ap.add_argument("--skip-consolidate", action="store_true",
                    help="跳过重归纳（仅消化 + 图谱）")
    args = ap.parse_args()

    plans = []
    for p in args.plan:
        tag, rel = p.split("=", 1)
        plans.append((tag, rel))

    log(f"=== 合并消化编排启动 {datetime.now():%m-%d %H:%M:%S} ===")
    for tag, rel in plans:
        log(f"  计划：{tag} ← {rel}")

    # 1. 等下载
    if not wait_idle("下载进程"):
        log("[中止] 下载进程长时间未退出，不启动入库（下载非原子落盘）")
        return 98
    # 1b. 落地校验门禁：进程退出不代表下完。多步下载若用 && 串联，
    # 前一步有失败项会让后一步静默跳过——此时必须识别出来并补跑，
    # 不能带着半程清单直接进消化（会漏学且不报错）。
    incomplete = check_all_landed(plans)
    if incomplete:
        for tag, rel, landed, total in incomplete:
            log(f"[门禁] {tag} 仅落地 {landed}/{total}，下载未完成")
        log("[中止] 有清单未下完，不启动入库。补齐后重跑本脚本。")
        return 97
    log("下载进程已全部退出，且各清单落地数校验通过")

    # 2. 核对
    verify(plans)

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
