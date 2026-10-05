"""
图结构核心

与设计稿的两点差异：

1. **维护邻接索引**。设计稿的 `find_related()` 每次扫全量边，
   `workflows_using()` 也是。1000 个 workflow × 20 节点 ≈ 2 万条边，
   每查一次全扫一遍，图越大越慢。这里用 `_out` / `_in` 两张
   邻接表，取邻居是 O(出度) 而不是 O(全部边)。

2. **加边去重、顶点合并**。设计稿 `add_node` 直接 `nodes[id] = node`
   —— 后一个 workflow 里的 KSampler 会把前一个已挂好的知识卡属性冲掉；
   `add_edge` 无脑 append，重建一次边数就翻倍。
   这里同 id 顶点走属性合并，同三元组边只更新属性。

另外**不定义 `__len__`**：LearningStore / TaskQueue 定义了 `__len__`，
于是 `store or DefaultStore()` 这类写法在空对象上是 falsy 的，
会把调用方传进来的对象悄悄顶掉（`learning_scheduler` 刚踩过）。
"""

from typing import Dict, List, Any, Optional, Iterable, Iterator, Set, Tuple

from .models import (
    GraphNode,
    GraphEdge,
    TYPE_NODE,
    nid,
    split_id,
)


class KnowledgeGraph:
    """
    知识图谱

    顶点: {id: GraphNode}
    边:   [(source, relation, target) -> GraphEdge]
    """

    def __init__(self) -> None:
        self.nodes: Dict[str, GraphNode] = {}
        # 邻接索引：id -> 该点发出的边
        self._out: Dict[str, List[GraphEdge]] = {}
        # 邻接索引：id -> 指向该点的边
        self._in: Dict[str, List[GraphEdge]] = {}
        # 去重索引：三元组 -> 边对象
        self._edges: Dict[Tuple[str, str, str], GraphEdge] = {}

    # ---------- 顶点 ----------

    def add_node(self, node: GraphNode) -> GraphNode:
        """
        加顶点

        同 id 已存在则**合并属性**并返回原对象。
        直接覆盖会丢掉先前挂上去的信息 —— 典型场景：
        builder 先给 KSampler 挂知识卡属性，后一个 workflow
        又用一个只有 id/type 的空壳把它顶掉。
        """
        existing = self.nodes.get(node.id)
        if existing is not None:
            existing.merge(node.properties)
            return existing

        self.nodes[node.id] = node
        return node

    def ensure_node(
        self,
        node_id: str,
        node_type: str = "",
        name: str = "",
        **props: Any
    ) -> GraphNode:
        """
        幂等地建一个顶点

        Args:
            node_id: 顶点 id（建议用 nid() 拼好前缀）
            node_type: 类型；给了 name 就能推导
            name: 对象名；给了 node_id 也能推导
            **props: 属性键值对

        Returns:
            GraphNode（新建或已存在的）
        """
        existing = self.nodes.get(node_id)
        if existing is not None:
            existing.merge(props)
            return existing

        _, derived = split_id(node_id)
        node = GraphNode(
            id=node_id,
            type=node_type or TYPE_NODE,
            name=name or derived,
            properties=dict(props),
        )
        self.nodes[node_id] = node
        return node

    def get_node(self, node_id: str) -> Optional[GraphNode]:
        """按 id 取顶点"""
        return self.nodes.get(node_id)

    def has_node(self, node_id: str) -> bool:
        return node_id in self.nodes

    def remove_node(self, node_id: str) -> bool:
        """
        删顶点（连带删掉它的边）

        不删边会留下悬空边 —— 之后任何遍历都要记得判空，
        而「删干净」这个约束一旦漏掉就很难查。
        """
        if node_id not in self.nodes:
            return False

        del self.nodes[node_id]

        for edge in list(self._out.get(node_id, [])):
            self._drop_edge(edge)
        for edge in list(self._in.get(node_id, [])):
            self._drop_edge(edge)

        self._out.pop(node_id, None)
        self._in.pop(node_id, None)

        return True

    def nodes_of_type(self, node_type: str) -> List[GraphNode]:
        """按类型过滤顶点"""
        return [
            n for n in self.nodes.values() if n.type == node_type
        ]

    # ---------- 边 ----------

    def add_edge(
        self,
        edge: GraphEdge,
        auto_nodes: bool = True
    ) -> GraphEdge:
        """
        加边

        Args:
            edge: 边
            auto_nodes: 两端顶点不存在时自动补空壳。
                        关掉可用于严格模式 —— 图里出现指向不存在顶点的
                        悬空边，查询时会静默漏结果，很难排查。

        Returns:
            边对象（新建或已合并的那条）
        """
        if auto_nodes:
            for end in (edge.source, edge.target):
                if end not in self.nodes:
                    self.ensure_node(end)

        existing = self._edges.get(edge.triple)
        if existing is not None:
            existing.merge(edge.properties)
            return existing

        self._edges[edge.triple] = edge
        self._out.setdefault(edge.source, []).append(edge)
        self._in.setdefault(edge.target, []).append(edge)
        return edge

    def link(
        self,
        source: str,
        relation: str,
        target: str,
        **props: Any
    ) -> GraphEdge:
        """建边的语法糖"""
        return self.add_edge(
            GraphEdge(
                source=source,
                relation=relation,
                target=target,
                properties=dict(props),
            )
        )

    def _drop_edge(self, edge: GraphEdge) -> None:
        """从索引里移除一条边（内部用）"""
        self._edges.pop(edge.triple, None)

        out_list = self._out.get(edge.source)
        if out_list and edge in out_list:
            out_list.remove(edge)

        in_list = self._in.get(edge.target)
        if in_list and edge in in_list:
            in_list.remove(edge)

    def has_edge(
        self,
        source: str,
        relation: str,
        target: str
    ) -> bool:
        return (source, relation, target) in self._edges

    @property
    def edges(self) -> List[GraphEdge]:
        """全部边"""
        return list(self._edges.values())

    def edge_count(self) -> int:
        return len(self._edges)

    # ---------- 遍历 ----------

    def out_edges(
        self,
        node_id: str,
        relation: str = ""
    ) -> List[GraphEdge]:
        """
        从该点出发的边

        Args:
            node_id: 顶点 id
            relation: 只取该关系；空串表示不限
        """
        edges = self._out.get(node_id, [])
        if relation:
            return [e for e in edges if e.relation == relation]
        return list(edges)

    def in_edges(
        self,
        node_id: str,
        relation: str = ""
    ) -> List[GraphEdge]:
        """指向该点的边"""
        edges = self._in.get(node_id, [])
        if relation:
            return [e for e in edges if e.relation == relation]
        return list(edges)

    def related(
        self,
        node_id: str,
        relation: str = "",
        direction: str = "out"
    ) -> List[GraphEdge]:
        """
        取关联边

        Args:
            node_id: 顶点 id
            relation: 关系过滤
            direction: out（发出）/ in（指入）/ both

        设计稿的 `find_related` 只返回出边，所以
        `workflows_using()` 得反过来自己扫全量边 ——
        方向参数在这里一次解决。
        """
        if direction == "out":
            return self.out_edges(node_id, relation)
        if direction == "in":
            return self.in_edges(node_id, relation)

        seen = set()
        result = []
        for edge in (
            self.out_edges(node_id, relation)
            + self.in_edges(node_id, relation)
        ):
            key = edge.triple
            if key not in seen:
                seen.add(key)
                result.append(edge)
        return result

    def neighbors(
        self,
        node_id: str,
        relation: str = "",
        direction: str = "out"
    ) -> List[str]:
        """关联的顶点 id"""
        return [
            e.other(node_id)
            for e in self.related(node_id, relation, direction)
        ]

    def __contains__(self, node_id: object) -> bool:
        return node_id in self.nodes

    def __iter__(self) -> Iterator[GraphNode]:
        return iter(self.nodes.values())

    def __repr__(self) -> str:
        return (
            f"<KnowledgeGraph {len(self.nodes)} 顶点 / "
            f"{self.edge_count()} 边>"
        )

    # ---------- 统计 ----------

    def stats(self) -> Dict[str, Any]:
        """
        图的规模统计

        孤立顶点与悬空边也统计进去 —— 有悬空边说明数据源出了问题
        （比如某个 workflow 的节点没建卡），这个信号值得暴露。
        """
        by_type: Dict[str, int] = {}
        for node in self.nodes.values():
            by_type[node.type] = by_type.get(node.type, 0) + 1

        by_relation: Dict[str, int] = {}
        for edge in self._edges.values():
            by_relation[edge.relation] = (
                by_relation.get(edge.relation, 0) + 1
            )

        connected = set()
        for edge in self._edges.values():
            connected.add(edge.source)
            connected.add(edge.target)

        dangling = [
            e for e in self._edges.values()
            if e.source not in self.nodes or e.target not in self.nodes
        ]

        return {
            "node_total": len(self.nodes),
            "edge_total": len(self._edges),
            "nodes_by_type": dict(sorted(
                by_type.items(), key=lambda x: -x[1]
            )),
            "edges_by_relation": dict(sorted(
                by_relation.items(), key=lambda x: -x[1]
            )),
            "isolated_nodes": len(self.nodes) - len(connected),
            "dangling_edges": len(dangling),
        }