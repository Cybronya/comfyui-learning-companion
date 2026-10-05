r"""
Knowledge Graph 模块测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_knowledge_graph

-X utf8 必须加，否则中文输出乱码。
"""

import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.knowledge_graph import (
    GraphNode,
    GraphEdge,
    KnowledgeGraph,
    GraphBuilder,
    GraphQuery,
    GraphStore,
    nid,
    split_id,
    parse_issue,
    problem_id,
    build_graph,
    load_graph,
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
    GRAPH_FORMAT_VERSION,
)

from engine.workflow_learning.learning_record import LearningRecord
from engine.knowledge_consolidation.models import WorkflowPattern


# ============================================================
# 测试数据
# ============================================================

NODE_INDEX = {
    "KSampler": {
        "knowledge_file": "ksampler.md",
        "category": "Diffusion Sampling",
        "role": "sampler",
        "difficulty": "beginner",
        "learning_topics": ["diffusion", "steps", "cfg", "sampler"],
    },
    "CheckpointLoaderSimple": {
        "knowledge_file": "checkpointloadersimple.md",
        "category": "Model Loading",
        "role": "loader",
        "difficulty": "beginner",
        "learning_topics": ["checkpoint"],
    },
    "LoraLoader": {
        "knowledge_file": "loraloader.md",
        "category": "Model Loading",
        "role": "modifier",
        "difficulty": "beginner",
        "learning_topics": ["lora"],
    },
}


def make_record(
    key,
    nodes,
    important=None,
    status="completed",
    issues=None,
    missing=None,
    wf_type="Text To Image",
):
    return LearningRecord(
        workflow_name=key.rsplit("/", 1)[-1].rsplit(".", 1)[0],
        file_path=f"comfyui_library/workflows/{key}",
        key=key,
        status=status,
        workflow_type=wf_type,
        nodes=list(nodes),
        important_nodes=list(important or []),
        diagnostic_issues=list(issues or []),
        missing_nodes=list(missing or []),
        learned_at="2026-10-06 01:00:00",
    )


def make_pattern(name, members, common, problems=None):
    return WorkflowPattern(
        name=name,
        workflow_type="Text To Image",
        frequency=len(members),
        common_nodes=list(common),
        members=list(members),
        common_problems=list(problems or []),
        level="strong",
        coverage=1.0,
    )


#: 一组自洽的样本：3 个 workflow，跨 2 个族，共享节点 + 独有节点
SAMPLE_RECORDS = [
    make_record(
        "sd1.5/basic.json",
        ["CheckpointLoaderSimple", "CLIPTextEncode", "CLIPTextEncode",
         "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage"],
        important=["CheckpointLoaderSimple", "KSampler", "VAEDecode"],
        issues=["[warning] CFG值较高（当前 12.0），约束可能过强 → 建议降到 7-10"],
    ),
    make_record(
        "sd1.5/lora.json",
        ["CheckpointLoaderSimple", "LoraLoader", "CLIPTextEncode",
         "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage"],
        important=["CheckpointLoaderSimple", "LoraLoader", "KSampler"],
        issues=["[warning] CFG值较高（当前 12.0），约束可能过强 → 建议降到 7-10"],
        missing=["LoraLoader"],
    ),
    make_record(
        "sdxl/portrait.json",
        ["CheckpointLoaderSimple", "ControlNetApply", "CLIPTextEncode",
         "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage"],
        important=["CheckpointLoaderSimple", "KSampler", "ControlNetApply"],
        issues=["[info] 采样步数偏低（当前 4），可能出图不完整 → 建议提升到 20 以上"],
        missing=["ControlNetApply"],
        wf_type="Image To Image",
    ),
]

SAMPLE_PATTERNS = [
    make_pattern(
        "sd15_t2i",
        ["sd1.5/basic.json", "sd1.5/lora.json"],
        ["CheckpointLoaderSimple", "CLIPTextEncode", "KSampler",
         "EmptyLatentImage", "VAEDecode", "SaveImage"],
        problems=[{
            "problem": "CFG值较高（当前 12.0），约束可能过强",
            "count": 2, "severity": "warning", "samples": [],
        }],
    ),
    make_pattern(
        "sdxl_portrait",
        ["sdxl/portrait.json"],
        ["CheckpointLoaderSimple", "ControlNetApply", "KSampler"],
    ),
]


def build_sample(**kwargs):
    builder = GraphBuilder(node_index=NODE_INDEX, **kwargs)
    return builder.build(SAMPLE_RECORDS, SAMPLE_PATTERNS), builder


# ============================================================
# A. 模型
# ============================================================

