r"""
Agent Core 模块测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -m engine.test_agent_core

两部分：
    A. 用假模块验证编排逻辑（阶段顺序 / 错误隔离 / 配置开关 / 上下文拼装）
    B. 用真实模块端到端跑一次真实 workflow（这是第一次，
       此前九个模块各自的单测都过，但从未串起来跑过）

控制台在中文 Windows 下是 GBK 编码，勾号会触发 UnicodeEncodeError，
因此统一用 [OK] / [FAIL] 这类 ASCII 标记。
"""

import sys
import json
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.agent_core import (
    ComfyUIAgent,
    AgentState,
    create_agent,
    merge_config,
    stages_of,
    Stage,
    AgentPipeline,
)


# ============================================================
# A. 假模块：验证编排逻辑
# ============================================================

class FakeNode:
    def __init__(self, node_type):
        self.node_type = node_type


class FakeWorkflow:
    """模拟 WorkflowParser 返回的 WorkflowKnowledge"""
    def __init__(self, workflow_id="wf_1", task_type="text_to_image",
                 nodes=None, features=None):
        self.workflow_id = workflow_id
        self.task_type = task_type
        self.nodes = [FakeNode(n) for n in (nodes or [])]
        self.features = features or ["sampling"]


class FakeIssue:
    def __init__(self, severity, message, suggestion):
        self.severity = severity
        self.message = message
        self.suggestion = suggestion


class FakeReport:
    def __init__(self, issues):
        self.issues = issues


class FakeParser:
    def __init__(self):
        self.calls = []

    def parse(self, filepath):
        self.calls.append(("parse", filepath))
        return FakeWorkflow()

    def parse_data(self, data, workflow_id="<dict>"):
        self.calls.append(("parse_data", workflow_id))
        return FakeWorkflow(
            nodes=[n.get("type") for n in data.get("nodes", [])]
        )


class FakeAnalyzer:
    def __init__(self):
        self.include_graph_seen = None

    def analyze(self, workflow_json, include_graph=False):
        self.include_graph_seen = include_graph
        return {
            "nodes": ["KSampler", "ControlNetApply"],
            "workflow_type": "controlnet_workflow",
            "patterns": ["controlnet"],
            "graph": "<Graph object>",
        }


class FakeContext:
    def __init__(self):
        self.questions = []
        self.workflows = []

    def update_question(self, question, topic=""):
        self.questions.append((question, topic))

    def set_workflow(self, workflow):
        self.workflows.append(workflow)

    def get_context(self):
        return {"workflow": {"workflow_id": "wf_1"}, "conversation": {}}

    def get_retrieval_context(self):
        return {
            "workflow": {"workflow_id": "wf_1"},
            "conversation": {},
            "workflow_nodes": ["KSampler", "ControlNetApply"],
            "workflow_type": "text_to_image",
            "parameters": {},
        }


class FakeDiagnostics:
    def __init__(self):
        self.seen_graph = "<unset>"

    def analyze(self, workflow, graph):
        self.seen_graph = graph
        return FakeReport([
            FakeIssue("high", "ControlNet weight 1.5 偏高", "降到 0.6-0.8"),
        ])


class FakeRetriever:
    def __init__(self):
        self.seen_context = None
        self.seen_limit = None

    def retrieve(self, question, context, limit=0):
        self.seen_context = context
        self.seen_limit = limit
        return [
            {
                "type": "evolution_knowledge",
                "name": "ControlNet 模式",
                "content": "权重 0.5-0.8",
                "score": 15.0,
            }
        ]

    def format_for_prompt(self, items):
        return "\n".join(f"[{i['type']}] {i['name']}" for i in items)


class FakeGenerator:
    def __init__(self):
        self.seen_knowledge = None
        self.seen_context = None

    def generate(self, question, context, knowledge=None):
        self.seen_knowledge = knowledge
        self.seen_context = context
        return {"prompt": "<prompt>", "analysis": {"type": "sampler"}}


