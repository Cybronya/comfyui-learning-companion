"""
自主学习控制器

给 Agent 一个任务，它自己去读懂一个未知 workflow。

完整链路（设计文档的 learn() 少了「检索知识」与「沉淀知识」两步，这里补上）：

    任务 + workflow
        ↓
    ① 制定计划        TaskPlanner.plan()      —— 真的依赖任务与节点特征
        ↓
    ② 探索结构        WorkflowExplorer        —— 结构 / 核心节点 / 流程链 / 参数
        ↓
    ③ 检索知识        KnowledgeRetriever      —— 每个节点查一次（原文缺此步）
        ↓
    ④ 检测缺口        KnowledgeGapDetector    —— 别名判定，避免误报
        ↓
    ⑤ 自我反思        Reflection              —— 量化理解程度 + 给出动作
        ↓
    ⑥ 生成报告        LearningReport
        ↓
    ⑦ 沉淀知识        KnowledgeEvolution.evolve（可选，原文缺此步）

不调 LLM。所有结论来自 analyzer / retriever / diagnostics 的确定性输出。
"""

import json
import time
from pathlib import Path
from typing import Any, Dict, List

from .learning_state import LearningState, GapItem
from .task_planner import TaskPlanner
from .workflow_explorer import WorkflowExplorer
from .knowledge_gap_detector import KnowledgeGapDetector
from .learning_report import LearningReport
from .reflection import Reflection
from .analysis_steps import SpecialAnalyzer


# 计划里的基础步骤 → 实际执行名（报告要显示「计划 vs 实际」的对照）
BASE_STEP_EXECUTIONS = {
    "analyze_workflow": "explore",
    "identify_core_nodes": "explore",
    "retrieve_node_knowledge": "retrieve",
    "analyze_parameters": "explore",
    "detect_knowledge_gaps": "detect_gaps",
    "generate_learning_report": "report",
    "reflect_and_summarize": "reflect",
    "build_knowledge_index": "retrieve",
}


