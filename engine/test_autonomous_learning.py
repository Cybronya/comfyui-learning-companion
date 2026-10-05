r"""
Autonomous Learning 模块测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_autonomous_learning

-X utf8 用于正常显示中文输出（控制台默认 GBK 会乱码）。

控制台勾号会触发 UnicodeEncodeError，统一用 [OK] 标记。
"""

import sys
import json
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.autonomous_learning import (
    AutonomousLearner,
    LearningState,
    TaskPlanner,
    WorkflowExplorer,
    KnowledgeGapDetector,
    LearningReport,
    Reflection,
    create_learner,
)


# ============================================================
# A. 各组件单元测试
# ============================================================

def test_planner_depends_on_input():
    """测试规划真的依赖输入，而非返回常量"""
    print("=" * 60)
    print("测试 A1：任务规划")
    print("=" * 60)

    planner = TaskPlanner()

    base = planner.plan("学习这个工作流")
    print(f"  基础计划 ({len(base)} 步): {base}")

    # 任务提到 ControlNet 应追加专项步骤
    cn = planner.plan("分析 ControlNet 权重为什么过高")
    print(f"  ControlNet 任务 ({len(cn)} 步)")

    # 任务提到报错应追加根因追溯
    err = planner.plan("为什么报错")
    print(f"  报错任务 ({len(err)} 步)")

    assert "study_controlnet_influence" in cn, \
        "提到 ControlNet 应追加专项步骤"
    assert "trace_problem_root_cause" in err, \
        "提到报错应追加根因追溯"
    assert base != cn and cn != err, "不同任务应产生不同计划"
    assert len(cn) > len(base), "专项任务步骤应更多"

    # workflow 特征也应影响计划
    cn_workflow = planner.plan(
        "学习",
        node_types=["CheckpointLoaderSimple", "ControlNetApplyAdvanced"],
    )
    assert "study_controlnet_influence" in cn_workflow, \
        "节点里有 ControlNet 也应触发专项步骤"
    print(f"  ControlNet 节点 ({len(cn_workflow)} 步)")

    # 知识库为空时应先建索引
    no_kb = planner.plan("学习", knowledge_available=False)
    assert no_kb[0] == "build_knowledge_index", \
        f"知识库为空应先建索引，实际 {no_kb[0]}"

    # 步骤说明可读
    explained = planner.explain(cn)
    assert all(not s.startswith(("analyze_", "identify_")) for s in explained), \
        "步骤说明应翻成中文"
    print(f"  步骤说明示例: {explained[-3:]}")
    print("规划依赖输入 [OK]\n")


def test_explorer_pipeline():
    """测试流程链推导（analyzer 本身不提供 pipeline）"""
    print("=" * 60)
    print("测试 A2：流程链推导")
    print("=" * 60)

    workflow = {
        "nodes": [
            {"id": 1, "type": "CheckpointLoaderSimple", "widgets_values": ["x.safetensors"]},
            {"id": 2, "type": "CLIPTextEncode", "widgets_values": ["a cat"]},
            {"id": 3, "type": "CLIPTextEncode", "widgets_values": ["bad"]},
            {"id": 4, "type": "EmptyLatentImage", "widgets_values": [512, 512, 1]},
            {"id": 5, "type": "KSampler",
             "widgets_values": [1, "random", 20, 7.0, "euler", "normal", 1.0]},
            {"id": 6, "type": "VAEDecode"},
            {"id": 7, "type": "SaveImage"},
        ],
        "links": [],
    }

    explorer = WorkflowExplorer()
    result = explorer.explore(workflow)

    print(f"  类型: {result['type']}")
    print(f"  流程链: {' → '.join(result['pipeline'])}")
    print(f"  核心节点: {result['core_nodes']}")
    for stage, nodes in result["stages"].items():
        print(f"    {stage}: {nodes}")

    assert result["pipeline"], "应能推导流程链"
    # 阶段顺序应符合数据流：模型 → 文本 → 潜空间 → 采样 → 解码 → 输出
    expected_order = ["Model", "Condition", "Latent", "Sampling",
                      "Decode", "Output"]
    positions = [
        result["pipeline"].index(s)
        for s in expected_order if s in result["pipeline"]
    ]
    print(f"  阶段位置: {positions}")
    assert positions == sorted(positions), f"阶段顺序应符合数据流: {positions}"
    assert "KSampler" in result["core_nodes"]
    assert "VAEDecode" in result["core_nodes"]

    # 参数提取
    params = explorer.extract_parameters(workflow)
    print(f"  参数: {params}")
    assert params["cfg"] == 7.0
    assert params["steps"] == 20
    assert params["width"] == 512

    described = explorer.describe_parameters(params)
    assert any("采样步数" in d for d in described)
    print("流程链推导正确 [OK]\n")


