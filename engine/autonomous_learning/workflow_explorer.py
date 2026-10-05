"""
工作流探索器

主动读懂一个 workflow：结构、核心节点、生成流程阶段、关键参数。

设计文档里的 explore() 只返回 analyzer.analyze() 的结果，
但 WorkflowAnalyzer 只给 nodes / connections / patterns / workflow_type，
缺少「Model → Condition → Sampling → Decode」这条生成流程链。
而这条链恰恰是理解一个 workflow 的关键 —— 它回答「数据怎么一步步变成图」。

所以这里在 analyzer 结果之上再推导：
    pipeline        生成流程阶段序列
    core_nodes      核心节点（对生成结果有实质影响的）
    parameters      关键参数实测值
"""

from typing import Any, Dict, List


# 节点类别 / 角色 → 生成流程阶段。
# 依据 comfyui_library/knowledge/node_index.json 的 category 与 role 字段。
CATEGORY_TO_STAGE = {
    "Model Loading": "Model",
    "Text Conditioning": "Condition",
    "Latent Generation": "Latent",
    "Diffusion Sampling": "Sampling",
    "Latent Conversion": "Decode",
    "Output": "Output",
    "Image Processing": "Process",
    "Control": "Control",
    "IPAdapter": "Control",
}

ROLE_TO_STAGE = {
    "load_checkpoint": "Model",
    "load_lora": "Model",
    "text_encoder": "Condition",
    "latent_initializer": "Latent",
    "sampler": "Sampling",
    "latent_decoder": "Decode",
    "latent_encoder": "Encode",
    "image_output": "Output",
}

# 阶段在生成流程中的先后顺序
STAGE_ORDER = [
    "Model", "Encode", "Condition", "Latent", "Control",
    "Sampling", "Decode", "Process", "Output",
]

# 核心节点：缺了它生成结果就不对
CORE_ROLES = {
    "load_checkpoint",
    "load_lora",
    "text_encoder",
    "sampler",
    "latent_decoder",
    "latent_initializer",
}

# 核心节点类型关键词（role 缺失时的兜底）
CORE_TYPE_HINTS = (
    "checkpointloader", "unetloader", "loraloader",
    "cliptextencode", "ksampler", "sampler",
    "vaedecode", "vaeencode", "emptylatent",
    "controlnetapply", "ipadapterapply",
)

# 参数名 → 中文说明
PARAM_LABELS = {
    "seed": "随机种子",
    "steps": "采样步数",
    "cfg": "Prompt 约束强度",
    "sampler_name": "采样算法",
    "scheduler": "调度器",
    "denoise": "重绘幅度",
    "width": "宽度",
    "height": "高度",
    "batch_size": "批量大小",
    "strength_model": "LoRA 模型强度",
    "strength_clip": "LoRA 文本强度",
    "weight": "ControlNet 权重",
    "control_after_generate": "步数控制方式",
}


