#!/usr/bin/env python3
"""i2i_learn_runner.py — 图生图补充任务收尾 runner（2026-10-20）。

流程：等待下载进程退出 → 核对落地 → 纯消化轮（入库+建卡+学习）→ 终轮（图谱重建）。

背景与设计要点：
- 图生图清单 6004 个，此前只下过 800 个，缺口 4565 个（download/
  图生图_missing_2026-10-20.txt）。
- 下载进程（download_by_ids.py）是**非原子落盘**（dest.write_bytes），
  学习/入库必须等它退出后进行，否则可能读到半个 JSON。
- 消化用 learn_pipeline 的 --skip-collect --skip-download 纯消化模式
  （docstring：不扩清单，只消化已下载的）；学习器逐文件写 Markdown、
  finally 兜底 save，中途崩溃重跑可续。
- 末轮不带 --skip-graph，一次性重建知识图谱（约 12 分钟）。
"""
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "download" / "i2i_learn_runner.log"
PY = sys.executable
MARK = "图生图_missing_2026-10-20"  # 下载进程命令行特征（pgrep 在 Git Bash 不可用，走 WMI）
TAG = "图片生成/图生图"
DL_DIR = ROOT / "download" / "workflows-by-tag" / "图片生成" / "图生图"
MISSING_TXT = ROOT / "download" / "ids-by-tag" / "图片生成" / "图生图_missing_2026-10-20.txt"


def log(msg: str) -> None:
    line = f"[{datetime.now():%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def tail(path: Path, n: int = 12) -> str:
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


def dl_alive() -> bool:
    """图生图下载进程是否还在跑。"""
    return wmi_count(MARK) > 0


def foreign_pipeline() -> int:
    """外来 learn_pipeline 进程数（不含本次图生图消化的阶段进程）。

    用户会在另一个会话/计划任务里跑文生图管线；两条 learn_pipeline
    同写 sqlite 会互相覆盖（AGENTS.md 2026-10-19 禁令），阶段启动前
    必须等外来管线退出。
    """
    return wmi_count("learn_pipeline") - wmi_count("learn_pipeline.py --tag " + TAG)


def verify_download() -> None:
    have = set()
    for f in os.listdir(DL_DIR):
        m = re.search(r"(\d{12,})\.json$", f)
        if m:
            have.add(m.group(1))
    missing = [l.strip() for l in MISSING_TXT.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    landed = [i for i in missing if i in have]
    failed = [i for i in missing if i not in have]
    log(f"下载核对：清单 {len(missing)} 个，落地 {len(landed)}，未落地 {len(failed)}")
    if failed:
        out = ROOT / "download" / "图生图_未落地_2026-10-20.txt"
        out.write_text("\n".join(failed) + "\n", encoding="utf-8")
        log(f"未落地 ID 已写入 {out.name}（{len(failed)} 个，多为 412 作者导出限制，"
            "按项目约定转登录态浏览器补，不无限重试）")


def run_stage(name: str, logfile: str, extra_args: list) -> int:
    # 防线：等外来 learn_pipeline（如用户另开的文生图管线）退出，避免同写 sqlite
    waited = 0
    while foreign_pipeline() > 0:
        if waited == 0:
            log(f"检测到外来 learn_pipeline 进程，阶段「{name}」等待中")
        time.sleep(60)
        waited += 60
    if waited:
        log(f"外来管线已退出（等待 {waited // 60} 分钟），继续阶段「{name}」")
    log(f"阶段「{name}」开始")
    args = [PY, "-X", "utf8", "skills/comfyui-learning/tools/learn_pipeline.py",
            "--tag", TAG, "--count", "500"] + extra_args
    with open(ROOT / "download" / logfile, "w", encoding="utf-8") as f:
        p = subprocess.run(args, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)
    log(f"阶段「{name}」结束，退出码 {p.returncode}")
    log(f"「{name}」日志尾部：\n{tail(ROOT / 'download' / logfile)}")
    return p.returncode


def main() -> int:
    log("runner 启动：等待图生图下载进程退出（下载非原子落盘，期间不并行入库）")
    waited = 0
    while dl_alive():
        time.sleep(60)
        waited += 60
        if waited % 600 == 0:
            log(f"仍在等待下载进程（已等 {waited // 60} 分钟）")
    log("下载进程已退出")
    verify_download()

    run_stage("消化：入库+建卡+学习（不建图谱）", "i2i_learn_b1.log",
              ["--skip-collect", "--skip-download", "--skip-graph"])
    run_stage("终轮：空转校验+图谱重建", "i2i_learn_final.log",
              ["--skip-collect", "--skip-download"])

    log("全部阶段完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
