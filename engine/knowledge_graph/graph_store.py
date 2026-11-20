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

2026-11-20 追加：**全量流式读写**（这是 F2 端到端测试的真实卡点）。

真实库规模：12.3 万顶点 / 288.6 万边，落盘 JSON **848MB**。
原先的 `json.load()` 会把整个文件读成一个 Python 对象树再拆，
峰值内存 = 848MB 文本 + 对象树（290 万个 dict）+ 已建好的图，
在 24GB 机器上直接 **MemoryError**（`MemoryError` 的 str 是空的，
所以控制台只打出「读取知识图谱失败:」四个字，看不出原因）。

现在改成**边读边建**：

- 写：逐条 `json.dumps` 写文件句柄，不先拼整份 payload
  （`to_payload()` 那条老路会把 290 万个边 dict 全堆在内存里）。
- 读：自实现增量 JSON 解析器（`json.JSONDecoder.raw_decode` +
  分块补读），顶层对象里只有 `nodes` / `edges` 两个数组是流式的，
  数组元素逐个解析、逐个建图，**任何时刻内存里只有一条记录**。

文件格式**不变**（仍是合法 JSON，仍是 `{version, stats, nodes, edges}`），
所以旧文件照样能读，别的工具解析它也不受影响。
"""

import json
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional

from ..streaming_json import JsonStreamReader, write_json_stream
from .graph import KnowledgeGraph
from .models import GraphNode, GraphEdge

#: 存储格式版本。结构不兼容变更时 +1，
#: load() 会拒绝读旧版本而不是给出莫名其妙的错。
GRAPH_FORMAT_VERSION = "1.0"

DEFAULT_PATH = "engine/knowledge_graph/knowledge_graph.json"


class _VersionMismatch(Exception):
    """版本不匹配（内部用，对外表现为 load() 返回 None）"""


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

        **逐条流式写 + 原子替换**：

        真实库 12.3 万顶点 / 288.6 万边，逐条 `json.dumps` 写句柄，
        内存里始终只有一条记录。原先 `atomic_write_json(payload)`
        那条路会先把 290 万个边 dict 全堆成一个 payload
        （`to_payload()`），峰值内存直接翻倍 —— 大图必 OOM。

        写失败时目标文件**保持原样**（临时文件 + `os.replace`）。

        Args:
            graph: KnowledgeGraph
            indent: JSON 缩进（仅作用于 stats 段）

        Returns:
            文件路径；失败返回空串（目标文件保持原样）
        """
        try:
            self._write_stream(graph, indent)
            return str(self.path)
        except Exception as e:
            print(f"保存知识图谱失败: {type(e).__name__}: {e}")
            return ""

    def _write_stream(self, graph: KnowledgeGraph, indent: int) -> None:
        """把图流式写进临时文件，再原子替换目标"""
        write_json_stream(
            self.path,
            header={
                "version": GRAPH_FORMAT_VERSION,
                "stats": graph.stats(),
            },
            arrays=[
                ("nodes", self._iter_nodes(graph)),
                ("edges", self._iter_edges(graph)),
            ],
            indent=indent,
        )

    @staticmethod
    def _iter_nodes(graph: KnowledgeGraph):
        """顶点（排序保证输出稳定，便于 diff 与抽查）"""
        for node in sorted(
            graph.nodes.values(),
            key=lambda n: (n.type, n.id),
        ):
            yield node.to_dict()

    @staticmethod
    def _iter_edges(graph: KnowledgeGraph):
        """边"""
        for edge in sorted(
            graph.edges,
            key=lambda e: (e.relation, e.source, e.target),
        ):
            yield edge.to_dict()

    def to_payload(self, graph: KnowledgeGraph) -> Dict:
        """
        图 → 可 JSON 序列化的 dict

        **注意：整份物化，大图会 OOM**（290 万个边 dict 全在内存里）。
        存盘请走 `save()`（流式），这个方法只给小图 / 调试用。
        """
        return {
            "version": GRAPH_FORMAT_VERSION,
            "stats": graph.stats(),
            "nodes": list(self._iter_nodes(graph)),
            "edges": list(self._iter_edges(graph)),
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
        读回图（**流式**，大图不会 OOM）

        Returns:
            KnowledgeGraph；文件不存在或格式不对返回 None
        """
        if not self.path.exists():
            return None

        try:
            # utf-8-sig：项目约定读 JSON 一律用它
            with open(self.path, "r", encoding="utf-8-sig") as f:
                graph = self._read_stream(f)
        except _VersionMismatch as e:
            print(str(e))
            return None
        except Exception as e:
            print(f"读取知识图谱失败: {type(e).__name__}: {e}")
            return None

        return graph

    def _read_stream(self, fp) -> KnowledgeGraph:
        """
        流式解析顶层对象并建图

        `nodes` / `edges` 两个数组逐元素建，
        其余字段整块解掉（version / stats）。
        """
        reader = JsonStreamReader(fp)

        reader.expect("{")
        graph = KnowledgeGraph()

        while True:
            ch = reader.peek()
            if ch == "":
                raise ValueError("文件提前结束")
            if ch == "}":
                reader.pos += 1
                break
            if ch == ",":
                reader.pos += 1
                continue

            key = reader.read_value()
            reader.expect(":")

            if key == "nodes":
                # 先建全部顶点，再建边 —— 边的两端必须已存在，
                # 否则 auto_nodes 会补出空壳顶点，掩盖「数据源缺节点」的问题
                for raw in reader.iter_array():
                    if isinstance(raw, dict) and raw.get("id"):
                        graph.add_node(GraphNode.from_dict(raw))
            elif key == "edges":
                for raw in reader.iter_array():
                    if not isinstance(raw, dict):
                        continue
                    edge = GraphEdge.from_dict(raw)
                    if not (edge.source and edge.relation and edge.target):
                        continue
                    # auto_nodes=False：悬空边要暴露，不要偷偷补顶点
                    graph.add_edge(edge, auto_nodes=False)
            else:
                value = reader.read_value()
                if key == "version":
                    version = str(value)
                    if version and version != GRAPH_FORMAT_VERSION:
                        raise _VersionMismatch(
                            f"知识图谱版本不匹配：文件 {version}，"
                            f"当前支持 {GRAPH_FORMAT_VERSION}，请重新生成"
                        )

            reader.compact()

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

    def summary(self, graph: Optional[KnowledgeGraph] = None) -> str:
        """
        图的一行摘要（存完直接可读）

        Args:
            graph: 已加载的图；给了就直接用，**不再重新读盘**。
                   大图场景必须给 —— 重新 load 一遍 848MB 的图
                   会再吃一份内存（大图下直接 MemoryError）。
        """
        if graph is None:
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
