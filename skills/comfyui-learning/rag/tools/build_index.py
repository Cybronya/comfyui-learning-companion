"""
RAG 索引构建（v0.6 第 4 步）

键名统一：产出 `content`（原来产出 `text`，而 search_database 读 `content`，
两边对不上，检索永远读不到正文）。

同时保留 `text` 作为兼容别名——历史落盘的索引文件里是 `text`，
读旧索引的调用方不应因此崩掉。检索侧按 `content` → `text` 的顺序取。
"""

import json
import argparse


def build_index(documents):
    """把文档列表转成索引条目。

    Args:
        documents: [{"type", "content", "metadata"}, ...]

    Returns:
        [{"content", "text", "type", "metadata"}, ...]
    """
    index = []

    for doc in documents:
        content = doc.get("content", "")
        index.append({
            "content": content,
            # 兼容别名：历史索引用 text
            "text": content,
            "type": doc.get("type", ""),
            "metadata": doc.get("metadata", {}),
        })

    return index


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="把文档列表转成索引")
    ap.add_argument("source", help="文档 JSON 文件")
    ap.add_argument("--out", help="输出 JSON 文件")
    args = ap.parse_args()

    with open(args.source, encoding="utf-8-sig") as f:
        docs = json.load(f)

    payload = json.dumps(build_index(docs), ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload)
    else:
        print(payload)
