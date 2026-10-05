"""
Knowledge Graph —— ComfyUI 工作流知识图谱

把 Agent 已经学到的 Workflow / 节点 / 模式 / 参数 / 问题 / 建议
连成一个可查询的网络。

它**不学新知识**，只做两件事：
    build()  把既有学习结果拼成图
    查询     回答跨 workflow 的问题（「哪些人像流用了 ControlNet」）

## 典型用法

    from engine.knowledge_graph import build_graph

    gq = build_graph()

    gq.workflows_using("ControlNetApply")
    # ['sd1.5/basic', ...]

    gq.nodes_of("sdxl_portrait_0")
    gq.problems_of("sdxl_portrait_0")
    gq.paths("KSampler", "ControlNetApply", max_depth=3)

## 与其它模块的分工

    workflow_learning       学单个 workflow → Markdown 记录
    knowledge_consolidation 从一批记录归纳模式 → Markdown 结论
    knowledge_graph         **把上面两者 + 知识卡索引连成网**，供跨条目查询

它不重复任何学习逻辑，只是换了一种组织方式回答问题。
Markdown 记录仍是唯一事实来源；JSON 图是由它生成的派生数据，
删掉重跑 build 就能再生。

## 为什么顶点 id 带类型前缀

`basic` 既是 workflow 名也可能是 pattern 名，
`sd1.5/basic.json` 与 `sdxl/basic.json` 同名不同族。
用裸 id 放进同一个 dict 会互相覆盖 —— 这是 LearningStore
早就踩过的坑（当时用文件名当键）。所以 id 一律 `类型:名字`。

## 边与关系

    workflow -[contains]->   node       结构上包含（带出现次数）
    workflow -[requires]->   node       生成流程必需的核心节点
    workflow -[member_of]->  family     属于哪个族
    workflow -[matches]->    pattern    命中哪个归纳模式
    workflow -[has_problem]-> problem  体检出的问题
    problem  -[suggests]->   solution   对应建议
    problem  -[problem_in]-> node       问题出在哪个节点上
    node     -[has_card]->   card       有知识卡
    card     -[covers]->     node       知识卡覆盖节点（反向边）
    node     -[co_used]->    node       常一起出现（弱关系）
    node     -[has_topic]->  concept    主题词

迁移路线：数据都在 `to_dict()` / `from_dict()` 里，
真要换 Neo4j 只需重写 graph_store.py，图本身的查询逻辑不用动。
"""

from typing import List

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
    ALL_TYPES,
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
    REL_FIXED_BY,
    REVERSE_RELATIONS,
    nid,
    split_id,
)
from .graph import KnowledgeGraph
from .graph_builder import (
    GraphBuilder,
    load_node_index,
    parse_issue,
    problem_id,
    DEFAULT_CO_USE_MIN,
    DEFAULT_MAX_CO_USE_NODES,
)
from .graph_query import GraphQuery
from .graph_store import GraphStore, GRAPH_FORMAT_VERSION, DEFAULT_PATH


def build_graph(
    store: GraphStore = None,
    builder: GraphBuilder = None,
    save: bool = True,
    verbose: bool = False,
    **builder_kwargs
) -> GraphQuery:
    """
    从现有知识库构建图（便捷入口）

    数据源：
        workflow_learning.LearningStore.completed_records()
        knowledge_consolidation.KnowledgeStore.load_all()
        comfyui_library/knowledge/node_index.json

    Args:
        store: 图存储；None 时用默认路径
        builder: 自定义构建器（一般不用传）
        save: 是否落盘
        verbose: 是否打印规模统计
        **builder_kwargs: 透传给 GraphBuilder
                           （co_use_min / max_co_use_nodes / include_gaps）

    Returns:
        GraphQuery（已带上构建好的图，可直接查）

    某个数据源缺失不是错误 —— 没学过的 workflow、
    没归纳过的模式都应该能出图。缺的源会在 stats 里体现。
    """
    from ..workflow_learning import LearningStore
    from ..knowledge_consolidation import KnowledgeStore as KStore

    records: List = []
    patterns: List = []

    try:
        records = LearningStore().completed_records()
    except Exception as e:
        print(f"读学习记录失败，图会缺少 workflow 顶点: {e}")

    try:
        patterns = KStore().load_all()
    except Exception as e:
        print(f"读归纳模式失败，图会缺少 pattern 顶点: {e}")

    builder = builder if builder is not None else GraphBuilder(**builder_kwargs)
    graph = builder.build(records, patterns)

    if verbose:
        stats = graph.stats()
        print(
            f"知识图谱构建完成：{stats['node_total']} 顶点 / "
            f"{stats['edge_total']} 边"
        )
        print(f"  workflow {len(records)} 个，pattern {len(patterns)} 个")
        if stats["dangling_edges"]:
            print(f"  ⚠ {stats['dangling_edges']} 条悬空边")

        # 模式成员匹配不上是有意义的信号：说明模式卡引用了
        # 没学过的 workflow（样本被删、或模式卡是手写的）。
        # 静默跳过会让图看起来正常，其实 matches 边全是空的。
        if getattr(builder, "unmatched_members", None):
            unmatched = builder.unmatched_members
            print(
                f"  ⚠ {len(unmatched)} 个模式成员匹配不上已学 workflow"
                f"（匹配率 {builder.match_rate:.0%}）"
            )
            for member in unmatched[:5]:
                print(f"      {member}")
            if len(unmatched) > 5:
                print(f"      …… 另有 {len(unmatched) - 5} 个")

    if save:
        store = store if store is not None else GraphStore()
        path = store.save(graph)
        if verbose and path:
            print(f"  已保存到 {path}")

    return GraphQuery(graph)


def load_graph(store: GraphStore = None) -> GraphQuery:
    """
    读回已保存的图

    Args:
        store: 图存储；None 时用默认路径

    Returns:
        GraphQuery；文件不存在时返回空图（`node_count == 0`），
        调用方用 `if not qy.graph.nodes` 判断即可
    """
    store = store if store is not None else GraphStore()
    graph = store.load()
    return GraphQuery(graph if graph is not None else KnowledgeGraph())


__all__ = [
    # 模型
    "GraphNode",
    "GraphEdge",
    "nid",
    "split_id",
    # 顶点类型
    "TYPE_WORKFLOW",
    "TYPE_NODE",
    "TYPE_PATTERN",
    "TYPE_CARD",
    "TYPE_PROBLEM",
    "TYPE_SOLUTION",
    "TYPE_FAMILY",
    "TYPE_CONCEPT",
    "ALL_TYPES",
    # 关系
    "REL_CONTAINS",
    "REL_MEMBER_OF",
    "REL_MATCHES",
    "REL_REQUIRES",
    "REL_USES",
    "REL_HAS_CARD",
    "REL_COVERS",
    "REL_HAS_PROBLEM",
    "REL_PROBLEM_IN",
    "REL_SUGGESTS",
    "REL_CO_USED",
    "REL_HAS_TOPIC",
    "REL_FIXED_BY",
    "REVERSE_RELATIONS",
    # 核心
    "KnowledgeGraph",
    "GraphBuilder",
    "GraphQuery",
    "GraphStore",
    "GRAPH_FORMAT_VERSION",
    "DEFAULT_PATH",
    "DEFAULT_CO_USE_MIN",
    "DEFAULT_MAX_CO_USE_NODES",
    # 入口
    "build_graph",
    "load_graph",
    # 工具
    "load_node_index",
    "parse_issue",
    "problem_id",
]