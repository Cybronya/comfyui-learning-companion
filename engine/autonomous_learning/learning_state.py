"""
自主学习状态

保存一次自主学习过程的全部中间产物与评估数据。

除设计文档给的字段外，补了几个「能不能判断学得好不好」的量化字段
（coverage / confidence），否则 reflection 只能输出「需要补充知识」这类无信息量的话。
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class GapItem:
    """
    一处知识缺口

    coverage 区分两档，差别很实质：
        exact    知识库里没有这个节点的任何知识 → 必须建卡
        related  只有同族节点的通用知识（如有 KSampler 卡，
                 但没有 WanVideoSampler 卡）→ 能类推，但不能保证正确
    """

    node_type: str
    reason: str = ""
    # 是否属于工作流的关键节点（关键节点的缺口更值得关注）
    is_core: bool = False
    # exact = 完全没知识；related = 只有相关主题的通用知识
    coverage: str = "none"
    # 系统内可用的替代说法（节点别名 → 所属主题）
    related_topics: List[str] = field(default_factory=list)

    @property
    def severity_rank(self) -> int:
        """
        排序权重：越严重越靠前
        """
        if self.coverage == "none" and self.is_core:
            return 0
        if self.coverage == "none":
            return 1
        if self.is_core:
            return 2
        return 3

    def to_dict(self) -> Dict:
        return {
            "node_type": self.node_type,
            "reason": self.reason,
            "is_core": self.is_core,
            "coverage": self.coverage,
            "related_topics": list(self.related_topics),
        }

    def __str__(self) -> str:
        mark = "核心" if self.is_core else "次要"
        cov = "无知识" if self.coverage == "none" else "仅通用知识"
        text = f"[{mark}/{cov}] {self.node_type}"
        if self.reason:
            text += f" —— {self.reason}"
        return text


@dataclass
class LearningState:
    """
    一次学习过程的状态
    """

    # ---- 输入 ----
    task: str = ""
    workflow: Any = None
    workflow_path: str = ""

    # ---- 过程产物 ----
    plan: List[str] = field(default_factory=list)
    analysis: Dict = field(default_factory=dict)
    pipeline: List[str] = field(default_factory=list)
    core_nodes: List[str] = field(default_factory=list)
    parameters: Dict = field(default_factory=dict)
    knowledge_used: List[Dict] = field(default_factory=list)
    missing_knowledge: List[GapItem] = field(default_factory=list)
    discoveries: List[str] = field(default_factory=list)
    report: str = ""
    # 专项分析结论：{计划步骤名: 结论}
    step_findings: Dict = field(default_factory=dict)
    # 参数体检结论（来自 diagnostics），与 parameters 分开存放
    diagnostic_findings: List[str] = field(default_factory=list)

    # ---- 评估 ----
    # 节点被知识覆盖的比例 0-1
    coverage: float = 0.0
    # 核心节点被覆盖的比例 0-1，权重高于整体 coverage
    core_coverage: float = 0.0
    # 综合置信度 0-1，由 coverage / core_coverage / 关键参数是否已知 合成
    confidence: float = 0.0
    # 自评等级：excellent / good / partial / insufficient
    level: str = "insufficient"
    # 造成等级封顶的核心缺口（完全无知识的节点名）
    blocking_gaps: List[str] = field(default_factory=list)

    # ---- 过程信息 ----
    steps_run: List[str] = field(default_factory=list)
    errors: List[Dict] = field(default_factory=list)
    # 沉淀出去的知识点（写入知识库的内容）
    deposited: List[Dict] = field(default_factory=list)
    elapsed_ms: float = 0.0

    def add_step(self, name: str) -> None:
        """记录已执行步骤"""
        self.steps_run.append(name)

    def add_error(self, step: str, error: Exception) -> None:
        """记录步骤错误"""
        self.errors.append({
            "step": step,
            "error_type": type(error).__name__,
            "message": str(error),
        })

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)

    def nodes(self) -> List[str]:
        """工作流节点清单"""
        return list(self.analysis.get("nodes", []))

    def compute_metrics(self) -> None:
        """
        计算覆盖率与置信度

        整体覆盖率会被核心节点稀释：一个 10 节点工作流里 9 个节点有卡、
        唯独 KSampler 没卡，整体覆盖率仍有 0.9，但对生成质量影响最大的是它。
        所以核心节点单独算一个指标，且在置信度里占更大权重。

        coverage=related 的缺口（有同族通用知识但没这个节点自己的说明）
        按半分计算 —— 能类推，但不能保证正确。
        """
        nodes = self.nodes()
        if not nodes:
            self.coverage = 0.0
            self.core_coverage = 0.0
            self.confidence = 0.0
            self.level = "insufficient"
            return

        gap_map = {g.node_type: g for g in self.missing_knowledge}

        def credit(node: str) -> float:
            gap = gap_map.get(node)
            if gap is None:
                return 1.0          # 无缺口记录 = 有知识
            if gap.coverage == "related":
                return 0.5          # 只有通用知识
            return 0.0

        self.coverage = sum(credit(n) for n in nodes) / len(nodes)

        core = self.core_nodes or nodes
        self.core_coverage = (
            sum(credit(n) for n in core) / len(core) if core else 0.0
        )

        # 关键参数已知也说明理解到位（KSampler 的 cfg/steps 至少要理解）
        param_factor = 0.0
        if self.parameters:
            param_factor = 1.0

        # 核心节点覆盖权重 0.6，整体覆盖 0.3，参数 0.1
        self.confidence = (
            self.core_coverage * 0.6
            + self.coverage * 0.3
            + param_factor * 0.1
        )

        # 等级封顶：加权平均会把「关键未知」稀释掉。
        # 例如一个专门做视频生成的工作流，若核心的视频采样器只有通用知识，
        # core_coverage 仍可能有 0.9，但最关键的一环并没搞懂，
        # 此时不该判为 good。
        #
        # 规则：核心节点只要有缺口（无论完全无知识还是仅通用知识），
        # 等级封顶 partial —— 核心节点之所以是核心，就是它对结果影响最大；
        # 两个及以上核心节点完全无知识则封顶 insufficient。
        core = set(self.core_nodes)
        blocking = [
            g for g in self.missing_knowledge
            if g.node_type in core and g.coverage == "none"
        ]
        partial_core = [
            g for g in self.missing_knowledge
            if g.node_type in core and g.coverage == "related"
        ]

        ceiling = "excellent"
        if blocking or partial_core:
            ceiling = "partial"
        if len(blocking) >= 2:
            ceiling = "insufficient"

        self.blocking_gaps = [g.node_type for g in blocking]

        order = [
            "insufficient", "partial", "good", "excellent",
        ]
        computed = "excellent"
        if self.confidence < 0.4:
            computed = "insufficient"
        elif self.confidence < 0.7:
            computed = "partial"
        elif self.confidence < 0.9:
            computed = "good"

        # 取两者中较低的一档
        self.level = min(
            [computed, ceiling], key=order.index
        )

    def to_dict(self) -> Dict:
        """可序列化摘要"""
        return {
            "task": self.task,
            "workflow_path": self.workflow_path,
            "workflow_type": self.analysis.get("workflow_type", ""),
            "nodes": self.nodes(),
            "core_nodes": self.core_nodes,
            "pipeline": self.pipeline,
            "parameters": self.parameters,
            "coverage": round(self.coverage, 2),
            "core_coverage": round(self.core_coverage, 2),
            "confidence": round(self.confidence, 2),
            "level": self.level,
            "blocking_gaps": list(self.blocking_gaps),
            "knowledge_used": [
                {"name": k.get("name", ""), "type": k.get("type", "")}
                for k in self.knowledge_used
            ],
            "missing_knowledge": [
                g.to_dict() for g in self.missing_knowledge
            ],
            "discoveries": self.discoveries,
            "step_findings": self.step_findings,
            "steps_run": self.steps_run,
            "errors": self.errors,
            "deposited": self.deposited,
            "elapsed_ms": round(self.elapsed_ms, 2),
        }
