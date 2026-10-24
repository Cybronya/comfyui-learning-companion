"""收尾编排：全量重归纳 → 知识图谱重建（串行、分进程、门禁外来管线）

为什么拆两阶段独立进程：
    2026-10-23 learn_pipeline 终轮（空转校验+图谱）在同一进程里先加载全库
    对账、再建 400MB 级图谱，内存叠加触发 0xC0000005 访问违例崩在图谱阶段。
    这里把归纳与图谱拆成两个 subprocess，各自的内存峰值不叠加；
    且阶段1（写模式卡 + 回库 + 三索引）必须先落盘，阶段2 才消费得到新模式。

门禁：每阶段启动前等「外来 learn_pipeline / consolidation / graph」进程退出，
    两条同写 sqlite 会互相覆盖（2026-10-19 禁令）。WMI 检测，Git Bash pgrep 不可用。

每阶段独立日志（Python -u 无缓冲，UTF-8 干净，不走 PowerShell 重定向避免乱码）。
阶段1 非 0 立即中止，不进阶段2。
"""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable


def running_pipelines():
    """返回正在跑的重型管线进程 pid 列表（排除本编排器自己）。"""
    ps = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
         "Where-Object { $_.CommandLine -match "
         "'learn_pipeline|finalize_phase|consolidat|build_graph' } | "
         "ForEach-Object { $_.ProcessId }"],
        capture_output=True, text=True, timeout=30)
    pids = [int(x) for x in ps.stdout.split() if x.strip().isdigit()]
    return [p for p in pids if p != os.getpid()]


def wait_no_pipeline(tag, deadline_s=600):
    """等外来管线退出（本编排子进程阶段之间不应有重叠）。"""
    t0 = time.time()
    while time.time() - t0 < deadline_s:
        others = [p for p in running_pipelines() if p != os.getpid()]
        if not others:
            return True
        print(f"[门禁] {tag}：等待外来管线退出 {others}", flush=True)
        time.sleep(10)
    return not running_pipelines()


def run_stage(name, log_name, script):
    """串行跑一个阶段脚本，rc=0 才算成功。日志文件由子进程自行写（无缓冲 UTF-8）。"""
    if not wait_no_pipeline(name):
        print(f"[中止] {name}：门禁超时，仍有外来管线在跑，不启动本阶段", flush=True)
        return 99
    log = os.path.join(ROOT, "download", log_name)
    print(f"[{name}] 开始 {time.strftime('%m-%d %H:%M:%S')} → {log_name}", flush=True)
    t0 = time.time()
    with open(log, "w", encoding="utf-8") as fh:
        rc = subprocess.call([PY, "-X", "utf8", "-u", os.path.join(ROOT, "download", script)],
                             cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
    dt = time.time() - t0
    print(f"[{name}] 结束 rc={rc} 耗时 {dt/60:.1f} 分钟", flush=True)
    return rc


def main():
    print(f"=== 收尾编排启动 {time.strftime('%m-%d %H:%M:%S')} ===", flush=True)

    rc1 = run_stage("阶段1 全量重归纳", "finalize1_consolidate.log",
                    "finalize_phase1_consolidate.py")
    if rc1 != 0:
        print(f"[中止] 阶段1 失败 rc={rc1}，不进入图谱重建（模式卡未刷新，图谱会缺 matches）",
              flush=True)
        return rc1

    rc2 = run_stage("阶段2 知识图谱重建", "finalize2_graph.log",
                    "finalize_phase2_graph.py")
    if rc2 != 0:
        print(f"[警告] 图谱重建失败 rc={rc2}（多为内存；重跑本编排或单跑阶段2脚本即可，"
              f"阶段1 的模式卡已落盘不受影响）", flush=True)
        return rc2

    print(f"=== 收尾全部完成 {time.strftime('%m-%d %H:%M:%S')} ===", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
