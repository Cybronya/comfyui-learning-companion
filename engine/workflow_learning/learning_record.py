"""
学习记录

保存一次 workflow 学习的结果。

与 design 给的字段相比补了几项，否则 registry 无法判断「是否需要重学」：
    content_hash   文件内容指纹。改了 workflow 必须能触发重新学习，
                   否则 exists(name) 永远为真，改了参数也不会被学进去
    source_kind    来源类型：json / png / png-metadata
    key            相对路径而非文件名。同名 workflow 放在不同目录下
                   用文件名当键会互相覆盖
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


# 学习状态
STATUS_COMPLETED = "completed"
STATUS_FAILED = "failed"
STATUS_SKIPPED = "skipped"
STATUS_STALE = "stale"


@dataclass
class LearningRecord:
    """
    一次 workflow 学习的结果
    """

    workflow_name: str
    file_path: str
    key: str = ""
    status: str = STATUS_COMPLETED
    source_kind: str = "json"
    content_hash: str = ""
    # 官方指导样本（ComfyUI 官方模板库）。检索/统计时可据此加权或过滤
    official: bool = False

    workflow_type: str = ""
    nodes: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)
    important_nodes: List[str] = field(default_factory=list)
    pipeline: List[str] = field(default_factory=list)
    parameters: Dict = field(default_factory=dict)

    # 有知识卡的节点 / 没知识卡的节点。
    # 分开存，因为「缺卡」比「有卡」更值得关注 —— design 里把
    # important_nodes 填成「有卡的节点」，语义是反的
    covered_nodes: List[str] = field(default_factory=list)
    missing_nodes: List[str] = field(default_factory=list)
    knowledge_refs: List[str] = field(default_factory=list)

    discoveries: List[str] = field(default_factory=list)
    diagnostic_issues: List[str] = field(default_factory=list)
    report_path: str = ""
    error: str = ""
    learned_at: str = ""

    def __post_init__(self):
        # key 缺省用文件名（兼容只传 name 的用法）
        if not self.key:
            self.key = self.workflow_name

    @property
    def coverage(self) -> float:
        """
        节点知识覆盖率 0-1
        """
        total = len(self.nodes)
        if not total:
            return 0.0
        return len(self.covered_nodes) / total

    def to_dict(self) -> Dict:
        """转为可序列化字典"""
        return {
            "key": self.key,
            "workflow_name": self.workflow_name,
            "file_path": self.file_path,
            "status": self.status,
            "source_kind": self.source_kind,
            "content_hash": self.content_hash,
            "official": self.official,
            "workflow_type": self.workflow_type,
            "nodes": list(self.nodes),
            "patterns": list(self.patterns),
            "important_nodes": list(self.important_nodes),
            "pipeline": list(self.pipeline),
            "parameters": dict(self.parameters),
            "covered_nodes": list(self.covered_nodes),
            "missing_nodes": list(self.missing_nodes),
            "knowledge_refs": list(self.knowledge_refs),
            "discoveries": list(self.discoveries),
            "diagnostic_issues": list(self.diagnostic_issues),
            "report_path": self.report_path,
            "error": self.error,
            "learned_at": self.learned_at,
            "coverage": round(self.coverage, 3),
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "LearningRecord":
        """从字典创建"""
        return cls(
            workflow_name=data.get("workflow_name", ""),
            file_path=data.get("file_path", ""),
            key=data.get("key", ""),
            status=data.get("status", STATUS_COMPLETED),
            source_kind=data.get("source_kind", "json"),
            content_hash=data.get("content_hash", ""),
            official=bool(data.get("official", False)),
            workflow_type=data.get("workflow_type", ""),
            nodes=data.get("nodes", []),
            patterns=data.get("patterns", []),
            important_nodes=data.get("important_nodes", []),
            pipeline=data.get("pipeline", []),
            parameters=data.get("parameters", {}),
            covered_nodes=data.get("covered_nodes", []),
            missing_nodes=data.get("missing_nodes", []),
            knowledge_refs=data.get("knowledge_refs", []),
            discoveries=data.get("discoveries", []),
            diagnostic_issues=data.get("diagnostic_issues", []),
            report_path=data.get("report_path", ""),
            error=data.get("error", ""),
            learned_at=data.get("learned_at", ""),
        )
