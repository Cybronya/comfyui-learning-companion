"""
图查询

Agent 的实际入口。这里所有方法返回**带类型前缀的 id 与可读名字**，
而不是裸字符串 —— 因为 `basic` 既可能是 workflow 也可能是 pattern，
只返回字符串的话调用方无从判断自己拿到的是什么。

设计稿的三个查询都是扫全量边（`for edge in self.graph.edges`）。
图有 2 万条边时每次查询都全扫一遍，这里全部走邻接索引。
"""

from typing import Any, Dict, List, Optional, Set, Tuple

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
    REL_HAS_CARD,
    REL_COVERS,
    REL_HAS_PROBLEM,
    REL_PROBLEM_IN,
    REL_SUGGESTS,
    REL_CO_USED,
    REL_HAS_TOPIC,
    nid,
    split_id,
)


class GraphQuery:
    """
    图查询接口
    """

    def __init__(self, graph: KnowledgeGraph = None) -> None:
        self.graph = graph if graph is not None else KnowledgeGraph()

    # ---------- id 解析 ----------

    def resolve(self, name: str, node_type: str = TYPE_NODE) -> str:
        """
        把一个名字解析成顶点 id

        支持三种写法（Agent 的输入往往是不规范的）：
            `KSampler` / `node:KSampler` / `sd1.5/basic.json`

        匹配顺序：完整 id → 同类型同名（忽略大小写）
                  → 同类型子串（`ControlNet` 命中 `ControlNetApply`）

        子串匹配只在唯一命中时返回 —— 多个候选时返回空串，
        因为「猜一个」比「明确说找不到」危险得多：
        把 ControlNet 的问题算到 LoraLoader 头上，
        用户完全看不出来。

        Args:
            name: 名字或完整 id
            node_type: 期望的类型

        Returns:
            顶点 id；找不到返回空串
        """
        if not name:
            return ""

        # 完整 id 直接用
        if name in self.graph.nodes:
            return name

        # 拼上类型前缀再找
        typed = nid(node_type, name)
        if typed in self.graph.nodes:
            return typed

        prefix = f"{node_type}:"

        # 同名（忽略大小写）
        exact = [
            key for key in self.graph.nodes
            if key.lower() == typed.lower()
        ]
        if len(exact) == 1:
            return exact[0]

        # 子串：沿用 retrieval 的做法（节点名互相包含）
        lowered = name.lower()
        partial = [
            key for key in self.graph.nodes
            if key.startswith(prefix)
            and lowered in key[len(prefix):].lower()
        ]
        if len(partial) == 1:
            return partial[0]

        return ""

    def name_of(self, node_id: str) -> str:
        """id → 可读名字"""
        node = self.graph.get_node(node_id)
        if node is None:
            _, name = split_id(node_id)
            return name
        return node.name or split_id(node_id)[1]

    def _labels(self, node_ids: List[str]) -> List[str]:
        """一组 id → 可读名字列表"""
        return [self.name_of(i) for i in node_ids]

    # ---------- 核心查询 ----------

    def workflows_using(
        self,
        node_name: str,
        relation: str = REL_CONTAINS
    ) -> List[str]:
        """
        哪些 workflow 用了这个节点

        对应设计稿第十节的用法（`workflows_using("ControlNetApply")`），
        但做了两处修正：
            - 走邻接索引，不扫全量边
            - `ControlNet` 这种不完整的名字也能匹配到
              `ControlNetApply`（唯一命中时）

        Args:
            node_name: 节点名或 id
            relation: contains（默认）/ requires / co_used

        Returns:
            workflow 名字列表（不含 id 前缀，便于直接给人看）
        """
        node_id = self.resolve(node_name, TYPE_NODE)
        if not node_id:
            return []

        if relation == REL_CO_USED:
            sources = [
                self.graph.out_edges(node_id, REL_CO_USED)
                + self.graph.in_edges(node_id, REL_CO_USED)
            ]
            pairs = [
                e.other(node_id)
                for group in sources for e in group
            ]
        else:
            # workflow 是 contains 的源端 —— 扫 node 的入边，
            # 而不是全量边里找 target == node 的
            pairs = [
                e.source
                for e in self.graph.in_edges(node_id, relation)
                if e.source.startswith(f"{TYPE_WORKFLOW}:")
            ]

        return self._dedupe(
            self._labels([p for p in pairs])
        )

    def nodes_of(
        self,
        workflow: str,
        relation: str = REL_CONTAINS
    ) -> List[str]:
        """
        这个 workflow 用了哪些节点

        对应设计稿的 `related_nodes`，另外支持筛核心节点（requires）。
        """
        wf_id = self.resolve(workflow, TYPE_WORKFLOW)
        if not wf_id:
            return []

        return self._dedupe(
            self._labels([
                e.target
                for e in self.graph.out_edges(wf_id, relation)
            ])
        )

    def core_nodes(self, workflow: str) -> List[str]:
        """workflow 的核心节点（生成流程必需）"""
        return self.nodes_of(workflow, REL_REQUIRES)

    def patterns_of(self, workflow: str) -> List[str]:
        """workflow 命中了哪些归纳模式"""
        wf_id = self.resolve(workflow, TYPE_WORKFLOW)
        if not wf_id:
            return []

        return self._dedupe(
            self._labels([
                e.target
                for e in self.graph.out_edges(wf_id, REL_MATCHES)
            ])
        )

    def workflows_in_pattern(self, pattern: str) -> List[str]:
        """某个模式包含哪些 workflow"""
        pattern_id = self.resolve(pattern, TYPE_PATTERN)
        if not pattern_id:
            return []

        return self._dedupe(
            self._labels([
                e.source
                for e in self.graph.in_edges(pattern_id, REL_MATCHES)
            ])
        )

    def family_of(self, workflow: str) -> str:
        """workflow 属于哪个族"""
        wf_id = self.resolve(workflow, TYPE_WORKFLOW)
        if not wf_id:
            return ""

        edges = self.graph.out_edges(wf_id, REL_MEMBER_OF)
        return self.name_of(edges[0].target) if edges else ""

    # ---------- 问题 / 建议 ----------

    def problems_of(self, workflow: str) -> List[str]:
        """workflow 有哪些体检问题"""
        wf_id = self.resolve(workflow, TYPE_WORKFLOW)
        if not wf_id:
            return []

        return self._dedupe([
            self.graph.get_node(e.target).name
            if self.graph.get_node(e.target) else e.target
            for e in self.graph.out_edges(wf_id, REL_HAS_PROBLEM)
        ])

    def workflows_with_problem(self, keyword: str) -> List[str]:
        """
        哪些 workflow 有含关键词的问题

        「哪些工作流有 CFG 过高的问题」这类查询走这里，
        比先 resolve 再遍历 workflow 更快 —— 直接在问题顶点里找。
        """
        keyword = (keyword or "").lower()
        if not keyword:
            return []

        hit = [
            node_id for node_id in self.graph.nodes
            if node_id.startswith(f"{TYPE_PROBLEM}:")
            and keyword in (
                self.graph.get_node(node_id).name or ""
            ).lower()
        ]

        if not hit:
            return []

        workflows = []
        for prob_id in hit:
            workflows.extend(
                e.source
                for e in self.graph.in_edges(prob_id, REL_HAS_PROBLEM)
                if e.source.startswith(f"{TYPE_WORKFLOW}:")
            )

        return self._dedupe(self._labels(workflows))

    def solutions_for(self, problem: str) -> List[str]:
        """某个问题的建议"""
        prob_id = self.resolve(problem, TYPE_PROBLEM)
        if not prob_id:
            # 问题 id 是哈希，用户手上通常是消息文本。
            # 解析失败时退回按子串找
            prob_id = self._find_problem_by_text(problem)

        if not prob_id:
            return []

        return self._dedupe([
            (
                self.graph.get_node(e.target).get("suggestion")
                or self.name_of(e.target)
            )
            for e in self.graph.out_edges(prob_id, REL_SUGGESTS)
        ])

    def _find_problem_by_text(self, text: str) -> str:
        """按消息文本找问题顶点（唯一命中才返回）"""
        if not text:
            return ""

        prefix = f"{TYPE_PROBLEM}:"
        exact = [
            key for key in self.graph.nodes
            if key.startswith(prefix)
            and (
                self.graph.get_node(key).name or ""
            ) == text
        ]
        if len(exact) == 1:
            return exact[0]

        partial = [
            key for key in self.graph.nodes
            if key.startswith(prefix)
            and text.lower() in (
                self.graph.get_node(key).name or ""
            ).lower()
        ]
        return partial[0] if len(partial) == 1 else ""

    def nodes_causing(self, workflow: str) -> Dict[str, List[str]]:
        """
        workflow 的问题分别出在哪些节点上

        Returns:
            {节点名: [问题, …]}；无法归属到具体节点的归到「(未归属)」
        """
        wf_id = self.resolve(workflow, TYPE_WORKFLOW)
        if not wf_id:
            return {}

        result: Dict[str, List[str]] = {}

        for edge in self.graph.out_edges(wf_id, REL_HAS_PROBLEM):
            prob_node = self.graph.get_node(edge.target)
            message = (
                prob_node.get("message") if prob_node else edge.target
            )

            targets = [
                self.name_of(e.target)
                for e in self.graph.out_edges(
                    edge.target, REL_PROBLEM_IN
                )
            ]

            if not targets:
                targets = ["(未归属到具体节点)"]

            for target in targets:
                result.setdefault(target, [])
                if message not in result[target]:
                    result[target].append(message)

        return result

    # ---------- 知识卡 ----------

    def card_for(self, node_name: str) -> Optional[str]:
        """节点的知识卡文件路径"""
        node_id = self.resolve(node_name, TYPE_NODE)
        if not node_id:
            return None

        edges = self.graph.out_edges(node_id, REL_HAS_CARD)
        if not edges:
            return None

        return self.name_of(edges[0].target)

    def nodes_without_cards(self) -> List[str]:
        """
        没有知识卡的节点（按被用到的次数排序）

        这是建卡的优先级依据 —— 用得越多越该先补。
        """
        result = []

        for node in self.graph.nodes_of_type(TYPE_NODE):
            if node.get("has_card"):
                continue
            result.append((self._usage_count(node.id), node.name))

        result.sort(reverse=True)
        return [name for _, name in result]

    def _usage_count(self, node_id: str) -> int:
        """节点被多少个 workflow 用到"""
        return len({
            e.source
            for e in self.graph.in_edges(node_id, REL_CONTAINS)
            if e.source.startswith(f"{TYPE_WORKFLOW}:")
        })

    def topics_of(self, name: str, node_type: str = TYPE_NODE) -> List[str]:
        """节点涉及的主题词"""
        node_id = self.resolve(name, node_type)
        if not node_id:
            return []

        return self._dedupe(
            self._labels([
                e.target
                for e in self.graph.out_edges(node_id, REL_HAS_TOPIC)
            ])
        )

    # ---------- 关系 / 路径 ----------

    def co_used_with(
        self,
        node_name: str,
        min_strength: int = 1
    ) -> List[Tuple[str, int]]:
        """
        常与该节点一起出现的其他节点

        Returns:
            [(节点名, 共现 workflow 数)]，按共现次数降序
        """
        node_id = self.resolve(node_name, TYPE_NODE)
        if not node_id:
            return []

        edges = (
            self.graph.out_edges(node_id, REL_CO_USED)
            + self.graph.in_edges(node_id, REL_CO_USED)
        )

        pairs = []
        seen = set()
        for edge in edges:
            other = edge.other(node_id)
            if other in seen:
                continue
            seen.add(other)
            strength = int(edge.get("strength", 1) or 1)
            if strength >= min_strength:
                pairs.append((self.name_of(other), strength))

        return sorted(pairs, key=lambda x: -x[1])

    def paths(
        self,
        start: str,
        end: str,
        max_depth: int = 4,
        direction: str = "both"
    ) -> List[List[str]]:
        """
        两点之间的路径（BFS，返回最短路径）

        「KSampler 和 ControlNet 是什么关系」这类问题需要多跳：
        workflow -contains-> node -co_used-> node。
        设计稿只有一层边查询，回答不了这类问题。

        Args:
            start: 起点（名字或 id）
            end: 终点
            max_depth: 最大跳数，防止在稠密图里跑爆炸
            direction: out / in / **both（默认）**。
                       默认 both 是因为问「A 和 B 什么关系」时
                       通常事先不知道方向；而图里 contains / co_used
                       混着正反两个方向，只走出边往往什么都找不到。

        Returns:
            路径列表，每条是节点 id 序列（含首尾）。
            只返回每个节点的最短路径 —— 不是所有简单路径，
            稠密图上枚举全部路径会爆炸。
        """
        start_id = self._resolve_any(start)
        end_id = self._resolve_any(end)

        if not start_id or not end_id:
            return []
        if start_id == end_id:
            return [[start_id]]

        queue: List[Tuple[str, List[str]]] = [(start_id, [start_id])]
        visited = {start_id}
        found: List[List[str]] = []

        while queue:
            current, trail = queue.pop(0)

            if len(trail) > max_depth:
                continue

            for edge in self.graph.related(
                current, direction=direction
            ):
                nxt = edge.other(current)
                if nxt in visited:
                    continue

                next_trail = trail + [nxt]

                if nxt == end_id:
                    found.append(next_trail)
                    if len(found) >= 10:
                        return found
                    continue

                visited.add(nxt)
                queue.append((nxt, next_trail))

        return found

    def neighborhood(
        self,
        name: str,
        depth: int = 1,
        limit: int = 40
    ) -> Dict[str, List[Dict[str, str]]]:
        """
        N 跳邻域（给「这个节点周围有什么」用）

        Args:
            name: 中心节点
            depth: 跳数
            limit: 最多返回多少个邻居（防止稠密节点炸掉输出）

        Returns:
            {中心 id: [邻居, …]}，同时含出边与入边
        """
        center = self._resolve_any(name)
        if not center:
            return {}

        seen = {center}
        frontier = [center]
        result: Dict[str, List[Dict[str, str]]] = {}

        for level in range(1, max(1, depth) + 1):
            level_nodes: List[Dict[str, str]] = []

            for node_id in frontier:
                for edge in self.graph.related(node_id):
                    other = edge.other(node_id)
                    if other in seen:
                        continue
                    seen.add(other)
                    level_nodes.append({
                        "id": other,
                        "name": self.name_of(other),
                        "type": split_id(other)[0],
                        "via": edge.relation,
                        "direction": (
                            "out" if edge.source == node_id else "in"
                        ),
                    })
                    if len(level_nodes) >= limit:
                        break
                if len(level_nodes) >= limit:
                    break

            result[center] = result.get(center, []) + level_nodes
            frontier = [n["id"] for n in level_nodes]

            if not frontier:
                break

        return result

    def _resolve_any(self, name: str) -> str:
        """不限类型地解析（先按原样，再按各类型逐个试）"""
        if not name:
            return ""

        if name in self.graph.nodes:
            return name

        for node_type in (
            TYPE_WORKFLOW, TYPE_NODE, TYPE_PATTERN,
            TYPE_PROBLEM, TYPE_CARD, TYPE_FAMILY,
        ):
            found = self.resolve(name, node_type)
            if found:
                return found

        return ""

    # ---------- 汇总 ----------

    def stats(self) -> Dict[str, Any]:
        """图统计（转给底层图）"""
        return self.graph.stats()

    def render(self, title: str = "知识图谱") -> str:
        """
        渲染成人读的概览

        没有 LLM 的项目里，这个字符串就是 Agent 的「看图」方式。
        """
        stats = self.graph.stats()

        lines = [
            f"# {title}",
            "",
            f"- 顶点 {stats['node_total']} 个，边 "
            f"{stats['edge_total']} 条",
            f"- 孤立顶点 {stats['isolated_nodes']} 个",
            f"- 悬空边 {stats['dangling_edges']} 条",
            "",
            "## 按类型",
            "",
        ]

        for node_type, count in stats["nodes_by_type"].items():
            lines.append(f"- {node_type}：{count}")

        lines.extend(["", "## 按关系", ""])
        for relation, count in stats["edges_by_relation"].items():
            lines.append(f"- `{relation}`：{count}")

        missing = self.nodes_without_cards()
        if missing:
            lines.extend([
                "",
                "## 缺知识卡的节点",
                "",
                "按被使用次数排序：",
                "",
            ])
            for name in missing[:15]:
                count = self._usage_count(
                    self.resolve(name, TYPE_NODE) or ""
                )
                lines.append(f"- `{name}` —— {count} 个 workflow 在用")
            if len(missing) > 15:
                lines.append(f"- …… 另有 {len(missing) - 15} 个")

        return "\n".join(lines)

    def describe(self, name: str) -> str:
        """
        描述一个节点及其直接关系（单点查询的人话输出）
        """
        node_id = self._resolve_any(name)
        if not node_id:
            return f"图里没有「{name}」"

        node = self.graph.get_node(node_id)
        lines = [node.describe()]

        outgoing = self.graph.out_edges(node_id)
        if outgoing:
            lines.append("")
            lines.append("它指向：")
            for edge in outgoing:
                lines.append(
                    f"  -{edge.relation}-> "
                    f"{self.name_of(edge.target)}"
                    + (
                        f"（{edge.get('count')} 次）"
                        if edge.get("count")
                        else ""
                    )
                )

        incoming = self.graph.in_edges(node_id)
        if incoming:
            lines.append("")
            lines.append("被指向：")
            for edge in incoming[:15]:
                lines.append(
                    f"  <-{edge.relation}- "
                    f"{self.name_of(edge.source)}"
                )
            if len(incoming) > 15:
                lines.append(f"  …… 另有 {len(incoming) - 15} 条")

        return "\n".join(lines)

    # ---------- 工具 ----------

    @staticmethod
    def _dedupe(items: List[str]) -> List[str]:
        """去重且保序"""
        return list(dict.fromkeys(items))