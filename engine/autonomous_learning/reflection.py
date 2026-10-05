"""
自我反思

学习完成后 Agent 自问：这次到底学懂了吗？还差什么？下一步做什么？

设计文档给的 reflect() 只输出两句固定文案（「需要补充节点知识」/「Workflow理解不足」），
信息量为零 —— 拿到这两句也无法决定下一步。反思的价值在于给出**可判断的结论**：
    1. 覆盖率与等级（够不够）
    2. 具体缺什么（缺口清单，按核心程度排序）
    3. 建议动作（能不能直接拿去建卡 / 补什么参数）
    4. 风险提示（有没有关键节点缺卡）
"""

from typing import List

from .learning_state import LearningState, GapItem


# 等级 → 结论与下一步
LEVEL_JUDGMENT = {
    "excellent": (
        "已完全掌握",
        "可以基于这个工作流做参数优化或迁移实验",
    ),
    "good": (
        "基本掌握",
        "可以开始实操验证，个别节点建议补卡",
    ),
    "partial": (
        "部分掌握",
        "能理解主流程，但不足以解释细节表现，建议补齐缺口后再实验",
    ),
    "insufficient": (
        "尚未掌握",
        "关键节点缺少知识，建议先补卡再重新学习",
    ),
}


class Reflection:
    """
    学习反思器
    """

    def reflect(self, state: LearningState) -> List[str]:
        """
        生成反思结论

        Args:
            state: 学习状态（调用前应先跑过 compute_metrics）

        Returns:
            反思要点列表
        """
        result: List[str] = []

        state.compute_metrics()

        judgment, next_action = LEVEL_JUDGMENT.get(
            state.level, ("未知", "建议重新执行学习流程")
        )

        result.append(
            f"**理解程度：{judgment}**"
            f"（置信度 {state.confidence:.0%}，"
            f"核心节点覆盖 {state.core_coverage:.0%}，"
            f"整体覆盖 {state.coverage:.0%}）"
        )
        result.append(f"**下一步**：{next_action}")

        # 缺口清单
        if state.missing_knowledge:
            hard_gaps = [
                g for g in state.missing_knowledge
                if g.coverage == "none"
            ]
            soft_gaps = [
                g for g in state.missing_knowledge
                if g.coverage != "none"
            ]

            parts = [f"缺少 {len(state.missing_knowledge)} 个节点的知识"]
            if hard_gaps:
                parts.append(f"其中 {len(hard_gaps)} 个完全无知识")
            if soft_gaps:
                parts.append(
                    f"{len(soft_gaps)} 个仅有同族通用知识"
                )
            result.append("**知识缺口**：" + "；".join(parts))

            # 全部列出节点名 —— 只给个数的话用户无法知道要补哪些卡
            for gap in hard_gaps:
                mark = "核心" if gap.is_core else "次要"
                result.append(
                    f"  - `{gap.node_type}`（{mark}，无知识）→ {gap.reason}"
                )
            for gap in soft_gaps:
                mark = "核心" if gap.is_core else "次要"
                result.append(
                    f"  - `{gap.node_type}`（{mark}，仅通用知识）→ {gap.reason}"
                )
        else:
            result.append(
                "**知识缺口**：无，工作流所有节点都有对应知识"
            )

        # 关键风险
        if state.blocking_gaps:
            result.append(
                "**风险**：核心节点 "
                + "、".join(state.blocking_gaps)
                + " 完全无知识，理解等级已被强制下调 —— "
                "在这些节点补卡前，不要基于本次学习做参数决策"
            )
        elif state.core_coverage < 0.5:
            result.append(
                "**风险**：核心节点过半没有知识，"
                "此时生成的回答不可信，建议先补卡"
            )

        # 参数理解
        if not state.parameters:
            result.append(
                "**参数**：未能提取到关键参数，"
                "无法解释生成质量，需检查 widgets_values 是否完整"
            )
        else:
            key_params = [
                k for k in ("cfg", "steps", "sampler_name", "denoise")
                if k in state.parameters
            ]
            if key_params:
                result.append(
                    "**参数**：已提取 "
                    + "、".join(key_params)
                    + "，共 " + str(len(state.parameters)) + " 项"
                )

        # 流程链自检
        if not state.pipeline:
            result.append(
                "**流程链**：未能推导生成流程阶段，"
                "说明节点类型都不在已知映射表里，属知识盲区"
            )
        else:
            result.append(
                "**流程链**：" + " → ".join(state.pipeline)
            )

        return result

    def action_items(self, state: LearningState) -> List[str]:
        """
        产出可执行动作（用于「请求知识」环节）

        Args:
            state: 学习状态

        Returns:
            动作描述列表
        """
        actions: List[str] = []

        for gap in state.missing_knowledge:
            mark = "核心" if gap.is_core else "次要"

            if gap.coverage == "related":
                actions.append(
                    f"补建知识卡：节点 {gap.node_type}"
                    f"（{mark}，可参考 {gap.related_topics[0]} 的现有卡"
                    f"做对照，只补差异部分）"
                )
            elif gap.related_topics:
                actions.append(
                    f"补建知识卡：节点 {gap.node_type}"
                    f"（{mark}，属 {gap.related_topics[0]} 主题，"
                    f"该主题整体缺卡）"
                )
            else:
                actions.append(
                    f"补建知识卡：节点 {gap.node_type}"
                    f"（{mark}，当前主题表未覆盖，"
                    f"建议同时补充主题映射）"
                )

        if not state.parameters:
            actions.append("检查 workflow 的 widgets_values 是否缺失")

        if not state.pipeline:
            actions.append(
                "补充节点类别映射："
                "在 workflow_explorer.CATEGORY_TO_STAGE 登记新节点"
            )

        return actions
