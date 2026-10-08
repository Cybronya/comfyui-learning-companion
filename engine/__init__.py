"""
ComfyUI Learning Companion Engine

把零散 ComfyUI Workflow 转化为结构化知识的可执行引擎。

对外统一入口（推荐用法）：

    from engine import create_agent

        agent = create_agent()
        print(agent.ask_text("为什么图很僵硬", "workflow.json"))

能力工厂一览（详细说明见各子包 __init__）：

    create_agent                 六阶段问答总控（context → parse → analyze
                                 → diagnose → retrieve → respond）
    AutonomousLearner            给任务自主读懂未知 workflow
    create_batch_learner         批量学习一个目录（幂等）
    create_scheduler             学习调度（先学什么 / 断点续跑）
    create_consolidation_engine  归纳一批学习记录 → 通用模式
    build_graph                  重建跨条目知识图谱

命令行入口（不写代码直接用）：

    python -m engine ask "为什么图很僵硬" --workflow path/to/wf.json
"""

from .learning_engine import LearningEngine
from .agent_core import (
    AgentState,
    ComfyUIAgent,
    DEFAULT_CONFIG,
    create_agent,
)
from .autonomous_learning import AutonomousLearner
from .workflow_learning import create_batch_learner
from .learning_scheduler import create_scheduler
from .knowledge_consolidation import create_consolidation_engine
from .knowledge_graph import build_graph

__all__ = [
    # 问答总控
    "ComfyUIAgent",
    "create_agent",
    "AgentState",
    "DEFAULT_CONFIG",
    # 自主学习
    "AutonomousLearner",
    # 批量学习 / 调度 / 归纳 / 图谱
    "create_batch_learner",
    "create_scheduler",
    "create_consolidation_engine",
    "build_graph",
    # 兼容旧用法（2026-10-04 最小闭环类）
    "LearningEngine",
]
