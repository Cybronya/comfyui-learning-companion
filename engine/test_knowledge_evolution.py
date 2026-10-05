r"""
Knowledge Evolution 模块测试

注意：本脚本从仓库根目录运行（使用 from engine.xxx 包导入）：
    cd "F:\Program Files\ComfyUI"
    python -m engine.test_knowledge_evolution

控制台在中文 Windows 下是 GBK 编码，勾号等符号会触发 UnicodeEncodeError，
因此下面统一用 [OK] / [FAIL] 这样的 ASCII 标记。
"""

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

# 兼容从 engine/ 目录直接运行
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.knowledge_evolution import (
    ExperienceCollector,
    PatternMiner,
    KnowledgeGenerator,
    KnowledgeStore,
    WorkflowExperience,
    PatternMiner as _PM,
    evolve,
)
from engine.knowledge_evolution.models import EvolutionKnowledge


def build_experiences():
    """
    构造测试经验：3 个 ControlNet 工作流 + 1 个 LoRA 工作流

    ControlNet 三条节点组合相同但 CFG/Steps 各不相同，
    用来验证模式挖掘（frequency=3）和参数区间统计。
    """
    return [
        WorkflowExperience(
            workflow_type="SDXL",
            nodes=["KSampler", "ControlNetApply", "VAEDecode"],
            parameters={"cfg": 7.0, "steps": 25, "sampler_name": "dpmpp_2m"},
            observation="CFG 7 时构图稳定",
            tags=["quality"],
        ),
        WorkflowExperience(
            workflow_type="SDXL",
            nodes=["ControlNetApply", "VAEDecode", "KSampler"],
            parameters={"cfg": 9.0, "steps": 35, "sampler_name": "dpmpp_2m"},
            observation="CFG 9 细节更好",
            tags=["quality"],
        ),
        WorkflowExperience(
            workflow_type="SDXL",
            nodes=["KSampler", "ControlNetApply", "VAEDecode"],
            parameters={"cfg": 15.0, "steps": 20, "sampler_name": "euler"},
            observation="CFG 15 脸部异常",
            tags=["quality", "risk"],
        ),
        WorkflowExperience(
            workflow_type="SD1.5",
            nodes=["CheckpointLoaderSimple", "LoraLoader", "KSampler"],
            parameters={"cfg": 6.0, "steps": 30},
            observation="LoRA 风格稳定",
            tags=["lora"],
        ),
    ]


def test_pattern_miner_dict_input():
    """测试 PatternMiner 兼容 dict 输入（原设计文档给的测试流程用 dict）"""
    print("=" * 60)
    print("测试 1：PatternMiner 兼容 dict 输入")
    print("=" * 60)

    experiences = [
        {"workflow_type": "SDXL", "nodes": ["KSampler", "ControlNetApply", "VAEDecode"]},
        {"workflow_type": "SDXL", "nodes": ["KSampler", "ControlNetApply", "VAEDecode"]},
    ]

    miner = PatternMiner()
    patterns = miner.mine(experiences)

    assert len(patterns) == 1, f"应挖出 1 个模式，实际 {len(patterns)}"
    assert patterns[0]["frequency"] == 2
    print(f"模式: {patterns[0]['nodes']}  频次: {patterns[0]['frequency']}")
    print("dict 输入兼容 [OK]\n")


def test_knowledge_generator():
    """测试知识生成器输出（对齐原设计文档第九节的预期输出）"""
    print("=" * 60)
    print("测试 2：知识生成器")
    print("=" * 60)

    experiences = [
        {"workflow_type": "SDXL", "nodes": ["KSampler", "ControlNetApply", "VAEDecode"]},
        {"workflow_type": "SDXL", "nodes": ["KSampler", "ControlNetApply", "VAEDecode"]},
    ]

    miner = PatternMiner()
    patterns = miner.mine(experiences)
    generator = KnowledgeGenerator()
    knowledge = generator.generate(patterns[0])

    print(f"pattern      : {knowledge['pattern']}")
    print(f"frequency    : {knowledge['frequency']}")
    print(f"description  : {knowledge['description']}")

    assert knowledge["pattern"] == "ControlNetApply + KSampler + VAEDecode"
    assert knowledge["frequency"] == 2
    assert knowledge["description"] == "该Workflow属于ControlNet增强流程"
    print("输出与设计文档一致 [OK]\n")


def test_parameter_ranges():
    """测试参数区间统计"""
    print("=" * 60)
    print("测试 3：参数区间统计")
    print("=" * 60)

    experiences = build_experiences()
    miner = PatternMiner()
    patterns = miner.mine(experiences)

    controlnet = patterns[0]
    params = controlnet["parameter_ranges"]

    print(f"模式: {controlnet['nodes']}  频次: {controlnet['frequency']}")
    for name, stats in params.items():
        print(f"  {name}: min={stats['min']} max={stats['max']} "
              f"median={stats['median']} common={stats['most_common']}")

    assert controlnet["frequency"] == 3
    assert params["cfg"]["min"] == 7.0
    assert params["cfg"]["max"] == 15.0
    assert params["cfg"]["median"] == 9.0
    assert params["steps"]["median"] == 25
    assert params["sampler_name"]["most_common"] == "dpmpp_2m"

    # 频次 1 的 LoRA 组合不应成为模式
    assert len(patterns) == 1, f"只应有 1 个模式，实际 {len(patterns)}"
    print("参数区间与频次门槛正确 [OK]\n")


