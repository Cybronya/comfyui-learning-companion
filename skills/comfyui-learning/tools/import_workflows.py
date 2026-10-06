# -*- coding: utf-8 -*-
"""
原始工作流导入工具：download/ 收件箱 → comfyui_library/workflows 知识库。

流程：
    1. 扫描知识库现有文件的内容指纹（sha256 前 16 位，与
       WorkflowLearner._hash_file 同一口径）
    2. 扫描下载目录，内容与库内重复的直接跳过（已学过），
       批次内互相重复的只保留第一份
    3. 不重复的按原目录结构复制入库；目标位置同名但内容不同时
       加数字后缀改名（key 含路径，改名即视为新 workflow）

学习层不去重、这里也不改已学记录 —— 本工具只负责
「原始数据 → 知识库」的一次性导入。入库后跑
BatchWorkflowLearner.learn_folder() 即可增量学习新文件。

用法（仓库根目录）：
    python -X utf8 skills/comfyui-learning/tools/import_workflows.py
    python -X utf8 skills/comfyui-learning/tools/import_workflows.py <下载目录> [库内目标子目录]
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LIBRARY = ROOT / "comfyui_library" / "workflows"
DEFAULT_SOURCE = ROOT / "download" / "workflows-by-tag"

WORKFLOW_EXTS = {".json", ".png"}


def hash_file(path: Path) -> str:
    """文件内容指纹（与 WorkflowLearner._hash_file 完全一致）"""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()[:16]


def is_comfyui_workflow(path: Path) -> bool:
    """JSON 必须解析为含 nodes 列表的 dict 才算工作流
    （download 目录混有 ids-state 之类的状态文件）"""
    if path.suffix.lower() != ".json":
        return True  # png 按元数据判断，交给学习器
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return False
    return isinstance(data, dict) and isinstance(data.get("nodes"), list)


def is_workflow_file(path: Path) -> bool:
    return (
        path.suffix.lower() in WORKFLOW_EXTS
        and not path.name.startswith("_")
        and "learning" not in path.parts
    )


def existing_hashes() -> set:
    return {
        hash_file(p) for p in LIBRARY.rglob("*") if is_workflow_file(p)
    }


def unique_target(rel: Path, taken: set) -> Path:
    """同名不同内容时生成不冲突的目标路径"""
    target = rel
    n = 1
    while target in taken:
        target = rel.with_name(f"{rel.stem}_dup{n}{rel.suffix}")
        n += 1
    return target


def main() -> int:
    args = sys.argv[1:]
    source = Path(args[0]) if args else DEFAULT_SOURCE
    # 可选第二个参数：库内目标子目录（散落的文件归组用，
    # 不传则按 source 内的相对路径原样入库）
    dest_sub = Path(args[1]) if len(args) > 1 else Path("")
    if not source.is_dir():
        print(f"下载目录不存在: {source}")
        return 1

    seen_hashes = existing_hashes()
    print(f"知识库现有 workflow 文件指纹: {len(seen_hashes)} 个")

    files = sorted(
        p for p in source.rglob("*")
        if is_workflow_file(p) and is_comfyui_workflow(p)
    )
    print(f"下载目录待导入: {len(files)} 个文件\n")

    imported, dup_existing, dup_batch, renamed = 0, 0, 0, 0
    batch_hashes = set()
    taken = set()

    for src in files:
        h = hash_file(src)

        if h in seen_hashes:
            dup_existing += 1
            continue
        if h in batch_hashes:
            dup_batch += 1
            continue
        batch_hashes.add(h)

        rel = dest_sub / src.relative_to(source)
        target = unique_target(rel, taken)
        if str(target) != str(rel):
            renamed += 1
        taken.add(target)

        dest = LIBRARY / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        seen_hashes.add(h)
        imported += 1

    print(f"导入 {imported} 个"
          f"（与库内重复跳过 {dup_existing}，"
          f"批次内重复跳过 {dup_batch}，改名 {renamed}）")
    print("下一步: python -X utf8 -m engine.workflow_learning 或")
    print("        create_batch_learner().learn_folder() 增量学习新文件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
