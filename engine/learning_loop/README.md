# Workflow Learning Loop

让 Agent 从分析 Workflow 升级到观察 Workflow 的变化 → 理解修改 → 总结经验。

## 概述

当前架构：
```
Workflow → Parser → Analyzer → Diagnostics → Response
```

新增 Learning Loop 后：
```
Workflow → Parser → Analyzer → Diagnostics → Response
                                    ↓
                              User Modification
                                    ↓
                            Workflow Compare
                                    ↓
                          Experience Learning
                                    ↓
                              Better Response
```

## 核心功能

### 1. Workflow Compare

比较两个 Workflow 的差异，识别：
- 节点变化（添加/删除）
- 参数变化（数值变化）

### 2. Improvement Analyzer

分析修改的影响，推断可能的效果：
- steps 增加 → 提升细节
- cfg 降低 → 减少过度约束
- denoise 增加 → 提升修改幅度
- 等等...

### 3. Experiment Tracker

保存和检索学习经验：
- 按工作流类型过滤
- 按标签统计
- 按时间排序
- 持久化存储

## 目录结构

```
engine/learning_loop/
├── __init__.py              # 统一入口
├── models.py                # 数据模型
├── workflow_compare.py      # 工作流比较器
├── improvement_analyzer.py  # 改进分析器
├── experiment_tracker.py    # 实验跟踪器
├── experience_store.json    # 经验存储（空数组）
├── USAGE_EXAMPLE.md         # 使用示例
└── README.md                # 本文档
```

## 快速开始

### 安装

无需额外安装，直接导入：

```python
from engine.learning_loop import (
    WorkflowComparator,
    ExperimentTracker,
    ImprovementAnalyzer,
    WorkflowSnapshot,
    WorkflowChange,
    LearningExperience,
)
```

### 基本使用

```python
# 1. 比较工作流
comparator = WorkflowComparator()
changes = comparator.compare(old_workflow, new_workflow)

# 2. 分析改进
analyzer = ImprovementAnalyzer()
observations = analyzer.analyze(changes)

# 3. 保存经验
tracker = ExperimentTracker()
experience = LearningExperience(
    workflow_type="image_generation",
    change=WorkflowChange(
        changed_nodes=changes.get('nodes_changed', []),
        parameter_changes=changes.get('parameters', {})
    ),
    observation="; ".join(observations),
    conclusion=analyzer.generate_conclusion(changes, observations),
    tags=analyzer.extract_tags(changes)
)
tracker.add_experience(experience)
```

## 数据模型

### WorkflowSnapshot

```python
@dataclass
class WorkflowSnapshot:
    workflow_id: str      # 工作流 ID
    timestamp: str        # 时间戳
    nodes: List[str]      # 节点列表
    parameters: Dict      # 参数字典
```

### WorkflowChange

```python
@dataclass
class WorkflowChange:
    changed_nodes: List[str]      # 变化的节点
    parameter_changes: Dict       # 参数变化
```

### LearningExperience

```python
@dataclass
class LearningExperience:
    workflow_type: str      # 工作流类型
    change: WorkflowChange  # 变化详情
    observation: str        # 观察结果
    conclusion: str         # 结论
    tags: List[str]         # 标签
    timestamp: str          # 时间戳
```

## 测试

运行测试：

```bash
python engine/test_learning_loop.py
```

测试包括：
- Workflow 比较器测试
- 改进分析器测试
- 实验跟踪器测试
- 完整工作流测试

## 示例场景

### 场景 1：参数优化

**第一次使用：**
- steps=10, cfg=15
- Agent 建议：提高 steps，降低 cfg

**用户修改后：**
- steps=30, cfg=8
- Agent 分析：steps增加提升细节，cfg降低减少过度约束
- Agent 记录经验：参数优化，细节与速度的平衡

### 场景 2：添加新组件

**第一次使用：**
- 节点：KSampler, CLIPTextEncode, VAEDecode
- Agent 建议：添加 ControlNet