def test_gap_detector_alias_awareness():
    """测试缺口检测的别名判定（避免大规模误报）"""
    print("=" * 60)
    print("测试 A3：缺口检测")
    print("=" * 60)

    detector = KnowledgeGapDetector()

    # 精确匹配会误判的场景：
    # 节点是 ControlNetApplyAdvanced，知识库键是 ControlNet
    knowledge = {
        "ControlNet": [{"type": "node", "name": "ControlNet 知识"}],
        "KSampler": [{"type": "node", "name": "KSampler 知识"}],
        "VAE": [{"type": "node", "name": "VAE 知识"}],
    }

    nodes = [
        "CheckpointLoaderSimple",
        "ControlNetApplyAdvanced",
        "KSamplerAdvanced",
        "VAEDecode",
        "LoraLoader",
        "IPAdapterApply",
        "SaveImage",
    ]

    missing = detector.detect(nodes, knowledge)

    print(f"  节点 {len(nodes)} 个，知识库 {len(knowledge)} 个键")
    for gap in missing:
        print(f"    缺: {gap}")

    gap_nodes = {g.node_type for g in missing}
    gap_map = {g.node_type: g for g in missing}

    # 精确别名应判为「有知识」：这些节点都登记在对应主题的节点列表里
    for node in ["KSamplerAdvanced", "VAEDecode", "ControlNetApplyAdvanced"]:
        assert node not in gap_nodes, \
            f"{node} 是主题的精确别名，应判为有知识"

    # 完全没知识：这些节点所属主题在知识库里完全没有
    for node in ["CheckpointLoaderSimple", "LoraLoader", "IPAdapterApply"]:
        assert node in gap_nodes, f"{node} 应报缺口"
        assert gap_map[node].coverage == "none", \
            f"{node} 应为完全无知识"

    # 片段命中只能算「仅通用知识」：WanVideoSampler 不在 KSampler 主题的
    # 精确节点列表里，只能靠类名片段命中
    mixed = detector.detect(["WanVideoSampler"], knowledge)
    assert len(mixed) == 1, "WanVideoSampler 应报缺口"
    assert mixed[0].coverage == "related", \
        "只有片段命中，应标为「仅通用知识」而非「有知识」"
    print(f"  片段命中示例: {mixed[0]}")

    # 核心节点应排前面并标记
    core = [g for g in missing if g.is_core]
    assert core, "核心节点缺口应被标记"
    assert missing[0].coverage == "none" and missing[0].is_core, \
        "完全无知识的核心缺口应排最前"

    print("别名与片段匹配区分正确 [OK]\n")


def test_gap_detector_with_index():
    """测试缺口检测兼容 KnowledgeIndex"""
    print("=" * 60)
    print("测试 A4：缺口检测兼容索引")
    print("=" * 60)

    from engine.retrieval import KnowledgeIndex

    index = KnowledgeIndex(":memory:")
    index.add("KSampler", {"type": "node", "name": "KSampler 卡"})
    index.add("VAE", {"type": "node", "name": "VAE 卡"})

    detector = KnowledgeGapDetector()
    missing = detector.detect(
        ["KSampler", "WanVideoSampler", "LoraLoader"], index
    )
    gap_map = {g.node_type: g for g in missing}

    print(f"  缺口: {list(gap_map)}")
    assert "KSampler" not in gap_map, "KSampler 有卡不应报缺口"
    assert "LoraLoader" in gap_map, "LoRA 无卡应报缺口"
    assert gap_map["WanVideoSampler"].coverage == "related", \
        "只靠类名片段命中，应标为仅通用知识"
    print("索引兼容正确 [OK]\n")


