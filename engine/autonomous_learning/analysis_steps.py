"""
专项分析

执行 TaskPlanner 规划出的专项步骤。规划里的步骤如果没有对应实现，
报告里就会出现「计划做但实际没做」的假条目 —— 那比不规划更糟。

每条专项分析都必须是**从数据推导**的结论，阈值来自通行经验；
未用真实样本校准的阈值标 TODO(待验证)。
"""

from typing import Dict, List

from .learning_state import LearningState


# 各节点的常用参数区间。
# TODO(待验证) 以下阈值来自通行经验，尚未用 comfyui_library/workflows/
#   的真实样本统计校准。样本攒够后应改由 knowledge_evolution 的统计驱动。
PARAM_EXPECTATIONS = {
    "cfg": {
        "label": "Prompt 约束强度",
        "min": 1.0,
        "max": 12.0,
        "ideal": "5-9",
        "too_high": "过高会过度约束，常见脸部异常、画面僵硬",
        "too_low": "过低会导致 Prompt 约束不足、结果偏离描述",
    },
    "steps": {
        "label": "采样步数",
        "min": 8,
        "max": 50,
        "ideal": "20-35",
        "too_high": "偏高收益递减且显著增加耗时",
        "too_low": "偏低会导致细节不足",
    },
    "denoise": {
        "label": "重绘幅度",
        "min": 0.15,
        "max": 1.0,
        "ideal": "文生图固定 1.0",
        "too_high": "接近 1.0 时初始潜空间影响被抹平，等于重新生成",
        "too_low": "很低时改动区域有限，出图与原图差异小",
    },
    "controlnet_strength": {
        "label": "ControlNet 权重",
        "min": 0.3,
        "max": 1.0,
        "ideal": "0.5-0.8",
        "too_high": "过高会导致构图僵硬、控制过强",
        "too_low": "过低则控制信号弱，形同没有",
    },
    "strength_model": {
        "label": "LoRA 模型强度",
        "min": 0.3,
        "max": 1.2,
        "ideal": "0.5-1.0",
        "too_high": "过高容易过拟合、风格过曝、人物不像",
        "too_low": "过低则 LoRA 几乎不起作用",
    },
    "strength_clip": {
        "label": "LoRA 文本强度",
        "min": 0.3,
        "max": 1.2,
        "ideal": "0.8-1.0",
        "too_high": "过高会削弱 Prompt 的其他描述",
        "too_low": "过低则 LoRA 对 Prompt 适配不足",
    },
}

# 采样器粗分类，用于判断是否与模型代际匹配
SAMPLER_FAMILY = {
    "euler": "euler",
    "euler_ancestral": "euler",
    "heun": "heun",
    "dpmpp_2m": "dpmpp",
    "dpmpp_2m_sde": "dpmpp",
    "dpmpp_3m_sde": "dpmpp",
    "dpm_2": "dpm",
    "dpm_2_ancestral": "dpm",
    "ddim": "ddim",
    "uni_pc": "uni_pc",
    "plms": "plms",
}


