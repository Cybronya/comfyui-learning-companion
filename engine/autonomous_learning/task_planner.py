"""
任务规划器

把「学一个 workflow」拆成可执行步骤。

与设计文档给的固定五步不同，这里的规划**真的依赖输入**：
任务描述里提到什么、工作流里有什么、已有多少知识，都会改变步骤。

为什么不能让 plan() 返回常量表：
    固定五步对任何工作流都一样，等于没规划。实际差异很大 ——
    对一个节点全部有卡的工作流，不需要「找缺口」；
    对一个带 IPAdapter 但库里没卡的工作流，必须先补知识再谈理解。
"""

from typing import List, Dict, Any


# 基础步骤：任何 workflow 都要走
BASE_STEPS = [
    "analyze_workflow",
    "identify_core_nodes",
    "retrieve_node_knowledge",
    "analyze_parameters",
    "detect_knowledge_gaps",
    "generate_learning_report",
    "reflect_and_summarize",
]

# 任务描述里的意图 → 追加的专项步骤
INTENT_STEPS = {
    "controlnet": "study_controlnet_influence",
    "权重": "study_controlnet_influence",
    "lora": "study_lora_influence",
    "风格": "study_lora_influence",
    "角色": "study_lora_influence",
    "参数": "compare_parameter_values",
    "调参": "compare_parameter_values",
    "为什么": "trace_problem_root_cause",
    "报错": "trace_problem_root_cause",
    "质量": "evaluate_generation_quality",
    "为什么好": "evaluate_generation_quality",
    "复现": "extract_reproducible_parameters",
    "迁移": "check_portability",
}


class TaskPlanner:
    """
    学习任务规划器
    """

    def __init__(self, base_steps: List[str] = None) -> None:
        """
        初始化规划器

        Args:
            base_steps: 自定义基础步骤（默认用 BASE_STEPS）
        """
        self.base_steps = list(base_steps) if base_steps else list(BASE_STEPS)

    def plan(
        self,
        task: str,
        workflow: Any = None,
        node_types: List[str] = None,
        knowledge_available: bool = True
    ) -> List[str]:
        """
        制定学习计划

        Args:
            task: 任务描述，如「学习这个 SDXL 人像 Workflow」
            workflow: workflow dict 或路径（可选，用于更细的规划）
            node_types: 已知的节点清单（可选）
            knowledge_available: 知识库是否可用

        Returns:
            有序步骤名列表
        """
        steps = list(self.base_steps)

        # 1. 任务描述里的意图
        steps.extend(self._intent_steps(task))

        # 2. workflow 特征触发
        nodes = node_types or self._nodes_of(workflow)
        steps.extend(self._feature_steps(nodes))

        # 3. 知识库不可用时，先建索引再谈理解
        if not knowledge_available:
            steps.insert(0, "build_knowledge_index")

        # 4. 节点全部有卡时，「找缺口」这一步没意义，但仍保留
        #    —— 缺口检测顺带产出会被哪些节点用到的信息，
        #    去掉会丢掉「这个工作流完全在已知范围内」这一结论

        return list(dict.fromkeys(steps))

    def explain(self, steps: List[str]) -> List[str]:
        """
        把步骤名翻成人话（报告里用）

        Args:
            steps: 步骤名列表

        Returns:
            中文说明列表
        """
        descriptions = {
            "build_knowledge_index": "建立知识索引（知识库为空或未建索引）",
            "analyze_workflow": "解析工作流结构与节点连接",
            "identify_core_nodes": "识别核心节点与生成流程阶段",
            "retrieve_node_knowledge": "检索每个节点的知识卡",
            "analyze_parameters": "提取并解释关键参数取值",
            "compare_parameter_values": "对比参数取值与经验区间的差距",
            "detect_knowledge_gaps": "检测知识缺口（哪些节点不懂）",
            "generate_learning_report": "生成学习报告",
            "reflect_and_summarize": "自评理解程度并总结",
            "study_controlnet_influence": "专项分析 ControlNet 的作用与参数影响",
            "study_lora_influence": "专项分析 LoRA 的作用与强度影响",
            "trace_problem_root_cause": "追溯现象的可能根因",
            "evaluate_generation_quality": "评估生成质量的关键因素",
            "extract_reproducible_parameters": "提取可复现的参数基线",
            "check_portability": "检查迁移到其他工作流的可行性",
        }

        return [descriptions.get(s, s) for s in steps]

    # ---------- 内部 ----------

    def _intent_steps(self, task: str) -> List[str]:
        """
        从任务描述里识别意图
        """
        if not task:
            return []

        lowered = task.lower()
        steps = []

        for keyword, step in INTENT_STEPS.items():
            if keyword.lower() in lowered:
                steps.append(step)

        return steps

    def _feature_steps(self, nodes: List[str]) -> List[str]:
        """
        由节点构成触发的专项步骤
        """
        if not nodes:
            return []

        steps = []
        lowered = " ".join(nodes).lower()

        # 工作流结构本身就是证据：含 ControlNet 就该深挖控制链路，
        # 哪怕任务描述里没提「ControlNet」
        if "controlnet" in lowered:
            steps.append("study_controlnet_influence")
        if "lora" in lowered:
            steps.append("study_lora_influence")

        # img2img / inpaint 类工作流需要看 denoise 语义
        if "img2img" in lowered or "inpaint" in lowered:
            steps.append("explain_denoise_semantics")

        # 放大流程需要评估后处理链路
        if "upscale" in lowered:
            steps.append("evaluate_upscale_chain")

        # 有 LoRA 但没 ControlNet → 可能只是想调风格，不必深挖控制链路
        if "lora" in lowered and "controlnet" not in lowered:
            steps.append("check_lora_only_workflow")

        return steps

    @staticmethod
    def _nodes_of(workflow: Any) -> List[str]:
        """
        从 workflow 取节点清单
        """
        if workflow is None:
            return []

        if isinstance(workflow, dict):
            return [
                n.get("type", "") for n in workflow.get("nodes", [])
                if n.get("type")
            ]

        nodes = getattr(workflow, "nodes", None)
        if nodes is None:
            return []

        result = []
        for node in nodes:
            node_type = getattr(node, "node_type", None)
            if node_type is None and isinstance(node, dict):
                node_type = node.get("node_type", "")
            if node_type:
                result.append(node_type)

        return result
