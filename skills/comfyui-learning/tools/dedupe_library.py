"""dedupe_library.py — 清理库内重复的工作流副本（三处同步：文件/记录/库行）。

背景（2026-10-16）：同一工作流在库内会出现多份，成因有三条：
  ① 同一平台 id 被导出成不同排版（缩进/换行/键序），字节指纹不同、
     内容完全一致 —— 实测同 id 最多 3 份
  ② 同一工作流被不同 id 重复上传（内容一致、id 不同）—— 实测 95 组
  ③ 早期批次把同一个文件收进了多个分类目录（文生图 / 反推提示词 / 图生视频…）

判等口径用**归一化 JSON 指纹**（`json.dumps(sort_keys=True, 紧凑分隔符)`
的 sha256），所以排版差异也会被认成同一份；只比字节指纹会漏掉①②，
这正是 2026-10-16「清完重复 → 下一轮流水线又导回来」回环的根因
（`import_workflows.py` 的闸门已同步加归一化二次判重）。

留哪一份的判据（rank 小者留）：
  1. 文件名与平台原名一致（`名字_id.json`）优先
  2. id 更小者留 —— RunningHub 是雪花 id，越小越接近原始上传
  3. 所在二级分类文件数少者留 —— 保住「反推提示词」这类小而专的技术分类，
     主分类少一份只是浏览列表里少一行
  4. 路径序，保证确定性

用法：
    python -X utf8 skills/comfyui-learning/tools/dedupe_library.py            # dry-run
    python -X utf8 skills/comfyui-learning/tools/dedupe_library.py --all      # 全库候选（含跨 id 同内容）
    python -X utf8 skills/comfyui-learning/tools/dedupe_library.py --all --apply

默认只查「字节重复 ∪ 同 id 多份」；`--all` 会解析全库（25636 个文件约 2 分钟）
额外抓出跨 id 的同内容副本。文件都在 git 里，删错了 `git checkout --` 即可回滚。
"""
import csv
import hashlib
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LIB = ROOT / "comfyui_library" / "workflows"
LEARN = LIB / "learning"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comfyui_library.database.database import WorkflowDatabase  # noqa: E402
from engine.workflow_learning import LearningStore, WorkflowScanner  # noqa: E402

ID_JSON = re.compile(r"_(\d{8,})\.json$")
BARE_ID = re.compile(r"^(\d{8,})\.json$")


def byte_hash(p: Path) -> str:
    """字节指纹（与学习器 content_hash 同口径，只用于分组候选）"""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(262144), b""):
            h.update(chunk)
    return h.hexdigest()


