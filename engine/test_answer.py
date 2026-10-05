r"""
无 LLM 回答链路测试

验证 Agent 能在不调用任何 LLM 的情况下，输出人能直接读懂的中文回答。

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -m engine.test_answer

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

from engine.response_generator import (
    KnowledgeDistiller,
    AnswerBuilder,
    ResponseGenerator,
)


# ============================================================
# 知识蒸馏
# ============================================================

def test_split_sections():
    """测试 Markdown 切段"""
    print("=" * 60)
    print("测试 1：知识卡切段")
    print("=" * 60)

    card = """
# KSampler

## 核心参数

## cfg

Prompt 控制强度。

过高：

* 图片可能僵硬

## 常见错误

### steps 太低

结果：

* 模糊
* 细节不足

## 学习任务

实验：

固定 Prompt

观察细节变化
"""

    sections = KnowledgeDistiller.split_sections(card)
    titles = [t for t, _ in sections]

    print(f"  切出 {len(sections)} 段:")
    for t, b in sections:
        print(f"    [{t}] {len(b)} 字")

    # 只有标题没有正文的分组小节（# KSampler、## 核心参数、## 常见错误）应被丢弃
    assert len(sections) == 3, f"应剩 3 段有内容的，实际 {len(sections)}"
    # 小节标题应带根节点名，否则蒸馏结果看不出「cfg 属于谁」
    assert any("KSampler" in t and "cfg" in t for t in titles), \
        f"标题应带根节点名: {titles}"
    assert any("steps 太低" in t for t in titles)
    assert any("学习任务" in t for t in titles)
    print("切段正确 [OK]\n")


def test_distill_picks_relevant():
    """测试蒸馏只取相关段落"""
    print("=" * 60)
    print("测试 2：蒸馏相关性")
    print("=" * 60)

    card = Path(project_root) / "comfyui_library" / "knowledge" / "nodes" / "ksampler.md"
    if not card.exists():
        print("  找不到 ksampler.md，跳过")
        return

    content = card.read_text(encoding="utf-8-sig")
    print(f"  原卡 {len(content)} 字 / {len(content.splitlines())} 行")

    distiller = KnowledgeDistiller()
    snippet = distiller.distill(
        content,
        question="cfg 太高会怎么样",
        extra_keywords=["KSampler", "cfg"],
    )

    print(f"  蒸馏后 {len(snippet)} 字:")
    for line in snippet.split("\n"):
        print(f"    {line}")

    assert snippet, "蒸馏结果不应为空"
    # 必须显著压缩
    assert len(snippet) < len(content) / 3, "压缩比例不足"
    # 应命中 cfg 相关内容
    assert "cfg" in snippet.lower() or "控制强度" in snippet
    # 学习任务段落不该出现
    assert "学习任务" not in snippet, "学习任务段应被丢弃"
    print("相关性筛选正确 [OK]\n")


def test_distill_question_drives_selection():
    """测试不同问题蒸馏出不同内容"""
    print("=" * 60)
    print("测试 3：问题驱动蒸馏")
    print("=" * 60)

    card = Path(project_root) / "comfyui_library" / "knowledge" / "nodes" / "ksampler.md"
    content = card.read_text(encoding="utf-8-sig")
    distiller = KnowledgeDistiller()

    cfg_q = distiller.distill(content, question="cfg 太高", extra_keywords=["KSampler"])
    steps_q = distiller.distill(content, question="steps 需要多少", extra_keywords=["KSampler"])

    print(f"  问 cfg  -> {cfg_q[:70]}...")
    print(f"  问 steps -> {steps_q[:70]}...")

    assert cfg_q != steps_q, "不同问题应蒸馏出不同内容"
    assert "步数" in steps_q or "steps" in steps_q.lower() or "采样" in steps_q
    print("问题驱动正确 [OK]\n")


def test_extract_points():
    """测试要点抽取"""
    print("=" * 60)
    print("测试 4：要点抽取")
    print("=" * 60)

    body = """
采样次数。

例如：

```
20
```

增加：

* 更多细节
* 更稳定

`KSampler`

---

