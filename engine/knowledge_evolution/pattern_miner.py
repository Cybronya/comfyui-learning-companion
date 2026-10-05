"""
模式挖掘器

从多条经验中找出重复出现的工作流结构。

挖掘两步：
    1. 节点组合：把每个工作流的节点排序成元组，统计出现次数，>= min_frequency 视为一个模式
    2. 参数区间：对每个模式内部的数值参数统计 min/max/median，
       非数值参数（如 sampler_name）统计最常用值

第 2 步是为了让 common_parameters 真正有内容 —— 只数节点组合的话，
「CFG 常用 6-9、Steps 常用 20-35」这类知识挖不出来。
"""

from collections import Counter
from typing import List, Dict, Any, Tuple

from .models import WorkflowExperience, WorkflowPattern, ParameterRange


class PatternMiner:
    """
    工作流模式挖掘器
    """

    def __init__(self, min_frequency: int = 2) -> None:
        """
        初始化挖掘器

        Args:
            min_frequency: 模式最小出现次数，低于此值视为偶然组合
        """
        self.min_frequency = min_frequency

    @staticmethod
    def _nodes_of(exp: Any) -> List[str]:
        """
        取经验的节点清单，兼容 dataclass 与 dict 两种输入
        """
        if isinstance(exp, dict):
            return list(exp.get("nodes", []))
        return list(getattr(exp, "nodes", []))

    @staticmethod
    def _type_of(exp: Any) -> str:
        """取经验的 workflow_type"""
        if isinstance(exp, dict):
            return exp.get("workflow_type", "")
        return getattr(exp, "workflow_type", "")

    @staticmethod
    def _params_of(exp: Any) -> Dict:
        """取经验的参数表"""
        if isinstance(exp, dict):
            return exp.get("parameters", {})
        return getattr(exp, "parameters", {})

    @staticmethod
    def _tags_of(exp: Any) -> List[str]:
        """取经验的标签"""
        if isinstance(exp, dict):
            return list(exp.get("tags", []))
        return list(getattr(exp, "tags", []))

    def mine(self, experiences: List[Any]) -> List[Dict]:
        """
        挖掘模式

        Args:
            experiences: WorkflowExperience 列表或 dict 列表

        Returns:
            模式字典列表，每项含 nodes / frequency / workflow_type /
            parameter_ranges / tags
        """
        node_sets: List[Tuple] = []
        bucket: Dict[Tuple, List[Any]] = {}

        for exp in experiences:
            nodes = self._nodes_of(exp)
            if not nodes:
                # 节点清单为空的经验无法参与模式挖掘，跳过
                continue

            key = tuple(sorted(set(nodes)))
            node_sets.append(key)
            bucket.setdefault(key, []).append(exp)

        counter = Counter(node_sets)
        patterns = []

        for nodes, count in counter.items():
            if count < self.min_frequency:
                continue

            members = bucket[nodes]
            types = Counter(
                self._type_of(exp) for exp in members
            )
            # 同一节点组合可能有不同 workflow_type，取出现最多的作为主类型
            workflow_type = types.most_common(1)[0][0] if types else ""

            patterns.append({
                "nodes": list(nodes),
                "frequency": count,
                "workflow_type": workflow_type,
                "parameter_ranges": self.mine_parameters(members),
                "tags": self._collect_tags(members, list(nodes)),
            })

        # 出现次数多的模式排前面
        patterns.sort(key=lambda p: p["frequency"], reverse=True)
        return patterns

    def mine_parameters(self, experiences: List[Any]) -> Dict:
        """
        统计一组经验的参数区间

        数值参数给 min/max/median，非数值参数给 most_common。

        Args:
            experiences: 同一模式下的经验列表

        Returns:
            {参数名: ParameterRange 字典}
        """
        collected: Dict[str, List[Any]] = {}

        for exp in experiences:
            for key, value in self._params_of(exp).items():
                if value is None:
                    continue
                collected.setdefault(key, []).append(value)

        ranges: Dict[str, Dict] = {}

        for key, values in collected.items():
            numeric = [v for v in values if isinstance(v, (int, float))
                       and not isinstance(v, bool)]
            counter = Counter(
                str(v) for v in values if not isinstance(v, (int, float))
                or isinstance(v, bool)
            )

            if numeric:
                numeric_sorted = sorted(numeric)
                mid = len(numeric_sorted) // 2
                if len(numeric_sorted) % 2 == 1:
                    median = numeric_sorted[mid]
                else:
                    median = (numeric_sorted[mid - 1] + numeric_sorted[mid]) / 2

                ranges[key] = ParameterRange(
                    count=len(numeric),
                    min=numeric_sorted[0],
                    max=numeric_sorted[-1],
                    median=median,
                    most_common=counter.most_common(1)[0][0] if counter else None,
                ).to_dict()
            else:
                ranges[key] = ParameterRange(
                    count=len(values),
                    min=None,
                    max=None,
                    median=None,
                    most_common=counter.most_common(1)[0][0] if counter else None,
                ).to_dict()

        return ranges

    def _collect_tags(self, experiences: List[Any], nodes: List[str]) -> List[str]:
        """
        汇总模式标签：经验自身的标签 + 由节点组合推断的标签
        """
        tags = set()

        for exp in experiences:
            tags.update(self._tags_of(exp))

        for node in nodes:
            lowered = node.lower()
            if "controlnet" in lowered:
                tags.add("controlnet")
            if "lora" in lowered:
                tags.add("lora")
            if "ipadapter" in lowered:
                tags.add("ipadapter")
            if "upscale" in lowered:
                tags.add("upscale")
            if "ksampler" in lowered or "sampler" in lowered:
                tags.add("sampling")

        return sorted(tags)
