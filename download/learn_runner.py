#!/usr/bin/env python3
"""learn_runner.py — 补充任务收尾 runner（参数化版，2026-10-21 泛化）。

流程：等待下载进程退出 → 核对落地 → 纯消化轮（入库+建卡+学习）→ 终轮（图谱重建）。

用法（仓库根目录）：
    python -X utf8 download/learn_runner.py --tag 图片生成/文生图 \
        --missing download/ids-by-tag/图片生成/文生图_missing_2026-10-21.txt

设计要点（2026-10-20 图生图实战验证）：
- 下载进程（download_by_ids.py）是**非原子落盘**（dest.write_bytes），
  学习/入库必须等它退出后进行，否则可能读到半个 JSON。
- 消化用 learn_pipeline 的 --skip-collect --skip-download 纯消化模式；
  学习器逐文件写 Markdown、finally 兜底 save，中途崩溃重跑可续。
- 每阶段启动前等**外来 learn_pipeline** 退出：用户会在另一会话/计划任务
  跑其它标签的管线，两条同写 sqlite 会互相覆盖（AGENTS.md 2026-10-19 禁令）。
- 末轮不带 --skip-graph，一次性重建知识图谱；「导入 0 / 学习 0」的
  空转结果同时作为「消化无遗漏」的反向校验。
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
LOG = ROOT / "download" / "learn_runner.log"
PY = sys.executable

# 日志前缀沿用项目惯例（t2i_b16.log / i2i_learn_b1.log）
LOG_PREFIX = {"图片生成/文生图": "t2i", "图片生成/图生图": "i2i"}


def log(msg: str) -> None:
    line = f"[{datetime.now():%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def tail(path: Path, n: int = 14) -> str:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return "(日志读取失败)"
    return "\n".join("    " + l for l in lines[-n:])


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


def wmi_pair(p1: str, p2: str) -> int:
    """命令行同时包含 p1 和 p2 的 python 进程数（WMI）。"""
    ps = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" "
         f"| Where-Object {{ $_.CommandLine -like '*{p1}*' -and $_.CommandLine -like '*{p2}*' }} "
         "| Measure-Object | ForEach-Object { $_.Count }"],
        capture_output=True, text=True)
    try:
        return int(ps.stdout.strip())
    except ValueError:
        return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True, help="如 图片生成/文生图")
    ap.add_argument("--missing", required=True, help="缺失 ID 清单文件（下载进程的命令行特征）")
    ap.add_argument("--count", type=int, default=500)
    args = ap.parse_args()

    tag = args.tag
    fam, t = tag.split("/")
    missing_txt = (ROOT / args.missing).resolve() if not os.path.isabs(args.missing) else Path(args.missing)
    mark = missing_txt.stem  # 下载进程命令行特征，如 文生图_missing_2026-10-21
    dl_dir = ROOT / "download" / "workflows-by-tag" / fam / t
    prefix = LOG_PREFIX.get(tag, tag.replace("/", "_"))
    stage_cmd = ["skills/comfyui-learning/tools/learn_pipeline.py",
                 "--tag", tag, "--count", str(args.count)]

    def dl_alive() -> bool:
        # 必须同时匹配 download_by_ids 与 mark：runner 自身命令行含 --missing
        # 清单名（即 mark），只按 mark 匹配会把 runner 自己算成下载进程，
        # 导致永远等不到退出（2026-10-21 文生图实战踩坑，已修复）。
        return wmi_pair("download_by_ids", mark) > 0

    def foreign_pipeline() -> int:
        """外来 learn_pipeline 进程数（不含本次消化的阶段进程）。"""
        return wmi_count("learn_pipeline") - wmi_count("learn_pipeline.py --tag " + tag)

    def verify_download() -> None:
        have = set()
        for f in os.listdir(dl_dir):
            m = re.search(r"(\d{12,})\.json$", f)
            if m:
                have.add(m.group(1))
        missing = [l.strip() for l in missing_txt.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        landed = [i for i in missing if i in have]
        failed = [i for i in missing if i not in have]
        log(f"下载核对：清单 {len(missing)} 个，落地 {len(landed)}，未落地 {len(failed)}")
        if failed:
            out = missing_txt.with_name(missing_txt.stem + "_未落地.txt")
            out.write_text("\n".join(failed) + "\n", encoding="utf-8")
            log(f"未落地 ID 已写入 {out.name}（{len(failed)} 个，412 作者导出限制转登录态"
                "浏览器补，404 为站点下架，不无限重试）")

    def run_stage(name: str, logfile: str, extra_args: list) -> int:
        # 防线：等外来 learn_pipeline 退出，避免同写 sqlite
        waited = 0
        while foreign_pipeline() > 0:
            if waited == 0:
                log(f"检测到外来 learn_pipeline 进程，阶段「{name}」等待中")
            time.sleep(60)
            waited += 60
        if waited:
            log(f"外来管线已退出（等待 {waited // 60} 分钟），继续阶段「{name}」")
        log(f"阶段「{name}」开始")
        with open(ROOT / "download" / logfile, "w", encoding="utf-8") as f:
            p = subprocess.run([PY, "-X", "utf8"] + stage_cmd + extra_args,
                               cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)
        log(f"阶段「{name}」结束，退出码 {p.returncode}")
        log(f"「{name}」日志尾部：\n{tail(ROOT / 'download' / logfile)}")
        return p.returncode

    log(f"runner 启动（tag={tag}，清单={missing_txt.name}）：等待下载进程退出"
        "（下载非原子落盘，期间不并行入库）")
    waited = 0
    while dl_alive():
        time.sleep(60)
        waited += 60
        if waited % 600 == 0:
            log(f"仍在等待下载进程（已等 {waited // 60} 分钟）")
    log("下载进程已退出")
    verify_download()

    run_stage("消化：入库+建卡+学习（不建图谱）", f"{prefix}_learn_b1.log",
              ["--skip-collect", "--skip-download", "--skip-graph"])
    run_stage("终轮：空转校验+图谱重建", f"{prefix}_learn_final.log",
              ["--skip-collect", "--skip-download"])

    log("全部阶段完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
