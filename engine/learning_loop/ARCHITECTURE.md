# Learning Loop 架构设计

## 整体架构

```
┌─────────────────────────────────────────────────────────────────┐
│                         Workflow                                  │
│                   (用户上传/编辑的工作流)                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Workflow Parser                             │
│                  (解析工作流，提取节点和参数)                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Graph Understanding                            │
│                  (图结构理解，连接分析)                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Diagnostics                                │
│                   (参数检测，图检查，质量检查)                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Response Generator                          │
│                   (生成诊断结果和建议)                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      User Modification                           │
│              (用户根据建议修改工作流)                              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Learning Loop (NEW)                              │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Workflow Compare                                        │   │
│  │  (比较新旧工作流，识别变化)                               │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                    │
│                              ▼                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Improvement Analyzer                                    │   │
│  │  (分析修改影响，推断效果)                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                    │
│                              ▼                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Experiment Tracker                                      │   │
│  │  (保存经验，支持检索)                                     │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Better Response                             │
│         (基于经验提供更智能的建议)                                │
└─────────────────────────────────────────────────────────────────┘
```

## 模块详解

### 1. Workflow Compare

**职责**：比较两个工作流的差异

**输入**：
- 旧工作流快照 (`WorkflowSnapshot`)
- 新工作流快照 (`WorkflowSnapshot`)

**输出**：
```python
{
    "nodes_changed": [
        "added:ControlNet",
        "removed:OldNode"
    ],
    "parameters": {
        "steps": {"old": 20, "new": 30},
        "cfg": {"old": 7.0, "new": 6.5}
    }
}
```

**实现**：
- 节点比较：使用集合操作
- 参数比较：逐个字段比较值

### 2. Improvement Analyzer

**职责**：分析修改的影响，推断可能的效果

**分析规则**：

| 参数 | 变化 | 影响 |
|------|------|------|
| steps | 增加 | 提升细节表现 |
| steps | 减少 | 提升生成速度 |
| cfg | 增加 | 增强Prompt约束 |
| cfg | 减少 | 减少过度约束，提升质量 |
| seed | 改变 | 生成结果不同 |
| sampler_name | 改变 | 影响生成风格 |
| denoise | 增加 | 提升修改幅度 |
| denoise | 减少 | 减少修改幅度 |
| width/height | 增加 | 提升分辨率，影响时间和细节 |

**实现**：
- 规则匹配：基于参数名称和变化方向
- 上下文感知：根据工作流类型调整分析
- 可扩展性：易于添加新规则

### 3. Experiment Tracker

**职责**：保存和检索学习经验

**数据结构**：
```python
@dataclass
class LearningExperience:
    workflow_type: str          # 工作流类型
    change: WorkflowChange      # 变化详情
    observation: str            # 观察结果
    conclusion: str             # 结论
    tags: List[str]             # 标签
    timestamp: str              # 时间戳
```

**功能**：
- 添加经验
- 按类型过滤
- 按时间排序
- 统计分析
- 持久化存储

**存储位置**：
- 文件：`engine/learning_loop/experience_store.json`

## 数据流

```
用户上传/编辑 Workflow
        ↓
Parser 解析并创建 WorkflowSnapshot
        ↓
Analyzer 分析工作流
        ↓
Diagnostics 检测问题
        ↓
Response Generator 生成建议
        ↓
用户根据建议修改 Workflow
        ↓
创建新的 WorkflowSnapshot
        ↓
┌─────────────────────────────────────┐
│ Workflow Compare                    │
│ - 比较新旧快照                      │
│ - 识别节点变化                      │
│ - 识别参数变化                      │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ Improvement Analyzer                │
│ - 分析参数变化                      │
│ - 推断可能效果                      │
│ - 生成观察结果                      │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ Experiment Tracker                  │
│ - 创建 LearningExperience            │
│ - 保存到文件                        │
│ - 支持检索和统计                    │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ Better Response                     │
│ - 基于经验提供更智能建议            │
│ - 考虑用户的历史修改                │
│ - 提供个性化推荐                    │
└─────────────────────────────────────┘
```

## 使用场景

### 场景 1：首次使用

```
用户上传 Workflow
    ↓
Parser 解析
    ↓
Analyzer 分析
    ↓
Diagnostics 检测
    ↓
Response 建议
    ↓
用户修改 Workflow
    ↓
Learning Loop 记录经验
    ↓
下次使用时提供更好的建议
```

### 场景 2：迭代优化

```
第1次使用：
- steps=10, cfg=15
- 建议：提高 steps，降低 cfg

第2次使用：
- steps=30, cfg=8
- Learning Loop 记录：参数优化，细节与速度的平衡

第3次使用：
- 基于历史经验，提供更精准的建议
```

