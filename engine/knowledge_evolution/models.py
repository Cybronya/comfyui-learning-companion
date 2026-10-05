"""
数据模型定义

把 learning_loop 里的孤立经验（LearningExperience）转换成可聚合的领域知识。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class WorkflowExperience:
    """
    单条工作流经验

    对应 learning_loop.LearningExperience 的扁平化版本：
    learning_loop 记录的是「一次修改」（WorkflowChange），
    这里记录的是「这个工作流长什么样 + 改成了什么 + 观察到什么」，
    因为挖模式需要节点清单，而节点清单属于工作流本身而非某次改动。
    """

    workflow_type: str
    nodes: List[str] = field(default_factory=list)
    changes: Dict = field(default_factory=dict)
    parameters: Dict = field(default_factory=dict)
    result: str = ""
    observation: str = ""
    tags: List[str] = field(default_factory=list)
    timestamp: str = ""

    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "workflow_type": self.workflow_type,
            "nodes": list(self.nodes),
            "changes": dict(self.changes),
            "parameters": dict(self.parameters),
            "result": self.result,
            "observation": self.observation,
            "tags": list(self.tags),
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "WorkflowExperience":
        """从字典创建"""
        return cls(
            workflow_type=data.get("workflow_type", ""),
            nodes=data.get("nodes", []),
            changes=data.get("changes", {}),
            parameters=data.get("parameters", {}),
            result=data.get("result", ""),
            observation=data.get("observation", ""),
            tags=data.get("tags", []),
            timestamp=data.get("timestamp", ""),
        )


@dataclass
class ParameterRange:
    """
    某个参数的统计区间

    数值参数给出 min/max/median，非数值参数（如 sampler_name）给出 most_common。
    """

    count: int = 0
    min: Any = None
    max: Any = None
    median: Any = None
    most_common: Any = None

    def to_dict(self) -> Dict:
        return {
            "count": self.count,
            "min": self.min,
            "max": self.max,
            "median": self.median,
            "most_common": self.most_common,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "ParameterRange":
        return cls(
            count=data.get("count", 0),
            min=data.get("min"),
            max=data.get("max"),
            median=data.get("median"),
            most_common=data.get("most_common"),
        )


@dataclass
class WorkflowPattern:
    """
    从多条经验中挖掘出的工作流模式

    common_nodes     该模式稳定出现的节点组合
    frequency        出现次数
    common_parameters 参数统计区间（CFG / Steps 等的范围与中位数）
    recommendations  基于统计得出的建议与风险提示
    """

    name: str
    workflow_type: str
    common_nodes: List[str] = field(default_factory=list)
    frequency: int = 0
    common_parameters: Dict = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "workflow_type": self.workflow_type,
            "common_nodes": list(self.common_nodes),
            "frequency": self.frequency,
            "common_parameters": dict(self.common_parameters),
            "recommendations": list(self.recommendations),
            "tags": list(self.tags),
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "WorkflowPattern":
        return cls(
            name=data.get("name", ""),
            workflow_type=data.get("workflow_type", ""),
            common_nodes=data.get("common_nodes", []),
            frequency=data.get("frequency", 0),
            common_parameters=data.get("common_parameters", {}),
            recommendations=data.get("recommendations", []),
            tags=data.get("tags", []),
        )


@dataclass
class EvolutionKnowledge:
    """
    一次演化产出的知识集合
    """

    patterns: List[WorkflowPattern] = field(default_factory=list)
    source_experience_count: int = 0
    updated_at: str = ""

    def to_dict(self) -> Dict:
        return {
            "patterns": [p.to_dict() for p in self.patterns],
            "source_experience_count": self.source_experience_count,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "EvolutionKnowledge":
        return cls(
            patterns=[
                WorkflowPattern.from_dict(p) for p in data.get("patterns", [])
            ],
            source_experience_count=data.get("source_experience_count", 0),
            updated_at=data.get("updated_at", ""),
        )
