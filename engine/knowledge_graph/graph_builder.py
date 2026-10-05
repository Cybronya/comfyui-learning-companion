"""
图构建器

把已有的学习结果拼成图。数据源是三个真实存储，不是设计稿里写的
`workflow_experience.json` / `workflow_patterns.json` —— 那两个文件
在把学习状态从 JSON 换成 Markdown 时就没了：

    LearningStore      workflows/learning/<family>/<name>.md
                       → workflow 顶点、contains / member_of 边
    KnowledgeStore     knowledge/patterns/_consolidated/*.md
                       → pattern 顶点、matches / common_nodes 边
    node_index.json    哪些节点写过卡、卡的分类与难度
                       → node / card / concept 顶点

## 边的语义

    workflow -[contains]->  node        结构上包含（带出现次数）
    workflow -[requires]->  node        生成流程必需的核心节点
    workflow -[member_of]-> family      属于哪个族（sd1.5 / sdxl / …）
    workflow -[matches]->   pattern     命中哪个归纳模式
    workflow -[has_problem]-> problem 体检出的问题
    problem  -[suggests]->  solution   对应建议
    problem  -[problem_in]-> node      问题出在哪个节点上
    node     -[has_card]->  card       节点有知识卡
    card     -[covers]->    node       知识卡覆盖节点（反向边）
    node     -[co_used]->   node       两个节点常一起出现（弱关系）
    node     -[has_topic]-> concept    主题词

设计稿只建 `contains` 一种边，第 11 节那张图却画了 `uses`
和 ControlNet 的子类层次 —— 只有一种边的话，
「哪些流程用了 ControlNet」就退化成反向 contains 查表，
图结构本身没有表达任何超出「A 有 B」的信息。
"""

import hashlib
from typing import Any, Dict, List, Optional, Iterable, Set

from .graph import KnowledgeGraph
from .models import (
    GraphNode,
    GraphEdge,
    TYPE_WORKFLOW,
    TYPE_NODE,
    TYPE_PATTERN,
    TYPE_CARD,
    TYPE_PROBLEM,
    TYPE_SOLUTION,
    TYPE_FAMILY,
    TYPE_CONCEPT,
    REL_CONTAINS,
    REL_MEMBER_OF,
    REL_MATCHES,
    REL_REQUIRES,
    REL_USES,
    REL_HAS_CARD,
    REL_COVERS,
    REL_HAS_PROBLEM,
    REL_PROBLEM_IN,
    REL_SUGGESTS,
    REL_CO_USED,
    REL_HAS_TOPIC,
    nid,
)

# 共现关系的出现次数门槛。低于此值不建边 ——
# 只在一个 workflow 里共现的两个节点大概率是巧合，
# 边上 thousands 条噪声边会把有意义的信号淹掉。
DEFAULT_CO_USE_MIN = 3

# 节点数超过此值的 workflow 不参与共现统计。
# N 个节点产生 N*(N-1)/2 对，60 个节点就是 1770 对，
# 一个超大 workflow 能把共现图刷成噪声。
DEFAULT_MAX_CO_USE_NODES = 40


def problem_id(message: str) -> str:
    """
    问题顶点的稳定 id

    用消息内容的哈希而不是消息本身：
    消息可能含中文、括号、换行，直接当 id 既难读也可能超长。
    同一条问题在多个 workflow 里出现时哈希一致 → 自动合并成一个顶点，
    这正是我们要的（「CFG 过高」在 8 个 workflow 里是**一个**问题）。
    """
    digest = hashlib.sha1(
        (message or "").strip().encode("utf-8")
    ).hexdigest()[:10]
    return nid(TYPE_PROBLEM, digest)