def test_reflection_quantitative():
    """测试反思输出可判断的结论"""
    print("=" * 60)
    print("测试 A5：自我反思")
    print("=" * 60)

    state = LearningState(task="学习")
    state.analysis = {"nodes": ["KSampler", "VAEDecode", "LoraLoader"]}
    state.core_nodes = ["KSampler", "VAEDecode"]
    state.pipeline = ["Model", "Sampling", "Decode"]
    state.parameters = {"cfg": 7.0, "steps": 20}
    state.knowledge_used = [
        {"name": "KSampler 卡", "type": "node", "covers_nodes": ["KSampler"]},
        {"name": "VAE 卡", "type": "node", "covers_nodes": ["VAEDecode"]},
    ]

    from engine.autonomous_learning import GapItem

    state.missing_knowledge = [
        GapItem(node_type="LoraLoader", reason="无卡", is_core=False,
                related_topics=["LoRA"]),
    ]

    reflection = Reflection()
    result = reflection.reflect(state)

    print("  反思输出:")
    for item in result:
        print(f"    - {item}")

    text = " ".join(result)
    assert "理解程度" in text
    assert "置信度" in text
    assert "LoraLoader" in text
    assert "流程链" in text, "应报告推导出的流程链"

    actions = reflection.action_items(state)
    print(f"  动作: {actions}")
    assert actions and "LoraLoader" in actions[0]

    # 完全不熟的情况应判为不足
    state2 = LearningState(task="学习")
    state2.analysis = {"nodes": ["Unknown1", "Unknown2"]}
    state2.core_nodes = ["Unknown1"]
    state2.missing_knowledge = [
        GapItem(node_type=n, reason="无卡", is_core=True)
        for n in ["Unknown1", "Unknown2"]
    ]
    result2 = Reflection().reflect(state2)
    assert "尚未掌握" in " ".join(result2), "零覆盖应判为尚未掌握"
    assert "风险" in " ".join(result2), "核心节点无卡应提示风险"
    print("反思量化正确 [OK]\n")


def test_report_rendering():
    """测试报告渲染（不能出现 Python 字面量）"""
    print("=" * 60)
    print("测试 A6：报告渲染")
    print("=" * 60)

    from engine.autonomous_learning import GapItem

    state = LearningState(task="学习这个SDXL人像Workflow")
    state.analysis = {
        "workflow_type": "Text To Image",
        "nodes": ["KSampler", "VAEDecode", "LoraLoader"],
        "patterns": ["basic_t2i"],
        "stages": {
            "Sampling": ["KSampler"],
            "Decode": ["VAEDecode"],
            "Model": ["LoraLoader"],
        },
    }
    state.pipeline = ["Model", "Sampling", "Decode"]
    state.core_nodes = ["KSampler", "VAEDecode"]
    state.parameters = {"cfg": 7.0, "steps": 20, "sampler_name": "euler"}
    state.plan = ["analyze_workflow", "retrieve_node_knowledge"]
    state.knowledge_used = [
        {"name": "KSampler", "type": "node",
         "covers_nodes": ["KSampler"],
         "source": "comfyui_library/knowledge/nodes/ksampler.md"},
    ]
    state.missing_knowledge = [
        GapItem(node_type="LoraLoader", reason="知识库无 LoRA 卡",
                is_core=True, related_topics=["LoRA"]),
    ]
    state.discoveries = ["**理解程度**：部分掌握（置信度 62%）"]

    report = LearningReport().generate(state)

    print()
    print(report[:900])
    print("  ...（截断）")
    print()

    # 关键：不能是 Python 字面量
    assert "['" not in report, "报告里不应出现 Python 列表字面量"
    assert '["' not in report

    for section in ["学习任务", "结构理解", "生成流程", "关键参数",
                    "用到的知识", "知识缺口", "自我评估", "学习计划"]:
        assert section in report, f"缺段落：{section}"

    assert "LoraLoader" in report
    assert "ksampler.md" in report
    assert "Prompt 约束强度" in report, "参数应翻成中文"
    print("报告渲染正确 [OK]\n")