def test_namespaced_ids():
    """测试 id 命名空间（裸 id 会跨类型撞车）"""
    print("=" * 60)
    print("测试 A1：id 命名空间")
    print("=" * 60)

    assert nid(TYPE_NODE, "KSampler") == "node:KSampler"
    assert nid(TYPE_WORKFLOW, "sd1.5/basic.json") == \
        "workflow:sd1.5/basic.json"

    # 同名不同族 / 不同类型不再互相覆盖
    g = KnowledgeGraph()
    g.add_node(GraphNode(id=nid(TYPE_WORKFLOW, "a/basic.json"),
                         type=TYPE_WORKFLOW))
    g.add_node(GraphNode(id=nid(TYPE_WORKFLOW, "b/basic.json"),
                         type=TYPE_WORKFLOW))
    g.add_node(GraphNode(id=nid(TYPE_PATTERN, "basic"),
                         type=TYPE_PATTERN))
    print(f"  同名顶点 {len(g.nodes)} 个: {list(g.nodes)}")
    assert len(g.nodes) == 3, "同名不同类型的顶点必须共存"

    assert split_id("node:KSampler") == (TYPE_NODE, "KSampler")
    assert split_id("ControlNetApply") == (TYPE_NODE, "ControlNetApply")

    print("命名空间正确 [OK]\n")


def test_node_property_merge():
    """测试同 id 顶点属性合并（覆盖会丢知识卡信息）"""
    print("=" * 60)
    print("测试 A2：顶点属性合并")
    print("=" * 60)

    g = KnowledgeGraph()
    first = g.add_node(GraphNode(
        id=nid(TYPE_NODE, "KSampler"), type=TYPE_NODE,
        properties={"has_card": True, "category": "Sampling"},
    ))
    second = g.add_node(GraphNode(
        id=nid(TYPE_NODE, "KSampler"), type=TYPE_NODE,
        properties={"used_in": 3},
    ))

    print(f"  合并后: {g.get_node(first.id).properties}")
    assert first is second, "应返回已存在的顶点"
    assert first.properties["has_card"] is True, "先挂的属性不能被冲掉"
    assert first.properties["category"] == "Sampling"
    assert first.properties["used_in"] == 3

    # ensure_node 也走合并
    g.ensure_node(nid(TYPE_NODE, "KSampler"), used_in=5)
    assert g.get_node(first.id).properties["used_in"] == 5

    print("属性合并正确 [OK]\n")


# ============================================================
# B. 图核心
# ============================================================

def test_edge_dedup():
    """测试加边去重（设计稿里 append 会让边翻倍）"""
    print("=" * 60)
    print("测试 B1：加边去重")
    print("=" * 60)

    g = KnowledgeGraph()
    g.link("workflow:a", REL_CONTAINS, "node:KSampler", count=2)
    g.link("workflow:a", REL_CONTAINS, "node:KSampler", count=5)
    print(f"  同一三元组加两次 -> 边数 {g.edge_count()}")
    assert g.edge_count() == 1, "重复边应合并"
    assert g.out_edges("workflow:a")[0].get("count") == 5, \
        "属性应更新"

    # 关系不同就是不同的边
    g.link("workflow:a", REL_REQUIRES, "node:KSampler")
    assert g.edge_count() == 2

    print("加边去重正确 [OK]\n")


def test_adjacency_index():
    """测试邻接索引（设计稿全是 O(E) 扫边）"""
    print("=" * 60)
    print("测试 B2：邻接索引")
    print("=" * 60)

    g = KnowledgeGraph()
    for i in range(50):
        g.link(f"workflow:w{i}", REL_CONTAINS, "node:KSampler")
    g.link("workflow:w0", REL_CONTAINS, "node:VAEDecode")

    out = g.out_edges("workflow:w0", REL_CONTAINS)
    into = g.in_edges("node:KSampler", REL_CONTAINS)

    print(f"  w0 的出边 {len(out)} 条，KSampler 的入边 {len(into)} 条")
    assert len(out) == 2
    assert len(into) == 50
    # 索引与全量一致
    assert len([e for e in g.edges
                if e.target == "node:KSampler"]) == 50

    print("邻接索引正确 [OK]\n")


def test_remove_node_cleans_edges():
    """测试删顶点连带删边（残留悬空边很难查）"""
    print("=" * 60)
    print("测试 B3：删顶点")
    print("=" * 60)

    g = KnowledgeGraph()
    g.link("workflow:a", REL_CONTAINS, "node:KSampler")
    g.link("node:KSampler", REL_HAS_CARD, "card:ksampler.md")

    assert g.remove_node("node:KSampler") is True
    print(f"  删后: {len(g.nodes)} 顶点 / {g.edge_count()} 边")
    assert len(g.nodes) == 2
    assert g.edge_count() == 0, "悬空边必须一起删"
    assert g.remove_node("不存在") is False

    print("删顶点正确 [OK]\n")