def build_fake_agent(**overrides):
    """构造装配了假模块的 Agent"""
    modules = {
        "parser": FakeParser(),
        "analyzer": FakeAnalyzer(),
        "context": FakeContext(),
        "diagnostics": FakeDiagnostics(),
        "retriever": FakeRetriever(),
        "generator": FakeGenerator(),
    }
    modules.update(overrides)
    return create_agent(**modules), modules


def test_stage_order():
    """测试阶段顺序"""
    print("=" * 60)
    print("测试 A1：阶段顺序")
    print("=" * 60)

    agent, mods = build_fake_agent()
    state = agent.ask("为什么 ControlNet 太强", {"nodes": [{"type": "KSampler"}]})

    print(f"  执行阶段: {state.stages_run}")
    assert state.stages_run == [
        "context", "parse", "analyze", "diagnose", "retrieve", "respond"
    ], f"实际 {state.stages_run}"
    assert not state.has_errors, f"不应有错误: {state.errors}"
    assert state.response["prompt"] == "<prompt>"
    print("阶段顺序正确 [OK]\n")


def test_workflow_input_normalization():
    """测试 workflow 输入归一化

    WorkflowParser.parse() 收路径而 WorkflowAnalyzer.analyze() 收 dict，
    Agent 层必须统一读一次，否则传路径时分析阶段会崩。
    """
    print("=" * 60)
    print("测试 A2：输入归一化")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_file = Path(tmp) / "wf.json"
        with open(wf_file, "w", encoding="utf-8") as f:
            json.dump(
                {"nodes": [{"type": "KSampler"}, {"type": "VAEDecode"}]},
                f,
            )

        agent, mods = build_fake_agent()

        # 传 dict
        state = agent.ask("问题", {"nodes": [{"type": "KSampler"}]})
        assert mods["parser"].calls[-1][0] == "parse_data", \
            "dict 应走 parse_data"

        # 传路径：Agent 先读成 dict，仍走 parse_data
        agent.ask("问题", str(wf_file))
        assert mods["parser"].calls[-1][0] == "parse_data", \
            "路径也应先归一化成 dict 再走 parse_data"
        print(f"  解析调用: {[c[0] for c in mods['parser'].calls]}")

        # 关键：路径输入时分析阶段不能崩
        state = agent.ask("问题", str(wf_file))
        assert not state.has_errors, f"路径输入不应报错: {state.errors}"
        assert state.workflow_analysis, "路径输入也应完成分析"
        assert state.workflow_nodes() == ["KSampler", "VAEDecode"]
        print(f"  解析出节点: {state.workflow_nodes()}")

        # 不存在的路径应被记为错误而不是崩掉整条链路
        state = agent.ask("问题", str(Path(tmp) / "nope.json"))
        assert state.has_errors
        assert state.errors[0]["stage"] == "load_workflow"
        print(f"  缺文件错误: {state.errors[0]['message']}")

    print("输入归一化正确 [OK]\n")


def test_graph_passed_to_diagnostics():
    """测试 graph 正确传给诊断"""
    print("=" * 60)
    print("测试 A3：graph 传递")
    print("=" * 60)

    agent, mods = build_fake_agent()
    agent.ask("问题", {"nodes": []})

    # analyzer 必须被要求带上 graph
    assert mods["analyzer"].include_graph_seen is True, \
        "analyze 应以 include_graph=True 调用"
    # 诊断拿到的应是 graph 而不是 None
    assert mods["diagnostics"].seen_graph == "<Graph object>", \
        f"诊断应收到 graph，实际 {mods['diagnostics'].seen_graph!r}"
    print("graph 传递正确 [OK]\n")


def test_retrieval_context_flat():
    """测试检索拿到扁平 workflow_nodes"""
    print("=" * 60)
    print("测试 A4：检索上下文")
    print("=" * 60)

    agent, mods = build_fake_agent()
    state = agent.ask("问题", {"nodes": [{"type": "KSampler"}]})

    ctx = mods["retriever"].seen_context
    print(f"  检索上下文键: {sorted(ctx.keys())}")
    print(f"  workflow_nodes: {ctx.get('workflow_nodes')}")

    # 排序器的 +10 加权依赖这个键，缺了就永远失效
    assert "workflow_nodes" in ctx, "检索上下文必须有 workflow_nodes"
    assert "workflow_type" in ctx
    print("检索上下文结构正确 [OK]\n")