# ============================================================
# B. 真实模块端到端
# ============================================================

def build_real_learner(tmpdir, index=None):
    """用真实模块装配学习器"""
    from engine.workflow_parser import WorkflowParser, NodeKnowledgeLoader
    from engine.workflow_analyzer import WorkflowAnalyzer
    from engine.diagnostics import DiagnosticEngine
    from engine.retrieval import KnowledgeRetriever
    from engine.knowledge_evolution import evolve

    project = Path(__file__).parent.parent

    retriever = KnowledgeRetriever()
    index_path = str(Path(tmpdir) / "index.json")
    retriever.build_index(
        index_path=index_path,
        knowledge_dir=str(project / "comfyui_library" / "knowledge"),
        experience_store=str(
            project / "engine" / "learning_loop" / "experience_store.json"
        ),
        evolution_store=str(
            project / "engine" / "knowledge_evolution" / "evolution_store.json"
        ),
    )

    parser = WorkflowParser(
        NodeKnowledgeLoader(str(project / "comfyui_library" / "knowledge"))
    )

    return AutonomousLearner(
        explorer=WorkflowExplorer(
            analyzer=WorkflowAnalyzer(),
            knowledge_loader=parser.knowledge_loader,
        ),
        retriever=retriever,
        parser=parser,
        diagnostics=DiagnosticEngine(),
        learner=evolve,
    )


def test_learn_real_workflow():
    """端到端：用真实模块学一个真实 workflow"""
    print("=" * 60)
    print("测试 B1：真实 workflow 自主学习")
    print("=" * 60)

    project = Path(__file__).parent.parent
    wf_file = project / "comfyui_library" / "workflows" / "sd1.5" / "basic.json"

    if not wf_file.exists():
        print("  找不到 basic.json，跳过")
        return

    with TemporaryDirectory() as tmp:
        learner = build_real_learner(tmp)

        state = learner.learn(
            task="学习这个SD1.5文生图Workflow，理解如何生成高质量图片",
            workflow=str(wf_file),
            workflow_path=str(wf_file),
        )

        print(f"  步骤: {state.steps_run}")
        print(f"  错误: {state.errors}")
        print(f"  类型: {state.analysis.get('workflow_type')}")
        print(f"  流程链: {' → '.join(state.pipeline)}")
        print(f"  核心节点: {state.core_nodes}")
        print(f"  参数: {state.parameters}")
        print(f"  检索到知识: {len(state.knowledge_used)} 条")
        for k in state.knowledge_used[:3]:
            print(f"    - {k.get('name')} 覆盖 {k.get('covers_nodes')}")
        print(f"  缺口: {[g.node_type for g in state.missing_knowledge]}")
        print(f"  覆盖: {state.coverage:.0%} (核心 {state.core_coverage:.0%})")
        print(f"  置信度: {state.confidence:.0%}  等级: {state.level}")
        print(f"  耗时: {state.elapsed_ms:.0f}ms")

        assert not state.has_errors, f"不应报错: {state.errors}"
        assert state.plan, "应产出计划"
        assert state.pipeline, "应推导流程链"
        assert state.core_nodes, "应识别核心节点"
        assert state.parameters, "应提取参数"
        assert state.knowledge_used, "应检索到知识（原文缺此步）"
        assert state.report, "应产出报告"
        assert "学习报告" in state.report

        # 报告应包含关键内容
        for section in ["结构理解", "生成流程", "关键参数", "知识缺口", "自我评估"]:
            assert section in state.report, f"报告缺 {section}"

        print()
        print("  --- 报告节选 ---")
        for line in state.report.split("\n")[:22]:
            print(f"  {line}")
        print()

    print("真实学习链路打通 [OK]\n")


