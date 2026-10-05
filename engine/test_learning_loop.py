"""
Learning Loop 模块测试
"""

import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from datetime import datetime
from engine.learning_loop import (
    WorkflowComparator,
    ExperimentTracker,
    ImprovementAnalyzer,
    WorkflowSnapshot,
    WorkflowChange,
    LearningExperience,
)


def test_workflow_compare():
    """测试 Workflow 比较器"""
    print("=" * 60)
    print("测试 Workflow 比较器")
    print("=" * 60)

    comparator = WorkflowComparator()

    # 创建两个工作流快照
    old_workflow = WorkflowSnapshot(
        workflow_id="workflow_1",
        timestamp="2026-10-04 10:00:00",
        nodes=["KSampler", "CLIPTextEncode", "VAEDecode"],
        parameters={
            "steps": 10,
            "cfg": 15,
            "seed": 123456,
            "sampler_name": "euler"
        }
    )

    new_workflow = WorkflowSnapshot(
        workflow_id="workflow_1",
        timestamp="2026-10-04 11:00:00",
        nodes=["KSampler", "CLIPTextEncode", "VAEDecode", "ControlNet"],
        parameters={
            "steps": 30,
            "cfg": 8,
            "seed": 123456,
            "sampler_name": "euler"
        }
    )

    # 比较工作流
    changes = comparator.compare(old_workflow, new_workflow)

    print("\n比较结果:")
    print(f"节点变化: {changes.get('nodes_changed', [])}")
    print(f"参数变化:")
    for key, value in changes.get('parameters', {}).items():
        print(f"  {key}: {value['old']} → {value['new']}")

    # 测试字典比较
    print("\n" + "-" * 40)
    print("测试字典比较:")
    old_dict = {
        "nodes": ["KSampler", "CLIPTextEncode"],
        "steps": 10,
        "cfg": 15
    }

    new_dict = {
        "nodes": ["KSampler", "CLIPTextEncode", "VAEDecode"],
        "steps": 30,
        "cfg": 8,
        "sampler_name": "euler"
    }

    changes_dict = comparator.compare_dicts(old_dict, new_dict)
    print(f"节点变化: {changes_dict.get('nodes_changed', [])}")
    print(f"参数变化:")
    for key, value in changes_dict.get('parameters', {}).items():
        print(f"  {key}: {value['old']} → {value['new']}")


def test_improvement_analyzer():
    """测试改进分析器"""
    print("\n" + "=" * 60)
    print("测试改进分析器")
    print("=" * 60)

    analyzer = ImprovementAnalyzer()

    # 测试用例1：steps 增加，cfg 降低
    changes = {
        "parameters": {
            "steps": {"old": 10, "new": 30},
            "cfg": {"old": 15, "new": 8}
        }
    }

    print("\n用例1: steps增加(10→30), cfg降低(15→8)")
    observations = analyzer.analyze(changes)
    print("观察:")
    for obs in observations:
        print(f"  - {obs}")

    # 测试用例2：添加 ControlNet
    changes2 = {
        "parameters": {},
        "nodes_changed": ["added:ControlNet"]
    }

    print("\n用例2: 添加 ControlNet 节点")
    observations2 = analyzer.analyze(changes2)
    print("观察:")
    for obs in observations2:
        print(f"  - {obs}")

    # 测试用例3：denoise 增加
    changes3 = {
        "parameters": {
            "denoise": {"old": 0.5, "new": 0.8}
        }
    }

    print("\n用例3: denoise增加(0.5→0.8)")
    observations3 = analyzer.analyze(changes3)
    print("观察:")
    for obs in observations3:
        print(f"  - {obs}")


