# ComfyUI Skill System Design

Version: v0.4

---

# 1. 概述


ComfyUI Learning Companion 使用 Skill System 作为 AI Agent 的能力扩展机制。


Skill 是一个独立的能力模块。

它定义：

- AI 可以执行什么任务
- 如何处理输入
- 使用哪些 Knowledge
- 输出什么结果


简单理解：


**Skill = AI Agent 的专业能力插件**



例如：


Workflow Analysis Skill

可以：

- 读取 Workflow
- 分析 Node
- 识别 Model
- 生成解释



---

# 2. Skill System 目标


Skill System 主要解决：

## 能力模块化


不同功能独立存在。


例如：

```
comfyui-learning

├── workflow-analysis
├── node-understanding
├── model-analysis
└── pattern-learning
```


---

## Knowledge 解耦


Skill 不直接保存大量知识。


关系：

```
Skill
负责：
如何处理

Knowledge
负责：
存储内容
```


---

## 可扩展


未来可以增加：

```
skills

├── comfyui-learning
├── workflow-optimizer
├── image-quality-analyzer
└── model-manager
```


---

# 3. Skill Architecture


整体结构：

```
AI Agent

    |

    v

Skill Router

    |

    v

Skill Module

    |

    v

Knowledge Base

    |

    v

Result
```


---

# 4. Skill Structure


标准 Skill 结构：

```
skill-name

├── SKILL.md
├── README.md
├── knowledge
├── templates
├── examples
└── tools
```


说明：

| 文件 | 作用 |
|-|-|
| SKILL.md | Skill 核心定义 |
| README.md | 使用说明 |
| knowledge | 关联知识 |
| templates | 输出模板 |
| examples | 示例 |
| tools | 可调用工具 |


---

# 5. SKILL.md


SKILL.md 是 Skill 的核心文件。


作用：

告诉 AI Agent：

- 这个 Skill 是什么。
- 什么时候使用。
- 如何执行。


示例：

```markdown
# Workflow Analysis Skill

## Purpose

Analyze ComfyUI Workflow structure.

## Input

ComfyUI workflow.json

## Process

1. Parse Nodes
2. Detect Models
3. Analyze Connections
4. Generate Explanation

## Output

Workflow Analysis Report
```


---

# 6. Skill 生命周期

Skill 生命周期：

```
Create

    |

    v

Register

    |

    v

Load

    |

    v

Execute

    |

    v

Improve

    |

    v

Update
```


---

# 7. Skill Registry

所有 Skill 通过 Registry 管理。

示例：

```json
{
  "skills": [
    {
      "name": "workflow-analysis",
      "type": "analysis",
      "version": "0.4",
      "enabled": true
    }
  ]
}
```


---

# 8. Core Skill

系统基础 Skill。

目录：

```
skills/_core
```


负责：

**Skill Discovery**

发现可用 Skill。

例如：

```
扫描 skills/

    ↓

找到新的 Skill
```


**Skill Loading**

加载 Skill。

流程：

```
Read SKILL.md

    ↓

Initialize Skill

    ↓

Register Capability
```


**Skill Management**

管理：

- Version
- Status
- Dependency


---

# 9. ComfyUI Learning Skill

核心 Skill：

```
skills/comfyui-learning
```


负责 ComfyUI 学习能力。

包含：

```
comfyui-learning

├── workflow-analysis
├── node-understanding
├── model-analysis
├── pattern-learning
└── knowledge-retrieval
```


---

# 10. Workflow Analysis Skill

**Purpose**

理解 Workflow 结构。

**输入：**

workflow.json


**处理：**

```
Parse Workflow

    ↓

Analyze Nodes

    ↓

Detect Pipeline

    ↓

Generate Explanation
```


**输出：**

analysis.md


---

# 11. Node Understanding Skill

**Purpose**

理解 ComfyUI Node。

**输入：**

Node Information


**输出：**

Node Explanation


字段：

- Function:
- Input:
- Output:
- Usage:
- Optimization:


---

# 12. Model Analysis Skill

**Purpose**

分析 Model 使用。

**输入：**

Model Information


**输出：**

Model Profile


字段：

- Name:
- Type:
- Usage:
- Requirement:
- Optimization:


---

# 13. Pattern Learning Skill

**Purpose**

从多个 Workflow 中发现 Pattern。

**流程：**

```
Multiple Workflows

    ↓

Structure Comparison

    ↓

Similarity Detection

    ↓

Pattern Extraction

    ↓

Pattern Knowledge
```


**输出：**

pattern.json


---

# 14. Knowledge Retrieval Skill

**Purpose**

从 Knowledge Base 查询信息。

**支持：**

**Keyword Search**

例如：

KSampler


**Semantic Search**

例如：

寻找适合低显存的人像 Workflow


**Relationship Search**

例如：

哪些 Workflow 使用 Flux？


---

# 15. Skill 与 Knowledge 的关系

关系：

```
             AI Agent

                 |

                 v

              Skill

                 |

                 v

            Knowledge Base

                 |

                 v

              Result
```


Skill 提供能力。

Knowledge 提供内容。

两者分离：

方便维护和扩展。


---

# 16. Skill Development Rules

新增 Skill 必须：


**独立**

不能依赖其他 Skill 内部实现。


**可解释**

必须说明：

- 输入
- 处理
- 输出


**可复用**

能力应该适用于多个 Workflow。


**可扩展**

未来可以加入：

- Tool
- API
- Model


---

# 17. Future Skill Extensions

未来可能增加：


**Workflow Optimizer Skill**

功能：

- VRAM 优化
- Speed Optimization
- Node Replacement


---

**Workflow Recommendation Skill**

功能：

根据目标推荐方案。


---

**Experiment Memory Skill**

功能：

记录用户实验结果。


---

**ComfyUI Tutor Skill**

功能：

像老师一样解释 ComfyUI。


---

# 18. Design Principle

Skill System 的核心原则：


> Skill 负责思考方式，Knowledge 负责经验内容。


最终目标：

构建一个可以持续学习和扩展的 ComfyUI AI Agent。