def test_dangling_edge_detected():
    """测试悬空边可被发现（数据源缺节点时要看得见）"""
    print("=" * 60)
    print("测试 B4：悬空边检测")
    print("=" * 60)

    g = KnowledgeGraph()
    g.link("workflow:a", REL_CONTAINS, "node:KSampler")
    # auto_nodes=False 时两端可以不存在
    g.add_edge(
        GraphEdge("workflow:ghost", REL_CONTAINS, "node:Ghost"),
        auto_nodes=False,
    )

    stats = g.stats()
    print(f"  stats: {stats['node_total']} 顶点 / "
          f"{stats['edge_total']} 边 / 悬空 {stats['dangling_edges']}")
    assert stats["dangling_edges"] == 1, "悬空边应被统计出来"

    print("悬空边检测正确 [OK]\n")


# ============================================================
# C. Builder
# ============================================================

def test_parse_issue():
    """测试诊断记录解析"""
    print("=" * 60)
    print("测试 C1：诊断记录解析")
    print("=" * 60)

    parsed = parse_issue(
        "[warning] CFG值较高（当前 12.0），约束可能过强 → 建议降到 7-10"
    )
    print(f"  {parsed}")
    assert parsed["severity"] == "warning"
    assert "CFG" in parsed["message"]
    assert "→" not in parsed["message"], "建议应被切走"
    assert "建议降到" in parsed["suggestion"]

    # 没有建议的
    plain = parse_issue("[error] 缺少 VAEDecode 节点")
    print(f"  {plain}")
    assert plain["severity"] == "error"
    assert plain["suggestion"] == ""

    # 格式不符
    assert parse_issue("") is None
    assert parse_issue("[warning] ") is None

    print("解析正确 [OK]\n")


def test_build_workflow_structure():
    """测试 workflow 顶点与结构边"""
    print("=" * 60)
    print("测试 C2：workflow 结构")
    print("=" * 60)

    g, _ = build_sample()
    qy = GraphQuery(g)

    wf = g.get_node(nid(TYPE_WORKFLOW, "sd1.5/basic.json"))
    print(f"  {wf.describe()}")
    assert wf is not None
    assert wf.get("workflow_type") == "Text To Image"
    assert wf.get("node_count") == 7, "CLIPTextEncode 出现两次也算 7"

    # CLIPTextEncode 出现两次 → contains 边 count=2
    nodes = qy.nodes_of("sd1.5/basic.json")
    print(f"  节点: {nodes}")
    assert len(nodes) == 6, "6 种节点（7 个实例）"

    edge = g.out_edges(
        nid(TYPE_WORKFLOW, "sd1.5/basic.json"), REL_CONTAINS
    )
    clip = [e for e in edge if "CLIPTextEncode" in e.target][0]
    print(f"  CLIPTextEncode count={clip.get('count')}")
    assert clip.get("count") == 2, "重复节点应记出现次数"

    # 核心节点 → requires
    core = qy.core_nodes("sd1.5/basic.json")
    print(f"  核心节点: {core}")
    assert "KSampler" in core
    assert "CLIPTextEncode" not in core, "CLIPTextEncode 不是核心"

    # 族
    assert qy.family_of("sd1.5/basic.json") == "sd1.5"
    assert qy.family_of("sdxl/portrait.json") == "sdxl"

    print("workflow 结构正确 [OK]\n")


def test_build_problems():
    """测试问题 / 建议 / 归属 / 缺卡"""
    print("=" * 60)
    print("测试 C3：问题与建议")
    print("=" * 60)

    g, _ = build_sample()
    qy = GraphQuery(g)

    problems = qy.problems_of("sd1.5/basic.json")
    print(f"  basic 的问题: {problems}")
    assert len(problems) == 1

    # 同一条问题在两个 workflow 里出现 → 合并成一个顶点
    both = set(problems) & set(qy.problems_of("sd1.5/lora.json"))
    print(f"  两个 sd1.5 workflow 共有问题: {both}")
    assert len(both) == 1, "同一消息应合并成一个问题顶点"

    # 建议
    solutions = qy.solutions_for(problems[0])
    print(f"  建议: {solutions}")
    assert len(solutions) == 1
    assert "7-10" in solutions[0]

    # 反查：哪些 workflow 有 CFG 问题
    hit = qy.workflows_with_problem("CFG")
    print(f"  含 CFG 的 workflow: {hit}")
    assert len(hit) == 2, "basic 与 lora 都有 CFG 问题"

    # 问题归属：消息里没点名节点 → 未归属
    causes = qy.nodes_causing("sd1.5/basic.json")
    print(f"  归属: {causes}")
    assert "(未归属到具体节点)" in causes, \
        "不该凭参数名猜节点"

    # 缺卡 → 问题
    gaps = qy.problems_of("sdxl/portrait.json")
    print(f"  portrait 的问题: {gaps}")
    assert any("ControlNetApply" in p and "缺" in p for p in gaps)
    # 缺卡节点归属明确（节点名就在消息里）
    causes2 = qy.nodes_causing("sdxl/portrait.json")
    print(f"  portrait 归属: {list(causes2)}")
    assert "ControlNetApply" in causes2

    print("问题与建议正确 [OK]\n")