def test_experiment_tracker():
    """测试实验跟踪器"""
    print("\n" + "=" * 60)
    print("测试实验跟踪器")
    print("=" * 60)

    tracker = ExperimentTracker("engine/learning_loop/experience_store.json")

    # 添加学习经验
    print("\n添加学习经验...")

    experience1 = LearningExperience(
        workflow_type="image_generation",
        change=WorkflowChange(
            changed_nodes=["added:ControlNet"],
            parameter_changes={"sampler_name": {"old": "euler", "new": "dpmpp_2m"}}
        ),
        observation="采样器从 euler 改为 dpmpp_2m，可能提升生成质量",
        conclusion="采样器优化，建议观察效果",
        tags=["quality", "sampling_method"]
    )

    experience2 = LearningExperience(
        workflow_type="image_generation",
        change=WorkflowChange(
            parameter_changes={"steps": {"old": 10, "new": 30}, "cfg": {"old": 15, "new": 8}}
        ),
        observation="steps增加提升细节，cfg降低减少过度约束",
        conclusion="参数优化，细节与速度的平衡",
        tags=["quality", "prompt_control"]
    )

    tracker.add_experience(experience1)
    tracker.add_experience(experience2)

    print("经验添加成功！")

    # 获取所有经验
    print("\n所有经验:")
    all_experiences = tracker.get_all_experiences()
    for i, exp in enumerate(all_experiences, 1):
        print(f"\n{i}. 工作流类型: {exp.workflow_type}")
        print(f"   观察: {exp.observation}")
        print(f"   结论: {exp.conclusion}")
        print(f"   标签: {exp.tags}")

    # 获取统计信息
    print("\n" + "-" * 40)
    print("统计信息:")
    stats = tracker.get_statistics()
    print(f"总经验数: {stats['total_experiences']}")
    print(f"按工作流类型分布: {stats['by_workflow_type']}")
    print(f"按标签分布: {stats['by_tag']}")

    # 获取最近经验
    print("\n最近3条经验:")
    recent = tracker.get_recent_experiences(count=3)
    for i, exp in enumerate(recent, 1):
        print(f"{i}. {exp.observation[:50]}...")

    # 清空数据（可选）
    # print("\n清空所有经验...")
    # tracker.clear()


def test_full_workflow():
    """测试完整工作流"""
    print("\n" + "=" * 60)
    print("测试完整工作流")
    print("=" * 60)

    # 1. 创建快照
    print("\n1. 创建工作流快照...")
    old_snapshot = WorkflowSnapshot(
        workflow_id="portrait_workflow",
        timestamp="2026-10-04 10:00:00",
        nodes=["KSampler", "CLIPTextEncode", "VAEDecode"],
        parameters={
            "steps": 20,
            "cfg": 7.0,
            "seed": 123456,
            "width": 512,
            "height": 768
        }
    )

    new_snapshot = WorkflowSnapshot(
        workflow_id="portrait_workflow",
        timestamp="2026-10-04 11:00:00",
        nodes=["KSampler", "CLIPTextEncode", "VAEDecode", "ControlNet"],
        parameters={
            "steps": 30,
            "cfg": 6.5,
            "seed": 123456,
            "width": 1024,
            "height": 1536
        }
    )

    print(f"旧快照: {len(old_snapshot.nodes)} 个节点, {len(old_snapshot.parameters)} 个参数")
    print(f"新快照: {len(new_snapshot.nodes)} 个节点, {len(new_snapshot.parameters)} 个参数")

    # 2. 比较差异
    print("\n2. 比较差异...")
    comparator = WorkflowComparator()
    changes = comparator.compare(old_snapshot, new_snapshot)

    print(f"节点变化: {len(changes.get('nodes_changed', []))} 处")
    print(f"参数变化: {len(changes.get('parameters', {}))} 个")

    # 3. 分析改进
    print("\n3. 分析改进...")
    analyzer = ImprovementAnalyzer()
    observations = analyzer.analyze(changes, workflow_type="image_generation")

    print("观察结果:")
    for i, obs in enumerate(observations, 1):
        print(f"   {i}. {obs}")

    # 4. 生成结论
    print("\n4. 生成结论...")
    conclusion = analyzer.generate_conclusion(changes, observations)
    print(f"结论: {conclusion}")

    # 5. 提取标签
    print("\n5. 提取标签...")
    tags = analyzer.extract_tags(changes)
    print(f"标签: {tags}")

    # 6. 保存经验
    print("\n6. 保存经验...")
    tracker = ExperimentTracker()
    experience = LearningExperience(
        workflow_type="image_generation",
        change=WorkflowChange(
            changed_nodes=changes.get('nodes_changed', []),
            parameter_changes=changes.get('parameters', {})
        ),
        observation="; ".join(observations),
        conclusion=conclusion,
        tags=tags
    )
    tracker.add_experience(experience)
    print("经验已保存！")

    # 7. 验证保存
    print("\n7. 验证保存...")
    tracker2 = ExperimentTracker()
    all_exps = tracker2.get_all_experiences()
    print(f"保存的经验数: {len(all_exps)}")
    if all_exps:
        last_exp = all_exps[-1]
        print(f"最新经验: {last_exp.observation[:50]}...")


if __name__ == "__main__":
    test_workflow_compare()
    test_improvement_analyzer()
    test_experiment_tracker()
    test_full_workflow()

    print("\n" + "=" * 60)
    print("所有测试完成！")
    print("=" * 60)