def test_knowledge_injected_into_generator():
    """测试检索结果被喂给生成器"""
    print("=" * 60)
    print("测试 A5：知识注入生成器")
    print("=" * 60)

    agent, mods = build_fake_agent()
    agent.ask("为什么 ControlNet 太强", {"nodes": []})

    knowledge = mods["generator"].seen_knowledge
    context = mods["generator"].seen_context

    print(f"  注入知识: {knowledge!r}")
    print(f"  回答上下文键: {sorted(context.keys())}")

    assert knowledge and "ControlNet 模式" in knowledge, \
        "生成器应收到检索到的知识"
    # 诊断结论也要进上下文，否则 LLM 看不到问题在哪
    assert "diagnostics" in context, "回答上下文应含诊断结论"
    assert "analysis" in context
    assert any("weight 1.5" in line for line in context["diagnostics"])
    print("知识与诊断注入正确 [OK]\n")


def test_error_isolation():
    """测试单阶段失败不拖垮整条链路"""
    print("=" * 60)
    print("测试 A6：错误隔离")
    print("=" * 60)

    class BoomAnalyzer:
        def analyze(self, workflow_json, include_graph=False):
            raise RuntimeError("analyzer 炸了")

    agent, mods = build_fake_agent(analyzer=BoomAnalyzer())
    state = agent.ask("问题", {"nodes": []})

    print(f"  阶段: {state.stages_run}")
    print(f"  错误: {state.errors}")

    assert state.has_errors, "应记录错误"
    assert state.errors[0]["stage"] == "analyze"
    assert state.errors[0]["error_type"] == "RuntimeError"
    # 关键：后续阶段仍要跑完，仍能给出回答
    assert "retrieve" in state.stages_run
    assert "respond" in state.stages_run
    assert state.response["prompt"] == "<prompt>"
    print("单阶段失败仍完成回答 [OK]\n")


def test_continue_on_error_false():
    """测试严格模式下错误直接抛出"""
    print("=" * 60)
    print("测试 A7：严格模式")
    print("=" * 60)

    class BoomParser:
        def parse_data(self, data, workflow_id="<dict>"):
            raise ValueError("坏 JSON")

    agent, _ = build_fake_agent(
        parser=BoomParser(),
        config={"continue_on_error": False},
    )

    try:
        agent.ask("问题", {"nodes": []})
        raise AssertionError("严格模式下应抛出异常")
    except ValueError as e:
        print(f"  捕获: {e}")

    print("严格模式正确 [OK]\n")


def test_config_switches():
    """测试配置开关"""
    print("=" * 60)
    print("测试 A8：配置开关")
    print("=" * 60)

    agent, _ = build_fake_agent(config={
        "enable_diagnostics": False,
        "enable_retrieval": False,
    })
    state = agent.ask("问题", {"nodes": []})

    print(f"  阶段: {state.stages_run}")
    assert "diagnose" not in state.stages_run
    assert "retrieve" not in state.stages_run
    assert state.diagnostics == []
    assert state.knowledge == []
    # 回答阶段仍要在
    assert "respond" in state.stages_run

    # 未知配置项应报错而非静默失效
    try:
        merge_config({"enable_typo": True})
        raise AssertionError("未知配置项应报错")
    except ValueError as e:
        print(f"  未知配置被拒: {e}")

    print("配置开关正确 [OK]\n")


