"""
Agent 状态

保存一次 Agent 推理过程中各阶段的产物，供阶段之间传递数据、供调用方事后检查。
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentState:
    """
    一次推理过程的状态
    """

    # ---- 输入 ----
    question: str = ""
    workflow_type: str = ""

    # ---- 各阶段产物 ----
    # 1. 解析：WorkflowKnowledge 对象（workflow_parser 产出）
    workflow: Any = None
    # 2. 分析：WorkflowAnalyzer 的返回字典
    workflow_analysis: Dict = field(default_factory=dict)
    # 3. 诊断：DiagnosticIssue 列表
    diagnostics: List = field(default_factory=list)
    # 4. 检索：排序后的知识条目
    knowledge: List = field(default_factory=list)
    # 5. 上下文：ContextManager.get_retrieval_context() 的结果
    context: Dict = field(default_factory=dict)
    # 6. 回答：给人直接读的 Markdown（规则拼装，无需 LLM）
    answer: str = ""
    # 7. 提示词：给 LLM 的输入（保留给接自有模型时用）
    response: Dict = field(default_factory=dict)
    # 8. 图谱：跨条目事实（问题里提到的节点/流程在知识图谱里的关联）
    #    每条是一句人读的中文，respond 阶段追加到 answer 末尾
    graph_facts: List[str] = field(default_factory=list)

    # ---- 过程信息 ----
    # 本次是否复用了 set_workflow() 登记的工作流
    reused_workflow: bool = False
    # 实际执行过的阶段名，配置关掉某些能力时这里会短于完整链路
    stages_run: List[str] = field(default_factory=list)
    # 被跳过的阶段及原因（如没传 workflow 就跳过解析）。
    # 与 stages_run 分开，因为「跑了但空转」和「真的做了」不是一回事，
    # 排查链路问题时要能看出差别。
    stages_skipped: List[Dict] = field(default_factory=list)
    # 阶段级错误：单个阶段失败不应让整条链路崩掉，错误记在这里
    errors: List[Dict] = field(default_factory=list)
    elapsed_ms: float = 0.0

    def add_stage(self, name: str) -> None:
        """
        记录已执行的阶段
        """
        self.stages_run.append(name)

    def skip_stage(self, name: str, reason: str = "") -> None:
        """
        记录被跳过的阶段

        Args:
            name: 阶段名
            reason: 跳过原因
        """
        self.stages_skipped.append({
            "stage": name,
            "reason": reason,
        })

    def add_error(
        self,
        stage: str,
        error: Exception
    ) -> None:
        """
        记录阶段错误

        Args:
            stage: 阶段名
            error: 异常对象
        """
        self.errors.append({
            "stage": stage,
            "error_type": type(error).__name__,
            "message": str(error),
        })

    @property
    def has_errors(self) -> bool:
        """
        本次推理是否有阶段失败
        """
        return bool(self.errors)

    def workflow_nodes(self) -> List[str]:
        """
        当前工作流的节点类型清单

        workflow 可能是 None（用户没传工作流），也可能不是 WorkflowKnowledge
        （注入了自定义 parser），所以逐层防御。
        """
        if self.workflow is None:
            return []

        nodes = getattr(self.workflow, "nodes", None)
        if nodes is None:
            return []

        result = []
        for node in nodes:
            node_type = getattr(node, "node_type", None)
            if node_type is None and isinstance(node, dict):
                node_type = node.get("node_type", "")
            if node_type:
                result.append(node_type)

        return result

    def diagnostic_issues(self) -> List[str]:
        """
        诊断问题摘要（给回答用）
        """
        lines = []

        for issue in self.diagnostics:
            if isinstance(issue, dict):
                severity = issue.get("severity", "")
                message = issue.get("message", "")
                suggestion = issue.get("suggestion", "")
            else:
                severity = getattr(issue, "severity", "")
                message = getattr(issue, "message", "")
                suggestion = getattr(issue, "suggestion", "")

            line = f"[{severity}] {message}" if severity else message
            if suggestion:
                line += f" → {suggestion}"
            lines.append(line)

        return lines

    def to_dict(self) -> Dict:
        """
        转为可序列化字典（workflow / graph 等对象转为摘要）
        """
        return {
            "question": self.question,
            "workflow_type": self.workflow_type,
            "workflow_summary": (
                {
                    "workflow_id": getattr(self.workflow, "workflow_id", ""),
                    "task_type": getattr(self.workflow, "task_type", ""),
                    "nodes": self.workflow_nodes(),
                    "features": list(
                        getattr(self.workflow, "features", []) or []
                    ),
                }
                if self.workflow is not None else None
            ),
            "workflow_analysis": {
                k: v for k, v in self.workflow_analysis.items()
                if k != "graph"
            },
            "diagnostics": self.diagnostic_issues(),
            "knowledge": [
                {
                    "type": item.get("type", ""),
                    "name": item.get("name", ""),
                    "score": item.get("score", 0),
                }
                for item in self.knowledge
            ],
            "context": self.context,
            "answer": self.answer,
            "response": self.response,
            "stages_run": self.stages_run,
            "stages_skipped": self.stages_skipped,
            "reused_workflow": self.reused_workflow,
            "errors": self.errors,
            "elapsed_ms": round(self.elapsed_ms, 2),
        }
