#!/usr/bin/env python3
"""learn_pipeline.py — 下载 → 去重入库 → 预建卡 → 学习 → 清库 → 图谱，一键流水线。

把此前靠人肉串联的八步固化下来，并修掉四个坑：
    1. 卡在**学习之前**按新批次文件预建（频次 ≥1 也建）——
       首次学习的覆盖率就是准的，不再需要「学完补卡再 force 重学」
    2. 数据库死键（文件被移动/删除后的残留）在每轮学习后自动对账清理
    3. 缺失 ID 以 manifest + 文件名后缀双口径计算，不再手写临时脚本
    4. 全程幂等：重复执行安全，无新文件时各阶段自动空转

用法（仓库根目录）：
    python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py               # 默认 文生图 100
    python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py --tag 图片生成/图生图 --count 50
    python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py --sort RECOMMEND
    python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py --skip-download   # 只学习/补卡/图谱
    python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py --skip-collect    # 不扩清单，只消化已下载的
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# 行缓冲：后台重定向到文件时进程被杀也能保留已执行阶段的输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)

ROOT = Path(__file__).resolve().parents[3]
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS.parent / "node-analysis" / "tools"))

WORKFLOWS = ROOT / "comfyui_library" / "workflows"
IDS_DIR = ROOT / "download" / "ids-by-tag"
DL_DIR = ROOT / "download" / "workflows-by-tag"
PY = sys.executable


def sh(cmd, **kw):
    """跑子进程，继承输出；失败不抛（阶段自行判断成果）"""
    return subprocess.run([PY, "-X", "utf8"] + [str(c) for c in cmd],
                          **kw).returncode


def snapshot_library():
    """库内 workflow 文件的 相对路径 → 内容指纹 快照"""
    import hashlib
    snap = {}
    for p in WORKFLOWS.rglob("*.json"):
        if "learning" in p.parts or p.name.startswith("_"):
            continue
        digest = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        snap[str(p.relative_to(WORKFLOWS))] = digest
    return snap


def missing_ids(tag_path, ids_txt, out_dir, limit):
    """清单里还没有下载文件的 ID（manifest + 文件名后缀双口径）"""
    have = set()
    manifest = out_dir / "manifest.csv"
    if manifest.exists():
        import csv
        with open(manifest, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                have.add(row.get("id", "").strip())
    for f in out_dir.glob("*.json"):
        m = re.search(r"_(\d+)\.json$", f.name)
        if m:
            have.add(m.group(1))

    ids = [l.strip() for l in ids_txt.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    missing = [i for i in ids if i not in have]
    return missing[:limit]


def main():
    args = sys.argv[1:]
    tag = "图片生成/文生图"
    count = 100
    sort = "NEWEST"
    skip_download = False
    skip_collect = False
    i = 0
    while i < len(args):
        if args[i] == "--tag" and i + 1 < len(args):
            tag = args[i + 1]; i += 2
        elif args[i] == "--count" and i + 1 < len(args):
            count = int(args[i + 1]); i += 2
        elif args[i] == "--sort" and i + 1 < len(args):
            sort = args[i + 1]; i += 2
        elif args[i] == "--skip-download":
            skip_download = True; i += 1
        elif args[i] == "--skip-collect":
            skip_collect = True; i += 1
        else:
            i += 1

    parts = tag.split("/")
    ids_txt = IDS_DIR / parts[0] / f"{parts[-1]}_ids.txt"
    out_dir = DL_DIR / parts[0] / parts[-1]
    safe_tag = tag.replace("/", "_")

    # ---- 1. 收集 ID（续收） ----
    # 目标 = 现有清单条数 + 冗余（collect 的语义是「补足到 target」，
    # 清单已远超 count 时固定倍数会导致一轮都不收集）
    known_n = 0
    if ids_txt.exists():
        known_n = len([l for l in ids_txt.read_text(encoding="utf-8-sig").splitlines() if l.strip()])
    if skip_collect:
        print("[1/6] 跳过收集（--skip-collect）")
    else:
        target = known_n + count * 4
        print(f"[1/6] 收集 ID：{tag} 目标 {target}（sort={sort}）")
        sh(["skills/comfyui-learning/tools/collect_by_tag.py",
            safe_tag if "/" not in tag else tag,
            str(target), "--out", "download/ids-by-tag", "--sort", sort])

    # ---- 2/3. 下载缺失的 ----
    if not skip_download and ids_txt.exists():
        missing = missing_ids(tag, ids_txt, out_dir, count)
        print(f"[2/6] 库外缺失 {len(missing)} 个，下载前 {min(count, len(missing))} 个")
        if missing:
            tmp = IDS_DIR / parts[0] / f"{parts[-1]}_next.txt"
            tmp.write_text("\n".join(missing[:count]), encoding="utf-8")
            meta_csv = IDS_DIR / parts[0] / f"{parts[-1]}_meta.csv"
            sh(["skills/comfyui-learning/tools/download_by_ids.py",
                tmp, "--meta", meta_csv, "--out", out_dir])
            tmp.unlink()
        else:
            print("  无缺失，跳过下载")
    else:
        print("[2/6] 跳过下载")

    # ---- 4. 去重入库，捕获新增文件 ----
    print("[3/6] 指纹去重入库")
    before = snapshot_library()
    sh(["skills/comfyui-learning/tools/import_workflows.py"])
    after = snapshot_library()
    new_keys = sorted(set(after) - set(before))
    new_files = [WORKFLOWS / k for k in new_keys]
    print(f"  新增 {len(new_keys)} 个工作流文件")

    # ---- 5. 学习前预建卡（频次 ≥1 也建，覆盖率首遍即准） ----
    print("[4/6] 为新节点预建卡")
    if new_files:
        import draft_cards_from_workflows as dc
        created = dc.draft_for_files([str(f) for f in new_files])
        print(f"  新建卡片 {created} 张")
    else:
        print("  无新文件，跳过")

    # ---- 6. 学习 + 清库死键 + 图谱 ----
    print("[5/6] 增量学习 + 数据库对账")
    from engine.workflow_learning import create_batch_learner, LearningStore
    from engine.workflow_learning.database_bridge import cleanup_stale
    from comfyui_library.database.database import WorkflowDatabase

    db = WorkflowDatabase()
    db.auto_save = False
    try:
        summary = create_batch_learner(database=db, verbose=False).learn_folder()
        stale = cleanup_stale(db)
    finally:
        db.save()
        # 派生索引（workflow/node/pattern）与主库一起刷新，否则 node_index
        # 停留在早期 sd1.5 时代，建卡优先级/反向索引全部失真
        db.indexes.save_all()
        db.auto_save = True
    print(f"  学习 {summary['learned']} / 跳过 {summary['skipped']} / "
          f"失败 {summary['failed']}，清理库死键 {stale}")

    print("[6/6] 重建知识图谱")
    from engine.knowledge_graph import build_graph
    stats = build_graph(verbose=False).graph.stats()
    print(f"  图谱 {stats['node_total']} 顶点 / {stats['edge_total']} 边")

    # ---- 报告 ----
    from engine.workflow_learning import LearningStore
    recs = [r for r in LearningStore().completed_records() if r.nodes]
    covs = [r.coverage for r in recs]
    if covs:
        deep = sum(1 for c in covs if c >= 0.8)
        shallow = sum(1 for c in covs if c < 0.2)
        print(f"\n== 全库 {len(recs)} 条 | 平均 {sum(covs)/len(covs):.0%} | "
              f"深懂(≥80%) {deep} | 浅懂(<20%) {shallow} ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