def norm_hash(p: Path) -> str | None:
    """归一化 JSON 指纹；非工作流（无 nodes / prompt 键）返回 None"""
    try:
        j = json.loads(p.read_text(encoding="utf-8-sig"))
    except Exception:
        return None
    if not isinstance(j, dict):
        return None
    if not isinstance(j.get("nodes"), list) and not isinstance(j.get("prompt"), dict):
        return None
    s = json.dumps(j, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_names() -> dict[str, str]:
    """id → 平台原名（判断文件名是否规范）"""
    names: dict[str, str] = {}
    for pat in (
        "download/workflows-by-tag/**/manifest.csv",
        "download/ids-by-tag/**/*_meta.csv",
    ):
        for mp in ROOT.glob(pat):
            with open(mp, encoding="utf-8-sig") as f:
                for r in csv.DictReader(f):
                    if r.get("id") and (r.get("name") or "").strip():
                        names.setdefault(r["id"].strip(), (r.get("name") or "").strip())
    return names


def main() -> int:
    args = sys.argv[1:]
    apply = "--apply" in args
    scan_all = "--all" in args

    names = load_names()
    t0 = time.time()
    keys = [f["key"] for f in WorkflowScanner().scan(str(LIB))]
    print(f"库内 {len(keys)} 个工作流，算字节指纹…", flush=True)

    by_hash: dict[str, list[str]] = {}
    for k in keys:
        p = LIB / k
        if p.suffix.lower() == ".json" and p.exists():
            by_hash.setdefault(byte_hash(p), []).append(k)
    byte_groups = sum(1 for v in by_hash.values() if len(v) > 1)
    print(f"  {time.time() - t0:.0f}s，字节级重复组 {byte_groups}")

    # 候选：字节重复的 ∪ 同 id 多份的（--all 时全库都算）
    cand: set[str] = set()
    for ks in by_hash.values():
        if len(ks) > 1:
            cand |= set(ks)
    by_id: dict[str, list[str]] = {}
    for k in keys:
        m = ID_JSON.search(k) or BARE_ID.search(Path(k).name)
        if m:
            by_id.setdefault(m.group(1), []).append(k)
    same_id = {i: ks for i, ks in by_id.items() if len(ks) > 1}
    for ks in same_id.values():
        cand |= set(ks)
    if scan_all:
        cand = set(keys)
        print("--all：全库作为候选（抓跨 id 的同内容副本）")
    print(f"同 id 多文件组 {len(same_id)}，候选文件 {len(cand)} 个")

    # 归一化分组
    by_norm: dict[str, list[str]] = {}
    non_wf = 0
    for k in sorted(cand):
        h = norm_hash(LIB / k)
        if h is None:
            non_wf += 1
            continue
        by_norm.setdefault(h, []).append(k)
    groups = {h: ks for h, ks in by_norm.items() if len(ks) > 1}
    pending = sum(len(v) - 1 for v in groups.values())
    print(f"归一化后重复组 {len(groups)}（候选里非工作流 {non_wf} 个跳过）")
    print(f"  组规模: {dict(Counter(len(v) for v in groups.values()))}")
    print(f"  待删副本数: {pending}")
    if not groups:
        print("没有重复，无需处理")
        return 0

    cat_count = Counter(
        "/".join(Path(k).parts[:2]) if len(Path(k).parts) > 2 else Path(k).parts[0]
        for k in keys
    )

    def wid_of(k: str) -> str:
        m = ID_JSON.search(k) or BARE_ID.search(Path(k).name)
        return m.group(1) if m else ""

    def rank(k: str) -> tuple:
        """保留优先级（排在前面的留下，见模块 docstring）"""
        parts = Path(k).parts
        cat = "/".join(parts[:2]) if len(parts) > 2 else parts[0]
        wid = wid_of(k)
        canonical = bool(wid) and Path(k).name == f"{names.get(wid, '')}_{wid}.json"
        return (not canonical, wid or "9" * 19, cat_count[cat], k)

    if not apply:
        print("\n(dry-run) 前 12 组计划：")
        for h, ks in sorted(groups.items(), key=lambda kv: kv[1][0])[:12]:
            ordered = sorted(ks, key=rank)
            print(f"  留 {ordered[0][:66]}")
            for d in ordered[1:]:
                print(f"    删 {d[:66]}")
        print("\n加 --apply 执行")
        return 0

    db = WorkflowDatabase()
    db.auto_save = False
    deleted = {"file": 0, "md": 0, "db": 0}
    moved: Counter = Counter()
    try:
        for h, ks in sorted(groups.items(), key=lambda kv: kv[1][0]):
            ordered = sorted(ks, key=rank)
            keep, drops = ordered[0], ordered[1:]
            for d in drops:
                md = LEARN / (d[: -len(".json")] + ".md")
                if md.exists():
                    md.unlink()
                    deleted["md"] += 1
                if db.workflows.delete(d):
                    deleted["db"] += 1
                p = LIB / d
                if p.exists():
                    p.unlink()
                    deleted["file"] += 1
                kc = "/".join(Path(d).parts[:2]) if len(Path(d).parts) > 2 else Path(d).parts[0]
                kp = "/".join(Path(keep).parts[:2]) if len(Path(keep).parts) > 2 else Path(keep).parts[0]
                moved[f"{kc} → 留 {kp}"] += 1
    finally:
        db.save()
        db.auto_save = True

    print(f"\n删文件 {deleted['file']} | 删记录 {deleted['md']} | 删库行 {deleted['db']}")
    print("分布（删掉的分类 → 保留在哪）:")
    for k, n in moved.most_common():
        print(f"  {n:4d}  {k}")

    store = LearningStore()
    md_keys = {r.key for r in store.all_records()}
    db_keys = {w["id"] for w in db.workflows.all()}
    files = {f["key"] for f in WorkflowScanner().scan(str(LIB))}
    print(f"\n复核：文件 {len(files)} | 记录 {len(md_keys)} | 库行 {len(db_keys)}")
    print(f"  文件^记录 {len(files ^ md_keys)} | 记录^库 {len(md_keys ^ db_keys)}")
    if files ^ md_keys or md_keys ^ db_keys:
        print("!! 三方不一致，先别提交")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())