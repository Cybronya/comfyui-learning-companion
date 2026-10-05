r"""
Knowledge Retrieval 模块测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -m engine.test_retrieval

控制台在中文 Windows 下是 GBK 编码，勾号会触发 UnicodeEncodeError，
因此统一用 [OK] / [FAIL] 这类 ASCII 标记。
"""

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.retrieval import (
    KnowledgeRetriever,
    KnowledgeIndex,
    KnowledgeMatcher,
    KnowledgeRanker,
)


def test_dict_knowledge_base():
    """对齐设计文档第九节：dict 形式知识库 + retrieve"""
    print("=" * 60)
    print("测试 1：dict 知识库检索（设计文档预期输出）")
    print("=" * 60)

    knowledge = {
        "ControlNet": [
            {
                "type": "node",
                "node": "ControlNet",
                "content": "ControlNet weight通常0.5-0.8",
            }
        ],
        "KSampler": [
            {
                "type": "node",
                "node": "KSampler",
                "content": "CFG影响Prompt控制强度",
            }
        ],
    }

    retriever = KnowledgeRetriever(knowledge)
    result = retriever.retrieve(
        "ControlNet效果太强怎么办",
        {"workflow_nodes": ["ControlNet"]},
    )

    for item in result:
        print(f"  type={item['type']}  node={item.get('node')}  "
              f"score={item.get('score')}")

    assert len(result) == 1, f"应只召回 ControlNet 一条，实际 {len(result)}"
    assert result[0]["type"] == "node"
    assert result[0]["node"] == "ControlNet"
    assert result[0]["content"] == "ControlNet weight通常0.5-0.8"
    print("输出与设计文档一致 [OK]\n")


def test_matcher_chinese_and_english():
    """测试中英文混排的主题识别"""
    print("=" * 60)
    print("测试 2：主题匹配")
    print("=" * 60)

    matcher = KnowledgeMatcher()

    cases = [
        ("ControlNet效果太强怎么办", "ControlNet"),
        ("为什么人物脸崩", None),          # 多主题，顺序不定
        ("CFG 是不是太高了", "KSampler"),
        ("vae 解码有问题", "VAE"),
        ("这个 lora 风格不对", "LoRA"),
        ("分辨率怎么调", "Resolution"),
        ("保存图片报错", "SaveImage"),
    ]

    for text, expected in cases:
        topics = matcher.match(text)
        flag = "" if expected is None else ("  [OK]" if expected in topics else "  [FAIL]")
        print(f"  {text!r} -> {topics}{flag}")
        if expected:
            assert expected in topics, f"{text} 应命中 {expected}"

    # 「脸崩」字面只命中 KSampler，但成因不止一个 —— 症状扩展在 ranker 层做
    face_topics = matcher.match("为什么人物脸崩")
    expanded = KnowledgeRanker().symptom_topics("为什么人物脸崩")
    print(f"  脸崩 字面命中: {face_topics}")
    print(f"  脸崩 症状扩展: {expanded}")

    assert face_topics == ["KSampler"], "字面应只命中 KSampler"
    assert set(expanded) == {"KSampler", "LoRA", "VAE"}, \
        "症状扩展应覆盖 LoRA 与 VAE 两种可能成因"
    print("中英文混排 + 症状扩展 [OK]\n")


