"""
数据模型定义
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class WorkflowSnapshot:
    """
    工作流快照
    """

    workflow_id: str
    timestamp: str
    nodes: List[str] = field(default_factory=list)
    parameters: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "workflow_id": self.workflow_id,
            "timestamp": self.timestamp,
            "nodes": self.nodes.copy(),
            "parameters": self.parameters.copy(),
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "WorkflowSnapshot":
        """从字典创建"""
        return cls(
            workflow_id=data["workflow_id"],
            timestamp=data["timestamp"],
            nodes=data.get("nodes", []),
            parameters=data.get("parameters", {}),
        )


@dataclass
class WorkflowChange:
    """
    工作流变化
    """

    changed_nodes: List[str] = field(default_factory=list)
    parameter_changes: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "changed_nodes": self.changed_nodes.copy(),
            "parameter_changes": self.parameter_changes.copy(),
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "WorkflowChange":
        """从字典创建"""
        return cls(
            changed_nodes=data.get("changed_nodes", []),
            parameter_changes=data.get("parameter_changes", {}),
        )


@dataclass
class LearningExperience:
    """
    学习经验
    """

    workflow_type: str
    change: WorkflowChange
    observation: str = ""
    conclusion: str = ""
    tags: List[str] = field(default_factory=list)
    timestamp: str = ""

    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "workflow_type": self.workflow_type,
            "change": self.change.to_dict(),
            "observation": self.observation,
            "conclusion": self.conclusion,
            "tags": self.tags.copy(),
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "LearningExperience":
        """从字典创建"""
        return cls(
            workflow_type=data["workflow_type"],
            change=WorkflowChange.from_dict(data["change"]),
            observation=data.get("observation", ""),
            conclusion=data.get("conclusion", ""),
            tags=data.get("tags", []),
            timestamp=data.get("timestamp", ""),
        )