class SpecialAnalyzer:
    """
    专项分析执行器
    """

    def run(self, step: str, state: LearningState) -> str:
        """
        执行一个专项步骤

        Args:
            step: 步骤名
            state: 学习状态

        Returns:
            一句话结论；无结论则返回空串
        """
        handler = {
            "study_controlnet_influence": self._controlnet,
            "study_lora_influence": self._lora,
            "compare_parameter_values": self._compare_params,
            "evaluate_generation_quality": self._quality,
            "extract_reproducible_parameters": self._reproducible,
            "trace_problem_root_cause": self._root_cause,
            "explain_denoise_semantics": self._denoise,
            "evaluate_upscale_chain": self._upscale,
            "check_lora_only_workflow": self._lora_only,
            "check_portability": self._portability,
        }.get(step)

        if handler is None:
            return ""

        try:
            return handler(state)
        except Exception:
            return ""

    # ---------- 各专项 ----------

    def _controlnet(self, state: LearningState) -> str:
        params = state.parameters
        if "controlnet_strength" not in params:
            return ""

        value = params["controlnet_strength"]
        rule = PARAM_EXPECTATIONS["controlnet_strength"]

        text = (
            f"ControlNet 权重 {value}（常用 {rule['ideal']}）。"
            f"控制过强会让构图僵硬，权重过低则形同没接。"
        )

        if isinstance(value, (int, float)) and value > rule["max"]:
            text += f" 当前值偏高：{rule['too_high']}。"
        elif isinstance(value, (int, float)) and value < rule["min"]:
            text += f" 当前值偏低：{rule['too_low']}。"

        # ControlNet 与 CFG 的相互影响
        cfg = params.get("cfg")
        if isinstance(cfg, (int, float)) and cfg > 9:
            text += (
                f" 另外 CFG={cfg} 偏高，ControlNet 流程中"
                f"过高 CFG 会与控制信号冲突，建议一起下调。"
            )

        return text

    def _lora(self, state: LearningState) -> str:
        params = state.parameters
        if "strength_model" not in params and "strength_clip" not in params:
            return ""

        parts = []
        for name in ("strength_model", "strength_clip"):
            value = params.get(name)
            if value is None:
                continue
            rule = PARAM_EXPECTATIONS[name]
            text = f"{rule['label']} {value}（常用 {rule['ideal']}）"
            if isinstance(value, (int, float)) and value > rule["max"]:
                text += f"，偏高会{rule['too_high'].lstrip('过高会')}"
            elif isinstance(value, (int, float)) and value < rule["min"]:
                text += f"，偏低会{rule['too_low'].lstrip('过低会')}"
            parts.append(text)

        if "lora_name" in params:
            parts.insert(0, f"加载 LoRA：{params['lora_name']}")

        return "；".join(parts) + "。"

    def _compare_params(self, state: LearningState) -> str:
        """参数与经验区间对比（经验区间来自演化知识，此处用阈值近似）"""
        findings = self._check_expectations(state)
        if not findings:
            return "所有关键参数都在常用区间内。"
        return "参数对比：" + "；".join(findings)

    def _quality(self, state: LearningState) -> str:
        findings = self._check_expectations(state)
        sampler = state.parameters.get("sampler_name")

        parts = []
        if findings:
            parts.append("参数偏离：" + "；".join(findings))

        if sampler:
            family = SAMPLER_FAMILY.get(str(sampler).lower(), "其他")
            parts.append(
                f"采样器 {sampler}（{family} 族）——"
                f"不同族的速度/细节/风格取向不同，"
                f"换族后不宜直接对比结果"
            )

        return "。".join(parts) + "。" if parts else ""

    def _reproducible(self, state: LearningState) -> str:
        """提取可复现基线"""
        params = state.parameters
        if not params:
            return ""

        keys = [
            "checkpoint", "lora_name", "strength_model", "strength_clip",
            "prompt", "negative", "seed", "steps", "cfg",
            "sampler_name", "scheduler", "denoise",
            "width", "height",
        ]
        present = [k for k in keys if k in params]

        if not present:
            return ""

        return (
            "可复现基线（固定这些参数后对比才有意义）："
            + "、".join(f"{k}={params[k]}" for k in present)
        )

    def _root_cause(self, state: LearningState) -> str:
        """现象与诊断的关联"""
        diagnostics = state.diagnostic_findings
        if not diagnostics:
            return ""

        return (
            f"本次参数体检发现 {len(diagnostics)} 个问题，"
            f"若你遇到的现象与它们相关，优先从这里查："
            + "；".join(diagnostics[:3])
        )

    def _denoise(self, state: LearningState) -> str:
        value = state.parameters.get("denoise")
        if value is None:
            return ""

        if isinstance(value, (int, float)) and value >= 0.99:
            return (
                f"denoise={value}：文生图标准做法，等于完全按 Prompt 重生成。"
            )

        if isinstance(value, (int, float)) and value < 0.6:
            return (
                f"denoise={value}：img2img 的低重绘模式，"
                f"保留原图结构更强，改动区域有限。"
            )

        return f"denoise={value}：部分重绘，改动幅度中等。"

    def _upscale(self, state: LearningState) -> str:
        if not any("upscale" in n.lower() for n in state.nodes()):
            return ""

        return (
            "工作流含放大环节：需注意放大模型与重绘比例的配合，"
            "重绘太低会把放大产生的伪影固化下来"
        )

    def _lora_only(self, state: LearningState) -> str:
        if "strength_clip" not in state.parameters:
            return ""

        return (
            "工作流只有 LoRA 没有 ControlNet：风格靠 LoRA 控制，"
            "构图靠 Prompt 与底模。此时调 LoRA 强度是改变风格的最直接手段"
        )

    def _portability(self, state: LearningState) -> str:
        params = state.parameters
        risks = []

        if "checkpoint" in params:
            risks.append("换底模会改变画风与分辨率适配")
        if "lora_name" in params:
            risks.append("LoRA 与底模不匹配时可能失效或出噪点")

        if not risks:
            return ""

        return "迁移注意：" + "；".join(risks)

    # ---------- 工具 ----------

    def _check_expectations(self, state: LearningState) -> List[str]:
        """
        检查所有参数是否落在常用区间
        """
        findings = []

        for name, value in state.parameters.items():
            rule = PARAM_EXPECTATIONS.get(name)
            if rule is None or not isinstance(value, (int, float)):
                continue
            if isinstance(value, bool):
                continue

            if value > rule["max"]:
                findings.append(
                    f"{rule['label']}={value} 超出常用上限 "
                    f"{rule['max']}（常用 {rule['ideal']}）：{rule['too_high']}"
                )
            elif value < rule["min"]:
                findings.append(
                    f"{rule['label']}={value} 低于常用下限 "
                    f"{rule['min']}（常用 {rule['ideal']}）：{rule['too_low']}"
                )

        return findings
