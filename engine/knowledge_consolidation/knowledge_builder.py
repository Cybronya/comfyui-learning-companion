"""
知识构建

把模式 + 参数统计 + 常见问题组装成可读可用的知识条目。

三件事设计稿没做，这里补上：

1. **常见问题要真正聚合**。目标是「Common Problems: ControlNet weight 过高」，
   但输入里根本没人处理 `diagnostic_issues`。而这份数据就在学习记录的
   frontmatter 里 —— 不聚合就等于丢掉了最有价值的部分。
   做法是按「去掉具体数值后的骨架」归并同类项，
   统计出现次数，次数越多说明这个模式越容易踩这个坑。

2. **参数建议要区分可信度**。3 个样本得出的「典型区间」是噪声。
   样本少或集中度低时，明说「样本不足」而不是硬给区间。

3. **阈值不重复定义**。cfg/steps 的安全上下限复用
   knowledge_evolution.knowledge_generator.RISK_RULES ——
   两边各写一份必然发散。
"""

import re
from typing import List, Dict, Any

from .models import (
    WorkflowPattern,
    ConsolidatedKnowledge,
    ParameterStat,
    LEVEL_STRONG,
    LEVEL_MODERATE,
    LEVEL_WEAK,
)
from .experience_loader import ExperienceRow


# 复用 knowledge_evolution 的风险阈值，不重复定义
try:
    from ..knowledge_evolution.knowledge_generator import RISK_RULES
except ImportError:                                  # pragma: no cover
    RISK_RULES = {}

# 问题文本里的具体数值，归并同类项时抹掉
_NUM_PATTERNS = [
    re.compile(r"\d+\.?\d*"),          # 数字（含小数）
    re.compile(r"[\w\-./]+\.(?:json|png|safetensors|ckpt)"),
]


