"""
ComfyUI Learning Agent 核心

把九个独立能力模块编成一个 Agent：
    解析 → 分析 → 诊断 → 检索 → 回答

依赖注入方式：各模块由外部构造后传入，agent_core 不关心它们怎么实现。
这样测试可以塞假模块，端到端也可以按需替换某一段（比如换成带真实索引的 retriever）。

模块签名适配（各模块真实 API 与直觉调用有出入，这里统一处理）：
    WorkflowParser.parse()      收文件路径，dict 走 parse_data()
    WorkflowAnalyzer.analyze()  返回值不含 graph，需 include_graph=True
    ContextManager.get_context() 不含 workflow_nodes，排序需 get_retrieval_context()
    ResponseGenerator.generate() 返回 dict 而非 str
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .state import AgentState
from .pipeline import AgentPipeline, build_pipeline
from .config import DEFAULT_CONFIG, merge_config, stages_of


# parser 未识别时填的占位值。这些是真值字符串，赋值时必须当空值过滤，
# 否则会把下游算出的真实分类挡掉。
_UNKNOWN_TOKENS = {"unknown", "none", "null", "n/a", "-"}


class ComfyUIAgent:
    """
    ComfyUI 学习助手总控
    """

    def __init__(
        self,
        parser=None,
        analyzer=None,
        context=None,
        diagnostics=None,
        retriever=None,
        generator=None,
        learner=None,
        config: Dict = None
    ) -> None:
        """
        初始化 Agent

        Args:
            parser: WorkflowParser 实例
            analyzer: WorkflowAnalyzer 实例
            context: ContextManager 实例
            diagnostics: DiagnosticEngine 实例
            retriever: KnowledgeRetriever 实例
            generator: ResponseGenerator 实例
            learner: knowledge_evolution 模块（用于 evolve()，不在 ask 链路上）
            config: 配置覆盖项
        """
        self.parser = parser
        self.analyzer = analyzer
        self.context = context
        self.diagnostics = diagnostics
        self.retriever = retriever
        self.generator = generator
        self.learner = learner

        self.config = merge_config(config)

        # 最近一次解析结果，供不带 workflow 的提问复用
        self._last_workflow = None
        self._last_workflow_data = None

    # ---------- 主入口 ----------

    def ask_text(
        self,
        question: str,
        workflow_path: str = None,
        limit: int = None
    ) -> str:
        """
        提问并直接返回给人看的回答（最常用入口，无需 LLM）

        Args:
            question: 用户问题
            workflow_path: workflow json 路径（可省略，用已登记的）
            limit: 知识条数上限

        Returns:
            Markdown 中文回答
        """
        state = self.ask(question, workflow_path, limit=limit)

        if state.answer:
            return state.answer

        # answer() 不可用时的兜底说明，避免调用方拿到空字符串
        if state.has_errors:
            return (
                "处理过程中出现问题：\n"
                + "\n".join(
                    f"- [{e['stage']}] {e['message']}"
                    for e in state.errors
                )
            )

        return "暂时无法生成回答。"

    def ask(
        self,
        question: str,
        workflow_json=None,
        limit: int = None
    ) -> AgentState:
        """
        提问主入口

        Args:
            question: 用户问题
            workflow_json: ComfyUI workflow JSON（dict）或文件路径；可省略
            limit: 本次最多返回几条知识（覆盖配置）

        Returns:
            AgentState，含各阶段产物与阶段级错误
        """
        state = AgentState(question=question)

        # 本次没传 workflow 就复用 set_workflow()/上次解析登记的工作流。
        # 「先告诉 Agent 当前工作流，之后连续追问」是主要用法，
        # 若不复用，连续追问时解析/分析/诊断三步会全部空转。
        if workflow_json is None and self._last_workflow is not None:
            workflow_json = self._last_workflow_data
            state.reused_workflow = True

        # 先归一化成 dict，各阶段就不必再分路径/dict 两种情况
        try:
            workflow_data = self.load_workflow(workflow_json)
        except Exception as e:
            state.add_error("load_workflow", e)
            workflow_data = None

        pipeline = build_pipeline(
            {
                "context": self._stage_context,
                "parse": lambda s: self._stage_parse(s, workflow_data),
                "analyze": lambda s: self._stage_analyze(s, workflow_data),
                "diagnose": self._stage_diagnose,
                "retrieve": lambda s: self._stage_retrieve(
                    s, limit
                ),
                "respond": self._stage_respond,
            },
            self.config,
        )

        return pipeline.run(state)

    @staticmethod
    def load_workflow(workflow_json) -> Any:
        """
        归一化 workflow 输入为 dict

        各模块的入参类型不统一：WorkflowParser.parse() 收文件路径、
        WorkflowAnalyzer.analyze() 收 dict。传路径给 analyzer 会直接崩
        （'str' object has no attribute 'get'），所以在 Agent 层统一读一次，
        后续所有阶段都拿 dict，避免各阶段各自判断类型。

        Args:
            workflow_json: dict 或文件路径

        Returns:
            workflow dict；输入本身已是 dict 时原样返回
        """
        if workflow_json is None or isinstance(workflow_json, dict):
            return workflow_json

        path = Path(str(workflow_json))
        if not path.exists():
            raise FileNotFoundError(f"workflow 文件不存在: {path}")

        with open(path, "r", encoding="utf-8-sig") as f:
            return json.load(f)

    # ---------- 各阶段 ----------

    def _stage_context(self, state: AgentState) -> AgentState:
        """
        阶段 0：记录本次提问到会话上下文

        先记录问题，检索与回答阶段才能拿到「最近讨论」这条上下文。
        """
        if self.context is None:
            state.skip_stage("context", "未注入 context 模块")
            return state

        if not self.config.get("update_context", True):
            state.skip_stage("context", "配置关闭 update_context")
            return state

        if hasattr(self.context, "update_question"):
            self.context.update_question(
                state.question, state.workflow_type
            )

        return state

    def _stage_parse(
        self,
        state: AgentState,
        workflow_json
    ) -> AgentState:
        """
        阶段 1：Workflow 解析
        """
        if not workflow_json:
            state.skip_stage("parse", "本次未提供 workflow")
            return state

        if self.parser is None:
            state.skip_stage("parse", "未注入 parser 模块")
            return state

        # workflow 在 load_workflow() 里已归一化成 dict
        if isinstance(workflow_json, dict):
            parsed = self.parser.parse_data(workflow_json)
        else:
            # 防御：直接调用本方法而绕过 load_workflow() 的情况
            parsed = self.parser.parse(str(workflow_json))

        state.workflow = parsed

        # parser 不推断 task_type，留的是字符串 "unknown"。
        # 它是真值，直接赋值会把分析阶段算出的真实分类挡掉，
        # 所以把 "unknown"/"None" 当空值处理。
        parsed_type = getattr(parsed, "task_type", "") or ""
        if parsed_type and parsed_type.lower() not in _UNKNOWN_TOKENS:
            state.workflow_type = parsed_type

        # 缓存，供后续不带 workflow 的提问复用（见 ask()）
        self._last_workflow_data = workflow_json
        self._last_workflow = parsed

        # 解析结果写回上下文，后续检索的「节点是否在当前工作流」加权依赖它
        if (
            self.config.get("update_context")
            and self.context is not None
            and hasattr(self.context, "set_workflow")
        ):
            self.context.set_workflow(parsed)

        return state

    def _stage_analyze(
        self,
        state: AgentState,
        workflow_json
    ) -> AgentState:
        """
        阶段 2：Workflow 结构分析
        """
        if not workflow_json:
            state.skip_stage("analyze", "本次未提供 workflow")
            return state

        if self.analyzer is None:
            state.skip_stage("analyze", "未注入 analyzer 模块")
            return state

        # include_graph=True：诊断阶段需要 graph 本身
        analysis = self.analyzer.analyze(
            workflow_json, include_graph=True
        )

        state.workflow_analysis = analysis

        # 分类器算出的类型比 parser 的占位值可靠，优先采用
        classified = analysis.get("workflow_type", "") or ""
        if classified.lower() not in _UNKNOWN_TOKENS:
            state.workflow_type = classified
        elif not state.workflow_type:
            state.workflow_type = classified

        return state

    def _stage_diagnose(self, state: AgentState) -> AgentState:
        """
        阶段 3：诊断
        """
        if state.workflow is None:
            state.skip_stage("diagnose", "无解析结果")
            return state

        if self.diagnostics is None:
            state.skip_stage("diagnose", "未注入 diagnostics 模块")
            return state

        graph = state.workflow_analysis.get("graph")

        report = self.diagnostics.analyze(
            state.workflow, graph
        )

        state.diagnostics = list(
            getattr(report, "issues", []) or []
        )

        return state

    def _stage_retrieve(
        self,
        state: AgentState,
        limit: int = None
    ) -> AgentState:
        """
        阶段 4：知识检索
        """
        if self.retriever is None:
            state.skip_stage("retrieve", "未注入 retriever 模块")
            return state

        # 检索排序需要扁平的 workflow_nodes，用 get_retrieval_context()
        context = self._retrieval_context(state)

        effective_limit = limit
        if effective_limit is None:
            effective_limit = self.config.get("retrieval_limit", 0)

        state.knowledge = self.retriever.retrieve(
            state.question,
            context,
            limit=effective_limit or 0,
        )

        return state

    def _stage_respond(self, state: AgentState) -> AgentState:
        """
        阶段 5：生成回答

        双产出：
            state.answer   规则拼装的中文回答（默认，给人直接看，无需 LLM）
            state.response 给 LLM 的提示词（保留，供接自有模型时用）
        """
        if self.generator is None:
            state.skip_stage("respond", "未注入 generator 模块")
            return state

        # 给人看的回答：全规则拼装
        if hasattr(self.generator, "answer"):
            try:
                state.answer = self.generator.answer(state)
            except Exception as e:
                state.add_error("answer", e)
        else:
            state.skip_stage("answer", "generator 不支持 answer()")

        # 给 LLM 的提示词：保留但不作为主产出
        knowledge_text = self._build_knowledge_text(state)
        answer_context = self._build_answer_context(state)

        try:
            result = self.generator.generate(
                state.question,
                answer_context,
                knowledge=knowledge_text,
            )

            state.response = result if isinstance(result, dict) else {
                "prompt": str(result)
            }
        except Exception as e:
            state.add_error("prompt", e)

        return state

    # ---------- 上下文拼装 ----------

    def _retrieval_context(self, state: AgentState) -> Dict:
        """
        构造检索用上下文

        优先用 ContextManager 的扁平视图（其中 workflow_nodes 来自
        上一阶段写入的解析结果），否则直接从 state.workflow 现算。
        """
        context: Dict = {}

        if self.context is not None:
            if hasattr(self.context, "get_retrieval_context"):
                context = self.context.get_retrieval_context()
            elif hasattr(self.context, "get_context"):
                context = self.context.get_context()

        # 兜底/校正：保证 workflow_nodes 一定反映当前这次解析结果
        nodes = state.workflow_nodes()
        if nodes:
            context["workflow_nodes"] = nodes

        if state.workflow_type:
            context["workflow_type"] = state.workflow_type

        return context

    def _build_answer_context(self, state: AgentState) -> Dict:
        """
        构造回答生成用上下文
        """
        context: Dict = {}

        if self.context is not None:
            if hasattr(self.context, "get_context"):
                context = self.context.get_context()
            elif isinstance(self.context, dict):
                context = dict(self.context)

        # 把本次分析的结论并进去，否则 LLM 只看到历史摘要
        if state.workflow is not None:
            context["workflow"] = {
                "workflow_id": getattr(
                    state.workflow, "workflow_id", ""
                ),
                "task_type": state.workflow_type,
                "nodes": state.workflow_nodes(),
                "features": list(
                    getattr(state.workflow, "features", []) or []
                ),
            }

        if state.workflow_analysis:
            context["analysis"] = {
                k: v for k, v in state.workflow_analysis.items()
                if k != "graph"
            }

        issues = state.diagnostic_issues()
        if issues:
            context["diagnostics"] = issues

        return context

    def _build_knowledge_text(self, state: AgentState) -> str:
        """
        把检索结果拼成生成器能用的文本
        """
        if not state.knowledge:
            return ""

        if self.retriever is not None and hasattr(
            self.retriever, "format_for_prompt"
        ):
            return self.retriever.format_for_prompt(state.knowledge)

        # retriever 未提供格式化能力时自己做最小拼接
        lines = []
        for item in state.knowledge:
            lines.append(
                f"[{item.get('type', 'knowledge')}] {item.get('name', '')}"
            )
            content = item.get("content") or item.get("description")
            if content:
                lines.append(f"    {content}")

        return "\n".join(lines)

    # ---------- 离线能力 ----------

    def evolve(self, experiences=None, save: bool = True):
        """
        知识演化（离线，不在 ask 链路上）

        Args:
            experiences: 经验列表，None 则从 learning_loop 经验库读
            save: 是否写入 evolution_store

        Returns:
            EvolutionKnowledge
        """
        if self.learner is None:
            raise RuntimeError(
                "Agent 未注入 learner（knowledge_evolution 模块）"
            )

        return self.learner(
            experiences,
            store_path=self.config.get("evolution_store"),
            save=save,
        )

    def build_index(self):
        """
        重建检索索引（知识库变动后调用）

        Returns:
            KnowledgeIndex
        """
        if self.retriever is None or not hasattr(
            self.retriever, "build_index"
        ):
            raise RuntimeError(
                "Agent 未注入 retriever，或 retriever 不支持 build_index"
            )

        return self.retriever.build_index(
            index_path=self.config.get("retrieval_index_path"),
            knowledge_dir=self.config.get("knowledge_dir"),
            experience_store=self.config.get("experience_store"),
            evolution_store=self.config.get("evolution_store"),
        )

    def set_workflow(self, workflow_json) -> AgentState:
        """
        只解析并写入上下文，不提问

        用于「先告诉 Agent 当前工作流，之后连续追问」的场景：
        避免每个问题都重复传一遍 workflow。

        Args:
            workflow_json: workflow dict 或文件路径

        Returns:
            AgentState（只含解析与分析结果）
        """
        state = AgentState()
        data = self.load_workflow(workflow_json)
        self._stage_parse(state, data)
        self._stage_analyze(state, data)
        return state

    def remember(self, question: str, topic: str = "") -> None:
        """
        记录一次提问到会话上下文

        Args:
            question: 问题文本
            topic: 讨论主题（可选）
        """
        if (
            self.config.get("update_context")
            and self.context is not None
            and hasattr(self.context, "update_question")
        ):
            self.context.update_question(question, topic)
