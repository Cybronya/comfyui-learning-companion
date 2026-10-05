"""
Workflow Knowledge Evolution - 工作流知识演化模块

把 learning_loop 产出的孤立经验聚合成可复用的 Pattern Knowledge。

链路：
    Learning Loop 经验  →  ExperienceCollector 归一化
                        →  PatternMiner       挖掘重复模式 + 参数区间
                        →  KnowledgeGenerator 转成可读知识 + 建议
                        →  KnowledgeStore     持久化

对外主入口：evolve()
"""

from .models import (
    WorkflowExperience,
    WorkflowPattern,
    ParameterRange,
    EvolutionKnowledge,
)
from .experience_collector import ExperienceCollector
from .pattern_miner import PatternMiner
from .knowledge_generator import KnowledgeGenerator, RISK_RULES
from .knowledge_store import KnowledgeStore


def evolve(
    experiences=None,
    store_path: str = "engine/knowledge_evolution/evolution_store.json",
    min_frequency: int = 2,
    collector: ExperienceCollector = None,
    save: bool = True
) -> EvolutionKnowledge:
    """
    一次完整演化：经验 → 模式 → 知识 → 存储

    Args:
        experiences: 经验列表（WorkflowExperience / dict），
                      传 None 则从 learning_loop 的 experience_store.json 读取
        store_path: 知识存储路径
        min_frequency: 模式最小出现次数
        collector: 复用已有收集器（需要先 register_nodes 时用得上）
        save: 是否写入存储

    Returns:
        EvolutionKnowledge
    """
    if collector is None:
        collector = ExperienceCollector()

    if experiences is None:
        # 从 learning_loop 的经验库读取。
        # 注意：原始数据不含节点清单，挖出的模式会是残缺节点组合，
        # 所以这里只用于演示链路，真实使用应配合 collector.register_nodes()。
        collector.load_from_store(
            "engine/learning_loop/experience_store.json"
        )
    else:
        for exp in experiences:
            collector.add(exp)

    miner = PatternMiner(min_frequency=min_frequency)
    patterns = miner.mine(collector.get_all())

    generator = KnowledgeGenerator()
    knowledge = generator.generate_knowledge(patterns)

    if save:
        store = KnowledgeStore(store_path)
        store.replace_all(knowledge)

    return knowledge


__all__ = [
    "WorkflowExperience",
    "WorkflowPattern",
    "ParameterRange",
    "EvolutionKnowledge",
    "ExperienceCollector",
    "PatternMiner",
    "KnowledgeGenerator",
    "KnowledgeStore",
    "RISK_RULES",
    "evolve",
]