def test_recommendations():
    """测试建议与风险提示"""
    print("=" * 60)
    print("测试 4：建议与风险提示")
    print("=" * 60)

    experiences = build_experiences()
    miner = PatternMiner()
    patterns = miner.mine(experiences)
    generator = KnowledgeGenerator()
    knowledge = generator.generate(patterns[0])

    for rec in knowledge["recommendations"]:
        print(f"  - {rec}")

    joined = " ".join(knowledge["recommendations"])
    assert "cfg" in joined.lower()
    # CFG 观测到 15 > 安全上限 12，应触发风险提示
    assert "CFG 偏高" in joined or "风险" in joined
    assert "ControlNet 权重" in joined
    print("风险提示触发正确 [OK]\n")


def test_experience_collector_from_learning_loop():
    """测试从 learning_loop 经验格式转换"""
    print("=" * 60)
    print("测试 5：learning_loop 经验转换")
    print("=" * 60)

    collector = ExperienceCollector()
    collector.register_nodes(
        "SDXL", ["KSampler", "ControlNetApply", "VAEDecode"]
    )

    # 模拟 learning_loop.LearningExperience 的字典形式
    raw = {
        "workflow_type": "SDXL",
        "change": {
            "changed_nodes": ["added:ControlNetApply"],
            "parameter_changes": {
                "cfg": {"old": 15, "new": 7},
                "steps": {"old": 10, "new": 30},
            },
        },
        "observation": "CFG 降低后改善",
        "conclusion": "参数优化",
        "tags": ["quality", "prompt_control"],
        "timestamp": "2026-10-05 12:00:00",
    }

    exp = collector.from_learning_experience(raw)
    collector.from_learning_experience(raw)
    collector.from_learning_experience(raw)

    print(f"节点清单（来自 register_nodes）: {exp.nodes}")
    print(f"参数（取 new 侧）: {exp.parameters}")
    print(f"标签: {exp.tags}")

    assert exp.nodes == ["KSampler", "ControlNetApply", "VAEDecode"]
    assert exp.parameters == {"cfg": 7, "steps": 30}
    assert len(collector.get_by_type("SDXL")) == 3

    # 三条相同经验应能挖出模式
    patterns = PatternMiner().mine(collector.get_all())
    assert len(patterns) == 1
    assert patterns[0]["frequency"] == 3
    print("经验转换 + 挖掘闭环正确 [OK]\n")


def test_knowledge_store():
    """测试知识持久化"""
    print("=" * 60)
    print("测试 6：知识存储")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = str(Path(tmp) / "evolution_store.json")

        experiences = build_experiences()
        knowledge = evolve(experiences, store_path=path, save=True)

        store = KnowledgeStore(path)
        loaded = store.get_all()

        print(f"存储条目数: {len(loaded)}")
        print(f"首条名称: {loaded[0]['name']}")
        print(f"源经验数: {knowledge.source_experience_count}")

        assert len(loaded) == 1
        assert loaded[0]["frequency"] == 3
        assert knowledge.source_experience_count == 3

        # 再演化一次，验证 replace_all 覆盖而非堆叠
        evolve(experiences, store_path=path, save=True)
        store2 = KnowledgeStore(path)
        assert len(store2.get_all()) == 1, "重复演化不应堆叠条目"

        # 名称检索
        found = store2.find_by_name("ControlNetApply + KSampler + VAEDecode")
        assert len(found) == 1
    print("持久化与覆盖语义正确 [OK]\n")


def test_empty_input():
    """测试经验不足时的降级行为"""
    print("=" * 60)
    print("测试 7：经验不足降级")
    print("=" * 60)

    collector = ExperienceCollector()
    collector.add(WorkflowExperience(workflow_type="SDXL", nodes=["KSampler"]))
    patterns = PatternMiner(min_frequency=2).mine(collector.get_all())
    assert patterns == []

    generator = KnowledgeGenerator()
    knowledge = generator.generate({
        "nodes": ["KSampler"], "frequency": 1, "parameter_ranges": {}
    })
    print(f"单样本建议: {knowledge['recommendations']}")
    assert "样本量不足" in knowledge["recommendations"][0]

    # 节点清单为空的经验应被跳过而不是报错
    collector.add(WorkflowExperience(workflow_type="SDXL", nodes=[]))
    assert len(PatternMiner().mine(collector.get_all())) == 0
    print("降级行为正确 [OK]\n")


def test_evolution_knowledge_roundtrip():
    """测试 EvolutionKnowledge 序列化往返"""
    print("=" * 60)
    print("测试 8：知识对象序列化")
    print("=" * 60)

    knowledge = evolve(build_experiences(), save=False)
    data = knowledge.to_dict()
    restored = EvolutionKnowledge.from_dict(data)

    assert len(restored.patterns) == len(knowledge.patterns)
    assert restored.source_experience_count == knowledge.source_experience_count
    assert restored.patterns[0].name == knowledge.patterns[0].name
    assert restored.patterns[0].common_parameters == \
        knowledge.patterns[0].common_parameters
    print(f"模式名: {restored.patterns[0].name}")
    print("序列化往返一致 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Knowledge Evolution 模块测试")
    print("=" * 60 + "\n")

    test_pattern_miner_dict_input()
    test_knowledge_generator()
    test_parameter_ranges()
    test_recommendations()
    test_experience_collector_from_learning_loop()
    test_knowledge_store()
    test_empty_input()
    test_evolution_knowledge_roundtrip()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
