"""图生图 backfill 下载 runner（2026-10-21）

背景：图生图清单补齐至 33,326 后，待下载 23,808 个（分 4 个批次 txt）。
单轮总量预计 4~5 小时，会撞后台进程 4 小时硬超时，故设计成**幂等可断点续跑**：
- download_by_ids 本身按 ID 跳过已存在文件（可断点续传），中断重跑无损；
- runner 记录已完成批次到状态文件，重启自动从第一个未完成批次继续；
- 批次失败（rc!=0，多为 404/412 记例外）不中止，继续下一批；
- 全部批次 DONE 后写完成标记，供后续消化阶段接线。

用法（仓库根）：
    python -X utf8 download/i2i_backfill_download.py
    python -X utf8 download/i2i_backfill_download.py --reset   # 重开全量核对
"""
import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DL = ROOT / "download"
BATCH_DIR = DL / "ids-by-tag" / "图片生成"
BATCHES = sorted(BATCH_DIR.glob("图生图_backfill_*.txt"))
META = BATCH_DIR / "图生图_meta.csv"
OUT = DL / "workflows-by-tag" / "图片生成" / "图生图"
LOG = DL / "i2i_backfill_dl.log"
STATE = DL / "i2i_backfill_state.json"
PY = sys.executable


def log(msg: str) -> None:
    line = f"[{datetime.now():%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_state() -> dict:
    import json
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"done": []}


def save_state(st: dict) -> None:
    import json
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reset", action="store_true", help="忽略状态文件重跑全部批次")
    args = ap.parse_args()
    if args.reset and STATE.exists():
        STATE.unlink()

    if not BATCHES:
        log("找不到批次 txt，退出")
        return 1
    st = load_state()
    log(f"启动：共 {len(BATCHES)} 批，已完成 {len(st['done'])} 批（状态文件可断点续跑）")

    rc_all = 0
    for bp in BATCHES:
        if bp.name in st["done"]:
            log(f"跳过已完成批次 {bp.name}")
            continue
        ids = [l.strip() for l in bp.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        log(f"批次 {bp.name} 开始：{len(ids)} 个 ID")
        t0 = time.time()
        with open(LOG, "a", encoding="utf-8") as f:
            p = subprocess.run(
                [PY, "-X", "utf8", "skills/comfyui-learning/tools/download_by_ids.py",
                 str(bp), "--meta", str(META), "--out", str(OUT)],
                cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)
        el = (time.time() - t0) / 60
        log(f"批次 {bp.name} 结束 rc={p.returncode} 耗时 {el:.0f} 分钟")
        if p.returncode not in (0, 2):  # 2 = 有失败个例（404/412），不算崩
            log(f"批次异常退出，中止 runner（重跑将续接本批次，已落盘文件自动跳过）")
            return p.returncode
        st["done"].append(bp.name)
        save_state(st)

    log("全部批次完成（如有 404/412 未落地个例，见各批次日志尾部失败清单）")
    return rc_all


if __name__ == "__main__":
    sys.exit(main())