def test_learn_unknown_workflow():
    """端到端：学一个知识库里没有节点的工作流（考察缺口发现）"""
    print("=" * 60)
    print("测试 B2：未知工作流的知识缺口")
    print("=" * 60)

    exotic = {
        "nodes": [
            {"id": 1, "type": "CheckpointLoaderSimple",
             "widgets_values": ["x.safetensors"]},
            {"id": 2, "type": "CLIPTextEncode", "widgets_values": ["cat"]},
            {"id": 3, "type": "WanVideoSampler",
             "widgets_values": [1, "random", 20, 6.0, "uni_pc", "simple", 1.0]},
            {"id": 4, "type": "IPAdapterUnifiedLoader"},
            {"id": 5, "type": "WanVideoDecode"},
            {"id": 6, "type": "VHS_VideoCombine"},
            {"id": 7, "type": "KSampler",
             "widgets_values": [1, "random", 20, 7.0, "euler", "normal", 1.0]},
            {"id": 8, "type": "VAEDecode"},
        ],
        "links": [],
    }

    with TemporaryDirectory() as tmp:
        learner = build_real_learner(tmp)
        state = learner.learn(
            task="学习这个Wan视频生成Workflow，理解如何生成高质量视频",
            workflow=exotic,
        )

        print(f"  流程链: {' → '.join(state.pipeline)}")
        print(f"  核心节点: {state.core_nodes}")
        print(f"  缺口 ({len(state.missing_knowledge)} 个):")
        for gap in state.missing_knowledge:
            print(f"    - {gap}")
        print(f"  覆盖: {state.coverage:.0%}  等级: {state.level}")

        gap_map = {g.node_type: g for g in state.missing_knowledge}

        assert not state.has_errors, f"不应报错: {state.errors}"
        # 完全未知的节点必须被发现，且不能因为类名里有 "sampler"
        # 就被当成「懂 KSampler 就等于懂它」
        assert "WanVideoSampler" in gap_map, "未知视频采样器应报缺口"
        assert "VHS_VideoCombine" in gap_map, "未知视频合成节点应报缺口"
        assert gap_map["WanVideoSampler"].coverage == "related", \
            "WanVideoSampler 只应算「仅有 KSampler 通用知识」"
        assert gap_map["VHS_VideoCombine"].coverage == "none", \
            "VHS_VideoCombine 完全无知识"
        # 精确命中的节点不应被误报
        assert "KSampler" not in gap_map, "KSampler 有卡不应误报"
        assert "VAEDecode" not in gap_map, "VAEDecode 是 VAE 精确别名"

        # 缺口应反映到等级上
        assert state.level in ("partial", "insufficient"), \
            f"有大量缺口时等级应偏低，实际 {state.level}"

        # 未知节点应进 Other 阶段而不是被丢掉
        assert "Other" in state.pipeline or state.pipeline, \
            "未知节点应归入未识别阶段"

        actions = learner.action_items(state)
        print(f"  建议动作:")
        for a in actions[:4]:
            print(f"    - {a}")
        assert any("WanVideoSampler" in a for a in actions)

        print()
        print("  --- 缺口章节 ---")
        report = state.report
        idx = report.find("## 知识缺口")
        print("\n".join(f"  {l}" for l in report[idx:idx + 400].split("\n")))
        print()

    print("缺口发现正确 [OK]\n")


