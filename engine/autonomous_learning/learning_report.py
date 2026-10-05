"""
学习报告生成

把学习状态渲染成人能直接读懂的学习报告。

设计文档用 f-string 直接插列表，输出会是 `['KSampler', 'VAEDecode']`
这种 Python 字面量，报告是给人看的（也是沉淀进知识库的资料），
所以这里逐字段显式渲染。
"""

from typing import List

from .learning_state import LearningState


# 等级 → 徽章
LEVEL_BADGE = {
    "excellent": "✅ 已掌握",
    "good": "🟢 基本掌握",
    "partial": "🟡 部分掌握",
    "insufficient": "🔴 尚未掌握",
}

STAGE_LABELS = {
    "Model": "加载模型",
    "Encode": "编码到潜空间",
    "Condition": "文本条件",
    "Latent": "初始潜空间",
    "Control": "额外控制",
    "Sampling": "采样生成",
    "Decode": "解码出图",
    "Process": "后处理",
    "Output": "保存输出",
    "Other": "未识别",
}

PARAM_LABELS = {
    "seed": "随机种子",
    "steps": "采样步数",
    "cfg": "Prompt 约束强度",
    "sampler_name": "采样算法",
    "scheduler": "调度器",
    "denoise": "重绘幅度",
    "width": "宽度",
    "height": "高度",
    "batch_size": "批量数量",
    "checkpoint": "底模",
    "lora_name": "LoRA",
    "strength_model": "LoRA 模型强度",
    "strength_clip": "LoRA 文本强度",
    "controlnet_strength": "ControlNet 权重",
}