**用户添加 ControlNet 后：**
- 节点：KSampler, CLIPTextEncode, VAEDecode, ControlNet
- Agent 分析：添加 ControlNet 节点
- Agent 记录经验：新组件引入，建议观察效果

### 场景 3：分辨率调整

**第一次使用：**
- width=512, height=768
- Agent 建议：提升分辨率以获得更好细节

**用户提升分辨率后：**
- width=1024, height=1536
- Agent 分析：分辨率提升，可能影响生成时间和细节
- Agent 记录经验：分辨率优化，需要平衡质量与速度

## 经验存储

所有学习经验保存在 `engine/learning_loop/experience_store.json` 文件中。

经验数据示例：
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

## 统计功能

```python
# 获取所有经验
all_experiences = tracker.get_all_experiences()

# 按类型过滤
portrait_exps = tracker.get_all_experiences(workflow_type="image_generation")

# 获取最近经验
recent = tracker.get_recent_experiences(count=10)

# 获取统计信息
stats = tracker.get_statistics()
# {
#     "total_experiences": 10,
#     "by_workflow_type": {"image_generation": 8, "video_generation": 2},
#     "by_tag": {"quality": 5, "speed": 3, "controlnet": 2}
# }
```

## 与现有模块的集成

### 与 Parser 集成

Parser 可以捕获 widgets_values，保存为 WorkflowSnapshot：

```python
from engine.workflow_parser import Parser

parser = Parser()
workflow_data = parser.parse_workflow(workflow_json)

# 保存快照
snapshot = WorkflowSnapshot(
    workflow_id=workflow_data['id'],
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    nodes=[node['type'] for node in workflow_data['nodes']],
    parameters=workflow_data.get('widgets_values', {})
)
```

### 与 Analyzer 集成

Analyzer 可以使用 Learning Loop 的经验：

```python
from engine.learning_loop import ExperimentTracker

tracker = ExperimentTracker()

# 获取所有经验
all_experiences = tracker.get_all_experiences()

# 根据工作流类型过滤
relevant_experiences = tracker.get_all_experiences(workflow_type="image_generation")

# 基于经验生成建议
for exp in relevant_experiences:
    if "quality" in exp.tags:
        # 可以基于经验生成更智能的建议
        pass
```

## 注意事项

1. **不是训练模型**：Learning Loop 不修改 LLM 权重，不训练神经网络
2. **经验积累**：学习的是 Workflow 经验知识，而非模型权重
3. **持久化存储**：经验保存在 JSON 文件中，可以长期保存
4. **可扩展性**：可以轻松添加新的分析规则和标签类型
5. **隐私保护**：经验存储在本地，不会上传到外部服务器

## 扩展建议

### 1. 添加更多分析规则

在 `ImprovementAnalyzer` 中添加更多参数分析：

```python
def analyze(self, changes, workflow_type=None):
    # 现有分析...
    observations = [...]

    # 新增分析
    if "clip_guidance" in params:
        # 添加 CLIP 指导分析
        pass

    if "refiner" in params:
        # 添加 Refiner 分析
        pass

    return observations
```

### 2. 添加更智能的标签

```python
def extract_tags(self, changes):
    tags = []

    # 基于参数变化提取标签
    for param, change in changes.get('parameters', {}).items():
        if change['new'] > change['old']:
            tags.append("increase")
        elif change['new'] < change['old']:
            tags.append("decrease")

    # 基于工作流类型提取标签
    if "ControlNet" in changes.get('nodes_changed', []):
        tags.append("controlnet")

    return list(set(tags))
```

### 3. 添加经验检索功能

```python
def find_similar_experiences(
    self,
    workflow_type: str,
    tags: List[str] = None
) -> List[LearningExperience]:
    """
    查找相似的经验
    """
    experiences = self.get_all_experiences(workflow_type)

    if tags:
        filtered = []
        for exp in experiences:
            if any(tag in exp.tags for tag in tags):
                filtered.append(exp)
        return filtered

    return experiences
```

## 许可证

与主项目相同。

## 贡献

欢迎提交 Issue 和 Pull Request！
