#!/usr/bin/env python3
"""collect_extra_2026-11-13.py — 补收「视频生视频」等漏掉的子分类。

背景（2026-11-13 盘点）：
    主线 7 分类（图生图 / 文生图 / 图生视频 / 文生视频 / 数字人 /
    反推提示词 / 音频生成）自 10-26 起每轮都在增量收集。
    但平台分类树里还有几个子分类从未建立 ids 清单：

        视频生成/视频生视频   平台上是正式子分类，本地只有 27 个历史零星文件
                              （其中 24 个是跨分类重复），无 ids.txt / meta.csv
        视频生成/其它视频处理  19 个零星文件
        视频生成/动作迁移      10 个零星文件

    这几个分类不补，会漏掉「只在这些子分类里发布」的工作流。

做法：
    复用 collect_download_2026-10-26.py 的同款流程（收集 → 写 new 清单 → 下载
    → 落地校验），只是分类列表不同、且 target 较小 —— 这些子分类体量远小于
    主线分类，NEWEST 前几百条足够覆盖近期新增。

只依赖标准库；串行跑，各分类附和后打印总表。
"""
import csv
import datetime
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

DAY = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") \
    else datetime.date.today().isoformat()
LOG = ROOT / "download" / "collect_extra.log"


def log(msg: str) -> None:
    line = f"[{datetime.datetime.now():%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# (分类 大类/小类, 单轮 target, 最大轮数)
# target 压到 150：这些子分类平台总量本身不大（几十到几百），
# 翻页很快就能触顶，多轮意义不大。
TAGS = [
    ("视频生成/视频生视频", 150, 2),
    ("视频生成/其它视频处理", 150, 2),
    ("视频生成/动作迁移", 150, 2),
]


def sh(cmd):
    return subprocess.run([PY, "-X", "utf8"] + [str(c) for c in cmd]).returncode


def read_ids(path: Path):
    if not path.exists():
        return []
    return [l.strip() for l in
            path.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def have_ids(out_dir: Path):
    """out_dir 已落地的 id 集合（manifest + 文件名后缀双口径）"""
    have = set()
    manifest = out_dir / "manifest.csv"
    if manifest.exists():
        with open(manifest, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                have.add(row.get("id", "").strip())
    for fp in out_dir.glob("*.json"):
        m = re.search(r"(\d{12,})\.json$", fp.name)
        if m:
            have.add(m.group(1))
    return have


def main():
    grand_new = grand_landed = 0
    summary = []
    for tag, target, max_rounds in TAGS:
        parent, name = tag.split("/")
        ids_txt = IDS / parent / f"{name}_ids.txt"
        meta_csv = IDS / parent / f"{name}_meta.csv"
        out_dir = DL / parent / name
        out_dir.mkdir(parents=True, exist_ok=True)

        new_ids: list = []
        print(f"\n=== {tag} ===", flush=True)
        for round_i in range(1, max_rounds + 1):
            before = set(read_ids(ids_txt))
            print(f"[收集 第{round_i}轮 target={target}"
                  f"（清单 {len(before)}）", flush=True)
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
        nxt = IDS / parent / f"{name}_next.txt"
        if nxt.exists():
            nxt.unlink()
        time.sleep(1)

    print("\n==== 汇总 ====")
    for tag, n, landed in summary:
        print(f"  {tag}: 新增 {n} / 落地 {landed}")
    print(f"合计新增 {grand_new} / 落地 {grand_landed}")
    log(f"补收完成：新增 {grand_new} / 落地 {grand_landed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