class LearningReport:
    """
    学习报告生成器
    """

    def generate(self, state: LearningState) -> str:
        """
        生成学习报告

        Args:
            state: 学习状态

        Returns:
            Markdown 报告
        """
        state.compute_metrics()

        sections = [
            self._header(state),
            self._understanding(state),
            self._pipeline(state),
            self._parameters(state),
            self._knowledge_section(state),
            self._gap_section(state),
            self._findings_section(state),
            self._reflection_section(state),
            self._plan_section(state),
            self._footer(state),
        ]

        return "\n\n".join(s for s in sections if s)

    # ---------- 各段 ----------

    def _header(self, state: LearningState) -> str:
        """任务与总体结论"""
        lines = [
            "# Workflow 学习报告",
            "",
            f"**学习任务**：{state.task or '（未指定）'}",
            "",
            f"**理解程度**：{LEVEL_BADGE.get(state.level, state.level)}"
            f"　置信度 {state.confidence:.0%}",
            "",
            f"- 工作流类型：{state.analysis.get('workflow_type') or '未识别'}",
            f"- 节点总数：{len(state.nodes())}",
            f"- 核心节点：{len(state.core_nodes)}",
            f"- 知识覆盖：{state.coverage:.0%}"
            f"（核心 {state.core_coverage:.0%}）",
        ]

        if state.workflow_path:
            lines.append(f"- 来源文件：`{state.workflow_path}`")

        return "\n".join(lines)

    def _understanding(self, state: LearningState) -> str:
        """结构理解：核心节点 + 识别到的模式"""
        lines = ["## 结构理解"]

        if state.core_nodes:
            lines.append("")
            lines.append("**核心节点**（对生成结果有实质影响）：")
            for node in state.core_nodes:
                lines.append(f"- `{node}`")
        else:
            lines.append("")
            lines.append("未识别出核心节点（节点类别信息缺失）。")

        nodes = state.nodes()
        if nodes:
            minor = [n for n in nodes if n not in state.core_nodes]
            if minor:
                lines.append("")
                lines.append("其他节点：")
                lines.append(
                    "、".join(f"`{n}`" for n in minor)
                )

        patterns = state.analysis.get("patterns", [])
        if patterns:
            lines.append("")
            lines.append("**识别到的模式**：")
            for pattern in patterns:
                lines.append(f"- {pattern}")

        return "\n".join(lines)

    def _pipeline(self, state: LearningState) -> str:
        """生成流程链"""
        lines = ["## 生成流程"]

        if not state.pipeline:
            lines.append("")
            lines.append("未能推导流程阶段。")
            return "\n".join(lines)

        stages = state.analysis.get("stages", {})

        lines.append("")
        lines.append(
            " → ".join(
                STAGE_LABELS.get(s, s) for s in state.pipeline
            )
        )
        lines.append("")
        lines.append("各阶段节点：")

        for stage in state.pipeline:
            nodes = stages.get(stage, [])
            label = STAGE_LABELS.get(stage, stage)
            if nodes:
                lines.append(
                    f"- **{label}**："
                    + "、".join(f"`{n}`" for n in nodes)
                )

        return "\n".join(lines)

    def _parameters(self, state: LearningState) -> str:
        """关键参数"""
        lines = ["## 关键参数"]

        if not state.parameters:
            lines.append("")
            lines.append("未提取到关键参数。")
        else:
            lines.append("")
            for name, value in state.parameters.items():
                label = PARAM_LABELS.get(name, name)
                lines.append(f"- {label}（`{name}`）= `{value}`")

        # 参数体检结果单列，不混进参数清单
        if state.diagnostic_findings:
            lines.append("")
            lines.append("**体检发现的问题**：")
            for item in state.diagnostic_findings:
                lines.append(f"- {item}")

        return "\n".join(lines)

    def _knowledge_section(self, state: LearningState) -> str:
        """用到的知识"""
        lines = ["## 用到的知识"]

        if not state.knowledge_used:
            lines.append("")
            lines.append("未检索到任何知识。")
            return "\n".join(lines)

        lines.append("")
        for item in state.knowledge_used:
            name = item.get("name", "未命名")
            kind = item.get("type", "knowledge")
            covers = item.get("covers_nodes", [])
            source = item.get("source", "")

            line = f"- **[{kind}]** {name}"
            if covers:
                line += f"　覆盖节点：" + "、".join(covers)
            lines.append(line)

            if source:
                lines.append(f"    - 来源：`{source}`")

        return "\n".join(lines)

    def _gap_section(self, state: LearningState) -> str:
        """知识缺口 —— 自主学习的重点"""
        lines = ["## 知识缺口"]

        if not state.missing_knowledge:
            lines.append("")
            lines.append(
                "无。工作流涉及的节点全部有对应知识，可以放心做参数实验。"
            )
            return "\n".join(lines)

        lines.append("")
        lines.append(f"共 {len(state.missing_knowledge)} 处缺口：")

        for gap in state.missing_knowledge:
            mark = "**核心**" if gap.is_core else "次要"
            cov = (
                "完全无知识" if gap.coverage == "none"
                else "仅有通用知识"
            )
            lines.append("")
            lines.append(f"- `{gap.node_type}`（{mark}，{cov}）")
            lines.append(f"    - 原因：{gap.reason}")
            if gap.related_topics:
                lines.append(
                    "    - 相关主题：" + "、".join(gap.related_topics)
                )

        return "\n".join(lines)

    def _findings_section(self, state: LearningState) -> str:
        """专项分析结论"""
        if not state.step_findings:
            return ""

        lines = ["## 专项分析"]

        for step, conclusion in state.step_findings.items():
            lines.append(f"- **{step}**")
            lines.append(f"    - {conclusion}")

        return "\n".join(lines)

    def _reflection_section(self, state: LearningState) -> str:
        """反思"""
        lines = ["## 自我评估"]

        if not state.discoveries:
            return ""

        for item in state.discoveries:
            lines.append(f"- {item}")

        return "\n".join(lines)

    def _plan_section(self, state: LearningState) -> str:
        """学习计划回顾"""
        if not state.plan:
            return ""

        from .task_planner import TaskPlanner
        from .learner_agent import BASE_STEP_EXECUTIONS

        descriptions = TaskPlanner().explain(state.plan)
        done = set(state.steps_run)

        lines = ["## 学习计划"]

        for i, (step, desc) in enumerate(
            zip(state.plan, descriptions), 1
        ):
            execution = BASE_STEP_EXECUTIONS.get(step, step)
            executed = execution in done

            if executed:
                mark = "✅"
            elif step in state.step_findings:
                mark = "✅"
            else:
                mark = "⏭️"

            lines.append(f"{i}. {mark} {desc}　`{step}`")

        return "\n".join(lines)

    def _footer(self, state: LearningState) -> str:
        """过程信息与沉淀"""
        lines = []

        if state.steps_run:
            lines.append(
                "## 执行过程\n\n"
                + " → ".join(state.steps_run)
            )

        if state.deposited:
            lines.append(
                "## 知识沉淀\n\n已写入知识库：\n"
                + "\n".join(
                    f"- {d.get('kind', '知识')}：{d.get('name', '')}"
                    for d in state.deposited
                )
            )

        if state.has_errors:
            lines.append(
                "## 执行中的问题\n\n"
                + "\n".join(
                    f"- [{e['step']}] {e['message']}"
                    for e in state.errors
                )
            )

        if state.elapsed_ms:
            lines.append(f"耗时 {state.elapsed_ms:.0f}ms")

        return "\n".join(lines)
