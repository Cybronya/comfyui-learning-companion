"""
知识缺口检测

自主学习的核心不是「读已有知识」，而是**知道自己不知道什么**。

设计文档给的 detect() 用 `node not in knowledge` 精确匹配，这样会大量误判：
知识库存的是主题键（`ControlNet`、`KSampler`），工作流里的节点名是
`ControlNetApplyAdvanced`、`KSamplerAdvanced`，精确匹配全部落进「缺口」，
结果 Agent 以为自己什么都不懂。

所以这里做三层判定：
    1. 精确命中        节点名就是知识库里的键
    2. 别名命中        节点名属于某主题（如 ControlNetApply → ControlNet）
    3. 真的缺          前两层都没命中，才算缺口
"""

from typing import Any, Dict, List, Iterable

from .learning_state import GapItem
from .workflow_explorer import CORE_ROLES, CORE_TYPE_HINTS
from ..retrieval.knowledge_matcher import KnowledgeMatcher


# 明确不重要、不值得建卡的节点（纯工具性）
IGNORABLE = {
    "Note", "PrimitiveNode", "Reroute",
    "PreviewImage",  # 与 SaveImage 功能重叠，暂不算缺口
}


class KnowledgeGapDetector:
    """
    知识缺口检测器
    """

    def __init__(self, matcher: KnowledgeMatcher = None) -> None:
        """
        初始化检测器

        Args:
            matcher: 主题匹配器（用于别名判定）
        """
        self.matcher = matcher or KnowledgeMatcher()

    def detect(
        self,
        nodes: List[str],
        knowledge: Any,
        core_nodes: List[str] = None
    ) -> List:
        """
        检测知识缺口

        Args:
            nodes: 工作流节点清单
            knowledge: 已知知识。接受三种形式：
                       - dict：{键: [条目]}（retrieval 的知识库形态）
                       - KnowledgeIndex：有 keys() / search()
                       - set/list：直接的节点名集合
            core_nodes: 核心节点清单，用于标注缺口的优先级

        Returns:
            [GapItem]，按「是否核心节点」排序
        """
        if not nodes:
            return []

        known_keys = self._keys_of(knowledge)
        core = set(core_nodes) if core_nodes else set()
        # 没传核心节点清单时自行推断，否则 is_core 恒为 False，
        # 「核心缺口排前面」这个优先级就形同虚设
        infer_core = not core

        missing = []

        for node in nodes:
            if node in IGNORABLE:
                continue

            # 第一档：知识库直接有这个节点
            if node in known_keys:
                continue

            # 第二档：精确别名（同族同类，如 ControlNetApplyAdvanced）
            exact_topics = [
                t for t in self.matcher.topics_for_node(node, exact_only=True)
                if t in known_keys
            ]
            if exact_topics:
                continue

            # 第三档：只有类名片段命中的通用知识。
            # 这仍算缺口 —— 我们有 KSampler 的卡不代表懂 WanVideoSampler，
            # 但严重程度低于「完全没知识」，所以标 coverage=related。
            fragment_topics = [
                t for t in self.matcher.topics_for_node(node)
                if t in known_keys
            ]

            all_topics = self.matcher.topics_for_node(node)

            missing.append(GapItem(
                node_type=node,
                reason=self._reason_for(node, all_topics, fragment_topics),
                is_core=(
                    (node in core) if core else self._infer_core(node)
                ),
                coverage=(
                    "related" if fragment_topics else "none"
                ),
                related_topics=fragment_topics or all_topics,
            ))

        missing.sort(key=lambda g: (g.severity_rank, g.node_type))
        return missing

    def covered_nodes(
        self,
        nodes: List[str],
        knowledge: Any
    ) -> Dict[str, List[str]]:
        """
        找出每个节点分别由哪些知识条目覆盖

        Args:
            nodes: 节点清单
            knowledge: 已知知识

        Returns:
            {节点名: [知识条目名, ...]}
        """
        result: Dict[str, List[str]] = {}

        for node in nodes:
            names = self.entries_for_node(node, knowledge)
            if names:
                result[node] = names

        return result

    def entries_for_node(
        self,
        node: str,
        knowledge: Any
    ) -> List[str]:
        """
        取覆盖某节点的知识条目名
        """
        names = []

        # 直接搜节点名
        for item in self._search(knowledge, node):
            names.append(item.get("name", node))

        # 搜别名主题
        for topic in self.matcher.topics_for_node(node):
            for item in self._search(knowledge, topic):
                name = item.get("name", topic)
                if name not in names:
                    names.append(name)

        return names

    # ---------- 内部 ----------

    def _keys_of(self, knowledge: Any) -> set:
        """
        取知识库的全部键
        """
        if knowledge is None:
            return set()

        if isinstance(knowledge, dict):
            return set(knowledge.keys())

        # KnowledgeIndex
        if hasattr(knowledge, "keys"):
            return set(knowledge.keys())

        if isinstance(knowledge, (set, list, tuple)):
            return set(knowledge)

        return set()

    @staticmethod
    def _search(knowledge: Any, keyword: str) -> List[Dict]:
        """
        在知识库里检索单个关键词
        """
        if knowledge is None:
            return []

        if isinstance(knowledge, dict):
            return list(knowledge.get(keyword, []))

        if hasattr(knowledge, "search"):
            return list(knowledge.search(keyword))

        if isinstance(knowledge, (set, list, tuple)):
            # 集合形式只能按名字匹配
            return [{"name": k} for k in knowledge if keyword in str(k)]

        return []

    @staticmethod
    def _infer_core(node_type: str) -> bool:
        """
        推断某节点是否为核心节点

        没有 knowledge_loader 可查 role 时按类名片段判断。
        """
        lowered = node_type.lower()
        return any(hint in lowered for hint in CORE_TYPE_HINTS)

    @staticmethod
    def _reason_for(
        node: str,
        topics: List[str],
        fragment_topics: List[str] = None
    ) -> str:
        """
        说明为什么判为缺口，以及缺到什么程度
        """
        if fragment_topics:
            return (
                f"仅有 {'/'.join(fragment_topics)} 的通用知识，"
                f"没有该节点自己的说明"
            )

        if topics:
            # 有主题但主题没在知识库里 —— 说明该主题整体缺卡
            return f"相关主题 {'/'.join(topics)} 在知识库中无对应知识"

        return "知识库中没有该节点类型的任何知识"


