"""
经验加载器

从 `workflow_learning` 的学习记录（Markdown）读入待归纳的 workflow。

为什么不读 JSON：
    workflow_learning 上一轮已把 registry.json / experience.json 换成
    Markdown 记录（comfyui_library/workflows/learning/*.md），
    设计稿里的 workflow_experience.json 已不存在。这里复用
    LearningStore 读取，不再另造一套格式。

加载后统一成 ExperienceRow —— 归纳只认这一个结构，
不关心上游是 Markdown 记录、JSON 还是将来的数据库。
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

    def __init__(self, store=None) -> None:
        """
        初始化加载器

        Args:
            store: workflow_learning.LearningStore；
                  None 时用默认（统一位置 comfyui_library/workflows/learning/）
        """
        self.store = store or LearningStore()

    def load(self, path=None) -> List[ExperienceRow]:
        """
        加载待归纳的记录

        Args:
            path: 兼容参数。设计稿里这里是「经验文件路径」，
                  现在记录是 Markdown 目录结构，传入会被忽略并记一条提示。
                  保留该参数是为了不改变调用方签名。

        Returns:
            ExperienceRow 列表（只含学习成功的记录）
        """
        if path:
            print(
                "提示：记录已改为 Markdown（workflows/learning/*.md），"
                "ExperienceLoader.load(path) 的 path 参数被忽略，"
                "改由 LearningStore 的位置决定"
            )

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