def parse_issue(line: str) -> Optional[Dict[str, str]]:
    """
    解析一条诊断记录

    LearningRecord.diagnostic_issues 存的是拼好的字符串：
        `[warning] CFG值较高（当前 9.0），可能导致Prompt约束过强 → 建议尝试CFG 7-10`

    Args:
        line: 原始行

    Returns:
        {"severity": str, "message": str, "suggestion": str}；
        格式不符返回 None
    """
    if not line:
        return None

    text = line.strip()
    severity = ""

    if text.startswith("["):
        end = text.find("]")
        if end > 0:
            severity = text[1:end].strip()
            text = text[end + 1:].strip()

    suggestion = ""
    # 用 → 切建议。中英文箭头都认。
    for arrow in ("→", "->"):
        if arrow in text:
            text, _, suggestion = text.partition(arrow)
            text = text.strip()
            suggestion = suggestion.strip()
            break

    if not text:
        return None

    return {
        "severity": severity,
        "message": text,
        "suggestion": suggestion,
    }


class GraphBuilder:
    """
    把学习记录 / 归纳模式 / 知识卡索引拼成图
    """

    def __init__(
        self,
        graph: KnowledgeGraph = None,
        node_index: Dict = None,
        co_use_min: int = DEFAULT_CO_USE_MIN,
        max_co_use_nodes: int = DEFAULT_MAX_CO_USE_NODES,
        include_gaps: bool = True
    ) -> None:
        """
        初始化构建器

        Args:
            graph: 已有图（传入则在上面增量添加）；None 时新建
            node_index: node_index.json 的内容；None 时自动读
            co_use_min: 共现关系的最少共现 workflow 数
            max_co_use_nodes: 超过此节点数的 workflow 不做共现统计
            include_gaps: 是否把「缺知识卡」建成问题顶点
        """
        self.graph = graph if graph is not None else KnowledgeGraph()
        self.co_use_min = co_use_min
        self.max_co_use_nodes = max_co_use_nodes
        self.include_gaps = include_gaps

        self._node_index = (
            node_index if node_index is not None
            else load_node_index()
        )

        # 共现计数：两阶段建边（先累计再过滤）
        self._co_use_counts: Dict[tuple, int] = {}
        # pattern 归属：workflow key -> [pattern name]
        self._pattern_members: Dict[str, List[str]] = {}
        # 匹配不上的模式成员：模式卡引用了没学过的 workflow。
        # 不静默丢掉 —— 这个缺口正是「样本量不足」的信号，
        # 合并成 matches 边反而会指向错误的 workflow。
        self.unmatched_members: List[str] = []

    @property
    def match_rate(self) -> float:
        """
        模式成员的匹配率

        1.0 表示每个模式成员都对应一个真学过的 workflow。
        偏低说明模式卡与学习记录脱节（常见于模式卡是手工写的、
        或样本 workflow 已被删除）。
        """
        total = sum(len(v) for v in self._pattern_members.values())
        if not total:
            return 1.0
        return 1.0 - len(self.unmatched_members) / total

    # ---------- 主入口 ----------

    def build(
        self,
        records: Iterable,
        patterns: Iterable = None,
        node_index: Dict = None
    ) -> KnowledgeGraph:
        """
        构建完整图

        Args:
            records: LearningRecord 列表
            patterns: WorkflowPattern 列表（可不给）
            node_index: 节点卡索引（不传用构造时的）

        Returns:
            KnowledgeGraph
        """
        if node_index is not None:
            self._node_index = node_index

        self._build_node_cards()

        records = list(records or [])
        for record in records:
            self.add_workflow(record)

        for pattern in (patterns or []):
            self.add_pattern(pattern)

        # 模式要在 workflow 之后建：matches 边需要知道成员 key，
        # 而成员关系是从学习记录里来的
        self._link_patterns()

        self._flush_co_occurrence()

        return self.graph

    # ---------- workflow ----------

    def add_workflow(self, record) -> Optional[str]:
        """
        加入一个学过的 workflow

        Args:
            record: LearningRecord

        Returns:
            workflow 顶点 id；状态非 completed 时返回 None
        """
        key = getattr(record, "key", "") or ""
        if not key:
            return None

        status = getattr(record, "status", "completed")
        if status != "completed":
            # 失败 / 过期的记录不该进图 ——
            # 它的 nodes / parameters 是残缺的，
            # 建出来的边会指向不存在的东西
            return None

        wf_id = nid(TYPE_WORKFLOW, key)

        self.graph.ensure_node(
            wf_id,
            TYPE_WORKFLOW,
            name=getattr(record, "workflow_name", "") or key,
            key=key,
            workflow_type=getattr(record, "workflow_type", ""),
            status=status,
            source=getattr(record, "source_kind", ""),
            coverage=round(
                getattr(record, "coverage", 0.0) or 0.0, 3
            ),
            node_count=len(getattr(record, "nodes", []) or []),
            learned_at=getattr(record, "learned_at", ""),
            source_file=getattr(record, "file_path", ""),
            patterns=list(getattr(record, "patterns", []) or []),
        )

        # 族
        family = self._family_of(key)
        if family:
            self.graph.link(
                wf_id, REL_MEMBER_OF, nid(TYPE_FAMILY, family),
                family=family,
            )

        # 节点
        core = set(getattr(record, "important_nodes", []) or [])
        self._add_nodes(
            wf_id, getattr(record, "nodes", []) or [], core
        )

        # 体检问题
        self._add_issues(wf_id, getattr(record, "diagnostic_issues", []) or [])

        # 缺卡节点 → 建成「待补知识卡」问题
        if self.include_gaps:
            self._add_gaps(wf_id, getattr(record, "missing_nodes", []) or [])

        return wf_id

    def _add_nodes(
        self,
        wf_id: str,
        nodes: List[str],
        core: Set[str]
    ) -> None:
        """把 workflow 的节点清单展开成 contains / requires 边"""
        counts: Dict[str, int] = {}
        for name in nodes:
            if name:
                counts[name] = counts.get(name, 0) + 1

        for name, count in counts.items():
            node_id = nid(TYPE_NODE, name)
            self._ensure_node_vertex(name)

            self.graph.link(
                wf_id, REL_CONTAINS, node_id,
                count=count,
                role="core" if name in core else "aux",
            )

            # 核心节点单独连一条 requires：
            # 「这个流程必需哪些节点」和「它包含哪些节点」是两个问题
            if name in core:
                self.graph.link(
                    wf_id, REL_REQUIRES, node_id, count=count
                )

        self._count_co_occurrence(list(counts))

    def _ensure_node_vertex(self, name: str) -> str:
        """建节点顶点，并挂上知识卡索引里的元信息"""
        node_id = nid(TYPE_NODE, name)
        card = (self._node_index or {}).get(name, {}) or {}

        self.graph.ensure_node(
            node_id,
            TYPE_NODE,
            name=name,
            has_card=bool(card),
            category=card.get("category", ""),
            role=card.get("role", ""),
            difficulty=card.get("difficulty", ""),
        )
        return node_id

    # ---------- 问题 / 建议 ----------

    def _add_issues(
        self,
        wf_id: str,
        lines: List[str]
    ) -> None:
        """把诊断记录拆成 has_problem / suggests / problem_in"""
        for line in lines:
            parsed = parse_issue(line)
            if not parsed:
                continue

            prob_id = self._ensure_problem(
                parsed["message"],
                severity=parsed["severity"],
                suggestion=parsed["suggestion"],
            )

            self.graph.link(
                wf_id, REL_HAS_PROBLEM, prob_id,
                severity=parsed["severity"],
            )

            # 消息里点名了某个节点才连 problem_in ——
            # 靠参数名猜（cfg→KSampler）是编造，不做
            self._link_problem_to_nodes(prob_id, parsed["message"])

    def _ensure_problem(
        self,
        message: str,
        severity: str = "",
        suggestion: str = ""
    ) -> str:
        """建问题顶点（同一条消息自动合并），并连上建议顶点"""
        prob_id = problem_id(message)

        self.graph.ensure_node(
            prob_id,
            TYPE_PROBLEM,
            name=message,
            message=message,
            severity=severity,
        )

        if suggestion:
            sol_id = nid(TYPE_SOLUTION, message[:60])
            self.graph.ensure_node(
                sol_id,
                TYPE_SOLUTION,
                name=suggestion,
                suggestion=suggestion,
            )
            self.graph.link(prob_id, REL_SUGGESTS, sol_id)

        return prob_id

    def _link_problem_to_nodes(
        self,
        prob_id: str,
        message: str
    ) -> None:
        """消息里出现了节点名才建立归属边"""
        if not message:
            return

        for name in (self._node_index or {}).keys():
            if name and name in message:
                self.graph.link(
                    prob_id, REL_PROBLEM_IN, nid(TYPE_NODE, name),
                    reason="消息中提及该节点",
                )

    def _add_gaps(self, wf_id: str, missing: List[str]) -> None:
        """
        缺知识卡的节点建成问题

        「ControlNetApply 没有知识卡」本身就是一条待办，
        建成图里的问题顶点后，Agent 才能反查「哪些节点该建卡了」。
        """
        for name in missing:
            if not name:
                continue

            message = f"`{name}` 缺少知识卡，无法解释其行为"
            prob_id = self._ensure_problem(message, severity="info")

            self.graph.link(
                wf_id, REL_HAS_PROBLEM, prob_id, severity="info"
            )
            self.graph.link(
                prob_id, REL_PROBLEM_IN, nid(TYPE_NODE, name),
                reason="无对应知识卡",
            )

    # ---------- 知识卡 ----------

    def _build_node_cards(self) -> None:
        """按 node_index.json 建 node / card / concept 顶点"""
        for node_type, info in (self._node_index or {}).items():
            if not node_type:
                continue

            info = info or {}
            node_id = nid(TYPE_NODE, node_type)

            self.graph.ensure_node(
                node_id,
                TYPE_NODE,
                name=node_type,
                has_card=True,
                category=info.get("category", ""),
                role=info.get("role", ""),
                difficulty=info.get("difficulty", ""),
            )

            card_file = info.get("knowledge_file", "")
            if card_file:
                card_id = nid(TYPE_CARD, card_file)
                self.graph.ensure_node(
                    card_id,
                    TYPE_CARD,
                    name=card_file,
                    file=card_file,
                    category=info.get("category", ""),
                    role=info.get("role", ""),
                    difficulty=info.get("difficulty", ""),
                )
                self.graph.link(node_id, REL_HAS_CARD, card_id)
                self.graph.link(card_id, REL_COVERS, node_id)

            for topic in info.get("learning_topics", []) or []:
                if not topic:
                    continue
                concept_id = nid(TYPE_CONCEPT, topic)
                self.graph.ensure_node(
                    concept_id, TYPE_CONCEPT, name=topic
                )
                self.graph.link(node_id, REL_HAS_TOPIC, concept_id)

    # ---------- 模式 ----------

    def add_pattern(self, pattern) -> str:
        """
        加入一个归纳出的模式

        Args:
            pattern: WorkflowPattern

        Returns:
            pattern 顶点 id
        """
        name = getattr(pattern, "name", "") or ""
        if not name:
            return ""

        pattern_id = nid(TYPE_PATTERN, name)

        self.graph.ensure_node(
            pattern_id,
            TYPE_PATTERN,
            name=name,
            workflow_type=getattr(pattern, "workflow_type", ""),
            frequency=getattr(pattern, "frequency", 0),
            level=getattr(pattern, "level", ""),
            coverage=round(
                getattr(pattern, "coverage", 0.0) or 0.0, 3
            ),
            recommendations=list(
                getattr(pattern, "recommendations", []) or []
            ),
        )

        # 成员关系先记下来，等 workflow 都建完再连边 ——
        # 成员 key 可能对应尚未建出的 workflow 顶点
        members = list(getattr(pattern, "members", []) or [])
        for member in members:
            self._pattern_members.setdefault(member, []).append(name)

        # 共有节点：pattern 也 contains 它们，
        # 这样「哪些模式用到 KSampler」和「哪些 workflow 用到」同一套查法
        for node_name in (
            getattr(pattern, "common_nodes", []) or []
        ):
            self._ensure_node_vertex(node_name)
            self.graph.link(
                pattern_id, REL_CONTAINS, nid(TYPE_NODE, node_name),
                scope="common",
            )

        # 模式层面的常见问题
        for problem in (
            getattr(pattern, "common_problems", []) or []
        ):
            if isinstance(problem, dict):
                message = problem.get("problem", "")
                severity = problem.get("severity", "")
                count = problem.get("count", 0)
            else:
                message = str(problem)
                severity = ""
                count = 0

            if not message:
                continue

            prob_id = self._ensure_problem(
                message, severity=severity
            )
            self.graph.link(
                pattern_id, REL_HAS_PROBLEM, prob_id,
                count=count, frequency=getattr(
                    pattern, "frequency", 0
                ),
            )

        return pattern_id

    def _link_patterns(self) -> None:
        """把 workflow 连到它命中的模式上"""
        for member, pattern_names in self._pattern_members.items():
            wf_id = nid(TYPE_WORKFLOW, member)

            # 成员名可能是裸文件名，而学习记录的 key 是相对路径。
            # 这里按 basename 兜底匹配一次，匹配不上就跳过 ——
            # 宁可少连一条边，也不要连到错误的 workflow 上
            if wf_id not in self.graph.nodes:
                wf_id = self._match_workflow_by_basename(member)

            if not wf_id:
                self.unmatched_members.append(member)
                continue

            for pattern_name in pattern_names:
                self.graph.link(
                    wf_id, REL_MATCHES, nid(TYPE_PATTERN, pattern_name)
                )

    def _match_workflow_by_basename(self, member: str) -> str:
        """按文件名找 workflow 顶点（只在唯一匹配时返回）"""
        base = member.rsplit("/", 1)[-1]
        matches = [
            key for key in self.graph.nodes
            if key.startswith(f"{TYPE_WORKFLOW}:")
            and key.rsplit("/", 1)[-1] == base
        ]

        if len(matches) == 1:
            return matches[0]

        return ""

    # ---------- 共现 ----------

    def _count_co_occurrence(self, nodes: List[str]) -> None:
        """累计节点共现次数（两阶段：这里只累计）"""
        if len(nodes) < 2:
            return

        if len(nodes) > self.max_co_use_nodes:
            # 节点太多的 workflow 产生的配对是噪声，不统计
            return

        unique = sorted(set(nodes))
        for i, left in enumerate(unique):
            for right in unique[i + 1:]:
                self._co_use_counts[(left, right)] = (
                    self._co_use_counts.get((left, right), 0) + 1
                )

    def _flush_co_occurrence(self) -> None:
        """把达标的共现关系建成边"""
        for (left, right), count in self._co_use_counts.items():
            if count < self.co_use_min:
                continue

            self.graph.link(
                nid(TYPE_NODE, left), REL_CO_USED, nid(TYPE_NODE, right),
                strength=count,
            )

    # ---------- 工具 ----------

    @staticmethod
    def _family_of(key: str) -> str:
        """
        从 key 推 workflow 族

        `sd1.5/basic.json` → `sd1.5`
        `basic.json`（无目录）→ 空串，不建 family 顶点
        """
        if "/" not in key:
            return ""
        return key.split("/", 1)[0]


def load_node_index(
    path: str = None
) -> Dict[str, Dict]:
    """
    读 node_index.json

    Args:
        path: 可选路径；默认 comfyui_library/knowledge/node_index.json

    Returns:
        {节点类型: {...}}；读不到返回空字典

    读不到不是错误 —— 知识卡索引是可选数据源，
    没有它图照样能建，只是 has_card 全为 False。
    """
    import json
    from pathlib import Path

    from ..workflow_learning.paths import PROJECT_ROOT

    target = Path(path) if path else (
        PROJECT_ROOT / "comfyui_library" / "knowledge"
        / "node_index.json"
    )

    if not target.exists():
        return {}

    try:
        # utf-8-sig：Windows 下 ComfyUI 导出的 JSON 带 BOM
        with open(target, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except Exception:
        return {}

    nodes = data.get("nodes", {}) if isinstance(data, dict) else {}
    return nodes if isinstance(nodes, dict) else {}