"""
回答构造器（无 LLM）

把 AgentState 里的各阶段产物拼成人能直接读懂的中文回答。

不调 LLM，纯规则拼装。理由：
    1. 本项目回答的是「你的工作流 CFG=30 太高了，先降到 7-10」这类**有确定答案**的问题，
       依据已在 diagnostics（实测值 + 阈值）和知识卡（参数说明）里，
       交给规则拼装比让模型自由发挥更可控，也不会编造参数。
    2. 无需 API key、无网络、可离线复现。
    3. 模板化输出结构固定，用户能预期每次回答长什么样。

代价：开放性提问（「讲讲扩散模型」）只能给出知识卡里的原文要点，
不会做推理和举例。这类需求才真正需要 LLM。
"""

from typing import List, Dict, Any

from .knowledge_distiller import KnowledgeDistiller


# 严重度 → 中文标签与处理建议语气
SEVERITY_LABELS = {
    "high": "严重",
    "critical": "严重",
    "medium": "中等",
    "low": "轻微",
    "info": "提示",
}

# 严重度排序权重，诊断问题按此从重到轻排列
SEVERITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "info": 4,
}

# 问题类型 → 归类标题，让回答更像「分析报告」而不是散乱清单。
# 取值需与 diagnostics 三个 checker 实际产出的 issue_type 对齐：
#   parameter_checker → parameter_warning
#   graph_checker     → missing_node
#   quality_checker   → workflow_warning
ISSUE_CATEGORY = {
    "parameter_warning": "参数问题",
    "parameter": "参数问题",
    "missing_node": "缺失节点",
    "node": "缺失节点",
    "graph": "连接问题",
    "workflow_warning": "结构问题",
    "quality": "结构问题",
}


