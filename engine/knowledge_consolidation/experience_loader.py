"""
经验加载器

从学习记录读入待归纳的 workflow。两个数据源，优先级：

1. WorkflowDatabase.experiences（database 参数传入时）——
   结构化载荷（LearningRecord.to_dict()），由 database_bridge 在
   学习落盘时镜像。这是数据层枢纽的标准来源。
2. LearningStore（Markdown 记录）—— 兜底。
   库是后建的，存量记录可能还没镜像；库里一条都没有时
   回退查 Markdown 并打印提示（不静默切换）。

加载后统一成 ExperienceRow —— 归纳只认这一个结构，
不关心上游是 Markdown 记录、JSON 还是数据库。
"""

from typing import List, Dict, Any, Optional

from ..workflow_learning import LearningStore
from .models import ParameterStat


class ExperienceRow:
    """
    一条待归纳的 workflow 记录
    """

    __slots__ = (
        "key", "workflow_type", "nodes", "parameters",
        "problems", "missing_nodes", "coverage", "patterns",
    )

    def __init__(
        self,
        key: str,
        workflow_type: str = "",
        nodes: List[str] = None,
        parameters: Dict = None,
        problems: List[str] = None,
        missing_nodes: List[str] = None,
        coverage: float = 0.0,
        patterns: List[str] = None,
    ) -> None:
        self.key = key
        self.workflow_type = workflow_type
        # 去重但保序：CLIPTextEncode 常出现两次，算共现频次时不该重复计
        self.nodes = list(dict.fromkeys(nodes or []))
        self.parameters = dict(parameters or {})
        self.problems = list(problems or [])
        self.missing_nodes = list(dict.fromkeys(missing_nodes or []))
        self.coverage = coverage
        self.patterns = list(patterns or [])

    def __repr__(self) -> str:
        return (
            f"<ExperienceRow {self.key} "
            f"{len(self.nodes)}节点 覆盖{self.coverage:.0%}>"
        )

    def to_dict(self) -> Dict:
        return {
            "key": self.key,
            "workflow_type": self.workflow_type,
            "nodes": self.nodes,
            "parameters": self.parameters,
            "problems": self.problems,
            "missing_nodes": self.missing_nodes,
            "coverage": self.coverage,
            "patterns": self.patterns,
        }


class ExperienceLoader:
    """
    经验加载器
    """

    def __init__(self, store=None, database=None) -> None:
        """
        初始化加载器

        Args:
            store: workflow_learning.LearningStore；
                  None 时用默认（统一位置 comfyui_library/workflows/learning/）
            database: WorkflowDatabase；传入则优先从
                     database.experiences 的结构化载荷读取
        """
        self.store = store or LearningStore()
        self.database = database

    def load(self, path=None) -> List[ExperienceRow]:
        """
        加载待归纳的记录

        Args:
            path: 兼容参数。设计稿里这里是「经验文件路径」，
                  现在记录来自数据库或 Markdown 目录，传入会被忽略并记一条提示。

        Returns:
            ExperienceRow 列表（只含学习成功的记录）
        """
        if path:
            print(
                "提示：ExperienceLoader.load(path) 的 path 参数被忽略，"
                "数据源由 database / LearningStore 的位置决定"
            )

        rows = []
        if self.database is not None:
            rows = self._load_from_database()
            if rows:
                return rows
            print(
                "提示：数据库里没有可归纳的经验"
                "（可能存量记录未镜像），回退读 Markdown 记录 ——"
                "可调用 BatchWorkflowLearner.sync_database() 补齐"
            )

        return self._load_from_store()

    def _load_from_store(self) -> List[ExperienceRow]:
        """从 LearningStore 的 Markdown 记录读取（兜底来源）"""
        records = self.store.completed_records()

        rows = []
        for record in records:
            # 节点清单为空无法参与归纳
            if not record.nodes:
                continue

            rows.append(ExperienceRow(
                key=record.key,
                workflow_type=record.workflow_type,
                nodes=record.nodes,
                parameters=self._parameters_of(record),
                problems=record.diagnostic_issues,
                missing_nodes=record.missing_nodes,
                coverage=record.coverage,
                patterns=record.patterns,
            ))

        return rows

    def _load_from_database(self) -> List[ExperienceRow]:
        """
        从 WorkflowDatabase.experiences 的结构化载荷读取

        只取 status=completed 的载荷（data 是 LearningRecord.to_dict()，
        含 status 字段）；节点清单为空的同样跳过。
        """
        experiences = self.database.experiences.all()

        rows = []
        for key in sorted(experiences):
            data = experiences[key].get("data") or {}
            if data.get("status", "completed") != "completed":
                continue

            nodes = list(data.get("nodes") or [])
            if not nodes:
                continue

            rows.append(ExperienceRow(
                key=data.get("key") or key,
                workflow_type=data.get("workflow_type", ""),
                nodes=nodes,
                parameters=dict(data.get("parameters") or {}),
                problems=list(data.get("diagnostic_issues") or []),
                missing_nodes=list(data.get("missing_nodes") or []),
                coverage=float(data.get("coverage", 0) or 0),
                patterns=list(data.get("patterns") or []),
            ))

        return rows

    @staticmethod
    def _parameters_of(record: Any) -> Dict:
        """
        从记录里取参数字典

        LearningRecord.parameters 已是 dict；但若将来记录来自别处，
        可能只有「关键参数」正文，这里做一次兜底解析。
        """
        params = getattr(record, "parameters", None)

        if isinstance(params, dict) and params:
            return params

        return {}

    def load_rows(self, rows: List[Dict]) -> List[ExperienceRow]:
        """
        从字典列表构造 ExperienceRow

        便于测试与将来接入别的数据源，不必先落盘。

        Args:
            rows: 字典列表

        Returns:
            ExperienceRow 列表
        """
        result = []

        for item in rows:
            params = item.get("parameters", {})

            # 允许把参数内联在 parameters 之外（如 nodes/parameters 平级）
            if not params:
                params = {
                    k: v for k, v in item.items()
                    if k not in (
                        "key", "workflow_type", "nodes", "problems",
                        "missing_nodes", "coverage", "patterns", "type",
                    )
                }

            result.append(ExperienceRow(
                key=item.get("key", ""),
                workflow_type=item.get(
                    "workflow_type", item.get("type", "")
                ),
                nodes=item.get("nodes", []),
                parameters=params,
                problems=item.get("problems", []),
                missing_nodes=item.get("missing", item.get(
                    "missing_nodes", []
                )),
                coverage=float(item.get("coverage", 0) or 0),
                patterns=item.get("patterns", []),
            ))

        return result