def test_no_workflow_still_answers():
    """测试不传工作流也能回答"""
    print("=" * 60)
    print("测试 A9：无工作流")
    print("=" * 60)

    agent, mods = build_fake_agent()
    state = agent.ask("什么是 latent？")

    print(f"  阶段: {state.stages_run}")
    print(f"  跳过: {state.stages_skipped}")
    assert state.workflow is None
    # 无工作流则跳过解析/分析/诊断，但检索与回答仍执行
    assert "parse" not in state.stages_run
    assert "diagnose" not in state.stages_run
    # 跳过的阶段要留下原因，方便排查「为什么这步没跑」
    skipped = {s["stage"]: s["reason"] for s in state.stages_skipped}
    assert "未提供 workflow" in skipped.get("parse", "")
    assert "无解析结果" in skipped.get("diagnose", "")
    assert "retrieve" in state.stages_run
    assert state.knowledge, "无工作流也应能检索到知识"
    assert state.response["prompt"] == "<prompt>"
    print("无工作流降级正确 [OK]\n")


def test_state_serialization():
    """测试状态可序列化"""
    print("=" * 60)
    print("测试 A10：状态序列化")
    print("=" * 60)

    agent, _ = build_fake_agent()
    state = agent.ask("问题", {"nodes": [{"type": "KSampler"}]})
    data = state.to_dict()

    # 必须能 JSON 序列化（graph 是对象，得被排除）
    text = json.dumps(data, ensure_ascii=False)
    print(f"  序列化长度: {len(text)}")
    print(f"  顶层键: {sorted(data.keys())}")

    assert "graph" not in json.dumps(data.get("workflow_analysis"))
    assert data["diagnostics"], "诊断应被转成可读文本"
    assert data["knowledge"], "知识应被摘要"
    print("状态可序列化 [OK]\n")


# ============================================================
# B. 真实模块端到端
# ============================================================

def test_pipeline_standalone():
    """测试 Pipeline 可独立使用"""
    print("=" * 60)
    print("测试 B1：Pipeline 独立使用")
    print("=" * 60)

    order = []

    def make(name):
        def handler(state):
            order.append(name)
            state.stages_run.append(name)
            return state
        return handler

    pipeline = AgentPipeline([
        Stage("a", make("a")),
        Stage("b", make("b")),
    ])
    pipeline.run(AgentState())

    print(f"  执行顺序: {order}")
    assert order == ["a", "b"]
    assert pipeline.stage_names() == ["a", "b"]
    print("Pipeline 独立可用 [OK]\n")


def build_real_agent(tmpdir):
    """用真实模块装配 Agent"""
    from engine.workflow_parser import WorkflowParser, NodeKnowledgeLoader
    from engine.workflow_analyzer import WorkflowAnalyzer
    from engine.context import ContextManager
    from engine.diagnostics import DiagnosticEngine
    from engine.retrieval import KnowledgeRetriever
    from engine.response_generator import ResponseGenerator
    from engine.knowledge_evolution import evolve

    project = Path(__file__).parent.parent

    context = ContextManager(str(Path(tmpdir) / "context_store.json"))
    # NodeKnowledgeLoader 收的是 knowledge 目录（内部自己拼 node_index.json）
    knowledge_loader = NodeKnowledgeLoader(
        str(project / "comfyui_library" / "knowledge")
    )
    parser = WorkflowParser(knowledge_loader, context=context)

    index_path = str(Path(tmpdir) / "retrieval_store.json")
    retriever = KnowledgeRetriever(auto_build=False)
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

    return ComfyUIAgent(
        parser=parser,
        analyzer=WorkflowAnalyzer(),
        context=context,
        diagnostics=DiagnosticEngine(),
        retriever=retriever,
        generator=ResponseGenerator(),
        learner=evolve,
        config={
            "retrieval_index_path": index_path,
            "context_store_path": str(Path(tmpdir) / "context_store.json"),
        },
    )


