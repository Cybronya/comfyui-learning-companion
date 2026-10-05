"""
Knowledge Retrieval - 知识检索模块

把项目已积累的四类知识（节点卡 / Pattern / 调整经验 / 演化知识）接到回答流程上。

    用户问题
       ↓
    KnowledgeMatcher   识别主题（支持中英文、多节点类型别名）
       ↓
    KnowledgeIndex     倒排索引查召回
       ↓
    KnowledgeRanker    按「是否在当前工作流 + 类型可信度」排序
       ↓
    format_for_prompt  拼成 response_generator 可直接用的文本

主入口：KnowledgeRetriever.retrieve()
"""

from .knowledge_matcher import KnowledgeMatcher
from .knowledge_index import KnowledgeIndex
from .ranking import KnowledgeRanker, TRUSTED_TYPES
from .retriever import (
    KnowledgeRetriever,
    DEFAULT_INDEX_PATH,
    KNOWLEDGE_DIR,
    EXPERIENCE_STORE,
    EVOLUTION_STORE,
)

__all__ = [
    "KnowledgeMatcher",
    "KnowledgeIndex",
    "KnowledgeRanker",
    "TRUSTED_TYPES",
    "KnowledgeRetriever",
    "DEFAULT_INDEX_PATH",
    "KNOWLEDGE_DIR",
    "EXPERIENCE_STORE",
    "EVOLUTION_STORE",
]