def test_build_node_cards():
    """测试知识卡索引接入"""
    print("=" * 60)
    print("测试 C4：知识卡索引")
    print("=" * 60)

    g, _ = build_sample()
    qy = GraphQuery(g)

    node = g.get_node(nid(TYPE_NODE, "KSampler"))
    print(f"  KSampler: {node.properties}")
    assert node.get("has_card") is True
    assert node.get("category") == "Diffusion Sampling"

    # 没卡片的节点：has_card 为 False
    vae = g.get_node(nid(TYPE_NODE, "VAEDecode"))
    assert vae.get("has_card") is False

    # has_card / covers 双向边
    card = qy.card_for("KSampler")
    print(f"  KSampler 的卡: {card}")
    assert card == "ksampler.md"
    assert g.has_edge(nid(TYPE_NODE, "KSampler"),
                      REL_HAS_CARD, nid(TYPE_CARD, "ksampler.md"))
    assert g.has_edge(nid(TYPE_CARD, "ksampler.md"),
                      REL_COVERS, nid(TYPE_NODE, "KSampler"))

    # 主题
    topics = qy.topics_of("KSampler")
    print(f"  KSampler 主题: {topics}")
    assert "diffusion" in topics and "cfg" in topics
    assert g.has_node(nid(TYPE_CONCEPT, "cfg"))

    print("知识卡索引正确 [OK]\n")


def test_build_patterns():
    """测试模式顶点与 matches 边"""
    print("=" * 60)
    print("测试 C5：模式")
    print("=" * 60)

    g, _ = build_sample()
    qy = GraphQuery(g)

    patterns = qy.patterns_of("sd1.5/basic.json")
    print(f"  basic 命中: {patterns}")
    assert patterns == ["sd15_t2i"]

    members = qy.workflows_in_pattern("sd15_t2i")
    print(f"  sd15_t2i 成员: {members}")
    assert len(members) == 2

    node = g.get_node(nid(TYPE_PATTERN, "sd15_t2i"))
    assert node.get("frequency") == 2
    assert node.get("level") == "strong"

    # pattern 也 contains 共有节点 → 「哪些模式用到 KSampler」与
    # 「哪些 workflow 用到」走同一套查法
    pattern_nodes = [
        qy.name_of(e.target)
        for e in g.out_edges(
            nid(TYPE_PATTERN, "sd15_t2i"), REL_CONTAINS
        )
    ]
    print(f"  sd15_t2i 共有节点: {pattern_nodes}")
    assert "KSampler" in pattern_nodes
    assert g.out_edges(
        nid(TYPE_PATTERN, "sd15_t2i"), REL_CONTAINS
    )[0].get("scope") == "common"

    # 两个 workflow 都用了 KSampler
    ksampler_users = qy.workflows_using("KSampler")
    print(f"  用 KSampler 的 workflow: {ksampler_users}")
    assert len(ksampler_users) == 3

    # 模式层面的问题
    probs = [
        g.get_node(e.target).get("message")
        for e in g.out_edges(
            nid(TYPE_PATTERN, "sd15_t2i"), REL_HAS_PROBLEM
        )
    ]
    print(f"  模式问题: {probs}")
    assert len(probs) == 1

    print("模式接入正确 [OK]\n")


def test_co_occurrence_threshold():
    """测试共现阈值（噪声共现会淹没信号）"""
    print("=" * 60)
    print("测试 C6：共现阈值")
    print("=" * 60)

    # 阈值 2：LoraLoader 与 CheckpointLoaderSimple 只在 lora.json 里
    # 共现一次，不该建边
    g, _ = build_sample(co_use_min=2)
    qy = GraphQuery(g)

    pairs = qy.co_used_with("KSampler")
    print(f"  KSampler 共现: {pairs}")
    assert pairs, "KSampler 与多个节点共现，应有边"
    # KSampler 出现在全部 3 个 workflow 里，与每个节点都共现 >= 3 次
    assert all(strength >= 2 for _, strength in pairs)

    co = dict(pairs)
    assert "CheckpointLoaderSimple" in co
    assert co["CheckpointLoaderSimple"] >= 3

    # LoraLoader 只在 1 个 workflow 里 → 无共现边
    assert not qy.co_used_with("LoraLoader"), \
        "只在单个 workflow 共现的节点不该建共现边"

    # 阈值调高后边变少
    g2, _ = build_sample(co_use_min=99)
    assert GraphQuery(g2).co_used_with("KSampler") == []
    print(f"  阈值 99 时共现: {GraphQuery(g2).co_used_with('KSampler')}")

    print("共现阈值正确 [OK]\n")


