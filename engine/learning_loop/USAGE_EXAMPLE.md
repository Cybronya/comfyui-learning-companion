# Learning Loop 使用示例

## 概述

Learning Loop 模块让 Agent 能够从用户修改 Workflow 的过程中学习，积累经验，从而提供更好的建议。

## 核心组件

### 1. WorkflowComparator - 工作流比较器

比较两个 Workflow 的差异，识别节点变化和参数变化。

```python
from engine.learning_loop import WorkflowComparator, WorkflowSnapshot

comparator = WorkflowComparator()

# 创建快照
old_snapshot = WorkflowSnapshot(
    workflow_id="portrait_workflow",
    timestamp="2026-10-04 10:00:00",
    nodes=["KSampler", "CLIPTextEncode", "VAEDecode"],
    parameters={"steps": 20, "cfg": 7.0, "seed": 123456}
)

new_snapshot = WorkflowSnapshot(
    workflow_id="portrait_workflow",
    timestamp="2026-10-04 11:00:00",
    nodes=["KSampler", "CLIPTextEncode", "VAEDecode", "ControlNet"],
    parameters={"steps": 30, "cfg": 6.5, "seed": 123456}
)

# 比较差异
changes = comparator.compare(old_snapshot, new_snapshot)
print(changes)
```

**输出示例：**
```json
{
  "nodes_changed": ["added:ControlNet"],
  "parameters": {
    "steps": {"old": 20, "new": 30},
    "cfg": {"old": 7.0, "new": 6.5}
  }
}
```

### 2. ImprovementAnalyzer - 改进分析器

分析修改的影响，推断可能的效果。

```python
from engine.learning_loop import ImprovementAnalyzer

analyzer = ImprovementAnalyzer()

changes = {
    "parameters": {
        "steps": {"old": 10, "new": 30},
        "cfg": {"old": 15, "new": 8}
    }
}

observations = analyzer.analyze(changes)
print(observations)
```

**输出示例：**
```
[
  "steps增加，可能提升细节表现",
  "CFG降低，可能减少Prompt过度约束，提升生成质量"
]
```

### 3. ExperimentTracker - 实验跟踪器

保存和检索学习经验。

```python
from engine.learning_loop import ExperimentTracker, LearningExperience

tracker = ExperimentTracker()

experience = LearningExperience(
    workflow_type="image_generation",
    change=WorkflowChange(
        changed_nodes=["added:ControlNet"],
        parameter_changes={"sampler_name": {"old": "euler", "new": "dpmpp_2m"}}
    ),
    observation="采样器从 euler 改为 dpmpp_2m，可能提升生成质量",
    conclusion="采样器优化，建议观察效果",
    tags=["quality", "sampling_method"]
)

tracker.add_experience(experience)

# 获取所有经验
all_experiences = tracker.get_all_experiences()

# 获取统计信息
stats = tracker.get_statistics()
print(f"总经验数: {stats['total_experiences']}")
```

## 完整工作流示例

```python
from engine.learning_loop import (
    WorkflowComparator,
    ImprovementAnalyzer,
    ExperimentTracker,
    WorkflowSnapshot,
    WorkflowChange,
    LearningExperience,
)

def process_workflow_change(old_workflow, new_workflow):
    """
    处理工作流变化，学习经验
    """
    # 1. 比较差异
    comparator = WorkflowComparator()
    changes = comparator.compare(old_workflow, new_workflow)

    # 2. 分析改进
    analyzer = ImprovementAnalyzer()
    observations = analyzer.analyze(changes)

    # 3. 生成结论
    conclusion = analyzer.generate_conclusion(changes, observations)

    # 4. 提取标签
    tags = analyzer.extract_tags(changes)

    # 5. 保存经验
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

    return {
        "changes": changes,
        "observations": observations,
        "conclusion": conclusion,
        "tags": tags
    }

# 使用示例
old = WorkflowSnapshot(
    workflow_id="workflow_1",
    timestamp="2026-10-04 10:00:00",
    nodes=["KSampler", "CLIPTextEncode"],
    parameters={"steps": 10, "cfg": 15}
)

new = WorkflowSnapshot(
    workflow_id="workflow_1",
    timestamp="2026-10-04 11:00:00",
    nodes=["KSampler", "CLIPTextEncode", "VAEDecode"],
    parameters={"steps": 30, "cfg": 8, "width": 512, "height": 768}
)

result = process_workflow_change(old, new)
print(result)
```

## Agent 集成示例