def test_symptom_multi_cause_recall():
    """测试症状跨主题召回：脸崩应同时召回 LoRA / VAE 相关知识"""
    print("=" * 60)
    print("测试 2b：症状多成因召回")
    print("=" * 60)

    knowledge = {
        "KSampler": [
            {"type": "node", "node": "KSampler", "name": "CFG 影响控制强度",
             "content": "CFG 过高会过度约束"}
        ],
        "LoRA": [
            {"type": "node", "node": "LoraLoader", "name": "LoRA 权重",
             "content": "权重过高会过拟合"}
        ],
        "VAE": [
            {"type": "node", "node": "VAEDecode", "name": "VAE 解码",
             "content": "解码异常导致色偏"}
        ],
    }

    retriever = KnowledgeRetriever(knowledge)
    result = retriever.retrieve("为什么人物脸崩", {})

    print(f"  召回 {len(result)} 条:")
    for item in result:
        print(f"    - {item['name']}  score={item.get('score')}  "
              f"type={item['type']}")

    names = " ".join(i["name"] for i in result)
    assert len(result) == 3, f"脸崩应召回 3 个成因候选，实际 {len(result)}"
    assert "CFG" in names
    assert "LoRA" in names
    assert "VAE" in names

    # 条目应带命中原因，便于回答时说明
    assert any(i.get("match_reasons") for i in result)
    print("症状多成因召回 [OK]\n")


def test_matcher_node_aliases():
    """测试节点类型别名反查"""
    print("=" * 60)
    print("测试 3：节点别名")
    print("=" * 60)

    matcher = KnowledgeMatcher()

    for node in [
        "ControlNetApply",
        "ControlNetApplyAdvanced",
        "ControlNetLoaderModelOnly",
    ]:
        topics = matcher.topics_for_node(node)
        assert "ControlNet" in topics, f"{node} 应归入 ControlNet 主题"
        print(f"  {node} -> {topics}  [OK]")

    # KSampler 系同理
    assert "KSampler" in matcher.topics_for_node("KSamplerAdvanced")

    # 未登记的变体靠类名片段兜底
    assert "ControlNet" in matcher.topics_for_node("MyControlNetHelper")

    # 索引关键词应同时含节点名与主题名
    keywords = matcher.index_keywords_for_node("ControlNetApplyAdvanced")
    assert "ControlNetApplyAdvanced" in keywords
    assert "ControlNet" in keywords
    print(f"  索引关键词: {keywords}")
    print("节点别名处理 [OK]\n")


def test_ranking():
    """测试排序逻辑"""
    print("=" * 60)
    print("测试 4：排序")
    print("=" * 60)

    ranker = KnowledgeRanker()

    items = [
        {
            "type": "node",
            "node": "LoraLoader",
            "name": "LoRA 知识",
            "content": "不在当前工作流里",
        },
        {
            "type": "node",
            "node": "ControlNetApply",
            "name": "ControlNet 知识",
            "content": "在当前工作流里",
        },
        {
            "type": "evolution_knowledge",
            "name": "ControlNet 增强流程",
            "nodes": ["ControlNetApply"],
            "content": "多经验统计",
        },
    ]

    ranked = ranker.rank(
        items,
        {"workflow_nodes": ["ControlNetApply", "KSampler"]},
        "ControlNet 为什么太强",
    )

    for i, item in enumerate(ranked, 1):
        print(f"  {i}. score={item['score']:>5}  {item['name']}  "
              f"({item['type']})")

    # 演化知识 + 当前工作流命中 → 应排最前
    assert ranked[0]["type"] == "evolution_knowledge"
    assert ranked[0]["score"] == 15.0, f"实际 {ranked[0]['score']}"
    # 其次是当前工作流里的静态节点卡（+10 工作流 +2 node 类型）
    assert ranked[1]["node"] == "ControlNetApply"
    assert ranked[1]["score"] == 12.0, f"实际 {ranked[1]['score']}"
    # 不在工作流里的 LoRA 应排最后
    assert ranked[-1]["node"] == "LoraLoader"
    assert ranked[-1]["score"] == 2.0, f"实际 {ranked[-1]['score']}"
    print("排序权重正确 [OK]\n")


