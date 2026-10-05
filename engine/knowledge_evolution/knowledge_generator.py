"""
知识生成器

把挖掘出的模式转换成人类（和 Agent）可读的知识条目。

三层输出：
    pattern         节点组合的可读串
    frequency       出现次数
    description     这个模式属于哪类流程
    common_parameters 参数区间（来自 PatternMiner 的统计）
    recommendations 建议与风险提示（依据参数区间 + 已知领域规则）
"""

from typing import Dict, List, Any

from .models import WorkflowPattern, EvolutionKnowledge


# 领域风险规则：参数超出区间时的提示。
# TODO(待验证) 以下阈值来自通行经验，尚未用本项目真实 workflow 统计校准，
#   等 comfyui_library/workflows/ 有足够样本后应改由 PatternMiner 统计驱动。
RISK_RULES = {
    "cfg": {
        "min": 1.0,
        "max": 12.0,
        "high_msg": "CFG 偏高容易出现过度约束（如脸部异常、过饱和）",
        "low_msg": "CFG 过低可能导致 Prompt 约束不足、结果偏离描述",
    },
    "steps": {
        "min": 1,
        "max": 60,
        "high_msg": "steps 偏高收益递减且显著增加耗时",
        "low_msg": "steps 偏低可能导致细节不足",
    },
    "denoise": {
        "min": 0.1,
        "max": 1.0,
        "high_msg": "denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平",
    },
}


class KnowledgeGenerator:
    """
    模式到知识的转换器
    """

    def generate(self, pattern: Any) -> Dict:
        """
        生成知识条目

        Args:
            pattern: PatternMiner 产出的模式字典

        Returns:
            知识字典
        """
        if isinstance(pattern, WorkflowPattern):
            pattern = pattern.to_dict()

        nodes = pattern.get("nodes", []) or pattern.get("common_nodes", [])
        frequency = pattern.get("frequency", 0)

        joined = " + ".join(nodes)

        knowledge = {
            # name 与 pattern 同值：name 供 WorkflowPattern / 检索使用，
            # pattern 保持生成器的可读串格式
            "name": joined,
            "pattern": joined,
            "frequency": frequency,
            "description": self.describe(nodes),
            "workflow_type": pattern.get("workflow_type", ""),
            "common_parameters": pattern.get("parameter_ranges", {}),
            "recommendations": self.recommend(
                pattern.get("parameter_ranges", {}), nodes
            ),
            "tags": pattern.get("tags", []),
        }

        return knowledge

    def describe(self, nodes: List[str]) -> str:
        """
        判断节点组合属于哪类工作流

        Args:
            nodes: 节点类型列表

        Returns:
            描述文字
        """
        lowered = [n.lower() for n in nodes]

        def has(keyword: str) -> bool:
            return any(keyword in n for n in lowered)

        if has("upscale"):
            return "该Workflow属于放大/后处理流程"

        if has("ipadapter"):
            return "该Workflow属于IPAdapter参考图控制流程"

        if has("controlnet"):
            return "该Workflow属于ControlNet增强流程"

        if has("lora"):
            return "该Workflow包含风格或角色微调"

        if has("ksampler") or has("sampler"):
            return "该Workflow属于基础采样生成流程"

        return "通用ComfyUI生成流程"

    def recommend(
        self,
        parameter_ranges: Dict,
        nodes: List[str] = None
    ) -> List[str]:
        """
        基于参数统计生成建议与风险提示

        Args:
            parameter_ranges: PatternMiner 统计出的参数区间
            nodes: 节点列表（用于追加节点相关建议）

        Returns:
            建议列表
        """
        recommendations: List[str] = []

        for name, stats in parameter_ranges.items():
            if not isinstance(stats, dict):
                continue

            rule = RISK_RULES.get(name)
            if not rule:
                continue

            # 统计区间本身就是知识
            if stats.get("median") is not None:
                recommendations.append(
                    f"{name} 常用中位数 {stats['median']}"
                    f"（观测区间 {stats.get('min')} - {stats.get('max')}）"
                )

            observed_max = stats.get("max")
            if observed_max is not None and observed_max > rule["max"]:
                recommendations.append(
                    f"风险：观测到 {name}={observed_max}，"
                    f"已超出安全上限 {rule['max']} —— {rule.get('high_msg', '')}"
                )

            observed_min = stats.get("min")
            if observed_min is not None and observed_min < rule["min"]:
                recommendations.append(
                    f"风险：观测到 {name}={observed_min}，"
                    f"低于常用下限 {rule['min']} —— {rule.get('low_msg', '')}"
                )

        # ControlNet 特有建议
        if nodes:
            lowered = [n.lower() for n in nodes]
            if any("controlnet" in n for n in lowered):
                recommendations.append(
                    "ControlNet 权重过高会导致构图僵硬，建议从 0.5-0.8 起步再微调"
                )
                recommendations.append(
                    "ControlNet 流程中 KSampler 的 CFG 不宜过高，否则会与控制信号冲突"
                )

        if not recommendations:
            recommendations.append("样本量不足，暂无可靠建议，建议继续积累经验")

        return recommendations

    def generate_knowledge(
        self,
        patterns: List[Any]
    ) -> EvolutionKnowledge:
        """
        批量生成并封装为 EvolutionKnowledge

        Args:
            patterns: 模式列表

        Returns:
            EvolutionKnowledge 对象
        """
        from datetime import datetime

        items = [self.generate(p) for p in patterns]

        return EvolutionKnowledge(
            patterns=[WorkflowPattern.from_dict(item) for item in items],
            source_experience_count=sum(
                item.get("frequency", 0) for item in items
            ),
            updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
