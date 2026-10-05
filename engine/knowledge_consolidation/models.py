"""
数据模型

归纳产出的知识单元。

与 knowledge_evolution.models 的区别（两者数据源不同，不是重复）：
    knowledge_evolution  从 learning_loop 的「参数改动记录」归纳，
                          数据源是 experience_store.json
    knowledge_consolidation 从「完整 workflow」归纳，
                          数据源是 workflows/learning/*.md
前者回答「改这个参数会怎样」，后者回答「这类 workflow 长什么样」。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


# 归纳置信等级
LEVEL_STRONG = "strong"      # 样本足够 + 参数集中
LEVEL_MODERATE = "moderate"  # 样本够但参数分散
LEVEL_WEAK = "weak"          # 样本不足，仅供参考


@dataclass
class ParameterStat:
    """
    单个参数的统计

    数值参数给 count/min/max/mean/median；
    非数值参数（如 sampler_name / checkpoint）给 most_common。

    为什么必须带 median：SD1.5 的 steps 集中在 20-30，
    若混入一个 steps=1 的异常 workflow，均值会被拉低到看不出典型值。
    """

    count: int = 0
    min: Any = None
    max: Any = None
    mean: Optional[float] = None
    median: Optional[float] = None
    # 集中度：0-1，越大说明取值越一致。用于判断「典型区间」是否可信
    consistency: float = 0.0
    most_common: Any = None
    values: List[Any] = field(default_factory=list)

    @property
    def is_numeric(self) -> bool:
        return self.median is not None

    @property
    def typical_range(self) -> Optional[str]:
        """
        典型区间文字

        样本少时不给区间 —— 三条样本得出的「区间」是噪声不是知识。
        """
        if not self.is_numeric or self.count < 3:
            return None
        return f"{self.min:g} - {self.max:g}"

    def to_dict(self) -> Dict:
        return {
            "count": self.count,
            "min": self.min,
            "max": self.max,
            "mean": (
                round(self.mean, 2) if self.mean is not None else None
            ),
            "median": self.median,
            "consistency": round(self.consistency, 2),
            "most_common": self.most_common,
        }


@dataclass
class WorkflowPattern:
    """
    从多个 workflow 中归纳出的模式

    common_nodes     该组**共有**的节点（出现在全部成员里），
                     与 all_nodes（并集）不同：共有节点才是模式的必要组成
    signature        用于聚类的特征节点（见 PatternMiner 的判定逻辑）
    """

    name: str
    workflow_type: str = ""
    frequency: int = 0

    # 共有节点 / 并集节点 / 差异节点
    common_nodes: List[str] = field(default_factory=list)
    all_nodes: List[str] = field(default_factory=list)
    variable_nodes: Dict[str, int] = field(default_factory=dict)

    # 按模式分组的参数统计（不与其他模式混合）
    parameter_stats: Dict[str, ParameterStat] = field(default_factory=dict)

    # 该组汇总出的常见问题 —— 来自各 workflow 的参数体检结论
    common_problems: List[Dict] = field(default_factory=list)
    # 缺知识卡的节点（值得建卡的线索）
    missing_nodes: List[str] = field(default_factory=list)

    recommendations: List[str] = field(default_factory=list)
    members: List[str] = field(default_factory=list)
    level: str = LEVEL_WEAK
    coverage: float = 0.0

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "workflow_type": self.workflow_type,
            "frequency": self.frequency,
            "common_nodes": self.common_nodes,
            "all_nodes": self.all_nodes,
            "variable_nodes": self.variable_nodes,
            "parameter_stats": {
                k: v.to_dict() for k, v in self.parameter_stats.items()
            },
            "common_problems": self.common_problems,
            "missing_nodes": self.missing_nodes,
            "recommendations": self.recommendations,
            "members": self.members,
            "level": self.level,
            "coverage": round(self.coverage, 3),
        }


@dataclass
class ConsolidatedKnowledge:
    """
    一次归纳的完整产出
    """

    patterns: List[WorkflowPattern] = field(default_factory=list)
    source_count: int = 0
    # 未形成模式（样本不足）的 workflow 数
    ungrouped: int = 0
    # 全局层面的观察，如「KSampler 出现在全部 workflow 中」
    global_observations: List[str] = field(default_factory=list)
    generated_at: str = ""

    def pattern_names(self) -> List[str]:
        return [p.name for p in self.patterns]

    def find(self, name: str) -> Optional[WorkflowPattern]:
        for pattern in self.patterns:
            if pattern.name == name:
                return pattern
        return None

    def to_dict(self) -> Dict:
        return {
            "patterns": [p.to_dict() for p in self.patterns],
            "source_count": self.source_count,
            "ungrouped": self.ungrouped,
            "global_observations": self.global_observations,
            "generated_at": self.generated_at,
        }
