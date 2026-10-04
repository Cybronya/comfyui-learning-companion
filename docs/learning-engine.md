# ComfyUI Learning Engine Design

Version: v0.5

---

# 1. 概述


Learning Engine 是 ComfyUI Learning Companion 的核心执行系统。


它负责协调：

- Workflow Input
- Skill Execution
- Workflow Analysis
- Knowledge Extraction
- Pattern Learning
- Knowledge Storage


简单理解：


**Skill 告诉 AI 怎么学习**

**Learning Engine 负责执行学习流程**



---

# 2. Learning Engine 定位


在整个系统中的位置：

```
                AI Agent

                   |

                   v

           Learning Engine

                   |

    +--------------+--------------+

    |              |              |

    v              v              v

 Skills       Analyzers      Knowledge

    |              |              |

    +--------------+--------------+

                   |

                   v

          Knowledge Base
```


---

# 3. 核心职责


Learning Engine 主要负责：


## Workflow Learning


读取 Workflow。


例如：


flux_portrait.json



并启动学习流程。


---

## Skill Orchestration


根据任务类型调用对应 Skill。


例如：

```
Workflow Analysis

    |

    v

workflow-analysis Skill
```


---

## Knowledge Generation


将分析结果转换为 Knowledge。


例如：

```
Workflow

    ↓

Analysis

    ↓

Knowledge Object
```


---

## Pattern Update


学习新的 Workflow 后：

检查：


是否存在类似 Pattern


并更新 Pattern Knowledge。


---

# 4. Learning Workflow


完整学习流程：

```
Input Workflow

    |

    v

Workflow Parser

    |

    v

Workflow Analyzer

    |

    v

Skill Router

    |

    v

Knowledge Extractor

    |

    v

Pattern Engine

    |

    v

Knowledge Base Update
```


---

# 5. Input Layer


Learning Engine 的输入：


主要来源：


comfyui_library/workflows/


例如：

```
comfyui_library/

└── workflows/
    └── flux/
        └── portrait.json
```


---

# 6. Workflow Loading


第一阶段：

读取 Workflow。


任务：


- 加载 JSON
- 验证格式
- 检查 Node
- 检查 Connection


输出：


Workflow Object


示例：

```json
{
  "name": "Flux Portrait",
  "nodes": [],
  "links": []
}
```


---

# 7. Skill Router

Skill Router 负责决定：

当前任务需要哪些 Skill。


例如：

输入：

学习这个 Workflow


Router 判断：

需要：

- workflow-analysis
- node-understanding
- model-analysis
- pattern-learning


然后依次调用。


---

# 8. Skill Execution

Skill 不直接操作文件。

Skill 提供：

- Analysis Strategy
- Knowledge Rules
- Output Format


例如：

Workflow Analysis Skill：

```
Input:
Workflow Object

Process:
1. Analyze Nodes
2. Detect Pipeline
3. Identify Models

Output:
Workflow Analysis
```


---

# 9. Analyzer Layer

Analyzer 是实际执行工具。

包括：

**Workflow Parser**

负责：

读取 Workflow JSON


**Node Analyzer**

负责：

- Node Classification
- Node Function Detection


**Model Detector**

负责：

Model Identification


**Pattern Detector**

负责：

Workflow Similarity Analysis


---

# 10. Knowledge Extraction

分析结果需要转换成 Knowledge。

流程：

```
Analysis Result

        |

        v

Knowledge Extractor

        |

        v

Knowledge Object
```


生成：

comfyui_library/knowledge/workflows/


结构：

```
workflow-name/

├── metadata.json
├── analysis.md
├── pattern.json
└── notes.md
```


---

# 11. Pattern Update

每次学习新的 Workflow：

执行：

```
New Workflow

        |

        v

Compare Existing Patterns

        |

        v

Similarity Check

        |

        +------------+

        |            |

        v            v

 Existing       New Pattern

 Update         Create
```


---

# 12. Learning Memory

Learning Engine 需要记录学习过程。

例如：

```json
{
  "workflow": "flux_portrait",
  "status": "completed",
  "skills": [
    "workflow-analysis",
    "pattern-learning"
  ],
  "time": ""
}
```


---

# 13. Error Handling

学习过程中可能出现：


**Invalid Workflow**

处理：

Workflow Validation Failed


---

**Unknown Node**

记录：

Unknown Node Type


并允许继续学习。


---

**Missing Model**

记录：

Model Information Missing


---

# 14. Engine Directory Design

建议结构：

```
engine/

├── learning_engine.py
├── workflow_loader.py
├── skill_router.py
├── knowledge_writer.py
└── pattern_manager.py
```


---

# 15. Learning Engine API Concept

未来接口：

```python
engine.learn_workflow(
    workflow_path
)
```


返回：

```json
{
  "status": "success",
  "knowledge_created": true,
  "patterns_updated": true
}
```


---

# 16. Agent Interaction

用户：

学习这个 Workflow


Agent：

```
调用 Learning Engine

    ↓

读取 Workflow

    ↓

调用 Skills

    ↓

生成 Knowledge

    ↓

更新 Pattern

    ↓

返回学习结果
```


---

# 17. Future Extensions

**Automatic Learning Queue**

支持：

批量 Workflow Learning


例如：

```
1000 workflows

        |

        v

Knowledge Base
```


---

**Continuous Learning**

自动监听：

workflow folder


发现新文件：

自动学习。


---

**Human Feedback Loop**

用户反馈：

- 这个分析正确
- 这个 Pattern 不准确


用于优化 Knowledge。


---

# 18. Design Principle

Learning Engine 的核心原则：


> Skill 定义学习方法，Engine 执行学习流程，Knowledge 保存学习结果。


最终目标：

让 ComfyUI Learning Companion 从一个 Workflow 管理工具，成长为可以持续学习的 AI Agent。


---

# 19. v0.5 文档链（阅读顺序）

到这里，v0.5 的核心逻辑已经补齐：

```text
docs/

architecture.md
        |
        v
skill-system.md
        |
        v
learning-engine.md
        |
        v
workflow-analysis.md
        |
        v
knowledge-system.md
        |
        v
pattern-learning.md
```