```python
class WorkflowLearningAgent:
    def __init__(self):
        self.comparator = WorkflowComparator()
        self.analyzer = ImprovementAnalyzer()
        self.tracker = ExperimentTracker()

    def analyze_user_modification(self, old_workflow, new_workflow):
        """
        分析用户的修改，学习经验
        """
        # 比较差异
        changes = self.comparator.compare(old_workflow, new_workflow)

        # 分析影响
        observations = self.analyzer.analyze(changes)

        # 生成建议
        suggestions = self.generate_suggestions(changes, observations)

        # 保存经验
        self.save_experience(new_workflow, changes, observations)

        return {
            "changes": changes,
            "observations": observations,
            "suggestions": suggestions
        }

    def generate_suggestions(self, changes, observations):
        """生成具体建议"""
        suggestions = []

        # 根据观察生成建议
        for obs in observations:
            if "细节表现" in obs:
                suggestions.append("建议进一步调整采样器以获得更好的细节")
            elif "Prompt过度约束" in obs:
                suggestions.append("建议优化 Prompt 以获得更自然的效果")

        return suggestions

    def save_experience(self, workflow, changes, observations):
        """保存学习经验"""
        experience = LearningExperience(
            workflow_type=self.get_workflow_type(workflow),
            change=WorkflowChange(
                changed_nodes=changes.get('nodes_changed', []),
                parameter_changes=changes.get('parameters', {})
            ),
            observation="; ".join(observations),
            conclusion=self.analyzer.generate_conclusion(changes, observations),
            tags=self.analyzer.extract_tags(changes)
        )

        self.tracker.add_experience(experience)

    def get_workflow_type(self, workflow):
        """推断工作流类型"""
        nodes = workflow.nodes

        if "ControlNet" in nodes:
            return "controlnet_workflow"
        elif "KSampler" in nodes and "VAEDecode" in nodes:
            return "image_generation"
        else:
            return "unknown_workflow"
```

## 实际应用场景

### 场景 1：参数优化

用户第一次使用 Workflow：
- steps=10, cfg=15
- Agent 建议：提高 steps，降低 cfg

用户修改后：
- steps=30, cfg=8
- Agent 分析：steps增加提升细节，cfg降低减少过度约束
- Agent 记录经验：参数优化，细节与速度的平衡

### 场景 2：添加新组件

用户第一次使用 Workflow：
- 节点：KSampler, CLIPTextEncode, VAEDecode
- Agent 建议：添加 ControlNet

用户添加 ControlNet 后：
- 节点：KSampler, CLIPTextEncode, VAEDecode, ControlNet
- Agent 分析：添加 ControlNet 节点
- Agent 记录经验：新组件引入，建议观察效果

### 场景 3：分辨率调整

用户第一次使用 Workflow：
- width=512, height=768
- Agent 建议：提升分辨率以获得更好细节

用户提升分辨率后：
- width=1024, height=1536
- Agent 分析：分辨率提升，可能影响生成时间和细节
- Agent 记录经验：分辨率优化，需要平衡质量与速度

## 数据持久化

所有学习经验都保存在 `engine/learning_loop/experience_store.json` 文件中。

经验数据结构：
```json
[
  {
    "workflow_type": "image_generation",
    "change": {
      "changed_nodes": ["added:ControlNet"],
      "parameter_changes": {
        "steps": {"old": 20, "new": 30},
        "cfg": {"old": 7.0, "new": 6.5}
      }
    },
    "observation": "steps增加，可能提升细节表现",
    "conclusion": "参数优化，细节与速度的平衡",
    "tags": ["quality", "prompt_control"],
    "timestamp": "2026-10-05 22:45:39"
  }
]
```

## 统计分析

```python
# 获取统计信息
stats = tracker.get_statistics()

print(f"总经验数: {stats['total_experiences']}")
print(f"按工作流类型分布: {stats['by_workflow_type']}")
print(f"按标签分布: {stats['by_tag']}")

# 按类型过滤
portrait_exps = tracker.get_all_experiences(workflow_type="image_generation")

# 获取最近经验
recent = tracker.get_recent_experiences(count=5)
```

## 注意事项

1. **不是训练模型**：Learning Loop 不修改 LLM 权重，不训练神经网络
2. **经验积累**：学习的是 Workflow 经验知识，而非模型权重
3. **持久化存储**：经验保存在 JSON 文件中，可以长期保存
4. **可扩展性**：可以轻松添加新的分析规则和标签类型
