r"""
agent_core 库事实通道测试（v0.6 第 2 步）

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_agent_db_facts

覆盖：
    A. 采集逻辑（用假 db_facts 注入，不依赖真实索引）
    B. 只读与降级（索引缺失/为空时不报错、facts 为空）
    C. 限流（db_facts_limit 生效）
    D. 阶段顺序不受影响（库事实不占独立阶段位）
    E. 回答分节呈现（图谱事实与库事实分开成节）
    F. LLM 上下文带上库事实
"""

import sys
from pathlib import Path
from types import SimpleNamespace

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.agent_core.agent import ComfyUIAgent
from engine.agent_core.config import merge_config

PASS, FAIL = "PASS", "FAIL"
_results = []


def check(name, cond, detail=""):
    _results.append((PASS if cond else FAIL, name, detail))
    print(f"  [{PASS if cond else FAIL}] {name}" + (f" — {detail}" if detail else ""))


class FakeFacts:
    """假 db_facts：不碰真实索引，可控输出。"""

    def __init__(self, nodes=None, usage=None, patterns=None, empty=False):
        self._nodes = nodes if nodes is not None else ["KSampler", "VAEDecode"]
        self._usage = usage if usage is not None else {"KSampler": 500, "VAEDecode": 300}
        self._patterns = patterns if patterns is not None else {}
        self._empty = empty

    def all_node_names(self):
        return [] if self._empty else list(self._nodes)

    def all_pattern_names(self):
        return [] if self._empty else list(self._patterns)

    def node_usage_count(self, name):
        return self._usage.get(name, 0)

    def workflows_using_node(self, name):
        # 返回全部 ID（与 usage_count 一致），文案里的「真实工作流数」
        # 取的就是这个长度，两者必须对得上
        n = self._usage.get(name, 0)
        return [f"{1000000000000000 + i}" for i in range(n)]

    def patterns_for_workflow(self, wf_id):
        return self._patterns.get(wf_id, [])


def make_agent(facts_obj=None, config=None, with_workflow=False):
    agent = ComfyUIAgent(
        parser=None, analyzer=None, context=None, diagnostics=None,
        retriever=SimpleNamespace(retrieve=lambda q, c, limit=0: []),
        generator=SimpleNamespace(
            answer=lambda s: "基础回答。",
            generate=lambda q, c, knowledge=None: {"prompt": "p"},
        ),
        auto_modules=False,
        config=config or {},
    )
    agent._db_facts_obj = facts_obj
    if with_workflow:
        agent._last_workflow = SimpleNamespace(
            workflow_id="2087218383308812289",
            nodes=[SimpleNamespace(node_type="KSampler")],
            features=[],
        )
    return agent


def test_collection():
    print("\n[A] 库事实采集")
    agent = make_agent(FakeFacts())
    state = agent._collect_db_facts(
        SimpleNamespace(question="KSampler 怎么用", workflow=None)
    ) if False else None

    from engine.agent_core.state import AgentState
    st = AgentState(question="KSampler 怎么用")
    agent._collect_db_facts(st)
    check("采到节点维度事实", len(st.db_facts) >= 1, f"{len(st.db_facts)} 条")
    check("事实含节点名与用量",
          any("KSampler" in f and "500" in f for f in st.db_facts),
          str(st.db_facts))
    check("事实含 workflow 预览",
          any("1000000000000000" in f for f in st.db_facts))


def test_workflow_patterns():
    print("\n[B] 工作流模式维度")
    from engine.agent_core.state import AgentState
    facts = FakeFacts(patterns={"2087218383308812289": ["pat_a", "pat_b", "pat_c"]})
    agent = make_agent(facts)
    st = AgentState(question="这个流程")
    st.workflow = SimpleNamespace(
        workflow_id="2087218383308812289",
        nodes=[SimpleNamespace(node_type="KSampler")],
    )
    agent._collect_db_facts(st)
    check("采到模式维度事实", any("模式" in f for f in st.db_facts))
    check("事实含模式数量",
          any("3 个" in f for f in st.db_facts), str(st.db_facts))


def test_degradation():
    print("\n[C] 降级")
    from engine.agent_core.state import AgentState
    # 索引为空 → 视为不可用
    agent = make_agent(FakeFacts(empty=True))
    agent._db_facts_obj = None
    agent._db_facts = lambda: None  # 模拟索引不可用
    st = AgentState(question="KSampler")
    agent._collect_db_facts(st)
    check("索引不可用时不报错", st.db_facts == [])
    check("记录跳过原因",
          any(s["stage"] == "db_facts" for s in st.stages_skipped),
          str(st.stages_skipped))

    # 关闭开关
    agent2 = make_agent(FakeFacts(), config={"enable_db_facts": False})
    st2 = AgentState(question="KSampler")
    agent2._collect_db_facts(st2)
    check("开关关闭时不采集", st2.db_facts == [])


def test_limit():
    print("\n[D] 限流")
    from engine.agent_core.state import AgentState
    facts = FakeFacts(usage={f"node{i}": 10 for i in range(20)})
    agent = make_agent(facts, config={"db_facts_limit": 3})
    st = AgentState(question="node1 node2 node3 node4 node5")
    st.workflow = SimpleNamespace(
        workflow_id="9999999999999999",
        nodes=[SimpleNamespace(node_type=f"node{i}") for i in range(5)],
    )
    agent._collect_db_facts(st)
    check("限流生效", len(st.db_facts) <= 3, f"{len(st.db_facts)} 条")


def test_stage_order():
    print("\n[E] 阶段顺序")
    from engine.agent_core.state import AgentState
    agent = make_agent(FakeFacts())
    st = AgentState(question="KSampler")
    st.workflow = SimpleNamespace(
        workflow_id="2087218383308812289",
        nodes=[SimpleNamespace(node_type="KSampler")],
    )
    agent._collect_db_facts(st)
    check("库事实不占独立阶段位", "db_facts" not in st.stages_run, str(st.stages_run))
    check("stages_run 未被污染", st.stages_run == [], str(st.stages_run))


def test_answer_sections():
    print("\n[F] 回答分节呈现")
    from engine.agent_core.state import AgentState
    agent = make_agent(FakeFacts())
    st = AgentState(question="KSampler")
    st.workflow = SimpleNamespace(
        workflow_id="2087218383308812289",
        nodes=[SimpleNamespace(node_type="KSampler")],
    )
    st.graph_facts = ["知识图谱：某节点被使用"]
    agent._collect_db_facts(st)
    agent._stage_respond(st)
    check("回答含图谱节", "## 跨条目知识图谱" in st.answer)
    check("回答含库事实节", "## 结构层库事实" in st.answer)
    check("两节不混淆",
          st.answer.index("## 跨条目知识图谱") < st.answer.index("## 结构层库事实"))
    check("LLM 上下文带库事实",
          "db_facts" in agent._build_answer_context(st),
          str(list(agent._build_answer_context(st).keys())))


def main():
    print("=" * 62)
    print("agent_core 库事实通道测试")
    print("=" * 62)
    test_collection()
    test_workflow_patterns()
    test_degradation()
    test_limit()
    test_stage_order()
    test_answer_sections()

    passed = sum(1 for s, _, _ in _results if s == PASS)
    failed = [r for r in _results if r[0] == FAIL]
    print("\n" + "=" * 62)
    print(f"通过 {passed} / 失败 {len(failed)}")
    if failed:
        for _, name, detail in failed:
            print(f"  失败: {name} {detail}")
        return 1
    print("全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
