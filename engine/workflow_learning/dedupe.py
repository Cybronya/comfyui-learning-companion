# -*- coding: utf-8 -*-
"""
聚合层内容去重。

同一个 workflow 常以不同文件名/平台 id 重复上传（2026-10-06 实测：
504 条记录里 45 组内容完全相同，涉及 96 条）。学习层**不去重**——
记录按 key 查找、判重学都依赖逐条存在；但**聚合统计必须去重**，
否则频次、共现、模式归纳都会把同一份文件数两遍：

    - 节点频次被夸大（最坏 2 倍：只在重复文件里出现的节点）
    - min_frequency=2 的模式归纳可能被「一个文件传两次」凑出假模式
    - 参数统计被同一作者的取值加权

使用方：learning_store.node_frequency / knowledge_graph.GraphBuilder /
knowledge_consolidation.ExperienceLoader。
"""

from typing import Iterable, List, Tuple


def dedupe_by_content_hash(records: Iterable) -> Tuple[List, int]:
    """
    按 content_hash 去重，保留首次出现

    Args:
        records: 带 content_hash 属性或字典键的记录（LearningRecord /
                 database experience 的 data dict 均可）

    Returns:
        (去重后的列表, 丢弃条数)。content_hash 为空的记录全部保留
        （没有指纹就无法判定相同，宁可多算不可漏算）。
    """
    seen = set()
    unique: List = []
    dropped = 0

    for record in records:
        if isinstance(record, dict):
            h = record.get("content_hash", "")
        else:
            h = getattr(record, "content_hash", "")
        if h:
            if h in seen:
                dropped += 1
                continue
            seen.add(h)
        unique.append(record)

    return unique, dropped