def test_co_occurrence_size_cap():
    """测试超大 workflow 不参与共现（否则一张图刷成噪声）"""
    print("=" * 60)
    print("测试 C7：共现规模上限")
    print("=" * 60)

    big = make_record(
        "sd1.5/huge.json",
        [f"Node{i}" for i in range(50)],
    )
    builder = GraphBuilder(node_index=NODE_INDEX, co_use_min=1)
    g = builder.build([big], [])
    qy = GraphQuery(g)

    print(f"  50 节点 workflow -> 共现边 {len([e for e in g.edges if e.relation == REL_CO_USED])}")
    assert not [e for e in g.edges if e.relation == REL_CO_USED], \
        "超大 workflow 应被排除在共现统计外"

    # 调大上限后就会有
    builder2 = GraphBuilder(
        node_index=NODE_INDEX, co_use_min=1, max_co_use_nodes=60
    )
    g2 = builder2.build([big], [])
    assert [e for e in g2.edges if e.relation == REL_CO_USED], \
        "上限调大后应统计共现"

    print("共现规模上限正确 [OK]\n")


def test_failed_record_excluded():
    """测试失败记录不进图（残缺数据会建出悬空边）"""
    print("=" * 60)
    print("测试 C8：排除失败记录")
    print("=" * 60)

    bad = make_record("sd1.5/broken.json", ["KSampler"], status="failed")
    good = make_record("sd1.5/good.json", ["KSampler", "VAEDecode"])

    builder = GraphBuilder(node_index=NODE_INDEX)
    g = builder.build([bad, good], [])

    print(f"  顶点数: {len(g.nodes)}")
    assert not g.has_node(nid(TYPE_WORKFLOW, "sd1.5/broken.json")), \
        "失败记录不该进图"
    assert g.has_node(nid(TYPE_WORKFLOW, "sd1.5/good.json"))

    print("排除失败记录正确 [OK]\n")


# ============================================================
# D. 查询
# ============================================================

def test_workflows_using():
    """测试核心查询：哪些 workflow 用了这个节点"""
    print("=" * 60)
    print("测试 D1：workflows_using")
    print("=" * 60)

    _, builder = build_sample()
    qy = GraphQuery(builder.graph)

    ksampler = qy.workflows_using("KSampler")
    print(f"  KSampler -> {ksampler}")
    assert len(ksampler) == 3, "三个 workflow 都用了 KSampler"

    cn = qy.workflows_using("ControlNetApply")
    print(f"  ControlNetApply -> {cn}")
    assert cn == ["portrait"], "只有 sdxl/portrait 用了 ControlNet"

    # 部分名：ControlNet -> ControlNetApply（唯一命中）
    partial = qy.workflows_using("ControlNet")
    print(f"  ControlNet -> {partial}")
    assert partial == ["portrait"], "不完整的节点名也应能查到"

    # 完整 id 也能用
    assert qy.workflows_using("node:KSampler") == ksampler

    # 不存在的节点
    assert qy.workflows_using("NonexistentNode") == []

    print("workflows_using 正确 [OK]\n")


def test_ambiguous_name_not_guessed():
    """测试歧义名不瞎猜（猜错比说找不到危险）"""
    print("=" * 60)
    print("测试 D2：歧义名不猜")
    print("=" * 60)

    records = [
        make_record("sd1.5/a.json", ["FooLoader"]),
        make_record("sdxl/b.json", ["BarLoader"]),
    ]
    builder = GraphBuilder(node_index=NODE_INDEX)
    g = builder.build(records, [])
    qy = GraphQuery(g)

    # Loader 命中 FooLoader 与 BarLoader → 两个候选，不猜
    print(f"  resolve('Loader') = {qy.resolve('Loader', TYPE_NODE)!r}")
    assert qy.resolve("Loader", TYPE_NODE) == "", \
        "多个候选时应返回空，而不是挑一个"

    # 但确定的名字正常
    assert qy.resolve("FooLoader", TYPE_NODE) == "node:FooLoader"

    print("歧义名处理正确 [OK]\n")