class AnswerBuilder:
    """
    把 AgentState 拼成可读回答
    """

    def __init__(self, distiller: KnowledgeDistiller = None) -> None:
        """
        初始化构造器

        Args:
            distiller: 知识蒸馏器
        """
        self.distiller = distiller or KnowledgeDistiller()

    def build(self, state: Any) -> str:
        """
        构造完整回答

        Args:
            state: AgentState（或任何具备相同字段属性的对象）

        Returns:
            Markdown 格式的中文回答
        """
        blocks = []

        conclusion = self._conclusion(state)
        if conclusion:
            blocks.append(conclusion)

        workflow_block = self._workflow_block(state)
        if workflow_block:
            blocks.append(workflow_block)

        issue_block = self._issues_block(state)
        if issue_block:
            blocks.append(issue_block)

        knowledge_block = self._knowledge_block(state)
        if knowledge_block:
            blocks.append(knowledge_block)

        actions_block = self._actions_block(state)
        if actions_block:
            blocks.append(actions_block)

        if not blocks:
            return (
                "这个问题我暂时没有足够的信息来回答。\n\n"
                "可以试着：\n"
                "- 提供当前的 workflow.json，让我能读取实际参数\n"
                "- 换个更具体的说法，比如「CFG 太高会导致什么」\n"
            )

        return "\n\n".join(blocks)

    # ---------- 开头：直接结论 ----------

    def _conclusion(self, state: Any) -> str:
        """
        给出直接结论 —— 用户问「为什么 X」时最想先看到的一句
        """
        lines = []

        issues = self._sorted_issues(state)
        knowledge = getattr(state, "knowledge", []) or []
        has_workflow = getattr(state, "workflow", None) is not None

        # 什么都没查到时不硬凑结论，交给兜底文案
        if not issues and not knowledge and not has_workflow:
            return ""

        # 有高危诊断时，直接点名最严重的那条
        blocking = [
            i for i in issues
            if self._severity_of(i) in ("critical", "high")
        ]

        if blocking:
            first = blocking[0]
            node = self._node_of(first)
            where = f"（{node}）" if node else ""
            lines.append(
                f"**最可能的原因**：{where}{self._message_of(first)}"
            )
            suggestion = self._suggestion_of(first)
            if suggestion:
                lines.append(f"建议：{suggestion}")

            if len(blocking) > 1:
                lines.append(
                    f"另外还有 {len(blocking) - 1} 个严重问题，一并列在下面。"
                )
        elif issues:
            lines.append(
                f"检查了当前工作流，发现 {len(issues)} 个需要注意的地方，"
                f"没有致命问题。"
            )
        elif knowledge:
            lines.append(
                "工作流本身没检查出明显问题，"
                "下面是相关知识，可能正好回答你的疑问。"
            )
        else:
            lines.append(
                "工作流没检查出明显问题。告诉我你想了解什么，"
                "我按节点给你讲清楚。"
            )

        if getattr(state, "question", ""):
            lines.append(f"**你的问题**：{state.question}")

        return "## 结论\n\n" + "\n\n".join(lines)

    # ---------- 工作流现状 ----------

    def _workflow_block(self, state: Any) -> str:
        """
        展示当前工作流的实际取值
        """
        workflow = getattr(state, "workflow", None)
        if workflow is None:
            return ""

        lines = ["## 当前工作流"]

        workflow_type = getattr(state, "workflow_type", "")
        if workflow_type and workflow_type.lower() != "unknown":
            lines.append(f"- 识别类型：{workflow_type}")

        nodes = self._nodes_of(state)
        if nodes:
            lines.append(f"- 节点组成（{len(nodes)} 个）：")
            for node in nodes:
                lines.append(f"    - {node}")

        params = self._parameters_of(state)
        if params:
            lines.append("- 关键参数取值：")
            for name, value in params.items():
                lines.append(f"    - {name} = {value}")

        return "\n".join(lines)

    def _parameters_of(self, state: Any) -> Dict:
        """
        抽取工作流里可读的关键参数
        """
        params: Dict = {}

        workflow = getattr(state, "workflow", None)
        if workflow is None:
            return params

        for node in getattr(workflow, "nodes", []) or []:
            node_type = getattr(node, "node_type", "")
            widgets = getattr(node, "widgets", None) or []

            # KSampler 的 widgets_values 顺序是固定的：
            # [seed, control_after_generate, steps, cfg, sampler_name, scheduler, denoise]
            if "KSampler" in node_type and len(widgets) >= 4:
                names = [
                    "seed", "control_after_generate", "steps",
                    "cfg", "sampler_name", "scheduler", "denoise",
                ]
                for name, value in zip(names, widgets):
                    if name == "control_after_generate":
                        continue
                    params[name] = value
            elif "EmptyLatent" in node_type and len(widgets) >= 2:
                params["width"], params["height"] = widgets[0], widgets[1]
            elif "CheckpointLoader" in node_type and widgets:
                params["checkpoint"] = widgets[0]

        return params

    # ---------- 诊断问题 ----------

    def _issues_block(self, state: Any) -> str:
        """
        按严重度分组列出诊断问题
        """
        issues = self._sorted_issues(state)
        if not issues:
            return ""

        lines = ["## 发现的问题"]

        current_category = None

        for issue in issues:
            category = ISSUE_CATEGORY.get(
                self._issue_type_of(issue), "其他问题"
            )

            if category != current_category:
                lines.append("")
                lines.append(f"### {category}")
                current_category = category

            severity = SEVERITY_LABELS.get(
                self._severity_of(issue), self._severity_of(issue) or "提示"
            )
            node = self._node_of(issue)
            where = f"`{node}` " if node else ""

            lines.append(
                f"- **[{severity}]** {where}{self._message_of(issue)}"
            )

            suggestion = self._strip_advice_prefix(
                self._suggestion_of(issue)
            )
            if suggestion:
                lines.append(f"    - {suggestion}")

        return "\n".join(lines)

    @staticmethod
    def _strip_advice_prefix(text: str) -> str:
        """
        去掉建议文本自带的「建议：」前缀

        diagnostics 的 suggestion 字段本身多以「建议」开头（如
        「建议尝试CFG 7-10」），模板再加一次会变成「建议：建议尝试…」，
        所以这里统一由模板加前缀，源文本的重复前缀先剥掉。
        """
        if not text:
            return text

        cleaned = text.strip()
        for prefix in ("建议：", "建议:", "建议", "可尝试", "尝试"):
            if cleaned.startswith(prefix):
                return cleaned[len(prefix):].lstrip("：: ")
        return cleaned

    # ---------- 相关知识 ----------

    def _knowledge_block(self, state: Any) -> str:
        """
        展示蒸馏后的相关知识
        """
        knowledge = getattr(state, "knowledge", []) or []
        if not knowledge:
            return ""

        question = getattr(state, "question", "")

        lines = ["## 相关知识"]

        for item in knowledge[:3]:
            name = item.get("name", "")
            if not name:
                continue

            lines.append("")
            lines.append(f"### {name}")

            content = item.get("content") or item.get("description") or ""

            if content:
                snippet = self.distiller.distill(
                    content,
                    question=question,
                    extra_keywords=self._knowledge_keywords(item),
                )
                if snippet:
                    lines.append(snippet)

            for rec in item.get("recommendations", []) or []:
                lines.append(f"- {rec}")

            params = item.get("common_parameters")
            if params:
                lines.append(f"- 历史统计区间：{self._format_ranges(params)}")

        return "\n".join(lines).strip()

    def _knowledge_keywords(self, item: Dict) -> List[str]:
        """
        取条目的关键词，用于知识卡切段
        """
        keywords = []

        node = item.get("node", "")
        if node:
            keywords.append(node)

        for topic in item.get("learning_topics", []) or []:
            keywords.append(topic)

        name = str(item.get("name", ""))
        # 从 "cfg 调整经验" 这类名字里抽出参数名
        for part in name.replace("_", " ").split():
            if len(part) >= 2:
                keywords.append(part)

        param = item.get("param", "")
        if param:
            keywords.append(param)

        return keywords

    def _format_ranges(self, params: Dict) -> str:
        """
        参数区间格式化
        """
        parts = []

        for name, stats in params.items():
            if not isinstance(stats, dict):
                continue

            if stats.get("median") is not None:
                parts.append(
                    f"{name} 中位 {stats['median']}"
                    f"（{stats.get('min')}-{stats.get('max')}）"
                )
            elif stats.get("most_common"):
                parts.append(f"{name} 常用 {stats['most_common']}")

        return "，".join(parts)

    # ---------- 下一步 ----------

    def _actions_block(self, state: Any) -> str:
        """
        给出可执行的下一步
        """
        issues = self._sorted_issues(state)
        knowledge = getattr(state, "knowledge", []) or []

        steps = []

        # 1. 先给有建议的诊断问题排序后的清单
        for issue in issues:
            suggestion = self._strip_advice_prefix(
                self._suggestion_of(issue)
            )
            if suggestion:
                steps.append(suggestion)

        # 2. 补来自演化知识的建议（基于多条历史经验统计，比单条问题更可信）
        for item in knowledge[:2]:
            for rec in item.get("recommendations", []) or []:
                if rec.startswith("风险"):
                    steps.append(rec)

        if not steps:
            return ""

        # 去重并保持顺序
        unique = list(dict.fromkeys(steps))

        lines = ["## 下一步建议", ""]
        for i, step in enumerate(unique[:6], 1):
            lines.append(f"{i}. {step}")

        lines.append("")
        lines.append(
            "改完可以让我再检查一次 —— "
            "参数变化会记录下来，积累成你的经验库。"
        )

        return "\n".join(lines)

    # ---------- 工具方法 ----------

    def _sorted_issues(self, state: Any) -> List[Any]:
        """
        诊断问题按严重度排序
        """
        issues = list(getattr(state, "diagnostics", []) or [])

        return sorted(
            issues,
            key=lambda i: SEVERITY_ORDER.get(
                self._severity_of(i), 99
            ),
        )

    def _nodes_of(self, state: Any) -> List[str]:
        """
        节点清单，优先用 state 自己的方法
        """
        if hasattr(state, "workflow_nodes"):
            return state.workflow_nodes()

        workflow = getattr(state, "workflow", None)
        if workflow is None:
            return []

        result = []
        for node in getattr(workflow, "nodes", []) or []:
            node_type = getattr(node, "node_type", None)
            if node_type is None and isinstance(node, dict):
                node_type = node.get("node_type", "")
            if node_type:
                result.append(node_type)

        return result

    @staticmethod
    def _field(issue: Any, name: str, default: str = "") -> str:
        """
        兼容 dataclass 与 dict 两种诊断项
        """
        if isinstance(issue, dict):
            return issue.get(name, default) or default
        return getattr(issue, name, default) or default

    def _severity_of(self, issue: Any) -> str:
        return str(self._field(issue, "severity", "")).lower()

    def _message_of(self, issue: Any) -> str:
        return self._field(issue, "message", "（无描述）")

    def _suggestion_of(self, issue: Any) -> str:
        return self._field(issue, "suggestion", "")

    def _node_of(self, issue: Any) -> str:
        return self._field(issue, "node", "")

    def _issue_type_of(self, issue: Any) -> str:
        return str(self._field(issue, "issue_type", "")).lower()
