#!/usr/bin/env python3
"""verify_sweep_2026-11-13.py — 全平台扫描批次的落地清点。

口径（与 11-13 盘点一致，勿改）：
    库内 `workflows.id` 存的是**相对路径**（`大类/小类/文件名.json`），不是纯 ID。
    按路径比对会得出虚高的「未入库」数字（同一工作流在多个标签目录各存一份）。
    正确口径是按 **ID 全局去重**。

用法：
    python -X utf8 download/verify_sweep_2026-11-13.py
"""
import csv
import re
import sqlite3
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DL = ROOT / "download" / "workflows-by-tag"
DB = ROOT / "comfyui_library" / "database" / "storage" / "workflow_database.sqlite"
ID_RE = re.compile(r"(\d{12,})\.json$")


def main() -> int:
    db = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    known_ids = set()
    for (k,) in db.execute("select id from workflows"):
        m = ID_RE.search(k)
        if m:
            known_ids.add(m.group(1))
    n_wf = db.execute("select count(*) from workflows").fetchone()[0]
    n_exp = db.execute("select count(*) from experiences").fetchone()[0]
    n_pat = db.execute("select count(*) from patterns").fetchone()[0]
    print(f"库内：workflows {n_wf} / experiences {n_exp} / patterns {n_pat}")
    print(f"库内可解析 ID：{len(known_ids)} 个\n")

    seen = set()
    total_files = 0
    rows = []
    for d in sorted(DL.glob("*/*")):
        if not d.is_dir():
            continue
        ids = set()
        for f in d.glob("*.json"):
            m = ID_RE.search(f.name)
            if m:
                ids.add(m.group(1))
        if not ids:
            continue
        total_files += len(ids)
        # 真正未入库 = 不在库里、且全局还没出现过
        new_ids = [i for i in ids if i not in known_ids and i not in seen]
        seen |= ids
        rows.append((f"{d.parent.name}/{d.name}", len(ids), len(new_ids)))

    print(f"{'分类':<24}{'去重工作流':>10}{'未入库':>8}")
    print("-" * 44)
    miss_total = 0
    for name, n, m in rows:
        miss_total += m
        flag = "" if m == 0 else f"  ← 待消化"
        print(f"{name:<24}{n:>10}{m:>8}{flag}")
    print("-" * 44)
    print(f"{'合计':<24}{len(seen):>10}{miss_total:>8}")
    print(f"\n下载目录文件总数 {total_files}（含跨标签重复），"
          f"去重后 {len(seen)} 个工作流")
    print(f"真实欠账（已下载未入库）：{miss_total} 个")
    return 0


if __name__ == "__main__":
    sys.exit(main())
