"""
Autonomous Learning - 自主学习模块

给 Agent 一个任务，它自己去读懂一个未知 workflow。

    任务 + workflow
        ↓
    TaskPlanner            制定计划（真的依赖任务意图与节点特征）
        ↓
    WorkflowExplorer       结构 / 核心节点 / 生成流程链 / 关键参数
        ↓
    KnowledgeRetriever     逐节点检索知识
        ↓
    KnowledgeGapDetector   别名感知地找出「我不知道什么」
        ↓
    Reflection             量化自评 + 给出可执行动作
        ↓
    LearningReport         渲染成人读的报告
        ↓
    KnowledgeEvolution     沉淀（可选）

全程不调 LLM：结论来自 analyzer / retriever / diagnostics 的确定性输出，
所以不会编造参数，也不会出现「模型幻觉出一个不存在的节点」。

主入口：AutonomousLearner.learn() / learn_text()
"""

from .learning_state import LearningState, GapItem
from .task_planner import TaskPlanner, BASE_STEPS
from .workflow_explorer import (
    WorkflowExplorer,
    CATEGORY_TO_STAGE,
    STAGE_ORDER,
)
from .knowledge_gap_detector import KnowledgeGapDetector
from .learning_report import LearningReport
from .reflection import Reflection
from .learner_agent import AutonomousLearner


def create_learner(knowledge=None, **modules) -> AutonomousLearner:
    """
    便捷构造

    Args:
        knowledge: 已知知识（默认从 retriever 索引取）
        **modules: retriever / parser / diagnostics / learner / planner /
                   explorer / gap_detector / report_generator / reflection

    Returns:
        AutonomousLearner 实例
    """
    return AutonomousLearner(knowledge=knowledge, **modules)


__all__ = [
    "LearningState",
    "GapItem",
    "TaskPlanner",
    "BASE_STEPS",
    "WorkflowExplorer",
    "CATEGORY_TO_STAGE",
    "STAGE_ORDER",
    "KnowledgeGapDetector",
    "LearningReport",
    "Reflection",
    "AutonomousLearner",
    "create_learner",
]