def test_paths_multihop():
    """测试多跳查询（设计稿只有一层边，回答不了关系问题）"""
    print("=" * 60)
    print("测试 D3：多跳路径")
    print("=" * 60)

    _, builder = build_sample()
    qy = GraphQuery(builder.graph)

    # workflow -> node -> card 两跳
    paths = qy.paths("KSampler", "ksampler.md", max_depth=3)
    print(f"  KSampler -> ksampler.md:")
    for p in paths[:3]:
        print(f"    {len(p) - 1} 跳: {' -> '.join(qy.name_of(x) for x in p)}")
    assert paths, "应能找到 KSampler 到知识卡的路径"
    # 最短路是直接 has_card（1 跳）
    assert paths[0] == [
        nid(TYPE_NODE, "KSampler"), nid(TYPE_CARD, "ksampler.md")
    ]

    # 节点 → workflow 反向也通
    back = qy.paths("ksampler.md", "sd1.5/basic.json", max_depth=3)
    print(f"  ksampler.md -> basic（反向）: {len(back)} 条")
    assert back, "反向遍历应能走到 workflow"
    # 只走出边则走不通（workflow 是 contains 的源端）
    assert not qy.paths(
        "ksampler.md", "sd1.5/basic.json", max_depth=3,
        direction="out",
    ), "只走出边时不该找到路径"

    # 同族节点之间：先有 1 跳共现边
    same = qy.paths("KSampler", "VAEDecode", max_depth=3)
    print(f"  KSampler -> VAEDecode: {len(same)} 条路径")
    assert same[0] == [nid(TYPE_NODE, "KSampler"),
                      nid(TYPE_NODE, "VAEDecode")], "应走最短的共现边"

    # 自己到自己
    assert qy.paths("KSampler", "KSampler") == [
        [nid(TYPE_NODE, "KSampler")]
    ]

    # 不连通
    assert qy.paths("KSampler", "不存在的节点") == []

    # 真正的多跳：两个节点之间没有直接边，只能经 workflow 中转
    g2 = KnowledgeGraph()
    g2.link(nid(TYPE_WORKFLOW, "wf1.json"), REL_CONTAINS,
            nid(TYPE_NODE, "Alpha"))
    g2.link(nid(TYPE_WORKFLOW, "wf1.json"), REL_CONTAINS,
            nid(TYPE_NODE, "Beta"))

    multi = GraphQuery(g2).paths("Alpha", "Beta", max_depth=3)
    print(f"  Alpha -> Beta（无直接边）: {len(multi)} 条")
    for p in multi:
        print(f"    {len(p) - 1} 跳: "
              f"{' -> '.join(GraphQuery(g2).name_of(x) for x in p)}")
    assert multi, "无直接边时应能经 workflow 找到路径"
    assert all(len(p) == 3 for p in multi), "只能是 2 跳"
    assert multi[0][1] == nid(TYPE_WORKFLOW, "wf1.json")

    # max_depth 不够时找不到
    assert GraphQuery(g2).paths("Alpha", "Beta", max_depth=1) == []

    print("多跳路径正确 [OK]\n")


def test_nodes_without_cards():
    """测试建卡优先级（用得多的该先补卡）"""
    print("=" * 60)
    print("测试 D4：缺卡节点排序")
    print("=" * 60)

    _, builder = build_sample()
    qy = GraphQuery(builder.graph)

    missing = qy.nodes_without_cards()
    print(f"  缺卡节点: {missing}")

    assert "KSampler" not in missing, "KSampler 有卡"
    assert "ControlNetApply" in missing

    # 按使用次数降序：KSampler 出现 3 次但有卡；
    # EmptyLatentImage / VAEDecode / SaveImage 各 3 次
    counts = {}
    for name in missing:
        counts[name] = len(qy.workflows_using(name))
    print(f"  各节点使用次数: {counts}")

    ordered = sorted(
        missing, key=lambda n: -counts[n]
    )
    assert qy.nodes_without_cards() == ordered

    print("缺卡排序正确 [OK]\n")


def test_describe_and_render():
    """测试人读输出（无 LLM 项目里这就是 Agent 的看图方式）"""
    print("=" * 60)
    print("测试 D5：人读输出")
    print("=" * 60)

    _, builder = build_sample()
    qy = GraphQuery(builder.graph)

    desc = qy.describe("KSampler")
    print(desc)
    print()
    assert "KSampler" in desc
    assert "有卡" in desc, "卡片状态应转成人话"
    assert "used_in" not in desc, "不该把内部属性名抛给用户"
    assert "properties" not in desc

    unknown = qy.describe("查无此节点")
    print(f"  {unknown}")
    assert "没有" in unknown

    text = qy.render()
    print()
    print("\n".join(text.split("\n")[:14]))
    print()
    assert "知识图谱" in text
    assert "缺知识卡的节点" in text
    assert "悬空边" in text

    print("人读输出正确 [OK]\n")