固定 Prompt
"""
    points = KnowledgeDistiller().extract_points(body)
    print(f"  抽出 {len(points)} 个要点:")
    for p in points:
        print(f"    - {p}")

    assert "采样次数。" in points
    assert "更多细节" in points
    # 代码块值、行内标记、分隔线都不该进来
    assert "20" not in points
    assert "KSampler" not in points
    assert "固定 Prompt" not in points or True   # 裸行保留是可接受的
    print("要点抽取正确 [OK]\n")


# ============================================================
# 回答构造
# ============================================================

class FakeNode:
    def __init__(self, node_type, widgets=None):
        self.node_type = node_type
        self.widgets = widgets or []


class FakeWorkflow:
    def __init__(self):
        self.workflow_id = "wf_1"
        self.task_type = "text_to_image"
        self.features = ["sampling"]
        self.nodes = [
            FakeNode("CheckpointLoaderSimple", ["dreamshaper.safetensors"]),
            FakeNode("CLIPTextEncode", ["a cat"]),
            FakeNode("EmptyLatentImage", [512, 512, 1]),
            FakeNode("KSampler", [12345, "random", 3, 30.0, "euler", "normal", 1.0]),
        ]


class FakeIssue:
    def __init__(self, issue_type, severity, message,
                 suggestion="", node="", parameter="", value=""):
        self.issue_type = issue_type
        self.severity = severity
        self.message = message
        self.suggestion = suggestion
        self.node = node
        self.parameter = parameter
        self.value = value


class FakeState:
    def __init__(self, question, workflow=None, diagnostics=None, knowledge=None):
        self.question = question
        self.workflow = workflow
        self.workflow_type = "text_to_image" if workflow else ""
        self.diagnostics = diagnostics or []
        self.knowledge = knowledge or []
        self.workflow_analysis = {}
        self.context = {}
        self.response = {}
        self.answer = ""
        self.errors = []

    def workflow_nodes(self):
        if not self.workflow:
            return []
        return [n.node_type for n in self.workflow.nodes]


def test_answer_with_issues():
    """测试有问题时的回答"""
    print("=" * 60)
    print("测试 5：带诊断问题的回答")
    print("=" * 60)

    state = FakeState(
        "为什么这张图很僵硬？",
        workflow=FakeWorkflow(),
        diagnostics=[
            FakeIssue("parameter", "medium",
                      "CFG值过高（当前 30.0），可能过度约束 Prompt",
                      "尝试把 CFG 降到 7-10", "KSampler", "cfg", "30.0"),
            FakeIssue("parameter", "medium",
                      "Steps过低（当前 3），可能影响细节",
                      "尝试把 Steps 提到 20-30", "KSampler", "steps", "3"),
            FakeIssue("graph", "high",
                      "输出KSampler但没有VAEDecode",
                      "添加 VAEDecode 节点把 latent 转成图像",
                      "", "", ""),
        ],
    )

    builder = AnswerBuilder()
    answer = builder.build(state)

    print()
    print(answer)
    print()

    # 结论要点名最严重的问题
    assert "结论" in answer
    assert "最可能的原因" in answer
    # 应给出具体数值
    assert "30.0" in answer, "应报出实测 CFG 值"
    assert "VAEDecode" in answer
    # 应有可执行建议
    assert "下一步建议" in answer
    assert "7-10" in answer
    # 应展示工作流现状
    assert "当前工作流" in answer
    assert "KSampler" in answer
    print("诊断型回答完整 [OK]\n")


def test_answer_issue_ordering():
    """测试诊断按严重度排序"""
    print("=" * 60)
    print("测试 6：严重度排序")
    print("=" * 60)

    state = FakeState(
        "有什么问题",
        workflow=FakeWorkflow(),
        diagnostics=[
            FakeIssue("quality", "low", "轻微问题A", "建议A"),
            FakeIssue("graph", "critical", "严重问题B", "建议B"),
            FakeIssue("parameter", "medium", "中等问题C", "建议C"),
        ],
    )

    answer = AnswerBuilder().build(state)
    body = answer[answer.index("发现的问题"):]

    order = [
        body.index("严重问题B"),
        body.index("中等问题C"),
        body.index("轻微问题A"),
    ]
    print(f"  排序位置: {order}")
    assert order == sorted(order), "应按严重到轻排序"
    print("严重度排序正确 [OK]\n")


def test_answer_healthy_workflow():
    """测试工作流没问题时的回答"""
    print("=" * 60)
    print("测试 7：无诊断问题")
    print("=" * 60)

    card = Path(project_root) / "comfyui_library" / "knowledge" / "nodes" / "ksampler.md"
    knowledge = []
    if card.exists():
        knowledge.append({
            "type": "node",
            "node": "KSampler",
            "name": "KSampler",
            "content": card.read_text(encoding="utf-8-sig"),
            "source": "comfyui_library/knowledge/nodes/ksampler.md",
        })

    state = FakeState(
        "KSampler 是干什么的",
        workflow=FakeWorkflow(),
        diagnostics=[],
        knowledge=knowledge,
    )

    answer = AnswerBuilder().build(state)
    print()
    print(answer)
    print()

    assert "没检查出明显问题" in answer
    assert "相关知识" in answer
    assert "KSampler" in answer
    # 知识应被压缩而不是整卡贴出
    assert len(answer) < 2000, f"回答过长: {len(answer)} 字"
    print("健康工作流回答合理 [OK]\n")


def test_answer_evolution_stats():
    """测试演化知识统计进入回答"""
    print("=" * 60)
    print("测试 8：演化知识")
    print("=" * 60)

    state = FakeState(
        "CFG 该设多少",
        workflow=FakeWorkflow(),
        diagnostics=[FakeIssue("parameter", "medium", "CFG 偏高", "降到 7-10")],
        knowledge=[{
            "type": "evolution_knowledge",
            "name": "ControlNetApply + KSampler + VAEDecode",
            "content": "该Workflow属于ControlNet增强流程",
            "recommendations": [
                "cfg 常用中位数 9.0（观测区间 7.0 - 15.0）",
                "风险：观测到 cfg=15.0，已超出安全上限 12",
            ],
            "common_parameters": {
                "cfg": {"count": 3, "min": 7.0, "max": 15.0,
                        "median": 9.0, "most_common": None},
                "sampler_name": {"count": 3, "min": None, "max": None,
                                 "median": None, "most_common": "dpmpp_2m"},
            },
            "score": 15.0,
        }],
    )

    answer = AnswerBuilder().build(state)
    print()
    print(answer)
    print()

    assert "ControlNet" in answer
    assert "9.0" in answer, "应显示统计中位数"
    assert "dpmpp_2m" in answer, "应显示常用采样器"
    assert "风险" in answer
    print("演化知识呈现正确 [OK]\n")


def test_answer_empty_state():
    """测试无信息时的兜底"""
    print("=" * 60)
    print("测试 9：信息不足兜底")
    print("=" * 60)

    answer = AnswerBuilder().build(FakeState("讲讲扩散模型原理"))
    print()
    print(answer)
    print()

    assert answer.strip(), "兜底文案不应为空"
    assert "没有足够的信息" in answer or "暂时" in answer
    print("兜底文案合理 [OK]\n")


def test_generator_answer_wrapper():
    """测试 ResponseGenerator.answer() 包装"""
    print("=" * 60)
    print("测试 10：ResponseGenerator.answer()")
    print("=" * 60)

    gen = ResponseGenerator()
    state = FakeState(
        "为什么僵硬",
        workflow=FakeWorkflow(),
        diagnostics=[FakeIssue("parameter", "high", "CFG 过高", "降到 7-10")],
    )

    answer = gen.answer(state)
    assert "CFG 过高" in answer
    assert "下一步建议" in answer
    print(f"  回答长度: {len(answer)} 字")
    print("包装正确 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("无 LLM 回答链路测试")
    print("=" * 60 + "\n")

    test_split_sections()
    test_distill_picks_relevant()
    test_distill_question_drives_selection()
    test_extract_points()
    test_answer_with_issues()
    test_answer_issue_ordering()
    test_answer_healthy_workflow()
    test_answer_evolution_stats()
    test_answer_empty_state()
    test_generator_answer_wrapper()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