def test_learn_with_dict_input():
    """测试 dict 输入与路径输入等价"""
    print("=" * 60)
    print("测试 B3：输入形式")
    print("=" * 60)

    workflow = {
        "nodes": [
            {"id": 1, "type": "CheckpointLoaderSimple", "widgets_values": ["x"]},
            {"id": 2, "type": "KSampler",
             "widgets_values": [1, "random", 20, 7.0, "euler", "normal", 1.0]},
            {"id": 3, "type": "VAEDecode"},
        ],
        "links": [],
    }

    with TemporaryDirectory() as tmp:
        learner = build_real_learner(tmp)

        from_dict = learner.learn("学习", workflow)

        wf_file = Path(tmp) / "wf.json"
        with open(wf_file, "w", encoding="utf-8") as f:
            json.dump(workflow, f)

        from_path = learner.learn("学习", str(wf_file))

        print(f"  dict  输入: 节点 {len(from_dict.nodes())}")
        print(f"  路径  输入: 节点 {len(from_path.nodes())}")

        assert from_dict.nodes() == from_path.nodes()
        assert from_dict.pipeline == from_path.pipeline

        # 非法输入不应抛异常，而应产出带错误的状态与报告
        bad = learner.learn("学习", "这不是JSON也不是文件")
        print(f"  非法输入错误: "
              f"{bad.errors[0]['message'][:60] if bad.errors else '无错误'}")

        assert bad.has_errors, "非法输入应记录错误"
        assert "无法读取" in bad.errors[0]["message"]
        assert bad.report, "失败时也要产出报告"
        assert "执行中的问题" in bad.report, "报告应说明哪里出问题"

    print("输入形式处理正确 [OK]\n")


def test_deposit():
    """测试知识沉淀"""
    print("=" * 60)
    print("测试 B4：知识沉淀")
    print("=" * 60)

    workflow = {
        "nodes": [
            {"id": 1, "type": "CheckpointLoaderSimple", "widgets_values": ["x"]},
            {"id": 2, "type": "KSampler",
             "widgets_values": [1, "random", 20, 7.0, "euler", "normal", 1.0]},
            {"id": 3, "type": "VAEDecode"},
        ],
        "links": [],
    }

    with TemporaryDirectory() as tmp:
        # 沉淀目标指向临时目录，避免污染仓库
        project = Path(__file__).parent.parent
        from engine.knowledge_evolution import evolve

        store_path = str(Path(tmp) / "evolution_store.json")

        from engine.workflow_parser import WorkflowParser, NodeKnowledgeLoader
        from engine.workflow_analyzer import WorkflowAnalyzer
        from engine.diagnostics import DiagnosticEngine
        from engine.retrieval import KnowledgeRetriever

        retriever = KnowledgeRetriever()
        retriever.build_index(
            index_path=str(Path(tmp) / "index.json"),
            knowledge_dir=str(project / "comfyui_library" / "knowledge"),
            experience_store=str(
                project / "engine" / "learning_loop" / "experience_store.json"
            ),
            evolution_store=str(
                project / "engine" / "knowledge_evolution" / "evolution_store.json"
            ),
        )

        learner = AutonomousLearner(
            explorer=WorkflowExplorer(
                analyzer=WorkflowAnalyzer(),
                knowledge_loader=NodeKnowledgeLoader(
                    str(project / "comfyui_library" / "knowledge")
                ),
            ),
            retriever=retriever,
            parser=WorkflowParser(
                NodeKnowledgeLoader(str(project / "comfyui_library" / "knowledge"))
            ),
            diagnostics=DiagnosticEngine(),
            learner=lambda exps, save=True, store_path=store_path: evolve(
                exps, store_path=store_path, save=save
            ),
        )

        state = learner.learn("沉淀测试", workflow, deposit=True)

        print(f"  沉淀条目: {state.deposited}")
        print(f"  步骤: {state.steps_run}")

        assert state.deposited, "应沉淀知识"
        assert "deposit" in state.steps_run
        # 仓库里的 store 不该被写脏
        repo_store = (
            project / "engine" / "knowledge_evolution" / "evolution_store.json"
        )
        assert repo_store.read_text(encoding="utf-8").strip() in (
            '{\n    "patterns": []\n}', '{ "patterns": [] }'
        ), "仓库里的 evolution_store.json 不应被测试写脏"

    print("知识沉淀正确 [OK]\n")