class KnowledgeBuilder:
    """
    知识构建器
    """

    def __init__(self, risk_rules: Dict = None) -> None:
        """
        初始化构建器

        Args:
            risk_rules: 风险阈值表；None 时复用 knowledge_evolution 的
        """
        self.risk_rules = risk_rules if risk_rules is not None \
            else RISK_RULES

    def build(
        self,
        patterns: List[WorkflowPattern],
        grouped: Dict[str, List[ExperienceRow]] = None
    ) -> ConsolidatedKnowledge:
        """
        构建知识

        Args:
            patterns: 已挖出的模式（参数统计可能尚未填入）
            grouped: {模式名: 成员记录}，用于填参数统计与常见问题

        Returns:
            ConsolidatedKnowledge
        """
        grouped = grouped or {}

        knowledge = ConsolidatedKnowledge()

        for pattern in patterns:
            members = grouped.get(pattern.name, [])

            if members:
                pattern.parameter_stats = self._parameter_stats(
                    members
                )
                pattern.common_problems = self.aggregate_problems(
                    members
                )

            pattern.recommendations = self.recommend(pattern)
            pattern.level = self._level(pattern)
            knowledge.patterns.append(pattern)

        return knowledge

    # ---------- 参数统计 ----------

    def _parameter_stats(
        self,
        members: List[ExperienceRow]
    ) -> Dict[str, ParameterStat]:
        """
        按模式分组统计参数（不与其他模式混合）
        """
        from .parameter_statistics import ParameterStatistics

        return ParameterStatistics().analyze(members)

    # ---------- 常见问题 ----------

    def aggregate_problems(
        self,
        members: List[ExperienceRow]
    ) -> List[Dict]:
        """
        聚合同类问题

        「[medium] CFG值较高（当前 30.0），可能导致Prompt约束过强」
        与「[medium] CFG值较高（当前 25.0），可能导致Prompt约束过强」
        是同一个问题，只是数值不同 —— 按骨架归并，
        次数越多说明这个模式越容易踩坑。

        Args:
            members: 模式成员

        Returns:
            [{"problem", "count", "severity", "samples"}]，按次数降序
        """
        buckets: Dict[str, Dict] = {}

        for row in members:
            for raw in row.problems or []:
                text = str(raw).strip()
                if not text:
                    continue

                severity, body = self._split_severity(text)
                skeleton = self._skeleton(body)

                if skeleton not in buckets:
                    buckets[skeleton] = {
                        "problem": skeleton,
                        "count": 0,
                        "severity": severity,
                        "samples": [],
                    }

                entry = buckets[skeleton]
                entry["count"] += 1
                if len(entry["samples"]) < 3 and body not in \
                        entry["samples"]:
                    entry["samples"].append(body)

        ranked = sorted(
            buckets.values(),
            key=lambda e: (-e["count"], e["problem"]),
        )

        return ranked

    @staticmethod
    def _split_severity(text: str):
        """
        拆出严重度

        输入形如 "[medium] 描述 → 建议"
        """
        text = text.strip()
        if text.startswith("["):
            end = text.find("]")
            if end > 0:
                return text[1:end].strip(), text[end + 1:].strip()

        return "", text

    @staticmethod
    def _skeleton(body: str) -> str:
        """
        抽取问题的骨架（去掉具体数值与建议尾巴）

        这样「CFG 30.0 偏高」和「CFG 25.0 偏高」会归成同一类。
        """
        # 去掉「→ 建议…」尾巴：建议是结果，不是问题本身
        text = body.split("→")[0].strip()

        for pattern in _NUM_PATTERNS:
            text = pattern.sub("N", text)

        # 归并空白与标点差异
        text = re.sub(r"[\s，,、]+", "", text)

        return text

    # ---------- 建议 ----------

    def recommend(self, pattern: WorkflowPattern) -> List[str]:
        """
        生成建议与风险提示
        """
        recommendations: List[str] = []

        sample_note = self._sample_note(pattern)

        # 1. 参数典型取值
        for name, stat in pattern.parameter_stats.items():
            if stat.count < 2:
                continue

            label = self._param_label(name)

            if stat.is_numeric:
                # 拼装成「A 中位数 X ｜ 区间 min-max ｜ n 个样本 ｜ 一致性 n%」
                # 避免嵌套括号：分句用「，」分隔，每项各自成句
                parts = [f"{label} 中位数 {stat.median:g}"]

                if stat.typical_range:
                    parts.append(f"观测区间 {stat.typical_range}")
                else:
                    parts.append("样本不足，未给区间")

                parts.append(f"{stat.count} 个样本")

                if stat.consistency >= 0.8:
                    parts.append(f"取值集中（一致性 {stat.consistency:.0%}）")
                elif stat.consistency < 0.5:
                    parts.append(
                        f"取值分散，一致性仅 {stat.consistency:.0%}"
                    )

                text = "，".join(parts)
            else:
                text = (
                    f"{label} 最常用 {stat.most_common}，"
                    f"{stat.count} 个样本，"
                    f"一致性 {stat.consistency:.0%}"
                )

            recommendations.append(text)

        # 2. 风险：实际观测超出安全阈值
        for name, stat in pattern.parameter_stats.items():
            if not stat.is_numeric:
                continue

            rule = self.risk_rules.get(name)
            if not rule:
                continue

            label = self._param_label(name)

            if stat.max > rule["max"]:
                recommendations.append(
                    f"风险：{label} 观测到 {stat.max:g}，"
                    f"超出安全上限 {rule['max']:g}"
                    f"（{rule.get('high_msg', '')}）"
                )
            if stat.min < rule["min"]:
                recommendations.append(
                    f"风险：{label} 观测到 {stat.min:g}，"
                    f"低于常用下限 {rule['min']:g}"
                    f"（{rule.get('low_msg', '')}）"
                )

        # 3. 常见问题
        for problem in pattern.common_problems[:2]:
            ratio = problem["count"] / max(pattern.frequency, 1)
            if ratio >= 0.5:
                recommendations.append(
                    f"高发问题（{problem['count']}/{pattern.frequency} "
                    f"个样本）：{problem['problem']}"
                )

        # 4. 知识缺口
        if pattern.missing_nodes:
            recommendations.append(
                "这些节点还没有知识卡，系统对它们的理解有限："
                + "、".join(pattern.missing_nodes[:5])
            )

        # 5. 样本量提醒放最后，避免盖过实质内容
        if sample_note:
            recommendations.append(sample_note)

        if not recommendations:
            recommendations.append(
                "样本量不足且无参数可统计，暂无法归纳出可靠结论"
            )

        return recommendations

    @staticmethod
    def _sample_note(pattern: WorkflowPattern) -> str:
        """
        样本量与可信度说明
        """
        if pattern.frequency < 3:
            return (
                f"注意：仅 {pattern.frequency} 个样本，"
                f"上述结论仅供参考，建议积累到 5 个以上再据此调参"
            )
        return ""

    @staticmethod
    def _level(pattern: WorkflowPattern) -> str:
        """
        归纳等级
        """
        if pattern.frequency < 3:
            return LEVEL_WEAK

        consistencies = [
            s.consistency for s in pattern.parameter_stats.values()
            if s.is_numeric and s.count >= 2
        ]

        if not consistencies:
            return LEVEL_MODERATE

        avg = sum(consistencies) / len(consistencies)
        if avg >= 0.85:
            return LEVEL_STRONG
        if avg >= 0.6:
            return LEVEL_MODERATE
        return LEVEL_WEAK

    @staticmethod
    def _param_label(name: str) -> str:
        """
        参数名转中文
        """
        return {
            "cfg": "Prompt 约束强度(CFG)",
            "steps": "采样步数",
            "denoise": "重绘幅度",
            "sampler_name": "采样算法",
            "scheduler": "调度器",
            "width": "宽度",
            "height": "高度",
            "controlnet_strength": "ControlNet 权重",
            "strength_model": "LoRA 模型强度",
            "strength_clip": "LoRA 文本强度",
        }.get(name, name)

    # ---------- 跨模式对比 ----------

    def cross_pattern_notes(
        self,
        knowledge: ConsolidatedKnowledge,
        grouped: Dict[str, List[ExperienceRow]]
    ) -> List[str]:
        """
        跨模式对比

        找出「不同流程参数偏好不同」这类规律。
        """
        from .parameter_statistics import ParameterStatistics

        notes = ParameterStatistics().compare_across(grouped)
        knowledge.global_observations.extend(notes)
        return notes
