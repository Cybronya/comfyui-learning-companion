#!/usr/bin/env python3
"""collect_download_2026-10-26.py — 七分类 NEWEST 增量收集 + 下载新增 ID。

与本日盘点衔接：数据层 10-26 已收官（库 76,725 条），本轮只做
「找新增 → 下载新增」，不入库、不学习（消化交给后续 digest_runner）。

每个分类的逻辑：
    1. NEWEST 续收（collect_by_tag.py，state 锚点跳过已见 ID）；
       单轮新收 == target 视为「可能没挖完」，再补一轮，最多 3 轮
    2. 新增 ID 落 <小类>_new_2026-10-26.txt
    3. download_by_ids.py 下载（--meta 解析名字），已存在文件自动跳过
    4. 落地校验：下载目录找不到文件的写 <小类>_未落地_2026-10-26.txt

只依赖标准库；串行跑，全部分类附和后打印总表。
"""
import csv
import re
import subprocess
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "skills" / "comfyui-learning" / "tools"
IDS = ROOT / "download" / "ids-by-tag"
DL = ROOT / "download" / "workflows-by-tag"
PY = sys.executable
DAY = "2026-10-26"

# (分类 大类/小类, 单轮 target)
TAGS = [
    ("图片生成/图生图", 600),
    ("图片生成/文生图", 600),
    ("视频生成/图生视频", 600),
    ("视频生成/文生视频", 300),
    ("数字人/数字人", 600),
    ("图片生成/反推提示词", 300),
    ("音频生成/音频生成", 300),
]


def sh(cmd):
    return subprocess.run([PY, "-X", "utf8"] + [str(c) for c in cmd]).returncode


def read_ids(path: Path):
    if not path.exists():
        return []
    return [l.strip() for l in path.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def have_ids(out_dir: Path):
    """out_dir 已落地的 id 集合（manifest + 文件名后缀双口径，
    与 learn_pipeline.missing_ids 同款判据）"""
    have = set()
    manifest = out_dir / "manifest.csv"
    if manifest.exists():
        with open(manifest, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                have.add(row.get("id", "").strip())
    for f in out_dir.glob("*.json"):
        m = re.search(r"(\d{12,})\.json$", f.name)
        if m:
            have.add(m.group(1))
    return have


def main():
    grand_new = grand_landed = 0
    summary = []
    for tag, target in TAGS:
        parent, name = tag.split("/")
        ids_txt = IDS / parent / f"{name}_ids.txt"
        meta_csv = IDS / parent / f"{name}_meta.csv"
        out_dir = DL / parent / name
        out_dir.mkdir(parents=True, exist_ok=True)

        known = set(read_ids(ids_txt))
        start_n = len(known)
        new_ids: list = []
        print(f"\n=== {tag} ===")
        for round_i in range(1, 4):
            before = set(read_ids(ids_txt))
            print(f"[收集 第{round_i}轮 target={target}（清单 {len(before)}）", flush=True)
            rc = sh([TOOLS / "collect_by_tag.py", tag, str(target),
                     "--out", "download/ids-by-tag", "--sort", "NEWEST"])
            if rc != 0:
                print(f"  ⚠ 收集进程 rc={rc}，跳过本轮")
                break
            after = read_ids(ids_txt)
            fresh = [i for i in after if i not in before]
            new_ids.extend(fresh)
            print(f"  本轮新收 {len(fresh)}，累计 {len(new_ids)}")
            if len(fresh) < target:
                break
            time.sleep(1)

        if not new_ids:
            print("  无新增，跳过下载")
            summary.append((tag, 0, 0))
            continue

        new_file = IDS / parent / f"{name}_new_{DAY}.txt"
        new_file.write_text("\n".join(new_ids), encoding="utf-8")
        print(f"[下载] 新增 {len(new_ids)} 个 → {new_file.name}")
        rc = sh([TOOLS / "download_by_ids.py", new_file,
                 "--meta", meta_csv, "--out", out_dir])
        landed = have_ids(out_dir)
        failed = [i for i in new_ids if i not in landed]
        summary.append((tag, len(new_ids), len(new_ids) - len(failed)))
        grand_new += len(new_ids)
        grand_landed += len(new_ids) - len(failed)
        if failed:
            fail_file = IDS / parent / f"{name}_未落地_{DAY}.txt"
            fail_file.write_text("\n".join(failed), encoding="utf-8")
            print(f"  ⚠ 未落地 {len(failed)} 个，清单 → {fail_file.name}")
        else:
            print("  全部落地 ✓")
        # 清理本轮 _next 临时文件（若 download 工具误产）
        nxt = IDS / parent / f"{name}_next.txt"
        if nxt.exists():
            nxt.unlink()
        time.sleep(1)

    print("\n==== 汇总 ====")
    for tag, n, landed in summary:
        print(f"  {tag}: 新增 {n} / 落地 {landed}")
    print(f"合计新增 {grand_new} / 落地 {grand_landed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
