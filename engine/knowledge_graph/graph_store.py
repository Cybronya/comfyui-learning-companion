"""
图持久化

设计稿给的 `GraphStore` 有三个问题：

1. **丢边属性**。`save()` 里边只写 source/relation/target，
   builder 挂在边上的 count / strength / severity 全丢。
2. **读不出来**。只有 save 没有 load，图存一次就只能给人看，
   下次要查还得重新跑一遍 build。
3. **JSON 不记版本**。将来改图结构时，旧文件会被当成新结构读，
   报错信息还很难懂。

这里补上 load、版本号与统计。

为什么这里用 JSON 而不是项目里统一的 Markdown：
Markdown 存的是**人读的状态**（学习记录、归纳结论），
要能被 grep、被 Agent 直接读。图是**派生数据**，用图自己的结构存更合适，
而且它本来就是从 Markdown 重新生成的副产品，不需要人工编辑。

2026-10-17 追加：save() 改走 `engine.atomic_write.atomic_write_json`
（流式写 + 临时文件原子替换）。原先 `write_text(json.dumps(...))`
会先拼几百 MB 文本再编码一份 bytes，4 万顶点时峰值内存翻倍 OOM；
而 write_text 先截断，老图谱被清成 0 字节。
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..atomic_write import atomic_write_json
from .graph import KnowledgeGraph
from .models import GraphNode, GraphEdge

#: 存储格式版本。结构不兼容变更时 +1，
#: load() 会拒绝读旧版本而不是给出莫名其妙的错。
GRAPH_FORMAT_VERSION = "1.0"

DEFAULT_PATH = "engine/knowledge_graph/knowledge_graph.json"


class GraphStore:
    """
    图的 JSON 存储
    """

    def __init__(self, path: str = None) -> None:
        """
        初始化存储

        Args:
            path: 文件路径；None 时用
                  engine/knowledge_graph/knowledge_graph.json
        """
        self.path = Path(path) if path else Path(DEFAULT_PATH)

    # ---------- 写 ----------

    def save(
        self,
        graph: KnowledgeGraph,
        indent: int = 2
    ) -> str:
        """
        保存图

        **流式写 + 原子替换**（走 `engine.atomic_write.atomic_write_json`）：
        图到 4 万顶点 / 90 万边时，`json.dumps` 先拼出的整份文本有几百 MB，
        `write_text` 内部还要再编码一份 bytes，峰值内存翻倍直接 OOM；
        而 `write_text` 是 mode 'w'，**先截断再写**，一旦中途失败老图谱
        就被清成 0 字节（2026-10-16 实测：39667 顶点时保存失败，文件变
        0 字节，整张图要重跑 4 分钟重建）。

        Args:
            graph: KnowledgeGraph
            indent: JSON 缩进

        Returns:
            文件路径；失败返回空串（目标文件保持原样）
        """
        try:
            atomic_write_json(
                self.path,
                self.to_payload(graph),
                indent=indent,
                ensure_ascii=False,
            )
            return str(self.path)
        except Exception as e:
            print(f"保存知识图谱失败: {type(e).__name__}: {e}")
            return ""

    def to_payload(self, graph: KnowledgeGraph) -> Dict:
        """图 → 可 JSON 序列化的 dict（save/render 共用）"""
        return {
            "version": GRAPH_FORMAT_VERSION,
            "stats": graph.stats(),
            "nodes": [
                node.to_dict()
                for node in sorted(
                    graph.nodes.values(),
                    key=lambda n: (n.type, n.id),
                )
            ],
            "edges": [
                edge.to_dict()
                for edge in sorted(
                    graph.edges,
                    key=lambda e: (e.relation, e.source, e.target),
                )
            ],
        }

    def render(self, graph: KnowledgeGraph, indent: int = 2) -> str:
        """把图序列化成 JSON 文本（大图别用，见 save 的注释）"""
        return json.dumps(
            self.to_payload(graph),
            indent=indent,
            ensure_ascii=False,
        ) + "\n"

    # ---------- 读 ----------

    def load(self) -> Optional[KnowledgeGraph]:
        """
        读回图

        Returns:
            KnowledgeGraph；文件不存在或格式不对返回 None
        """
        if not self.path.exists():
            return None

        try:
            # utf-8-sig：项目约定读 JSON 一律用它
            with open(self.path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
        except Exception as e:
            print(f"读取知识图谱失败: {e}")
            return None

        if not isinstance(data, dict):
            print("知识图谱格式不对：顶层不是对象")
            return None

        version = str(data.get("version", ""))
        if version and version != GRAPH_FORMAT_VERSION:
            # 结构变了就明确拒绝，比读出一堆 None 强
            print(
                f"知识图谱版本不匹配：文件 {version}，"
                f"当前支持 {GRAPH_FORMAT_VERSION}，请重新生成"
            )
            return None

        graph = KnowledgeGraph()

        # 先建全部顶点，再建边 —— 边的两端必须已存在，
        # 否则 auto_nodes 会补出空壳顶点，掩盖「数据源缺节点」的问题
        for raw in data.get("nodes", []) or []:
            if isinstance(raw, dict) and raw.get("id"):
                graph.add_node(GraphNode.from_dict(raw))

        for raw in data.get("edges", []) or []:
            if not isinstance(raw, dict):
                continue
            edge = GraphEdge.from_dict(raw)
            if not (edge.source and edge.relation and edge.target):
                continue
            # auto_nodes=False：悬空边要暴露，不要偷偷补顶点
            graph.add_edge(edge, auto_nodes=False)

        return graph

    def exists(self) -> bool:
        return self.path.exists()

    def clear(self) -> bool:
        """删除图文件"""
        try:
            if self.path.exists():
                self.path.unlink()
            return True
        except Exception as e:
            print(f"删除知识图谱失败: {e}")
            return False

    # ---------- 汇总 ----------

    def summary(self) -> str:
        """
        图的一行摘要（存完直接可读）
        """
        graph = self.load()
        if graph is None:
            return f"没有可用的知识图谱（{self.path}）"

        stats = graph.stats()
        return (
            f"{self.path}：{stats['node_total']} 顶点 / "
            f"{stats['edge_total']} 边"
            + (
                f"，{stats['dangling_edges']} 条悬空边"
                if stats["dangling_edges"] else ""
            )
        )