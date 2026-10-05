"""
改进分析器

分析修改是否符合预期，推断可能的效果
"""

from typing import List, Dict
from .models import WorkflowChange


class ImprovementAnalyzer:
    """
    改进分析器
    """

    def analyze(
        self,
        changes: Dict,
        workflow_type: str = None
    ) -> List[str]:
        """
        分析修改的影响

        Args:
            changes: 比较结果
            workflow_type: 工作流类型（可选）

        Returns:
            观察列表
        """
        observations = []

        params = changes.get("parameters", {})

        # 分析 steps 参数
        if "steps" in params:
            old = params["steps"]["old"]
            new = params["steps"]["new"]

            if new > old:
                observations.append(
                    "steps增加，可能提升细节表现"
                )
            elif new < old:
                observations.append(
                    "steps减少，可能提升生成速度"
                )

        # 分析 cfg 参数
        if "cfg" in params:
            old = params["cfg"]["old"]
            new = params["cfg"]["new"]

            if new > old:
                observations.append(
                    "CFG提高，可能增强Prompt约束"
                )
            elif new < old:
                observations.append(
                    "CFG降低，可能减少Prompt过度约束，提升生成质量"
                )

        # 分析种子参数
        if "seed" in params:
            old = params["seed"]["old"]
            new = params["seed"]["new"]

            if new != old:
                observations.append(
                    "种子值改变，生成结果会不同"
                )

        # 分析采样器参数
        if "sampler_name" in params:
            old = params["sampler_name"]["old"]
            new = params["sampler_name"]["new"]

            if old != new:
                observations.append(
                    f"采样器从 {old} 改为 {new}，可能影响生成风格"
                )

        # 分析步长/迭代次数
        if "denoise" in params:
            old = params["denoise"]["old"]
            new = params["denoise"]["new"]

            if new > old:
                observations.append(
                    "denoise增加，可能提升修改幅度"
                )
            elif new < old:
                observations.append(
                    "denoise减少，可能减少修改幅度"
                )

        # 分析预处理器参数
        if "preprocessor" in params:
            old = params["preprocessor"]["old"]
            new = params["preprocessor"]["new"]

            if old != new:
                observations.append(
                    f"预处理器从 {old} 改为 {new}"
                )

        # 如果没有检测到参数变化，给出通用建议
        if not observations and params:
            observations.append(
                "参数已修改，建议观察生成效果"
            )

        # 根据工作流类型添加特定分析
        if workflow_type == "image_generation":
            if "width" in params and "height" in params:
                old_w = params["width"]["old"]
                old_h = params["height"]["old"]
                new_w = params["width"]["new"]
                new_h = params["height"]["new"]

                if new_w > old_w or new_h > old_h:
                    observations.append(
                        "分辨率提升，可能影响生成时间和细节"
                    )

        return observations

    def generate_conclusion(
        self,
        changes: Dict,
        observations: List[str]
    ) -> str:
        """
        生成总结性结论

        Args:
            changes: 比较结果
            observations: 观察列表

        Returns:
            结论
        """
        if not observations:
            return "无明显变化"

        # 统计变化类型
        param_changes = changes.get("parameters", {})
        node_changes = changes.get("nodes_changed", [])

        # 构建结论
        conclusion_parts = []

        if param_changes:
            conclusion_parts.append(f"修改了 {len(param_changes)} 个参数")

        if node_changes:
            conclusion_parts.append(f"添加/删除了 {len(node_changes)} 个节点")

        if conclusion_parts:
            conclusion = "，".join(conclusion_parts)
            conclusion += "，效果需要实际验证"
        else:
            conclusion = "无明显变化"

        return conclusion

    def extract_tags(
        self,
        changes: Dict
    ) -> List[str]:
        """
        从变化中提取标签

        Args:
            changes: 比较结果

        Returns:
            标签列表
        """
        tags = []

        params = changes.get("parameters", {})

        # 从参数变化中提取标签
        for param_name in params.keys():
            if "steps" in param_name.lower():
                tags.append("quality")
            elif "cfg" in param_name.lower():
                tags.append("prompt_control")
            elif "seed" in param_name.lower():
                tags.append("reproducibility")
            elif "sampler" in param_name.lower():
                tags.append("sampling_method")

        # 从节点变化中提取标签
        nodes = changes.get("nodes_changed", [])
        for node in nodes:
            if "added" in node:
                tags.append("new_component")
            elif "removed" in node:
                tags.append("removed_component")

        return list(set(tags))  # 去重