def test_end_to_end_with_real_modules():
    """端到端：九个模块串起来跑真实 workflow"""
    print("=" * 60)
    print("测试 B2：真实模块端到端")
    print("=" * 60)

    project = Path(__file__).parent.parent
    workflow_file = project / "comfyui_library" / "workflows" / "sd1.5" / "basic.json"

    if not workflow_file.exists():
        print("  找不到 basic.json，跳过")
        return

    with open(workflow_file, "r", encoding="utf-8-sig") as f:
        workflow_json = json.load(f)

    print(f"  workflow 节点数: {len(workflow_json.get('nodes', []))}")

    with TemporaryDirectory() as tmp:
        agent = build_real_agent(tmp)

        state = agent.ask(
            "为什么图片效果不稳定",
            workflow_json,
        )

        print(f"  阶段: {state.stages_run}")
        print(f"  错误: {state.errors}")
        print(f"  task_type: {state.workflow_type}")
        print(f"  解析节点数: {len(state.workflow_nodes())}")
        print(f"  分析出的节点: {state.workflow_analysis.get('nodes')}")
        print(f"  识别模式: {state.workflow_analysis.get('patterns')}")
        print(f"  诊断问题数: {len(state.diagnostics)}")
        for line in state.diagnostic_issues()[:3]:
            print(f"    - {line}")
        print(f"  检索到知识: {len(state.knowledge)} 条")
        for item in state.knowledge[:3]:
            print(f"    - [{item['type']}] {item['name']} "
                  f"score={item.get('score')}")
        print(f"  耗时: {state.elapsed_ms:.1f}ms")

        assert not state.has_errors, f"端到端不应报错: {state.errors}"
        assert state.workflow is not None, "应完成解析"
        assert state.workflow_analysis.get("nodes"), "应完成分析"
        assert state.workflow_nodes(), "应拿到节点清单"
        assert state.knowledge, "应检索到知识"
        assert state.response.get("prompt"), "应生成提示词"

        # 检索结果应带排序分数
        assert all("score" in item for item in state.knowledge)

        # 生成器应收到知识与诊断
        assert state.knowledge, "知识链未通"

        # 上下文应被持久化（记录了本次问题）
        store_file = Path(tmp) / "context_store.json"
        assert store_file.exists(), "上下文应落盘"
        with open(store_file, "r", encoding="utf-8-sig") as f:
            saved = json.load(f)
        print(f"  上下文记录的问题: {saved.get('recent_questions')}")
        assert saved.get("recent_questions"), "应记录本次问题"

    print("端到端链路打通 [OK]\n")


def test_retrieval_uses_workflow_nodes():
    """端到端验证：当前工作流节点影响检索排序"""
    print("=" * 60)
    print("测试 B3：工作流节点影响排序")
    print("=" * 60)

    project = Path(__file__).parent.parent
    workflow_file = project / "comfyui_library" / "workflows" / "sd1.5" / "basic.json"

    if not workflow_file.exists():
        print("  找不到 basic.json，跳过")
        return

    with open(workflow_file, "r", encoding="utf-8-sig") as f:
        workflow_json = json.load(f)

    with TemporaryDirectory() as tmp:
        agent = build_real_agent(tmp)
        state = agent.ask("KSampler 的 CFG 怎么设", workflow_json)

        print(f"  检索到 {len(state.knowledge)} 条:")
        for item in state.knowledge[:5]:
            reasons = item.get("match_reasons", [])
            print(f"    - [{item['type']}] {item['name']} "
                  f"score={item.get('score')} {reasons}")

        # KSampler 在工作流里，相关知识应有命中原因
        assert state.knowledge
        assert any(
            item.get("match_reasons") for item in state.knowledge
        ), "工作流命中的知识应带 match_reasons"

    print("排序受工作流影响 [OK]\n")


