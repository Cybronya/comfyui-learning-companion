"""
RAG 文档准备（v0.6 第 4 步）

按 `skills/comfyui-learning/rag/rag_rules.md` 的「Document Types」把原始数据
转成可检索文档。

改动要点（2026-10-26）：
    1. **content 不再是 `str(item)`**。原来把整个 dict 的 Python repr 塞进
       content，检索时命中的是 `{'name': 'KSampler', 'usage_count': 42}` 这种
       噪声文本，真正的语义字段被引号和括号淹没。
       现在按文档类型把关键字段拼成自然语言，content 是人能读的摘要，
       metadata 保留完整原对象供过滤与排序。
    2. **键名统一为 `content`**。原来 build_index 产出 `text`、
       search_database 读 `content`，两者对不上，等于检索永远读不到正文。

三类文档的字段转换（依 rag_rules.md）：
    workflow → Name / Category / Nodes / Models / Description / Parameters
    node     → Name / Purpose / Input / Output / Category
    model    → Name / Type / Architecture / Compatibility / Requirement
"""

import json
import argparse
from typing import Any, Dict, List


def load_json(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


# ---- 各类型的字段别名表：同一个语义在不同来源里可能叫不同的名字 ----

_WORKFLOW_FIELDS = {
    "name": ("name", "workflow_name", "title", "workflow"),
    "category": ("category", "task_type", "type", "classification"),
    "nodes": ("nodes", "node_types", "node_list", "used_nodes"),
    "models": ("models", "model_names", "model_list", "checkpoints"),
    "description": ("description", "summary", "desc", "brief"),
    "parameters": ("parameters", "params", "settings", "config"),
}

_NODE_FIELDS = {
    "name": ("name", "node", "node_type", "title"),
    "purpose": ("purpose", "description", "summary", "desc"),
    "input": ("input", "inputs", "input_types"),
    "output": ("output", "outputs", "output_types"),
    "category": ("category", "type", "classification"),
}

_MODEL_FIELDS = {
    "name": ("name", "model", "model_name", "title"),
    "type": ("type", "model_type", "kind"),
    "architecture": ("architecture", "arch", "family"),
    "compatibility": ("compatibility", "compatible_with", "supports"),
    "requirement": ("requirement", "requirements", "note"),
}

_FIELD_MAPS = {
    "workflow": _WORKFLOW_FIELDS,
    "node": _NODE_FIELDS,
    "model": _MODEL_FIELDS,
}


def _pick(item: Dict, aliases) -> Any:
    """按别名列表取第一个有值的字段。"""
    if not isinstance(item, dict):
        return None
    for key in aliases:
        if key in item and item[key] not in (None, "", [], {}):
            return item[key]
    return None


def _as_text(value: Any) -> str:
    """把字段值转成适合放进正文的一行文本。"""
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (list, tuple, set)):
        return "、".join(_as_text(v) for v in value if v is not None and str(v).strip())
    if isinstance(value, dict):
        # dict 展开成 key: value，避免整个 repr 进正文
        return "；".join(
            f"{k}: {_as_text(v)}" for k, v in value.items() if v not in (None, "", [], {})
        )
    return str(value).strip()


def _compose(doc_type: str, item: Dict) -> str:
    """按文档类型拼装 content 正文。"""
    field_map = _FIELD_MAPS.get(doc_type)
    if field_map is None:
        # 未知类型：只取常见字段，至少别退化成 repr
        parts = []
        for key in ("name", "title", "description", "summary"):
            val = _pick(item, (key,))
            if val:
                parts.append(_as_text(val))
        return "；".join(parts) if parts else _as_text(item)

    lines: List[str] = []
    for label, aliases in field_map.items():
        val = _pick(item, aliases)
        if val in (None, "", [], {}):
            continue
        text = _as_text(val)
        if not text:
            continue
        if label == "name":
            lines.insert(0, text)
        else:
            lines.append(f"{label}: {text}")
    return "\n".join(lines)


def create_documents(data_type, data):
    """把原始数据转成文档列表。

    Args:
        data_type: "workflow" / "node" / "model"（其它类型按通用规则处理）
        data: 原始数据（dict 列表，或 dict-of-lists）

    Returns:
        [{"type": ..., "content": ..., "metadata": ...}, ...]
    """
    if isinstance(data, dict):
        # dict-of-lists：合并各分类的条目
        items: List[Dict] = []
        for value in data.values():
            if isinstance(value, list):
                items.extend(x for x in value if isinstance(x, dict))
            elif isinstance(value, dict):
                items.append(value)
    elif isinstance(data, list):
        items = [x for x in data if isinstance(x, dict)]
    else:
        items = []

    docs = []
    for item in items:
        docs.append({
            "type": data_type,
            "content": _compose(data_type, item),
            "metadata": item,
        })
    return docs


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="把原始数据转成 RAG 文档")
    ap.add_argument("source", help="源 JSON 文件")
    ap.add_argument("--type", dest="doc_type", default="workflow",
                    choices=["workflow", "node", "model"])
    ap.add_argument("--out", help="输出 JSON 文件（默认打印到 stdout）")
    args = ap.parse_args()

    docs = create_documents(args.doc_type, load_json(args.source))
    payload = json.dumps(docs, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload)
    else:
        print(payload)