class WorkflowExplorer:
    """
    workflow 主动探索器
    """

    def __init__(self, analyzer=None, knowledge_loader=None) -> None:
        """
        初始化探索器

        Args:
            analyzer: WorkflowAnalyzer 实例
            knowledge_loader: NodeKnowledgeLoader 实例，
                             用来取节点的 category / role（判断核心节点与阶段必需）
        """
        self.analyzer = analyzer
        self.knowledge_loader = knowledge_loader

    def explore(self, workflow: Any) -> Dict:
        """
        探索 workflow

        Args:
            workflow: workflow dict（analyzer 收 dict，不收路径）

        Returns:
            {
                "type": 工作流类型,
                "nodes": 节点清单,
                "pipeline": 生成流程阶段,
                "core_nodes": 核心节点,
                "stages": 每个阶段的节点归属,
                "connections": 连接信息,
                "patterns": 识别到的模式,
            }
        """
        analysis = {}

        if self.analyzer is not None:
            analysis = self.analyzer.analyze(workflow) or {}

        node_info = self._node_info_of(workflow)

        stages = self._build_stages(node_info)
        pipeline = self._order_stages(stages)
        core_nodes = self._core_nodes(node_info)

        result = {
            "type": analysis.get("workflow_type", "") or "",
            "nodes": analysis.get("nodes") or list(node_info.keys()),
            "pipeline": pipeline,
            "core_nodes": core_nodes,
            "stages": stages,
            "connections": analysis.get("connections", {}),
            "patterns": analysis.get("patterns", []),
        }

        return result

    def extract_parameters(
        self,
        workflow: Any
    ) -> Dict:
        """
        提取关键参数实测值

        Args:
            workflow: workflow dict

        Returns:
            {参数名: 值}，附中文说明放在 PARAM_LABELS
        """
        params: Dict = {}

        if not isinstance(workflow, dict):
            return params

        for node in workflow.get("nodes", []):
            node_type = node.get("type", "")
            widgets = node.get("widgets_values", []) or []

            if "KSampler" in node_type and len(widgets) >= 7:
                names = [
                    "seed", "control_after_generate", "steps", "cfg",
                    "sampler_name", "scheduler", "denoise",
                ]
                for name, value in zip(names, widgets):
                    if name == "control_after_generate":
                        continue
                    params[name] = value
            elif "EmptyLatent" in node_type and len(widgets) >= 2:
                params["width"] = widgets[0]
                params["height"] = widgets[1]
                if len(widgets) >= 3:
                    params["batch_size"] = widgets[2]
            elif "CheckpointLoader" in node_type and widgets:
                params["checkpoint"] = widgets[0]
            elif "LoraLoader" in node_type and len(widgets) >= 3:
                params["lora_name"] = widgets[0]
                params["strength_model"] = widgets[1]
                params["strength_clip"] = widgets[2]
            elif "ControlNetApply" in node_type and widgets:
                # ControlNetApplyAdvanced 的 widgets:
                # [strength, start, end, ...]；基础版只有 strength
                params["controlnet_strength"] = widgets[0]

        return params

    @staticmethod
    def describe_parameters(params: Dict) -> List[str]:
        """
        把参数翻成「中文名 = 值」
        """
        lines = []

        for name, value in params.items():
            label = PARAM_LABELS.get(name, name)
            lines.append(f"{label}（{name}）= {value}")

        return lines

    # ---------- 内部 ----------

    def _node_info_of(self, workflow: Any) -> Dict[str, Dict]:
        """
        取每个节点的 type / category / role
        """
        result: Dict[str, Dict] = {}

        if not isinstance(workflow, dict):
            return result

        for node in workflow.get("nodes", []):
            node_type = node.get("type", "")
            if not node_type:
                continue

            info = {"type": node_type}

            if self.knowledge_loader is not None:
                try:
                    meta = self.knowledge_loader.load(node_type)
                except Exception:
                    meta = None
                if meta:
                    info["category"] = meta.get("category", "")
                    info["role"] = meta.get("role", "")
                    info["difficulty"] = meta.get("difficulty", "")

            result.setdefault(node_type, info)

        return result

    def _stage_of(self, info: Dict) -> str:
        """
        判断节点属于哪个生成阶段
        """
        category = info.get("category", "")
        role = info.get("role", "")

        if category in CATEGORY_TO_STAGE:
            return CATEGORY_TO_STAGE[category]
        if role in ROLE_TO_STAGE:
            return ROLE_TO_STAGE[role]

        # 都没有时按类名片段兜底
        lowered = info.get("type", "").lower()

        if "checkpoint" in lowered or "unet" in lowered:
            return "Model"
        if "lora" in lowered:
            return "Model"
        if "controlnet" in lowered or "ipadapter" in lowered:
            return "Control"
        if "cliptext" in lowered or "conditioning" in lowered:
            return "Condition"
        if "emptylatent" in lowered:
            return "Latent"
        if "sampler" in lowered:
            return "Sampling"
        if "vaedecode" in lowered:
            return "Decode"
        if "vaeencode" in lowered:
            return "Encode"
        if "upscale" in lowered:
            return "Process"
        if "saveimage" in lowered or "previewimage" in lowered:
            return "Output"

        return "Other"

    def _build_stages(self, node_info: Dict[str, Dict]) -> Dict[str, List[str]]:
        """
        按阶段归类节点
        """
        stages: Dict[str, List[str]] = {}

        for node_type, info in node_info.items():
            stage = self._stage_of(info)
            stages.setdefault(stage, []).append(node_type)

        return stages

    @staticmethod
    def _order_stages(stages: Dict[str, List[str]]) -> List[str]:
        """
        把阶段排成生成流程顺序
        """
        known = [s for s in STAGE_ORDER if s in stages]
        unknown = [s for s in stages if s not in STAGE_ORDER]

        return known + sorted(unknown)

    def _core_nodes(self, node_info: Dict[str, Dict]) -> List[str]:
        """
        识别核心节点
        """
        core = []

        for node_type, info in node_info.items():
            role = info.get("role", "")
            if role in CORE_ROLES:
                core.append(node_type)
                continue

            lowered = node_type.lower()
            if any(hint in lowered for hint in CORE_TYPE_HINTS):
                core.append(node_type)

        return core
