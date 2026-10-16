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
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LIBRARY = ROOT / "comfyui_library" / "workflows"
DEFAULT_SOURCE = ROOT / "download" / "workflows-by-tag"

sys.path.insert(0, str(ROOT))
from engine.workflow_learning.workflow_scanner import SIDECAR_NAMES  # noqa: E402

WORKFLOW_EXTS = {".json", ".png"}


def hash_file(path: Path) -> str:
    """文件内容指纹（与 WorkflowLearner._hash_file 完全一致）"""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()[:16]


def semantic_hash(path: Path) -> str | None:
    """
    归一化内容指纹：同一工作流的**不同排版**算同一个

    RunningHub 不同批次导出的同一工作流，缩进/换行/键序会变（实测
    tab 缩进 195KB vs 无换行 148KB，内容逐字段一致）。字节指纹认不出
    差异，会把同一份工作流当新文件反复导入 —— 2026-10-16 实测：清完
    重复副本后，一轮流水线又把 316 个「刚删掉的副本」导回库里。

    非工作流（无 nodes / prompt 键）返回 None，不参与语义判重。
    """
    if path.suffix.lower() != ".json":
        return None  # png 按元数据判重，交给字节闸门
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    if not isinstance(data.get("nodes"), list) and not isinstance(
        data.get("prompt"), dict
    ):
        return None
    canon = json.dumps(
        data, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:16]


def library_semantic_hashes() -> set:
    """库内全部 json 工作流的归一化指纹（较慢：逐个解析）"""
    hashes = set()
    files = [
        p for p in LIBRARY.rglob("*")
        if is_workflow_file(p) and p.suffix.lower() == ".json"
    ]
    for i, p in enumerate(files, 1):
        h = semantic_hash(p)
        if h:
            hashes.add(h)
        if i % 5000 == 0:
            print(f"  …已解析 {i}/{len(files)}", flush=True)
    return hashes


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
    """
    是否算一个待导入的 workflow 文件

    伴生文件判定复用扫描器的 SIDECAR_NAMES（整名匹配），**不要写成
    `name.startswith("_")`** —— 下载的工作流名本身可能以 `_` 开头
    （`_开源_minimax_h3*.json`、`_T8_SkyReel*.json`、`_全能图片V1*`），
    那种一刀切会让真实工作流永远进不了库（2026-10-15 连着踩了三次）。
    """
    return (
        path.suffix.lower() in WORKFLOW_EXTS
        and path.name.lower() not in SIDECAR_NAMES
        and "learning" not in path.parts
    )


def library_name(path: Path) -> str:
    """入库文件名：去掉前导下划线（平台给的名字有时带 `_`）"""
    return path.name.lstrip("_")


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
    # 归一化闸门默认开（--no-semantic 关掉，只走字节指纹，快但会漏排版重复）
    semantic = "--no-semantic" not in args
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

    # 第一轮：字节指纹闸门（便宜，先过一遍）
    candidates, batch_hashes = [], set()
    dup_existing, dup_batch = 0, 0
    for src in files:
        h = hash_file(src)
        if h in seen_hashes:
            dup_existing += 1
            continue
        if h in batch_hashes:
            dup_batch += 1
            continue
        batch_hashes.add(h)
        candidates.append(src)

    # 第二轮：归一化闸门。字节指纹认不出「同一工作流不同排版」，
    # 会把同一份内容当新文件反复导入（见 semantic_hash 注释）
    dup_semantic = 0
    if semantic and candidates:
        t0 = time.time()
        print(f"字节闸门候选 {len(candidates)} 个，算库内归一化指纹…", flush=True)
        seen_sem = library_semantic_hashes()
        print(f"  库内唯一内容 {len(seen_sem)} 个（{time.time() - t0:.0f}s）")
        kept, batch_sem = [], set()
        for src in candidates:
            sh = semantic_hash(src)
            if sh and (sh in seen_sem or sh in batch_sem):
                dup_semantic += 1
                continue
            if sh:
                batch_sem.add(sh)
                seen_sem.add(sh)
            kept.append(src)
        candidates = kept

    imported, renamed = 0, 0
    taken = set()

    for src in candidates:
        rel = dest_sub / src.relative_to(source)
        target = unique_target(rel, taken)
        if str(target) != str(rel):
            renamed += 1
        taken.add(target)

        dest = LIBRARY / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        seen_hashes.add(hash_file(src))
        imported += 1

    print(f"导入 {imported} 个"
          f"（与库内重复跳过 {dup_existing}，"
          f"排版重复跳过 {dup_semantic}，"
          f"批次内重复跳过 {dup_batch}，改名 {renamed}）")
    print("下一步: python -X utf8 -m engine.workflow_learning 或")
    print("        create_batch_learner().learn_folder() 增量学习新文件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