def test_evolution_outranks_static():
    """测试演化知识优先于静态知识卡"""
    print("=" * 60)
    print("测试 5：演化知识优先级")
    print("=" * 60)

    ranker = KnowledgeRanker()
    items = [
        {"type": "node", "name": "KSampler 静态卡", "node": "KSampler"},
        {"type": "evolution_knowledge", "name": "SDXL ControlNet 模式"},
        {"type": "workflow_pattern", "name": "ControlNet 模式卡"},
    ]
    ranked = ranker.rank(items, {}, "")

    assert ranked[0]["type"] == "evolution_knowledge"
    assert ranked[1]["type"] == "workflow_pattern"
    assert ranked[2]["type"] == "node"
    print("演化知识 > Pattern 卡 > 静态节点卡 [OK]\n")


def test_fallback_by_workflow_nodes():
    """测试问题无关键词命中时的兜底"""
    print("=" * 60)
    print("测试 6：按工作流节点兜底")
    print("=" * 60)

    knowledge = {
        "ControlNet": [
            {
                "type": "node",
                "node": "ControlNetApply",
                "name": "ControlNet 知识",
                "content": "权重控制",
            }
        ],
    }

    retriever = KnowledgeRetriever(knowledge)
    # 问题里没有任何已知主题词
    result = retriever.retrieve(
        "这个东西怎么调",
        {"workflow_nodes": ["ControlNetApply"]},
    )

    print(f"  兜底召回: {[i['name'] for i in result]}")
    assert len(result) == 1, "无关键词时应按工作流节点兜底"
    assert result[0]["name"] == "ControlNet 知识"
    print("兜底召回正确 [OK]\n")


def test_dedup():
    """测试去重"""
    print("=" * 60)
    print("测试 7：跨关键词去重")
    print("=" * 60)

    knowledge = {
        "ControlNet": [
            {"type": "node", "node": "ControlNet", "name": "ControlNet 知识",
             "content": "x"}
        ],
        "controlnet": [
            {"type": "node", "node": "ControlNet", "name": "ControlNet 知识",
             "content": "x"}
        ],
    }

    retriever = KnowledgeRetriever(knowledge)
    # 匹配器对同一主题只返回一个 key，但大小写不同的键会被分别命中
    result = retriever.retrieve(
        "ControlNet 问题", {}
    )
    print(f"  召回条数: {len(result)}")
    assert len(result) == 1, f"重复条目应去重，实际 {len(result)}"
    print("去重正确 [OK]\n")


def test_index_persistence():
    """测试索引持久化"""
    print("=" * 60)
    print("测试 8：索引持久化")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = str(Path(tmp) / "retrieval_store.json")

        index = KnowledgeIndex(path)
        index.add("ControlNet", {"type": "node", "name": "卡 A", "node": "X"})
        index.add("ControlNet", {"type": "node", "name": "卡 B", "node": "Y"})
        index.add("ControlNet", {"type": "node", "name": "卡 A", "node": "X"})
        index.save()

        reloaded = KnowledgeIndex(path)
        items = reloaded.search("ControlNet")
        print(f"  关键词 ControlNet 下 {len(items)} 条（重复添加应去重）")

        assert len(items) == 2, "同名条目重复添加应被忽略"
        assert reloaded.size() == 2
        assert reloaded.search("不存在的关键词") == []
    print("持久化与去重 [OK]\n")


