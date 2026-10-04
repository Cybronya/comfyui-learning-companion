# ComfyUI Learning Engine API Design

Version: v0.5

---

# 1. 概述


Engine API 定义 Learning Engine 的程序接口。


目标：

让不同模块可以协同工作：

```
Workflow

    |

    v

LearningEngine

    |

    +-------------+

    |             |

    v             v

Skills        Knowledge

    |

    v

Patterns
```


---

# 2. Engine Module Structure


推荐代码结构：

```
engine/

├── learning_engine.py
├── workflow_loader.py
├── skill_router.py
├── knowledge_writer.py
├── pattern_manager.py
└── models.py
```


---

# 3. Core Data Model


Learning Engine 内部使用统一数据结构。


---

## 3.1 WorkflowObject


表示一个 ComfyUI Workflow。

示例：

```python
WorkflowObject(
    id="flux_portrait",
    path="workflow.json",
    nodes=[],
    links=[],
    metadata={}
)
```


字段：

| 字段 | 说明 |
|-|-|
| id | Workflow ID |
| path | 文件路径 |
| nodes | Node 列表 |
| links | 连接关系 |
| metadata | 附加信息 |


## 3.2 AnalysisResult

表示 Workflow 分析结果。

示例：

```python
AnalysisResult(
    workflow_id="flux_portrait",
    models=[],
    nodes=[],
    pipeline="text-to-image",
    patterns=[]
)
```


包含：

- Node Analysis
- Model Detection
- Pipeline Recognition
- Pattern Match


## 3.3 KnowledgeObject

表示生成后的 Knowledge。

示例：

```python
KnowledgeObject(
    type="workflow",
    name="Flux Portrait",
    content="",
    tags=[]
)
```


---

# 4. LearningEngine

核心 Class。

文件：

engine/learning_engine.py

职责：

协调完整学习流程。

## 4.1 初始化

```python
LearningEngine(
    skill_router,
    analyzers,
    knowledge_writer,
    pattern_manager
)
```


## 4.2 learn_workflow()

主要 API。

用途：

学习一个 Workflow。

接口：

```python
learn_workflow(
    workflow_path
)
```


输入：

workflow.json


输出：

```json
{
  "status": "success",
  "workflow": "flux_portrait",
  "knowledge_created": true,
  "pattern_updated": true
}
```


---

# 5. Learning Process

内部执行：

```python
def learn_workflow(path):

    workflow = loader.load(path)

    analysis = analyzer.run(workflow)

    skills = router.select(analysis)

    knowledge = extractor.create(analysis)

    writer.save(knowledge)

    pattern.update(analysis)
```


---

# 6. WorkflowLoader

文件：

engine/workflow_loader.py

职责：

读取 Workflow。


**API**

```python
load_workflow(
    path
)
```


输入：

workflow.json


输出：

WorkflowObject


---

# 7. SkillRouter

文件：

engine/skill_router.py

职责：

决定调用哪些 Skill。


**API**

```python
select_skills(
    workflow_analysis
)
```


返回：

```json
[
  "workflow-analysis",
  "node-understanding",
  "pattern-learning"
]
```


---

# 8. Skill Execution Interface

Skill 应该提供统一接口。

例如：

```python
Skill.execute(
    context
)
```


输入：

SkillContext

输出：

SkillResult


---

# 9. SkillContext

Skill 执行上下文。

示例：

```json
{
  "workflow": "WorkflowObject",
  "analysis": "AnalysisResult",
  "knowledge": "KnowledgeBase"
}
```


---

# 10. KnowledgeWriter

文件：

engine/knowledge_writer.py

职责：

保存学习结果。


**API**

```python
save_knowledge(
    knowledge
)
```


输出：

生成：

```
comfyui_library/

└── knowledge/
    └── workflows/
```


---

# 11. PatternManager

文件：

engine/pattern_manager.py

职责：

管理 Pattern。


**API**

```python
check_pattern()
```


检查是否存在类似 Pattern。

```python
check_pattern(
    analysis
)
```


返回：

```json
{
  "match": true,
  "pattern": "basic-flux"
}
```


**update_pattern()**

更新 Pattern。

```python
update_pattern(
    analysis
)
```


---

# 12. Engine Event Flow

完整事件：

```
WorkflowLoaded

        |

        v

AnalysisStarted

        |

        v

SkillExecuted

        |

        v

KnowledgeCreated

        |

        v

PatternUpdated

        |

        v

LearningCompleted
```


---

# 13. Error Handling API

所有模块统一返回：

EngineResult


格式：

```json
{
  "status": "error",
  "message": "Unknown Node"
}
```


---

# 14. Extension Interface

未来扩展：


**New Analyzer**

例如：

performance_analyzer.py


只需要实现：

```python
analyze(
    workflow
)
```


---

**New Skill**

新增：

```
skills/
└── new-skill
```


无需修改 Engine。


---

**New Knowledge Type**

例如：

```
knowledge/
└── experiments
```


只需增加 Writer。


---

# 15. CLI Interface

未来支持：

**Learn Workflow**

命令：

```bash
python -m engine learn workflow.json
```


**Analyze Workflow**

```bash
python -m engine analyze workflow.json
```


**Update Pattern**

```bash
python -m engine pattern-update
```


---

# 16. Example Usage

Python：

```python
from engine import LearningEngine

engine = LearningEngine()

result = engine.learn_workflow(
    "workflow.json"
)

print(result)
```


输出：

```json
{
  "status": "success",
  "knowledge_created": true
}
```


---

# 17. Design Rules

Engine 不保存知识

错误：

```
engine/
└── flux.md
```


正确：

```
knowledge/
└── workflows/
```


---

Engine 不定义专业知识

Engine 负责：

- 流程
- 调度
- 执行


Skill 和 Knowledge 负责：

专业内容


---

Engine 保持通用

未来：

不仅支持 ComfyUI。

也可以支持：

- Workflow Learning
- Model Research
- Experiment Tracking


---

# 18. Design Principle

Engine API 的核心原则：


> Engine 负责让系统学习，Skill 负责告诉系统如何学习，Knowledge 负责保存学习结果。


最终形成：

```
Data

    ↓

Learning Engine

    ↓

Knowledge

    ↓

Experience

    ↓

AI Capability
```


---

# 19. v0.5 设计链路


现在 v0.5 的软件设计链路已经完整：

```text
docs/

architecture.md
        ↓
skill-system.md
        ↓
learning-engine.md
        ↓
engine-api.md
        ↓
workflow-analysis.md
        ↓
pattern-learning.md
        ↓
knowledge-system.md
```
