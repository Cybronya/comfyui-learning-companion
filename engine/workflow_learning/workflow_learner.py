"""
Workflow 学习器

读一个 workflow 文件 → 分析 → 检索知识 → 体检 → 产出 LearningRecord。

设计文档的 learn() 有几处会直接失败，这里都改掉了：
    1. analyzer.analyze() 收的是 dict，design 传的是 f.read() 的字符串
    2. workflow_file.split("/")[-1] 在 Windows 上拿不到文件名（路径用 \）
    3. important_nodes 填成「有知识卡的节点」—— 语义反了，
       真正值得关注的是**没有卡**的节点
    4. 只用 utf-8 读 JSON，遇到 ComfyUI 导出的 BOM 会解析失败
       （项目约定一律 utf-8-sig）
"""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .learning_record import (
    LearningRecord,
    STATUS_COMPLETED,
    STATUS_FAILED,
)
from .workflow_scanner import load_png_workflow
from .ignore_nodes import is_ignored
from .paths import relative_to_project


class WorkflowLearner:
    """
    单文件 workflow 学习器
    """

    def __init__(
        self,
        analyzer=None,
        retriever=None,
        parser=None,
        diagnostics=None,
        explorer=None,
        gap_detector=None,
        knowledge=None,
        auto_modules: bool = True
    ) -> None:
        """
        初始化学习器

        Args:
            analyzer: WorkflowAnalyzer
            retriever: KnowledgeRetriever
            parser: WorkflowParser（诊断需要 WorkflowKnowledge 对象）
            diagnostics: DiagnosticEngine
            explorer: autonomous_learning.WorkflowExplorer（复用流程链推导）
            gap_detector: autonomous_learning.KnowledgeGapDetector
            knowledge: 已知知识；None 时从 retriever 索引取
            auto_modules: 未传入的模块自动装配真实实现。
                          **默认开**：全 None 的 learner 是个空壳，
                          学出的记录没有类型 / 参数 / 知识覆盖 / 体检，
                          而调用方很难察觉这种静默降级 ——
                          2026-10-06 实跑发现 create_batch_learner()
                          默认产出的就是这种空壳，真实库里的 3 条
                          学习记录全是降级版。只想测最小依赖时显式传 False
        """
        self.analyzer = analyzer
        self.retriever = retriever
        self.parser = parser
        self.diagnostics = diagnostics
        self.explorer = explorer
        self.gap_detector = gap_detector
        self.knowledge = knowledge

        if auto_modules and (
            self.analyzer is None or self.retriever is None
            or self.parser is None or self.diagnostics is None
            or self.explorer is None or self.gap_detector is None
        ):
            self._fill_default_modules()

        # 最近一次分析得到的图对象，供 _fill_diagnostics 用。
        # 不放进 LearningRecord —— graph 不可序列化
        self._graph = None

    def _fill_default_modules(self) -> None:
        """
        补齐未传入的模块（与 test_workflow_learning.build_learner 同一接线）
        """
        from ..workflow_parser import WorkflowParser, NodeKnowledgeLoader
        from ..workflow_analyzer import WorkflowAnalyzer
        from ..diagnostics import DiagnosticEngine
        from ..retrieval import KnowledgeRetriever
        from ..autonomous_learning import (
            WorkflowExplorer,
            KnowledgeGapDetector,
        )
        from .paths import PROJECT_ROOT

        knowledge_dir = PROJECT_ROOT / "comfyui_library" / "knowledge"

        loader = None
        if self.parser is None or self.explorer is None:
            loader = NodeKnowledgeLoader(str(knowledge_dir))

        if self.analyzer is None:
            self.analyzer = WorkflowAnalyzer()

        if self.retriever is None:
            self.retriever = KnowledgeRetriever()
            self.retriever.build_index()

        if self.parser is None:
            self.parser = WorkflowParser(loader)

        if self.diagnostics is None:
            self.diagnostics = DiagnosticEngine()

        if self.explorer is None:
            self.explorer = WorkflowExplorer(
                analyzer=WorkflowAnalyzer(),
                knowledge_loader=loader,
            )

        if self.gap_detector is None:
            self.gap_detector = KnowledgeGapDetector()

    # ---------- 对外 ----------

    def learn(
        self,
        workflow_file: str,
        key: str = ""
    ) -> LearningRecord:
        """
        学习一个 workflow 文件

        Args:
            workflow_file: 文件路径（.json 或 .png）
            key: 相对路径标识；不传则用文件名

        Returns:
            LearningRecord（失败时 status=failed 且带 error，不抛异常）
        """
        path = Path(workflow_file)
        name = path.stem

        record = LearningRecord(
            workflow_name=name,
            # 存相对仓库根的路径：绝对路径换机器后全部失效
            file_path=relative_to_project(path),
            key=key or name,
            source_kind="png" if path.suffix.lower() == ".png" else "json",
            # ComfyUI 官方模板库目录下的样本标记为官方指导
            official="comfyui-workflow-templates-json"
            in path.as_posix(),
        )

        try:
            if not path.exists():
                record.status = STATUS_FAILED
                record.error = "文件不存在"
                return record

            record.content_hash = self._hash_file(path)
            workflow_json = self._load_workflow(path)

            if not workflow_json:
                record.status = STATUS_FAILED
                record.error = (
                    "无法提取工作流内容"
                    "（JSON 格式不符，或 PNG 未内嵌 workflow 元数据）"
                )
                return record

            self._fill_analysis(record, workflow_json)
            self._fill_knowledge(record)
            self._fill_diagnostics(record, workflow_json)

            record.status = STATUS_COMPLETED
            record.learned_at = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        except Exception as e:
            record.status = STATUS_FAILED
            record.error = f"{type(e).__name__}: {e}"

        return record

    # ---------- 各步骤 ----------

    def _fill_analysis(
        self,
        record: LearningRecord,
        workflow_json: Dict
    ) -> None:
        """
        结构分析：类型、节点、模式、流程链
        """
        if self.analyzer is not None:
            # include_graph=True：diagnostics.analyze() 的第二个参数要 graph，
            # 不显式要求就只能拿 None，图结构检查会静默失效
            analysis = self.analyzer.analyze(
                workflow_json, include_graph=True
            ) or {}

            record.nodes = list(analysis.get("nodes", []))
            record.patterns = list(analysis.get("patterns", []))
            record.workflow_type = analysis.get("workflow_type", "") or ""
            self._graph = analysis.get("graph")
        else:
            record.nodes = [
                n.get("type", "")
                for n in workflow_json.get("nodes", [])
                if n.get("type")
            ]

        # 流程链与核心节点复用 autonomous_learning 的推导，
        # 避免在两个模块里各写一份阶段映射表
        if self.explorer is not None:
            explored = self.explorer.explore(workflow_json)
            record.pipeline = list(explored.get("pipeline", []))
            record.important_nodes = list(explored.get("core_nodes", []))
            record.parameters = self.explorer.extract_parameters(
                workflow_json
            )

    def _fill_knowledge(self, record: LearningRecord) -> None:
        """
        知识检索与缺口检测
        """
        if self.retriever is None:
            return

        context = {"workflow_nodes": record.nodes}

        # 用节点清单当检索词；问题串里带节点名才能召回对应知识卡
        try:
            knowledge = self.retriever.retrieve(
                " ".join(record.nodes), context, limit=0
            )
        except Exception:
            knowledge = []

        record.knowledge_refs = [
            item.get("name", "")
            for item in knowledge
            if item.get("name")
        ]

        # 已覆盖：有知识条目明确关联到这个节点
        covered = set()
        for item in knowledge:
            node = item.get("node")
            if node:
                covered.add(node)
            for n in item.get("nodes", []) or []:
                covered.add(n)

        record.covered_nodes = [
            n for n in record.nodes if n in covered
        ]

        # 缺口：复用自主学习的检测器（有别名判定，不会把
        # ControlNetApply 误判成完全没 ControlNet 知识）
        known = self.knowledge
        if known is None and hasattr(self.retriever, "base"):
            known = self.retriever.base

        if self.gap_detector is not None:
            gaps = self.gap_detector.detect(
                record.nodes,
                known,
                core_nodes=record.important_nodes,
            )
            # 布线/注释/预览节点不建卡，也不算知识缺口
            gaps = [g for g in gaps if not is_ignored(g.node_type)]
            record.missing_nodes = [g.node_type for g in gaps]

            # 缺口本身就是最有价值的发现
            for gap in gaps:
                record.discoveries.append(
                    f"{'核心节点' if gap.is_core else '次要节点'} "
                    f"`{gap.node_type}` {gap.reason}"
                )

        if not record.covered_nodes and record.nodes:
            record.discoveries.append(
                "该工作流的所有节点都没有对应知识卡，"
                "当前无法解释其行为"
            )

    def _fill_diagnostics(
        self,
        record: LearningRecord,
        workflow_json: Dict
    ) -> None:
        """
        参数体检
        """
        if self.diagnostics is None:
            return

        workflow_knowledge = None

        if self.parser is not None:
            try:
                workflow_knowledge = self.parser.parse_data(workflow_json)
            except Exception:
                workflow_knowledge = None

        if workflow_knowledge is None:
            # 没有 parser 时诊断跑不了（它要 WorkflowKnowledge 对象），
            # 明确记下来而不是静默跳过
            record.discoveries.append(
                "未注入 parser，参数体检未执行"
            )
            return

        try:
            report = self.diagnostics.analyze(
                workflow_knowledge, getattr(self, "_graph", None)
            )
        except Exception as e:
            record.discoveries.append(f"参数体检失败: {e}")
            return

        for issue in getattr(report, "issues", []) or []:
            severity = getattr(issue, "severity", "")
            message = getattr(issue, "message", "")
            suggestion = getattr(issue, "suggestion", "")
            line = f"[{severity}] {message}"
            if suggestion:
                line += f" → {suggestion}"
            record.diagnostic_issues.append(line)
            record.discoveries.append(line)

    # ---------- 工具 ----------

    def _load_workflow(self, path: Path) -> Dict:
        """
        读出 workflow dict

        .json 直接读；.png 走元数据提取。
        统一用 utf-8-sig —— ComfyUI 导出的 JSON 常带 BOM。
        """
        if path.suffix.lower() == ".png":
            return load_png_workflow(str(path)) or {}

        with open(path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise ValueError("JSON 顶层不是对象")

        return data

    @staticmethod
    def _hash_file(path: Path) -> str:
        """
        文件内容指纹（sha256 前 16 位，够用且短）
        """
        digest = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                digest.update(chunk)
        return digest.hexdigest()[:16]
