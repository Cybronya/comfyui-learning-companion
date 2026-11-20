"""resume_2026-11-15.py — 2026-11-13 批次收尾的后半程补跑

背景：2026-11-14 03:05 机器重启，finalize_2026-11-13.py 在消化轮
`[5/6] 增量学习` 阶段落盘完成后被强杀，后续的
    db.indexes.save_all() → 全量重归纳 → 知识图谱重建
三段都没跑。

已核实的现场（2026-11-15 巡检）：
  - 学习记录 94,353 个 .md 文件，全部完整（零半截、frontmatter 齐全）
  - 数据库 workflows/experiences 各 94,353 条，node_used_in 216 万行
  - 数据库空洞 0%，无损坏
  - 派生索引 workflow_index/node_index/pattern_index 仍是 11-02 旧版
  - 模式卡 10,089 张、图谱 688MB（11-02 版）都是旧水位

本脚本只编排，不含业务逻辑：
  1. 重建派生索引（save_all）
  2. 全量重归纳（finalize_phase1_consolidate.py）
  3. 知识图谱重建（finalize_phase2_graph.py）

每个阶段独立进程、独立日志，rc=0 才进下一阶段。
归纳失败就不建图谱 —— 模式卡没刷新时图谱会缺 matches 边。

用法（仓库根目录）：
    python -X utf8 download/resume_2026-11-15.py
"""
import argparse
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable
LOG = ROOT / "download" / "resume_2026-11-15.log"


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
         "'learn_pipeline|finalize_phase|resume_2026|consolidat|build_graph' } | "
         "ForEach-Object { $_.ProcessId }"],
        capture_output=True, text=True, timeout=60)
    pids = [int(x) for x in ps.stdout.split() if x.strip().isdigit()]
    return [p for p in pids if p != os.getpid()]


def wait_idle(what: str, deadline_s: int = 7200) -> bool:
    t0 = time.time()
    waited = False
    while time.time() - t0 < deadline_s:
        others = heavy_pipelines()
        if not others:
            return True
        if not waited:
            log(f"等待 {what} 退出：{others}")
            waited = True
        time.sleep(15)
    return not heavy_pipelines()


def run_stage(name: str, log_name: str, argv: list) -> int:
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


def stage_rebuild_indexes() -> int:
    """重建三个派生索引（节点使用索引 / 节点卡索引 / 模式索引）。

    save_all() 要扫 node_used_in 的 216 万行 + nodes/patterns 全表，
    内存峰值与归纳不叠加，所以单独一阶段跑。
    """
    code = (
        "import sys;"
        "sys.path.insert(0, r'%s');"
        "from comfyui_library.database.database import WorkflowDatabase;"
        "db = WorkflowDatabase();"
        "db.auto_save = False;"
        "paths = db.indexes.save_all();"
        "print('索引已重建:', paths, flush=True);"
        "db.auto_save = True"
    ) % str(ROOT)
    return run_stage("重建派生索引", "resume_indexes.log", ["-c", code])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-indexes", action="store_true",
                    help="跳过派生索引重建（已重建过时用）")
    ap.add_argument("--skip-consolidate", action="store_true",
                    help="跳过全量重归纳")
    ap.add_argument("--skip-graph", action="store_true",
                    help="跳过图谱重建")
    args = ap.parse_args()

    log(f"=== 2026-11-13 批次后半程补跑启动 {datetime.now():%m-%d %H:%M:%S} ===")

    if not args.skip_indexes:
        rc = stage_rebuild_indexes()
        if rc != 0:
            log(f"[中止] 派生索引重建失败 rc={rc}")
            return rc

    if not args.skip_consolidate:
        rc = run_stage(
            "全量重归纳", "resume_consolidate.log",
            [str(ROOT / "download" / "finalize_phase1_consolidate.py")])
        if rc != 0:
            log(f"[中止] 重归纳失败 rc={rc}，不进入图谱"
                "（模式卡未刷新，图谱会缺 matches 边）")
            return rc

    if not args.skip_graph:
        rc = run_stage(
            "知识图谱重建", "resume_graph.log",
            [str(ROOT / "download" / "finalize_phase2_graph.py")])
        if rc != 0:
            log(f"[警告] 图谱重建失败 rc={rc}（多为内存峰值；"
                "重跑 download/finalize_phase2_graph.py 即可，模式卡已落盘不受影响）")
            return rc

    log(f"=== 全部完成 {datetime.now():%m-%d %H:%M:%S} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