def test_continuous_questions():
    """测试连续追问：先登记工作流，再问多次"""
    print("=" * 60)
    print("测试 B4：连续追问")
    print("=" * 60)

    project = Path(__file__).parent.parent
    workflow_file = project / "comfyui_library" / "workflows" / "sd1.5" / "basic.json"

    if not workflow_file.exists():
        print("  找不到 basic.json，跳过")
        return

    with TemporaryDirectory() as tmp:
        agent = build_real_agent(tmp)

        # 只登记工作流，不提问
        state = agent.set_workflow(str(workflow_file))
        print(f"  登记后 task_type: {state.workflow_type}")
        print(f"  登记后节点: {state.workflow_nodes()}")
        assert state.workflow is not None
        # 分类器应给出真实类型，而不是 parser 的 "unknown" 占位值
        assert state.workflow_type != "unknown", \
            "分类结果不应停在 unknown"
        assert state.workflow_type, "应得出工作流类型"

        # 连问三次，均不传 workflow —— 应复用已登记的工作流
        questions = [
            "这个工作流在做什么",
            "KSampler 参数有什么建议",
            "为什么保存的图偏灰",
        ]
        for q in questions:
            s = agent.ask(q)
            assert not s.has_errors, f"{q} 出错: {s.errors}"
            assert s.reused_workflow, f"{q} 应复用已登记工作流"
            # 复用后解析/分析/诊断必须真的跑，不能空转
            assert "parse" in s.stages_run, f"{q} 未执行解析"
            assert "analyze" in s.stages_run, f"{q} 未执行分析"
            assert "diagnose" in s.stages_run, f"{q} 未执行诊断"
            assert s.workflow_analysis.get("nodes"), f"{q} 分析结果为空"
            print(f"  Q: {q}")
            print(f"    阶段 {s.stages_run}")
            print(f"    知识 {len(s.knowledge)} 条，"
                  f"诊断 {len(s.diagnostics)} 项")

        store_file = Path(tmp) / "context_store.json"
        with open(store_file, "r", encoding="utf-8-sig") as f:
            saved = json.load(f)
        print(f"  会话记录了 {len(saved.get('recent_questions', []))} 个问题")
        assert len(saved.get("recent_questions", [])) == 3

    print("连续追问正常 [OK]\n")


def test_diagnostics_fire_on_bad_params():
    """验证诊断阶段真的能发现问题（basic.json 参数正常，需构造异常值）"""
    print("=" * 60)
    print("测试 B5：诊断触发")
    print("=" * 60)

    # KSampler 的 widgets_values 顺序：seed, control_after_generate, steps, cfg, ...
    bad_workflow = {
        "nodes": [
            {"id": 1, "type": "CheckpointLoaderSimple",
             "widgets_values": ["model.safetensors"]},
            {"id": 2, "type": "KSampler",
             "widgets_values": [12345, "random", 3, 30.0, "euler", "normal", 1.0]},
        ],
        "links": [],
    }

    with TemporaryDirectory() as tmp:
        agent = build_real_agent(tmp)
        state = agent.ask("这个工作流有什么问题", bad_workflow)

        issues = state.diagnostic_issues()
        print(f"  诊断出 {len(issues)} 个问题:")
        for line in issues:
            print(f"    - {line}")

        assert state.diagnostics, "异常参数应触发诊断"
        assert any("cfg" in line.lower() for line in issues), \
            f"应报出 cfg 问题: {issues}"

        # 诊断结论必须进回答上下文，否则 LLM 看不到
        ctx = agent._build_answer_context(state)
        assert "diagnostics" in ctx, "诊断结论应进回答上下文"
        print(f"  回答上下文含 {len(ctx['diagnostics'])} 条诊断")

    print("诊断触发正常 [OK]\n")


def test_config_validation():
    """测试配置校验"""
    print("=" * 60)
    print("测试 B5：配置")
    print("=" * 60)

    config = merge_config({"retrieval_limit": 2})
    print(f"  默认阶段: {stages_of(merge_config())}")
    print(f"  关诊断后: {stages_of(merge_config({'enable_diagnostics': False}))}")

    assert config["retrieval_limit"] == 2
    assert "diagnose" in stages_of(merge_config())
    assert "diagnose" not in stages_of(
        merge_config({"enable_diagnostics": False})
    )
    print("配置校验正确 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Agent Core 模块测试")
    print("=" * 60 + "\n")

    # A：编排逻辑
    test_stage_order()
    test_workflow_input_normalization()
    test_graph_passed_to_diagnostics()
    test_retrieval_context_flat()
    test_knowledge_injected_into_generator()
    test_error_isolation()
    test_continue_on_error_false()
    test_config_switches()
    test_no_workflow_still_answers()
    test_state_serialization()

    # B：真实模块
    test_pipeline_standalone()
    test_end_to_end_with_real_modules()
    test_retrieval_uses_workflow_nodes()
    test_continuous_questions()
    test_diagnostics_fire_on_bad_params()
    test_config_validation()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