# ============================================================
# E. 存储
# ============================================================

def test_store_roundtrip():
    """测试存取往返（边属性不能丢）"""
    print("=" * 60)
    print("测试 E1：存取往返")
    print("=" * 60)

    _, builder = build_sample()
    g = builder.graph

    with TemporaryDirectory() as tmp:
        store = GraphStore(str(Path(tmp) / "graph.json"))
        path = store.save(g)

        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        print(f"  文件: version={raw['version']} "
              f"{len(raw['nodes'])} 顶点 {len(raw['edges'])} 边")
        assert raw["version"] == GRAPH_FORMAT_VERSION
        assert len(raw["nodes"]) == len(g.nodes)
        assert len(raw["edges"]) == g.edge_count()

        # 关键：边属性在文件里
        co = [
            e for e in raw["edges"] if e["relation"] == REL_CO_USED
        ]
        print(f"  共现边样例: {co[0] if co else None}")
        assert co and "strength" in co[0]["properties"], "边的属性不能丢"
        contains = [
            e for e in raw["edges"]
            if e["relation"] == REL_CONTAINS and e["properties"].get("count")
        ]
        assert contains, "contains 边的 count 应存下来"

        loaded = store.load()
        assert loaded is not None
        print(f"  读回: {len(loaded.nodes)} 顶点 / "
              f"{loaded.edge_count()} 边")
        assert len(loaded.nodes) == len(g.nodes)
        assert loaded.edge_count() == g.edge_count()

        # 读回后查询仍可用
        qy = GraphQuery(loaded)
        assert len(qy.workflows_using("KSampler")) == 3

        # 边属性读回后还在
        edge = loaded.out_edges(
            nid(TYPE_WORKFLOW, "sd1.5/basic.json"), REL_CONTAINS
        )
        clip = [e for e in edge if "CLIPTextEncode" in e.target][0]
        assert clip.get("count") == 2

        print(f"  {store.summary()}")

    print("存取往返正确 [OK]\n")


def test_store_version_guard():
    """测试版本守卫（旧结构要明确拒绝）"""
    print("=" * 60)
    print("测试 E2：版本守卫")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        target = Path(tmp) / "graph.json"

        target.write_text(json.dumps({
            "version": "0.1",
            "nodes": [], "edges": [],
        }, ensure_ascii=False), encoding="utf-8")

        loaded = GraphStore(str(target)).load()
        print(f"  旧版本读回: {loaded}")
        assert loaded is None, "版本不匹配应拒绝读"

        # 缺文件
        missing = GraphStore(str(Path(tmp) / "nope.json")).load()
        print(f"  缺文件读回: {missing}")
        assert missing is None

        # 坏 JSON
        broken = Path(tmp) / "broken.json"
        broken.write_text("{不是合法 JSON", encoding="utf-8")
        assert GraphStore(str(broken)).load() is None

        # 顶层不是对象
        weird = Path(tmp) / "weird.json"
        weird.write_text("[1,2,3]", encoding="utf-8")
        assert GraphStore(str(weird)).load() is None

    print("版本守卫正确 [OK]\n")


def test_store_exposes_dangling():
    """测试存读后悬空边仍然可见"""
    print("=" * 60)
    print("测试 E3：悬空边往返")
    print("=" * 60)

    g = KnowledgeGraph()
    g.link("workflow:a", REL_CONTAINS, "node:KSampler")
    g.add_edge(
        GraphEdge("workflow:ghost", REL_CONTAINS, "node:Ghost"),
        auto_nodes=False,
    )

    with TemporaryDirectory() as tmp:
        store = GraphStore(str(Path(tmp) / "g.json"))
        store.save(g)
        loaded = store.load()

        stats = loaded.stats()
        print(f"  读回后悬空边: {stats['dangling_edges']}")
        assert stats["dangling_edges"] == 1, \
            "读回时不能偷偷补顶点把问题盖掉"
        assert "node:Ghost" not in loaded.nodes

    print("悬空边可见 [OK]\n")


# ============================================================
# F. 端到端
# ============================================================

def test_end_to_end_real_library():
    """测试真实知识库端到端"""
    print("=" * 60)
    print("测试 F1：真实知识库")
    print("=" * 60)

    qy = build_graph(save=False, verbose=True)
    stats = qy.stats()

    print()
    print(f"  顶点 {stats['node_total']}，边 {stats['edge_total']}")
    print(f"  按类型: {stats['nodes_by_type']}")
    print(f"  按关系: {stats['edges_by_relation']}")
    print()

    assert stats["node_total"] > 0, "真实库里应有已学过的 workflow"
    assert stats["dangling_edges"] == 0, \
        f"不该有悬空边，实际 {stats['dangling_edges']}"

    workflows = qy.workflows_using("KSampler")
    print(f"  用 KSampler 的 workflow: {workflows}")
    assert workflows, "sd1.5 的样本都用了 KSampler"

    missing = qy.nodes_without_cards()
    print(f"  缺知识卡节点: {len(missing)} 个")
    assert "KSampler" not in missing

    print()
    print("\n".join(qy.render().split("\n")[:12]))
    print()
    print("真实库端到端通过 [OK]\n")