### 场景 3：组件学习

```
第1次使用：
- 节点：KSampler, CLIPTextEncode, VAEDecode
- 建议：添加 ControlNet

第2次使用：
- 添加 ControlNet
- Learning Loop 记录：新组件引入，建议观察效果

第3次使用：
- 基于经验，知道用户已使用 ControlNet
- 提供更具体的 ControlNet 配置建议
```

## 与其他模块的集成

### 1. 与 Parser 集成

```python
from engine.workflow_parser import Parser
from engine.learning_loop import WorkflowSnapshot

# 解析工作流
parser = Parser()
workflow_data = parser.parse_workflow(workflow_json)

# 创建快照
snapshot = WorkflowSnapshot(
    workflow_id=workflow_data['id'],
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    nodes=[node['type'] for node in workflow_data['nodes']],
    parameters=workflow_data.get('widgets_values', {})
)

# 保存快照用于比较
save_workflow_snapshot(snapshot)
```

### 2. 与 Analyzer 集成

```python
from engine.learning_loop import ExperimentTracker

tracker = ExperimentTracker()

# 获取相关经验
experiences = tracker.get_all_experiences(workflow_type="image_generation")

# 基于经验调整分析
for exp in experiences:
    if "quality" in exp.tags:
        # 调整质量检查的严格程度
        pass
```

### 3. 与 Response Generator 集成

```python
from engine.response_generator import PromptBuilder

# 加载历史经验
tracker = ExperimentTracker()
experiences = tracker.get_all_experiences()

# 将经验注入到 Prompt 中
prompt_builder = PromptBuilder()
prompt = prompt_builder.build_prompt(
    workflow=workflow,
    experiences=experiences  # 注入经验
)
```

## 扩展点

### 1. 添加新的分析规则

在 `improvement_analyzer.py` 中：

```python
def analyze(self, changes, workflow_type=None):
    # 现有分析...

    # 新增：分析预处理器参数
    if "preprocessor" in params:
        old = params["preprocessor"]["old"]
        new = params["preprocessor"]["new"]

        if old != new:
            observations.append(
                f"预处理器从 {old} 改为 {new}，可能影响边缘检测质量"
            )

    # 新增：分析 Refiner 参数
    if "refiner" in params:
        old = params["refiner"]["old"]
        new = params["refiner"]["new"]

        if new and not old:
            observations.append("启用 Refiner，可能提升最终质量")
        elif old and not new:
            observations.append("禁用 Refiner，可能提升生成速度")

    return observations
```

### 2. 添加新的标签类型

```python
def extract_tags(self, changes):
    tags = []

    # 现有标签...

    # 新增：基于参数值提取标签
    for param, change in changes.get('parameters', {}).items():
        if param == "width":
            if change['new'] >= 1024:
                tags.append("high_res")
            else:
                tags.append("low_res")

    # 新增：基于变化幅度提取标签
    for param, change in changes.get('parameters', {}).items():
        if param == "steps":
            ratio = change['new'] / change['old']
            if ratio > 2:
                tags.append("significant_change")

    return list(set(tags))
```

### 3. 添加经验检索功能

```python
def find_similar_experiences(
    self,
    workflow_type: str,
    tags: List[str] = None,
    limit: int = 5
) -> List[LearningExperience]:
    """
    查找相似的经验
    """
    experiences = self.get_all_experiences(workflow_type)

    if tags:
        # 按标签匹配
        filtered = [
            exp for exp in experiences
            if any(tag in exp.tags for tag in tags)
        ]
        return filtered[:limit]

    return experiences[:limit]
```

## 性能考虑

1. **存储优化**：经验数据量不大，直接存储为 JSON
2. **检索优化**：使用列表存储，支持简单过滤
3. **内存管理**：经验数据加载到内存，可以按需加载
4. **持久化**：定期保存，避免内存丢失

## 安全性

1. **本地存储**：经验存储在本地，不上传到外部服务器
2. **隐私保护**：不存储敏感信息（如 Prompt 内容）
3. **可删除**：提供清空功能，用户可以删除所有经验

## 未来扩展

1. **机器学习**：基于历史经验训练推荐模型
2. **可视化**：展示经验积累的图表
3. **分享**：支持经验分享和社区学习
4. **导出**：支持导出经验到其他格式

## 总结

Learning Loop 是一个轻量级、可扩展的模块，它通过记录和积累用户修改工作流的经验，让 Agent 能够提供更智能、更个性化的建议。它不修改模型权重，而是学习 Workflow 的经验知识，类似于人类的"从实践中学习"。