def test_build_index_from_real_knowledge():
    """测试从真实知识库构建索引"""
    print("=" * 60)
    print("测试 9：从 comfyui_library 构建真实索引")
    print("=" * 60)

    project = Path(__file__).parent.parent
    knowledge_dir = str(project / "comfyui_library" / "knowledge")

    if not Path(knowledge_dir).exists():
        print("  知识库目录不存在，跳过")
        return

    with TemporaryDirectory() as tmp:
        path = str(Path(tmp) / "retrieval_store.json")

        retriever = KnowledgeRetriever(auto_build=False)
        index = retriever.build_index(
            index_path=path,
            knowledge_dir=knowledge_dir,
            experience_store=str(
                project / "engine" / "learning_loop" / "experience_store.json"
            ),
            evolution_store=str(
                project / "engine" / "knowledge_evolution" / "evolution_store.json"
            ),
        )

        stats = retriever.stats()
        print(f"  关键词数: {stats['keyword_count']}")
        print(f"  知识条目数: {stats['knowledge_count']}")

        assert stats["keyword_count"] > 0, "应索引到关键词"
        assert stats["knowledge_count"] >= 6, "至少应索引到 6 张节点卡"

        # 真实检索：KSampler 相关问题
        result = retriever.retrieve(
            "CFG 太高会导致什么问题",
            {"workflow_nodes": ["KSampler", "CLIPTextEncode"]},
            limit=3,
        )
        print(f"  'CFG太高' 召回 {len(result)} 条:")
        for item in result:
            print(f"    - [{item['type']}] {item['name']} "
                  f"(score={item.get('score')})")

        assert len(result) > 0, "应召回 KSampler 相关知识"

        # 输出 prompt 文本
        text = retriever.format_for_prompt(result)
        assert len(text) > 0
        print(f"\n  --- format_for_prompt 前 5 行 ---")
        for line in text.split("\n")[:5]:
            print(f"  {line}")

        # 关键：知识卡的 node 字段必须是**真实节点类型**（PascalCase），
        # 不能是 snake_case 文件名 —— 否则 workflow_learning 的覆盖率统计
        # 会把「有卡」的节点算成没卡（实测覆盖率从 100% 掉到 14%）
        node_types = set()
        for items in index.index.values():
            for item in items:
                if item.get("type") == "node" and item.get("node"):
                    node_types.add(item["node"])

        expected = {
            "CheckpointLoaderSimple", "CLIPTextEncode",
            "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage",
        }
        found = expected & node_types
        print(f"  索引到的节点类型: {sorted(node_types)}")
        print(f"  匹配到 {len(found)}/{len(expected)} 个预期节点类型")

        assert found == expected, (
            f"节点类型未正确解析，缺少: {expected - node_types}"
            f"（疑似退化成 snake_case 文件名）"
        )

        # 元信息必须真的挂上（role / category / learning_topics）
        ksampler_items = [
            item for item in index.index.get("KSampler", [])
            if item.get("node") == "KSampler"
        ]
        assert ksampler_items, "KSampler 索引下应有条目"
        meta = ksampler_items[0]
        assert meta.get("role") == "sampler", \
            f"role 应来自 node_index.json，实际 {meta.get('role')!r}"
        assert meta.get("category"), "category 应来自 node_index.json"
        assert meta.get("learning_topics"), \
            "learning_topics 应来自 node_index.json"

    print("节点类型与元信息解析正确 [OK]\n")


def test_format_for_prompt():
    """测试 prompt 文本拼接"""
    print("=" * 60)
    print("测试 10：prompt 文本")
    print("=" * 60)

    retriever = KnowledgeRetriever({})
    assert "未检索到" in retriever.format_for_prompt([])

    text = retriever.format_for_prompt([
        {
            "type": "evolution_knowledge",
            "name": "SDXL ControlNet 模式",
            "content": "该Workflow属于ControlNet增强流程",
            "recommendations": ["ControlNet 权重建议 0.5-0.8"],
            "common_parameters": {"cfg": {"min": 6, "max": 9}},
            "match_reasons": ["当前工作流包含该节点"],
        }
    ])

    print(text)
    assert "SDXL ControlNet 模式" in text
    assert "0.5-0.8" in text
    assert "命中原因" in text
    print("prompt 拼接 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Knowledge Retrieval 模块测试")
    print("=" * 60 + "\n")

    test_dict_knowledge_base()
    test_matcher_chinese_and_english()
    test_symptom_multi_cause_recall()
    test_matcher_node_aliases()
    test_ranking()
    test_evolution_outranks_static()
    test_fallback_by_workflow_nodes()
    test_dedup()
    test_index_persistence()
    test_build_index_from_real_knowledge()
    test_format_for_prompt()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