def test_save_and_load_roundtrip_real():
    """测试真实图落盘再读回"""
    print("=" * 60)
    print("测试 F2：真实图存取")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        store = GraphStore(str(Path(tmp) / "graph.json"))

        qy = build_graph(store=store, save=True, verbose=False)
        before = qy.stats()

        loaded = load_graph(store)
        after = loaded.stats()

        print(f"  保存前 {before['node_total']} 顶点 / "
              f"{before['edge_total']} 边")
        print(f"  读回后 {after['node_total']} 顶点 / "
              f"{after['edge_total']} 边")

        assert after["node_total"] == before["node_total"]
        assert after["edge_total"] == before["edge_total"]

        # 读回后查询一致
        assert (
            loaded.workflows_using("KSampler")
            == qy.workflows_using("KSampler")
        )
        print(f"  {store.summary()}")

    print("真实图存取正确 [OK]\n")


def test_empty_graph_is_usable():
    """测试空图（没数据时也不该崩）"""
    print("=" * 60)
    print("测试 F3：空图")
    print("=" * 60)

    qy = GraphQuery(KnowledgeGraph())
    assert qy.workflows_using("KSampler") == []
    assert qy.nodes_of("任何东西") == []
    assert qy.patterns_of("任何东西") == []
    assert qy.problems_of("任何东西") == []
    assert qy.solutions_for("任何问题") == []
    assert qy.card_for("KSampler") is None
    assert qy.paths("a", "b") == []
    assert qy.neighborhood("a") == {}
    assert qy.nodes_without_cards() == []
    assert "没有" in qy.describe("KSampler")
    assert qy.render()

    builder = GraphBuilder(node_index={})
    g = builder.build([], [])
    assert g.stats()["node_total"] == 0

    print("空图可用 [OK]\n")


def test_unmatched_pattern_members_visible():
    """测试未匹配的模式成员可见（静默跳过会让 matches 边全是空的）"""
    print("=" * 60)
    print("测试 C9：未匹配成员可见")
    print("=" * 60)

    patterns = [
        make_pattern(
            "ghost_pattern",
            ["sd1.5/ghost.json", "sd1.5/basic.json"],
            ["KSampler"],
        ),
    ]
    builder = GraphBuilder(node_index=NODE_INDEX)
    g = builder.build([SAMPLE_RECORDS[0]], patterns)
    qy = GraphQuery(g)

    print(f"  未匹配: {builder.unmatched_members}")
    print(f"  匹配率: {builder.match_rate:.0%}")

    assert builder.unmatched_members == ["sd1.5/ghost.json"]
    assert abs(builder.match_rate - 0.5) < 0.01
    # 匹配上的那条照常连边
    assert qy.patterns_of("sd1.5/basic.json") == ["ghost_pattern"]
    # ghost 不该被凭空建出 workflow 顶点
    assert not g.has_node(nid(TYPE_WORKFLOW, "sd1.5/ghost.json"))
    # matches 边只有一条（给 basic），没有多连到谁
    match_edges = [
        e for e in g.edges if e.relation == REL_MATCHES
    ]
    print(f"  matches 边: {[qy.name_of(e.source) for e in match_edges]}")
    assert len(match_edges) == 1

    print("未匹配成员可见 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Knowledge Graph 模块测试")
    print("=" * 60 + "\n")

    # A 模型
    test_namespaced_ids()
    test_node_property_merge()

    # B 图核心
    test_edge_dedup()
    test_adjacency_index()
    test_remove_node_cleans_edges()
    test_dangling_edge_detected()

    # C Builder
    test_parse_issue()
    test_build_workflow_structure()
    test_build_problems()
    test_build_node_cards()
    test_build_patterns()
    test_co_occurrence_threshold()
    test_co_occurrence_size_cap()
    test_failed_record_excluded()
    test_unmatched_pattern_members_visible()

    # D 查询
    test_workflows_using()
    test_ambiguous_name_not_guessed()
    test_paths_multihop()
    test_nodes_without_cards()
    test_describe_and_render()

    # E 存储
    test_store_roundtrip()
    test_store_version_guard()
    test_store_exposes_dangling()

    # F 端到端
    test_end_to_end_real_library()
    test_save_and_load_roundtrip_real()
    test_empty_graph_is_usable()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()