class AutonomousLearner:
    """
    自主学习 Agent
    """

    def __init__(
        self,
        planner=None,
        explorer=None,
        gap_detector=None,
        report_generator=None,
        reflection=None,
        retriever=None,
        parser=None,
        diagnostics=None,
        learner=None,
        knowledge=None,
        special_analyzer=None
    ) -> None:
        """
        初始化学习器

        Args:
            planner: TaskPlanner
            explorer: WorkflowExplorer
            gap_detector: KnowledgeGapDetector
            report_generator: LearningReport
            reflection: Reflection
            retriever: KnowledgeRetriever（步骤③需要）
            parser: WorkflowParser（拿不到 dict 时的兜底）
            diagnostics: DiagnosticEngine（顺带把参数体检结果写进报告）
            learner: knowledge_evolution.evolve 函数（步骤⑦沉淀知识）
            knowledge: 已知知识；None 时从 retriever 的索引取
            special_analyzer: SpecialAnalyzer（执行计划里的专项步骤）
        """
        self.planner = planner or TaskPlanner()
        self.explorer = explorer or WorkflowExplorer()
        self.gap_detector = gap_detector or KnowledgeGapDetector()
        self.report_generator = report_generator or LearningReport()
        self.reflection = reflection or Reflection()
        self.retriever = retriever
        self.parser = parser
        self.diagnostics = diagnostics
        self.learner = learner
        self.knowledge = knowledge
        self.special_analyzer = special_analyzer or SpecialAnalyzer()

    # ---------- 主入口 ----------

    def learn(
        self,
        task: str = "",
        workflow: Any = None,
        knowledge: Any = None,
        workflow_path: str = "",
        deposit: bool = False
    ) -> LearningState:
        """
        执行一次自主学习

        Args:
            task: 任务描述
            workflow: workflow dict 或文件路径
            knowledge: 已知知识（默认用 retriever 索引）
            workflow_path: 来源路径，仅记录到报告
            deposit: 是否把本次发现沉淀进知识库
                     （调用 learner / evolve）

        Returns:
            LearningState，state.report 是完整学习报告
        """
        started = time.perf_counter()

        # workflow_path 只接受真正的路径标记。调用方常把 dict 直接当第二个
        # 位置参数传进来，若照单全收会把整个 workflow dict 当路径打印进报告。
        if isinstance(workflow, (str, Path)) and not workflow_path:
            workflow_path = str(workflow)
        elif workflow_path and not isinstance(workflow_path, str):
            workflow_path = ""

        state = LearningState(task=task, workflow_path=workflow_path)

        known = knowledge if knowledge is not None else self._knowledge()

        try:
            # 输入归一化放在 try 内：非法输入应该产出「带错误的状态 + 报告」，
            # 而不是把异常抛给调用方 —— learn() 的契约是必定返回 LearningState
            workflow_data = self._load_workflow(workflow)
            state.workflow = workflow_data

            # ① 制定计划（先粗探一次拿节点清单，规划才能依赖实际内容）
            node_types = self._node_types_of(workflow_data)
            state.plan = self.planner.plan(
                task,
                workflow=workflow_data,
                node_types=node_types,
                knowledge_available=bool(known),
            )
            state.add_step("plan")

            # ② 探索结构
            state.analysis = self.explorer.explore(workflow_data)
            state.pipeline = state.analysis.get("pipeline", [])
            state.core_nodes = state.analysis.get("core_nodes", [])
            state.parameters = self.explorer.extract_parameters(
                workflow_data
            )
            state.add_step("explore")

            # ③ 检索知识（原文缺此步，但整条链路的意义就在这）
            state.knowledge_used = self._retrieve(
                task, node_types, workflow_data
            )
            state.add_step("retrieve")

            # 顺带体检：把参数诊断结果也算作「学习到的东西」。
            # 存在独立字段而非塞进 parameters —— 否则报告的「关键参数」
            # 里会混进 "_diagnostics: [...]" 这种非参数项
            if self.diagnostics is not None:
                state.diagnostic_findings = self._diagnose(workflow_data)

            # ④ 检测缺口
            explored_nodes = state.nodes() or node_types
            state.missing_knowledge = self.gap_detector.detect(
                explored_nodes,
                known,
                core_nodes=state.core_nodes,
            )
            state.add_step("detect_gaps")

            # ⑤ 专项分析：执行计划里的专项步骤。
            # 必须在反思与报告之前 —— 否则专项结论进不了任何输出，
            # 报告里就会出现「计划做但实际没做」的假条目
            state.step_findings = self._run_special_steps(state)

            # ⑥ 自我反思
            state.discoveries = self.reflection.reflect(state)
            state.add_step("reflect")

            # ⑦ 生成报告
            state.report = self.report_generator.generate(state)
            state.add_step("report")

            # ⑧ 沉淀知识（可选）
            if deposit:
                state.deposited = self._deposit(state, workflow_data)
                if state.deposited:
                    state.add_step("deposit")

        except Exception as e:
            state.add_error("learn", e)
            # 失败也要出报告，否则调用方什么都看不到
            try:
                state.report = self.report_generator.generate(state)
            except Exception:
                pass

        state.elapsed_ms = (time.perf_counter() - started) * 1000
        return state

    def learn_text(
        self,
        task: str,
        workflow_path: str,
        knowledge: Any = None
    ) -> str:
        """
        学习并直接返回报告文本

        Args:
            task: 任务描述
            workflow_path: workflow json 路径
            knowledge: 已知知识

        Returns:
            Markdown 学习报告
        """
        state = self.learn(
            task=task,
            workflow=workflow_path,
            knowledge=knowledge,
            workflow_path=workflow_path,
        )
        return state.report

    def action_items(self, state: LearningState) -> List[str]:
        """
        取可执行动作（补知识卡清单）

        Args:
            state: 学习状态

        Returns:
            动作列表
        """
        return self.reflection.action_items(state)

    # ---------- 各步骤 ----------

    def _run_special_steps(self, state: LearningState) -> Dict:
        """
        执行计划里的专项步骤

        Args:
            state: 学习状态

        Returns:
            {步骤名: 结论}，无结论的步骤不出现在结果里
        """
        base = set(BASE_STEP_EXECUTIONS)
        findings = {}

        for step in state.plan:
            if step in base:
                continue

            conclusion = self.special_analyzer.run(step, state)
            if conclusion:
                findings[step] = conclusion

        return findings

    def pending_steps(self, state: LearningState) -> List[str]:
        """
        计划里尚未真正执行的步骤

        用于自查规划与执行的一致性 —— 报告与状态里都体现为「计划但未执行」，
        而不是假装都做了。

        Args:
            state: 学习状态

        Returns:
            未执行的计划步骤
        """
        pending = []

        for step in state.plan:
            execution = BASE_STEP_EXECUTIONS.get(step, step)
            if execution not in state.steps_run:
                pending.append(step)

        return pending

    def _load_workflow(self, workflow: Any) -> Dict:
        """
        归一化 workflow 输入为 dict

        与 ComfyUIAgent 同样的问题：analyzer 收 dict、parser 收路径。
        这里统一：路径自己读；parser 已注入但 analyzer 收 dict 时仍需 dict。

        Args:
            workflow: dict 或路径

        Returns:
            workflow dict
        """
        if workflow is None:
            return {}

        if isinstance(workflow, dict):
            return workflow

        path = Path(str(workflow))
        if path.exists():
            with open(path, "r", encoding="utf-8-sig") as f:
                return json.load(f)

        # 路径不存在但传了内容，尝试当 JSON 字符串解析
        try:
            return json.loads(str(workflow))
        except Exception as e:
            raise ValueError(
                f"无法读取 workflow：{workflow}（既不是存在的文件也不是 JSON）"
            ) from e

    def _node_types_of(self, workflow_data: Dict) -> List[str]:
        """
        取节点清单
        """
        if not isinstance(workflow_data, dict):
            return []

        return [
            n.get("type", "")
            for n in workflow_data.get("nodes", [])
            if n.get("type")
        ]

    def _knowledge(self) -> Any:
        """
        取默认知识来源
        """
        if self.knowledge is not None:
            return self.knowledge

        if self.retriever is not None:
            return self.retriever.base

        return None

    def _retrieve(
        self,
        task: str,
        node_types: List[str],
        workflow_data: Dict
    ) -> List[Dict]:
        """
        为每个节点检索知识

        设计文档的 learn() 完全没调检索器，但「检索知识」是这条链路的核心目的。
        这里逐节点查一次，再把任务文本也查一遍（任务里的关键词可能指向
        某个节点或参数，节点清单里未必体现）。

        Args:
            task: 任务描述
            node_types: 节点清单
            workflow_data: workflow dict

        Returns:
            知识条目列表，每项附 covers_nodes 标明它覆盖了哪个节点
        """
        if self.retriever is None:
            return []

        results: List[Dict] = []
        seen = set()

        def add(items, covers):
            for item in items:
                key = (
                    item.get("type", ""),
                    item.get("name", ""),
                    item.get("source", ""),
                )
                if key in seen:
                    # 同一知识被多个节点命中时合并 covers
                    for existing in results:
                        ekey = (
                            existing.get("type", ""),
                            existing.get("name", ""),
                            existing.get("source", ""),
                        )
                        if ekey == key and covers not in \
                                existing["covers_nodes"]:
                            existing["covers_nodes"].append(covers)
                    continue
                seen.add(key)
                entry = dict(item)
                entry["covers_nodes"] = [covers]
                results.append(entry)

        context = {"workflow_nodes": node_types}

        for node in node_types:
            try:
                items = self.retriever.retrieve_for_topics(
                    [node], context=context, question=task
                )
            except Exception:
                continue
            add(items[:2], node)

        # 任务文本本身
        if task:
            try:
                items = self.retriever.retrieve(
                    task, context, limit=3
                )
            except Exception:
                items = []
            for item in items:
                key = (
                    item.get("type", ""),
                    item.get("name", ""),
                    item.get("source", ""),
                )
                if key in seen:
                    continue
                seen.add(key)
                entry = dict(item)
                entry["covers_nodes"] = []
                results.append(entry)

        return results

    def _diagnose(self, workflow_data: Dict) -> List[str]:
        """
        跑一遍诊断，把参数体检结果并入报告
        """
        if self.diagnostics is None or not workflow_data:
            return []

        try:
            workflow_knowledge = None
            if self.parser is not None:
                workflow_knowledge = self.parser.parse_data(workflow_data)

            if workflow_knowledge is None:
                return []

            report = self.diagnostics.analyze(workflow_knowledge, None)
        except Exception:
            return []

        lines = []
        for issue in getattr(report, "issues", []) or []:
            message = getattr(issue, "message", "")
            suggestion = getattr(issue, "suggestion", "")
            severity = getattr(issue, "severity", "")
            line = f"[{severity}] {message}"
            if suggestion:
                line += f" → {suggestion}"
            lines.append(line)

        return lines

    def _deposit(
        self,
        state: LearningState,
        workflow_data: Dict
    ) -> List[Dict]:
        """
        把本次学习结果沉淀进知识库

        沉淀的是「一条经验」：工作流的节点组合 + 参数 + 缺口情况。
        后续 knowledge_evolution 会把它聚合成 Pattern Knowledge。

        Args:
            state: 学习状态
            workflow_data: workflow dict

        Returns:
            实际写入的条目
        """
        if self.learner is None:
            return []

        from ..knowledge_evolution import WorkflowExperience

        nodes = state.nodes()

        experience = WorkflowExperience(
            workflow_type=state.analysis.get("workflow_type", "") or "",
            nodes=nodes,
            parameters=state.parameters,
            observation=(
                f"学习任务：{state.task}；"
                f"理解程度 {state.level}；"
                f"覆盖 {state.coverage:.0%}"
            ),
            tags=["autonomous_learning", state.level],
        )

        try:
            self.learner([experience], save=True)
        except Exception as e:
            state.add_error("deposit", e)
            return []

        return [{
            "kind": "学习经验",
            "name": state.task or "未命名任务",
            "nodes": nodes,
            "coverage": state.coverage,
        }]
