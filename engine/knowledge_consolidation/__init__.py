"""
Knowledge Consolidation - 工作流知识归纳

把「一堆 workflow」变成「几条通用规律」。

    workflows/learning/*.md（每个 workflow 一份学习记录）
        ↓ ExperienceLoader
    ExperienceRow
        ↓ PatternMiner        按 workflow_type 分组 + Jaccard 相似度聚类
    WorkflowPattern
        ↓ ParameterStatistics 逐模式统计（不跨模式混合）
        ↓ KnowledgeBuilder    聚合常见问题 + 生成建议
    ConsolidatedKnowledge
        ↓ KnowledgeStore      写 Markdown + index.md
    comfyui_library/knowledge/patterns/_consolidated/

与 knowledge_evolution 的分工（并存，非重复）：
    knowledge_evolution      从「参数改动记录」归纳 → 「改这个参数会怎样」
    knowledge_consolidation  从「完整 workflow」归纳 → 「这类流程长什么样、
                            常用什么参数、容易踩什么坑」

三个刻意的设计取舍：

1. **聚类不用精确节点集合相等**。真实 workflow 几乎不会节点完全相同，
   差一个 LoraLoader 就归不到同一模式（Jaccard 相似度解决）。
   knowledge_evolution 的 PatternMiner 目前仍是精确匹配，
   同样有这个局限，后续可考虑让它复用这里的聚类。

2. **参数统计按模式分组**。全局混算会让 SD1.5 与 Wan 的步数平均成
   没有代表性的数字，而且所有模式会拿到同一份结果，等于没分组。

3. **常见问题必须聚合**。诊断结论在各 workflow 的体检里，
   不汇总就丢掉「这个模式最常踩什么坑」这条最有价值的知识。

全程不调 LLM：所有结论来自 analyzer / diagnostics 的确定性计算。

主入口：ConsolidationEngine.consolidate()
"""

from .models import (
    WorkflowPattern,
    ConsolidatedKnowledge,
    ParameterStat,
    LEVEL_STRONG,
    LEVEL_MODERATE,
    LEVEL_WEAK,
)
from .experience_loader import ExperienceLoader, ExperienceRow
from .pattern_miner import PatternMiner, jaccard, FEATURE_HINTS, IGNORED_NODES
from .parameter_statistics import (
    ParameterStatistics,
    INTERESTING_PARAMS,
    NOISE_PARAMS,
)
from .knowledge_builder import KnowledgeBuilder
from .knowledge_store import KnowledgeStore, DEFAULT_FOLDER
from .consolidation_engine import ConsolidationEngine


def create_consolidation_engine(
    store_path: str = None,
    similarity: float = 0.6,
    min_frequency: int = 2,
    save: bool = True,
) -> ConsolidationEngine:
    """
    便捷构造

    Args:
        store_path: 输出目录；None 时用默认
                   comfyui_library/knowledge/patterns/_consolidated/
        similarity: 聚类相似度阈值
        min_frequency: 模式最小成员数
        save: 归纳时是否落盘

    Returns:
        ConsolidationEngine 实例
    """
    engine = ConsolidationEngine(
        miner=PatternMiner(
            similarity=similarity, min_frequency=min_frequency
        ),
        store=KnowledgeStore(store_path) if store_path else KnowledgeStore(),
    )

    return engine


__all__ = [
    "WorkflowPattern",
    "ConsolidatedKnowledge",
    "ParameterStat",
    "LEVEL_STRONG",
    "LEVEL_MODERATE",
    "LEVEL_WEAK",
    "ExperienceLoader",
    "ExperienceRow",
    "PatternMiner",
    "jaccard",
    "FEATURE_HINTS",
    "IGNORED_NODES",
    "ParameterStatistics",
    "INTERESTING_PARAMS",
    "NOISE_PARAMS",
    "KnowledgeBuilder",
    "KnowledgeStore",
    "DEFAULT_FOLDER",
    "ConsolidationEngine",
    "create_consolidation_engine",
]
