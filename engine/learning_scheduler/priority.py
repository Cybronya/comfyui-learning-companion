"""
优先级计算

决定「先学哪个」。设计稿的做法是只看文件名里有没有 sdxl/controlnet/lora，
权重 10/10/5。这条规则有两个问题：

    1. 文件名是用户随手取的。`img_20240312.png` 得 0 分，
       而一个真正用了 ControlNet 但叫 `a.json` 的 workflow 也只按名字判断 ——
       名字里的关键词和实际节点结构没有必然关系。
    2. 内容完全没参与排序。1000 个文件里哪个「知识缺口最大」才是真正该优先的。

所以优先级改成三档信号，文件名只占最小权重：

    内容信号（主要，读 workflow 实际节点）
        节点越多 → 流程越复杂 → 越该先学
        没有知识卡的节点越多 → 缺口越大 → 学完收益越高
        含已建卡但从未学过的节点类型 → 新颖

    历史信号
        上次失败过但可能已修好 → 略微提权
        重试次数越多 → 提权（可能是偶发问题）

    文件名信号（保留但弱化）
        sdxl/controlnet 等关键词仅作 tie-break，不主导排序

排序结果附带 priority_reasons，写进记录 ——
「为什么先学它」应该能事后解释，否则调度不可调试。
"""

from typing import List, Dict, Any, Optional, Set

from ..autonomous_learning.knowledge_gap_detector import KnowledgeGapDetector


# 文件名关键词 → 分值。刻意给得很低（远小于内容信号），
# 只用于节点数相当时决定先后
FILENAME_HINTS = {
    "sdxl": 10,
    "flux": 10,
    "controlnet": 10,
    "pose": 5,
    "lora": 5,
    "hires": 3,
    "video": 3,
    "wan": 5,
}

# 内容信号权重
WEIGHT_PER_NODE = 1              # 每个节点 1 分
WEIGHT_PER_UNKNOWN_NODE = 8      # 每个缺卡节点 8 分（缺口价值最大）
WEIGHT_NOVEL_NODE_TYPE = 4        # 每种没见过的节点类型
WEIGHT_RETRY = 2                 # 每失败过一次
WEIGHT_CONTENT_CHANGED = 5       # 内容变了（用户改过，更该重学）


class PriorityCalculator:
    """
    优先级计算器
    """

    def __init__(
        self,
        known_node_types: Set[str] = None,
        known_knowledge: Any = None,
        gap_detector: KnowledgeGapDetector = None,
        filename_weight: float = 1.0
    ) -> None:
        """
        初始化计算器

        Args:
            known_node_types: **已有知识卡**的节点类型集合。
                              通常来自 comfyui_library/knowledge/node_index.json ——
                              它精确列出了哪些节点写过卡，是「有无知识」的权威依据。
            known_knowledge: 已知知识对象；给了就用缺口检测器做别名判定
                             （更准，能识别「有同族通用知识」）
            gap_detector: 缺口检测器
            filename_weight: 文件名信号缩放，默认 1.0（只作 tie-break）
        """
        self.known_node_types = known_node_types or set()
        self.known_knowledge = known_knowledge
        self.gap_detector = gap_detector or KnowledgeGapDetector()
        self.filename_weight = filename_weight

    def calculate(
        self,
        workflow: Dict,
        nodes: List[str] = None,
        retry_count: int = 0,
        content_changed: bool = False
    ) -> Dict:
        """
        计算优先级

        Args:
            workflow: 扫描器产出的条目（含 name / path / key）
            nodes: 该 workflow 的节点清单；None 时由调用方预先读出
            retry_count: 之前失败次数
            content_changed: 内容是否变化过

        Returns:
            {"score": int, "reasons": [str], "node_count": int,
             "unknown_node_count": int}
        """
        nodes = nodes or []
        reasons: List[str] = []
        score = 0

        # ---- 内容信号 ----
        node_count = len(nodes)
        if node_count:
            score += node_count * WEIGHT_PER_NODE
            reasons.append(f"{node_count} 个节点（+{node_count}）")

        unknown = self._unknown_nodes(nodes)
        if unknown:
            score += len(unknown) * WEIGHT_PER_UNKNOWN_NODE
            reasons.append(
                f"{len(unknown)} 个节点缺知识卡："
                + "、".join(unknown[:4])
                + ("…" if len(unknown) > 4 else "")
                + f"（+{len(unknown) * WEIGHT_PER_UNKNOWN_NODE}）"
            )

        novel = [
            n for n in nodes if n not in self.known_node_types
        ]
        if novel:
            score += len(novel) * WEIGHT_NOVEL_NODE_TYPE
            reasons.append(
                f"{len(novel)} 种未见过的节点类型："
                + "、".join(list(dict.fromkeys(novel))[:4])
            )

        # ---- 历史信号 ----
        if retry_count:
            score += retry_count * WEIGHT_RETRY
            reasons.append(
                f"曾失败 {retry_count} 次（+{retry_count * WEIGHT_RETRY}）"
            )

        if content_changed:
            score += WEIGHT_CONTENT_CHANGED
            reasons.append(
                f"内容已变更，需重学（+{WEIGHT_CONTENT_CHANGED}）"
            )

        # ---- 文件名信号（弱化，只作 tie-break）----
        name = str(workflow.get("name", "")).lower()
        filename_score = 0
        matched = [
            hint for hint in FILENAME_HINTS if hint in name
        ]
        if matched:
            filename_score = sum(
                FILENAME_HINTS[h] for h in matched
            )
            score += int(filename_score * self.filename_weight)
            reasons.append(
                f"文件名含 {'/'.join(matched)}"
                f"（+{int(filename_score * self.filename_weight)}，弱信号）"
            )

        return {
            "score": score,
            "reasons": reasons,
            "node_count": node_count,
            "unknown_node_count": len(unknown),
        }

    def _unknown_nodes(self, nodes: List[str]) -> List[str]:
        """
        找出没有知识卡的节点

        优先用 known_node_types（node_index.json 的权威列表），
        它是精确的「有没有写过卡」。没有该集合时才退回缺口检测器 ——
        检测器有别名判定，能识别「只有同族通用知识」这种半吊子情况，
        但需要传入真实的知识对象。
        """
        if not nodes:
            return []

        if self.known_node_types:
            return [n for n in nodes if n not in self.known_node_types]

        if self.known_knowledge is not None:
            gaps = self.gap_detector.detect(nodes, self.known_knowledge)
            return [g.node_type for g in gaps]

        return []
