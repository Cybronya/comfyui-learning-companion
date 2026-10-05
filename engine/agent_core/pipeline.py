"""
Agent Pipeline

把各能力模块编成有序阶段链，逐阶段处理同一个 AgentState。

设计取舍：
    1. 阶段是「对象 + process(state) -> state」而非函数，因为各引擎模块
       本身是带内部状态的对象（GraphBuilder 缓存节点表、ExperimentTracker
       持有经验列表），包一层 process 能统一接口又不丢失对象引用。
    2. 单阶段异常不拖垮整条链路 —— 记入 state.errors 后继续，
       因为「没有诊断信息」时仍可以基于解析+检索给出回答，
       比整条链路失败对用户更有用。
    3. 阶段可跳过：需要的状态不存在时（如没传 workflow 就跳过解析），
       阶段自己 return state，由 Pipeline 统一记录。
"""

import time
from typing import List, Callable

from .state import AgentState
from .config import stages_of


class Stage:
    """
    单个处理阶段
    """

    def __init__(self, name: str, handler: Callable) -> None:
        """
        初始化阶段

        Args:
            name: 阶段名
            handler: 处理函数，签名 (state) -> state 或 None
        """
        self.name = name
        self.handler = handler

    def process(self, state: AgentState) -> AgentState:
        """
        执行阶段

        Args:
            state: 当前状态

        Returns:
            处理后的状态
        """
        result = self.handler(state)
        return result if result is not None else state

    def was_skipped(self, state: AgentState) -> bool:
        """
        本阶段是否被处理器标记为跳过
        """
        return any(
            s["stage"] == self.name
            for s in state.stages_skipped
        )


class AgentPipeline:
    """
    阶段链执行器
    """

    def __init__(self, stages: List[Stage], continue_on_error: bool = True) -> None:
        """
        初始化 pipeline

        Args:
            stages: 阶段列表
            continue_on_error: 单阶段失败是否继续执行后续阶段
        """
        self.stages = list(stages)
        self.continue_on_error = continue_on_error

    def run(self, state: AgentState) -> AgentState:
        """
        依次执行所有阶段

        Args:
            state: 初始状态

        Returns:
            最终状态
        """
        started = time.perf_counter()

        for stage in self.stages:
            try:
                state = stage.process(state)

                # 处理器主动标记跳过的阶段不计入「已执行」，
                # 否则 stages_run 里混着空转阶段，排查时看不出哪步真做了事
                if stage.was_skipped(state):
                    continue

                state.add_stage(stage.name)
            except Exception as e:
                state.add_error(stage.name, e)

                if not self.continue_on_error:
                    state.elapsed_ms = (
                        time.perf_counter() - started
                    ) * 1000
                    raise

        state.elapsed_ms = (time.perf_counter() - started) * 1000
        return state

    def add_stage(self, name: str, handler: Callable) -> None:
        """
        追加一个阶段

        Args:
            name: 阶段名
            handler: 处理函数
        """
        self.stages.append(Stage(name, handler))

    def stage_names(self) -> List[str]:
        """
        当前阶段链的阶段名
        """
        return [s.name for s in self.stages]


def build_pipeline(
    handlers: dict,
    config: dict
) -> AgentPipeline:
    """
    按配置与处理器字典组装 pipeline

    Args:
        handlers: {阶段名: 处理函数}，缺的阶段自动跳过
        config: 配置

    Returns:
        AgentPipeline
    """
    stages = []

    for name in stages_of(config):
        handler = handlers.get(name)
        if handler is not None:
            stages.append(Stage(name, handler))

    return AgentPipeline(
        stages,
        continue_on_error=config.get("continue_on_error", True),
    )
