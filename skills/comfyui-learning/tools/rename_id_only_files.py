"""rename_id_only_files.py — 存量修复：把 <id>.json 命名的下载文件改为 <名字>_<id>.json。

背景（2026-10-09 用户要求）：下载文件一律 名字_id.json 命名；早期批次 meta 未覆盖
时落成了纯 id 文件，本脚本用 manifest + 分类 meta 表回填名字批量改名。

用法：python -X utf8 skills/comfyui-learning/tools/rename_id_only_files.py [目录...]
    不传目录则处理 download/workflows-by-tag/ 下全部分类目录。
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BAD = re.compile("[" + re.escape('\\/:*?"<>|') + "\t\n\r]")


def safe_name(s: str) -> str:
    return BAD.sub("_", s).strip().strip(".")[:80]


def load_meta(paths):
    m = {}
    for p in paths:
        if not Path(p).exists():
            continue
        with open(p, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r.get("id"):
                    m[r["id"].strip()] = (r.get("name", "") or "").strip()
    return m


def rename_dir(d: Path):
    # meta 表按「大类/小类」两级存放：download/ids-by-tag/<大类>/<小类>_meta.csv
    meta_paths = [d / "manifest.csv"]
    ids_base = ROOT / "download" / "ids-by-tag"
    if d.parent.name:
        meta_paths.append(ids_base / d.parent.name / f"{d.name}_meta.csv")
    meta = load_meta(meta_paths)
    renamed = 0
    for f in sorted(d.glob("*.json")):
        m = re.fullmatch(r"(\d{8,})\.json", f.name)
        if not m:
            continue
        wid = m.group(1)
        safe = safe_name(meta.get(wid, ""))
        if not safe:
            print(f"  无法改名（无名字映射）: {d.name}/{wid}")
            continue
        nf = d / f"{safe}_{wid}.json"
        if nf.exists():
            # 目标已有同名内容文件：本文件是重复下载，直接删除裸 id 副本
            try:
                if nf.read_bytes() == f.read_bytes():
                    f.unlink()
                    print(f"  重复裸id副本已删: {wid}（与 {nf.name} 同内容）")
                    continue
            except OSError:
                pass
            print(f"  目标已存在，保留原名: {d.name}/{wid} -> {nf.name}")
            continue
        f.rename(nf)
        renamed += 1
    print(f"{d.name}: 改名 {renamed} 个")


def main() -> int:
    base = ROOT / "download" / "workflows-by-tag"
    dirs = [Path(a) for a in sys.argv[1:]] or sorted(
        p for p in base.rglob("*") if p.is_dir())
    for d in dirs:
        if not (d / "manifest.csv").exists():
            # 子目录没有 manifest，试其父级（分类目录结构不一致时兜底）
            pass
        rename_dir(d)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
