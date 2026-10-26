"""
RAG 检索（v0.6 第 4 步）

键名统一：读 `content`（历史索引里是 `text`，按 `content` → `text` 顺序兜底）。

匹配改进：原来只做整串 `query.lower() in content.lower()`，
查询词只要是整串才命中。现在拆成词元逐个匹配（全部命中才算命中），
这样搜「KSampler 采样」也能命中只写了「KSampler」但正文里分散描述的文档。
"""

from typing import List


def _doc_text(doc: dict) -> str:
    """取文档正文，兼容 content / text 两种键名。"""
    for key in ("content", "text"):
        value = doc.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def _tokenize(query: str) -> List[str]:
    """把查询拆成词元。中文按空格/标点切，英文按空格切并小写。"""
    import re
    parts = re.split(r"[\s,，、;；/]+", query.strip())
    return [p for p in parts if p]


def search(query, documents, limit: int = 0):
    """在文档中检索。

    Args:
        query: 查询串
        documents: 文档列表（键名 content 或 text 均可）
        limit: 最多返回条数，0 = 不限

    Returns:
        命中的文档列表（保持原顺序）
    """
    if not query or not query.strip():
        return []

    result = []
    lowered_q = query.strip().lower()
    tokens = [t.lower() for t in _tokenize(query)]

    for doc in documents:
        text = _doc_text(doc)
        if not text:
            continue
        lowered = text.lower()

        # 整串命中 → 直接算
        if lowered_q in lowered:
            result.append(doc)
            continue

        # 词元全命中 → 也算（多词查询更宽容）
        if tokens and all(t in lowered for t in tokens):
            result.append(doc)
            continue

    if limit and limit > 0:
        return result[:limit]
    return result