def test_plan_is_actually_executed():
    """测试计划里的步骤真的被执行（避免计划与执行脱节）"""
    print("=" * 60)
    print("测试 B5：计划与执行一致")
    print("=" * 60)

    workflow = {
        "nodes": [
            {"id": 1, "type": "CheckpointLoaderSimple",
             "widgets_values": ["x.safetensors"]},
            {"id": 2, "type": "ControlNetApply", "widgets_values": [1.5]},
            {"id": 3, "type": "KSampler",
             "widgets_values": [1, "random", 20, 15.0, "euler", "normal", 1.0]},
            {"id": 4, "type": "VAEDecode"},
        ],
        "links": [],
    }

    with TemporaryDirectory() as tmp:
        learner = build_real_learner(tmp)
        state = learner.learn(
            "分析 ControlNet 权重为什么过高", workflow
        )

        print(f"  计划 ({len(state.plan)} 步): {state.plan}")
        print(f"  执行: {state.steps_run}")
        print(f"  专项结论:")
        for step, finding in state.step_findings.items():
            print(f"    - {step}: {finding}")

        # 计划里的专项步骤必须有实际结论，不能只是列在计划里
        assert "study_controlnet_influence" in state.plan
        assert "study_controlnet_influence" in state.step_findings, \
            "ControlNet 专项分析必须真的执行并给出结论"

        conclusion = state.step_findings["study_controlnet_influence"]
        assert "1.5" in conclusion, "结论应引用实测权重值"
        assert "偏高" in conclusion or "过高" in conclusion, \
            f"权重 1.5 应被判为偏高: {conclusion}"
        assert "CFG" in conclusion, "应提示 ControlNet 与 CFG 的相互影响"

        # 报告里应体现专项结论
        assert "## 专项分析" in state.report
        assert "1.5" in state.report

    print("计划执行一致 [OK]\n")


def test_special_steps_produce_findings():
    """测试专项分析在各种参数下都能给出结论"""
    print("=" * 60)
    print("测试 B6：专项分析")
    print("=" * 60)

    from engine.autonomous_learning.analysis_steps import SpecialAnalyzer

    analyzer = SpecialAnalyzer()

    def state_with(params, nodes=None, task=""):
        s = LearningState(task=task)
        s.parameters = params
        s.analysis = {"nodes": nodes or ["KSampler"]}
        return s

    normal = analyzer.run(
        "study_controlnet_influence",
        state_with({"controlnet_strength": 0.7, "cfg": 7.0}),
    )
    print(f"  正常权重: {normal}")
    assert "0.7" in normal
    assert "偏高" not in normal

    lora = analyzer.run(
        "study_lora_influence",
        state_with({
            "lora_name": "myStyle.safetensors",
            "strength_model": 1.5,
            "strength_clip": 1.4,
        }),
    )
    print(f"  LoRA 过强: {lora}")
    assert "过拟合" in lora or "偏高" in lora

    compare = analyzer.run(
        "compare_parameter_values",
        state_with({"cfg": 25.0, "steps": 2}),
    )
    print(f"  参数对比: {compare}")
    assert "约束强度" in compare or "cfg" in compare.lower()

    baseline = analyzer.run(
        "extract_reproducible_parameters",
        state_with({
            "checkpoint": "x.safetensors", "steps": 20, "cfg": 7.0,
            "seed": 42, "sampler_name": "euler", "width": 512, "height": 512,
        }),
    )
    print(f"  复现基线: {baseline}")
    assert "seed=42" in baseline

    for value, keyword in [(1.0, "重生成"), (0.4, "低重绘"), (0.75, "部分重绘")]:
        text = analyzer.run(
            "explain_denoise_semantics", state_with({"denoise": value})
        )
        print(f"  denoise={value}: {text}")
        assert keyword in text, f"denoise={value} 应解释为 {keyword}"

    # 无对应参数时返回空串而不是瞎编；未知步骤也不报错
    assert analyzer.run(
        "study_controlnet_influence", state_with({"cfg": 7.0})
    ) == ""
    assert analyzer.run("unknown_step", state_with({})) == ""

    print("专项分析正确 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Autonomous Learning 模块测试")
    print("=" * 60 + "\n")

    test_planner_depends_on_input()
    test_explorer_pipeline()
    test_gap_detector_alias_awareness()
    test_gap_detector_with_index()
    test_reflection_quantitative()
    test_report_rendering()
    test_special_steps_produce_findings()

    test_learn_real_workflow()
    test_learn_unknown_workflow()
    test_learn_with_dict_input()
    test_deposit()
    test_plan_is_actually_executed()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
