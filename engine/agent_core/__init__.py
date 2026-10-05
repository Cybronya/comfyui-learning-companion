"""
Agent Core - ComfyUI Learning Agent 总控模块

把九个独立能力模块编成一个可用的 Agent。

    用户提问 (+ 可选 workflow)
          ↓
    context      记录问题到会话上下文
          ↓
    parse        workflow_parser    JSON → WorkflowKnowledge
          ↓
    analyze      workflow_analyzer  图构建 / 模式识别 / 分类
          ↓
    diagnose     diagnostics        参数 / 图结构 / 质量诊断
          ↓
    retrieve     retrieval          关键词召回 + 排序
          ↓
    respond      response_generator  生成教学回答

离线能力（不在 ask 链路上）：
    evolve()      knowledge_evolution  经验 → 模式知识
    build_index() retrieval            重建检索索引
    set_workflow()                     只登记工作流，供连续追问

主入口：ComfyUIAgent.ask()
"""

from .state import AgentState
from .config import (
    DEFAULT_CONFIG,
    merge_config,
    stages_of,
)
from .pipeline import (
    Stage,
    AgentPipeline,
    build_pipeline,
)
from .agent import ComfyUIAgent


def create_agent(config=None, **modules) -> ComfyUIAgent:
    """
    便捷构造：按需注入模块，未注入的环节自动降级跳过

    Args:
        config: 配置覆盖项
        **modules: parser / analyzer / context / diagnostics /
                   retriever / generator / learner

    Returns:
        ComfyUIAgent 实例
    """
    return ComfyUIAgent(config=config, **modules)


__all__ = [
    "AgentState",
    "Stage",
    "AgentPipeline",
    "build_pipeline",
    "ComfyUIAgent",
    "create_agent",
    "DEFAULT_CONFIG",
    "merge_config",
    "stages_of",
]
