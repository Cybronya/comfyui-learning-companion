"""rename_library_workflows.py — 库内 <id>.json 文件批量改为 <名字>_<id>.json。

背景（2026-10-09 用户要求）：库内 workflow 文件一律 名字_id.json 命名。
早期批次 meta 未覆盖时落成了纯 id 文件（3371 个），本脚本五处同步改名：
    ① 库 JSON 文件
    ② 学习记录 .md（文件名 + frontmatter 的 key/file/name 三行）
    ③ WorkflowDatabase 记录 key（id 字段同 key）
    ④ 派生索引（node_index.used_in / workflow_index / pattern_index）
    ⑤ 知识图谱 JSON（workflow 顶点 id + 边端点）

名字来源：下载目录 manifest + 分类 meta 表 + 实验留档；无名字的跳过并列出。

用法：python -X utf8 skills/comfyui-learning/tools/rename_library_workflows.py
    默认 dry-run 只打印计划；--apply 才真正执行。
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LIB = ROOT / "comfyui_library" / "workflows"
LEARN = LIB / "learning"
DB_PATH = ROOT / "comfyui_library" / "database" / "storage" / "workflow_database.json"
GRAPH_PATH = ROOT / "engine" / "knowledge_graph" / "knowledge_graph.json"
BAD = re.compile("[" + re.escape('\\/:*?"<>|') + "\t\n\r]")
ID_JSON = re.compile(r"(\d{8,})\.json$")


def safe_name(s: str) -> str:
    return BAD.sub("_", s).strip().strip(".")[:80]


def load_names() -> dict[str, str]:
    """id -> 名字，来自 manifest / 分类 meta / 实验留档。"""
    names: dict[str, str] = {}
    dl = ROOT / "download" / "workflows-by-tag"
    for mp in dl.rglob("manifest.csv"):
        with open(mp, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r.get("id") and r.get("name"):
                    names.setdefault(r["id"].strip(), r["name"].strip())
    ids_base = ROOT / "download" / "ids-by-tag"
    for mp in ids_base.rglob("*_meta.csv"):
        with open(mp, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r.get("id") and r.get("name"):
                    names.setdefault(r["id"].strip(), r["name"].strip())
    rec = ids_base / "图片生成" / "文生图_rec_new.json"
    if rec.exists():
        for row in json.loads(rec.read_text(encoding="utf-8-sig")):
            names.setdefault(row[0], row[1])
    return names


def build_rename_plan(names: dict[str, str]):
    """返回 [(子路径, 新文件名, wid)]，子路径相对 LIB。"""
    plan = []
    for p in sorted(LIB.rglob("*.json")):
        if "learning" in p.parts:
            continue
        m = ID_JSON.search(p.name)
        if not m:
            continue
        wid = m.group(1)
        safe = safe_name(names.get(wid, ""))
        if not safe or f"{safe}_{wid}.json" == p.name:
            continue
        plan.append((p.relative_to(LIB).as_posix(), f"{safe}_{wid}.json", wid))
    return plan


def rewrite_md(md_path: Path, old_key: str, new_key: str, old_name: str, new_name: str):
    """改 frontmatter 的 key/file/name 三行 + 正文标题里的旧名。"""
    text = md_path.read_text(encoding="utf-8-sig")
    text = text.replace(f"key: {old_key}", f"key: {new_key}", 1)
    text = text.replace(f"file: {old_key}", f"file: {new_key}", 1)
    text = text.replace(f"name: {old_name}", f"name: {new_name}", 1)
    text = text.replace(f"# {old_key}", f"# {new_key}", 1)
    text = text.replace(f"`{old_key}`", f"`{new_key}`")
    md_path.write_text(text, encoding="utf-8")


def main() -> int:
    apply = "--apply" in sys.argv
    names = load_names()
    plan = build_rename_plan(names)
    print(f"计划改名 {len(plan)} 个")

    # 无名字的纯 id 文件列出
    no_name = []
    for p in LIB.rglob("*.json"):
        if "learning" in p.parts:
            continue
        if not re.fullmatch(r"\d{8,}\.json", p.name):
            continue
        if not safe_name(names.get(p.stem, "")):
            no_name.append(p.stem)
    if no_name:
        print(f"⚠ {len(no_name)} 个无名字映射，跳过: {no_name[:5]}")

    if not apply:
        for sub, new_name, _ in plan[:5]:
            print(f"  {sub} -> {new_name}")
        print("（dry-run，加 --apply 执行）")
        return 0

    # --- ① 库文件 + ② 学习记录 ---
    for sub, new_name, _ in plan:
        src = LIB / sub
        dst = src.parent / new_name
        if dst.exists():
            print(f"  目标已存在，跳过: {sub}")
            continue
        old_key = sub
        new_key = (src.parent / new_name).relative_to(LIB).as_posix()
        src.rename(dst)
        # 学习记录
        md = LEARN / (old_key[:-5] + ".md")
        if md.exists():
            old_name = old_key.rsplit("/", 1)[-1][:-5]
            new_md = LEARN / (new_key[:-5] + ".md")
            rewrite_md(md, old_key, new_key, old_name, new_name)
            md.rename(new_md)

    # --- ③ 数据库 ---
    db = json.loads(DB_PATH.read_text(encoding="utf-8-sig"))
    renames = {sub: sub.rsplit("/", 1)[0] + "/" + nn for sub, nn, _ in plan}
    n_db = 0
    for old_key in list(db["workflows"]):
        if old_key in renames:
            w = db["workflows"].pop(old_key)
            new_key = renames[old_key]
            w["id"] = new_key
            w["file_path"] = f"comfyui_library/workflows/{new_key}"
            w["name"] = new_key.rsplit("/", 1)[-1][:-5]
            db["workflows"][new_key] = w
            n_db += 1
    DB_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=4), encoding="utf-8")
    print(f"数据库改 key: {n_db}")

    # --- ④ 派生索引 ---
    for idx_name in ["node_index", "workflow_index", "pattern_index"]:
        ip = DB_PATH.parent / f"{idx_name}.json"
        if not ip.exists():
            continue
        idx = json.loads(ip.read_text(encoding="utf-8-sig"))
        changed = False
        for item in idx.get("workflows", {}).values():
            pass
        # 索引里 workflow id 字段统一替换
        def fix(obj):
            nonlocal changed
            if isinstance(obj, dict):
                for k, v in list(obj.items()):
                    if isinstance(v, str) and v in renames:
                        obj[k] = renames[v]
                        changed = True
                    elif isinstance(v, list) and all(isinstance(x, str) for x in v):
                        newv = [renames.get(x, x) for x in v]
                        if newv != v:
                            obj[k] = newv
                            changed = True
                    else:
                        fix(v)
            elif isinstance(obj, list):
                for i, x in enumerate(obj):
                    if isinstance(x, str) and x in renames:
                        obj[i] = renames[x]
                        changed = True
                    else:
                        fix(x)
        fix(idx)
        # 顶层 workflow 键名也是路径
        for sec in ["workflows", "patterns"]:
            if isinstance(idx.get(sec), dict):
                for k in list(idx[sec]):
                    if k in renames:
                        idx[sec][renames[k]] = idx[sec].pop(k)
                        changed = True
        if changed:
            ip.write_text(json.dumps(idx, ensure_ascii=False, indent=4), encoding="utf-8")
            print(f"{idx_name}: 引用已同步")

    # --- ⑤ 知识图谱 ---
    # 图谱是派生物（build_graph 从学习记录重建），逐点改顶点/边易漏，直接提示重建。
    if GRAPH_PATH.exists():
        print("知识图谱: 派生物，请重跑 build_graph() 重建（python -m engine 或 learn_pipeline 第 6 步）")
    print("完成")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
