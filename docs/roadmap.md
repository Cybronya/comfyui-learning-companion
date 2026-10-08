# ComfyUI Learning Companion Roadmap

本文是**全项目唯一的版本号权威来源**。
`README.md` 与根目录 `AGENTS.md` 均只做指针，不重复维护版本表 —— 2026-10-05 之前
`CHANGELOG.md` / `README.md` / 本文三处各有一套版本号且互相矛盾（v0.2 与 v0.5 含义都不同），
已删除 `CHANGELOG.md` 并把版本号收敛到此。

版本号是**规划中的阶段**，不是 git 发布标记（仓库目前无 tag）。对外发布时用
`git tag` + GitHub Releases 承载 release notes。实时开发进度见 `AGENTS.md` 第 9 节。

---

# 1. 项目发展目标


ComfyUI Learning Companion 的最终目标：

构建一个能够理解、学习和辅助用户使用 ComfyUI 的 AI Agent。


发展路径：

```
Workflow Collection

    ↓

Workflow Understanding

    ↓

Knowledge Extraction

    ↓

Pattern Learning

    ↓

AI Assistant

    ↓

Personal ComfyUI Expert
```


---

# 2. Development Philosophy


项目开发遵循：


## Knowledge First


优先建立知识体系。


原因：

AI 能力依赖高质量 Knowledge。


---

## Incremental Learning


通过持续积累增强能力。


不是一次性构建完成。


---

## Human + AI Collaboration


AI 负责：

- 分析
- 整理
- 发现规律


用户负责：

- 验证
- 创造
- 提供经验


---

# 3. Version Overview

> **本表是全项目唯一的版本号权威来源。** `README.md` 不再重复列版本，只做指针；
> 仓库无 git tag，版本号表示「作者规划中的阶段」而非可验证的发布标记。
> 实时开发进度（哪些模块已落地、待办优先级）见根目录 `AGENTS.md` 第 9 节。

| Version | Goal | Status |
|-|-|-|
| v0.1 | Skill Framework | Completed |
| v0.2 | Workflow Understanding | Completed |
| v0.3 | Pattern Learning Design | Completed |
| v0.4 | Architecture Standardization | Completed |
| v0.5 | Workflow Analysis Engine | Current（引擎 14 个子包全部落地，agent_core 六阶段端到端跑通，对外入口与 CLI 已完成 2026-10-08）|
| v0.6 | Pattern Learning Engine | Planned |
| v0.7 | Knowledge Retrieval System | Planned |
| v0.8 | Experiment Memory System | Planned（对应 `engine/learning_loop/`，已有雏形）|
| v0.9 | AI ComfyUI Tutor | Planned（对应 `engine/response_generator/`，已有雏形）|
| v1.0 | Personal ComfyUI Expert | Future |


---

# 4. v0.1 - Skill Framework


## Goal


建立 AI Agent Skill 基础结构。


完成内容：


- Skill Directory
- Skill Definition
- Skill Loading Concept
- Skill Registry Design


输出：

```
skills/

├── _core
└── comfyui-learning
```


---

# 5. v0.2 - Workflow Understanding


## Goal


让 AI 能够理解 ComfyUI Workflow。


完成内容：


- Workflow Analysis Concept
- Node Understanding
- Model Understanding
- Workflow Explanation


能力：


输入：


workflow.json



输出：


analysis.md



---

# 6. v0.3 - Pattern Learning Design


## Goal


从 Workflow 中发现重复结构。


完成内容：


- Pattern Concept
- Similarity Analysis Design
- Pattern Knowledge Structure


实现目标：

```
Many Workflows

    ↓

Common Pattern

    ↓

Reusable Knowledge
```


---

# 7. v0.4 - Architecture Standardization


## Goal


将项目从 Prototype 转换为 Framework。


完成内容：


## Documentation


新增：

```
docs/

├── architecture.md
├── workflow-schema.md
├── knowledge-system.md
├── skill-system.md
├── workflow-analysis.md
├── pattern-learning.md
└── roadmap.md
```


---

## Standardization


定义：

- Workflow Schema
- Knowledge Structure
- Skill Structure
- Pattern Format


---

## Purpose


为后续代码实现建立标准。


---

# 8. v0.5 - Workflow Analysis Engine


目标：

实现真正的 Workflow Scanner。


主要功能：


## Workflow Parser


读取：


workflow.json



解析：

- Nodes
- Links
- Parameters


---

## Node Analyzer


自动识别：


- Node Type
- Node Function
- Node Category


---

## Model Detector


识别：


- Checkpoint
- LoRA
- VAE
- Control Model


---

## Analysis Generator


自动生成：


analysis.md



---

# 9. v0.6 - Pattern Learning Engine


目标：

让系统自动发现 Workflow Pattern。


主要功能：


## Workflow Similarity


比较：

- Node Structure
- Connection Flow
- Model Usage


---

## Pattern Extraction


自动生成：


pattern.json



---

## Pattern Knowledge Base


保存：


- Common Pipeline
- Best Practice
- Optimization Strategy


---

# 10. v0.7 - Knowledge Retrieval System


目标：

让 AI 可以快速查询知识。


功能：


## Keyword Search


例如：


KSampler



返回：

- Node Knowledge
- Examples


---

## Semantic Search


例如：

用户：


低显存生成图片的方法



返回：

相关：

- Workflow
- Pattern
- Optimization


---

## RAG Integration


加入：


Knowledge Base + Embedding + Vector Search


实现 AI Knowledge Retrieval。


---

# 11. v0.8 - Experiment Memory System


目标：

记录用户实验经验。


保存：


- 使用过的 Workflow
- 参数变化
- 成功案例
- 失败案例


形成：


Personal Experience Database



---

# 12. v0.9 - AI ComfyUI Tutor


目标：

成为学习助手。


能力：


## Explain Workflow


例如：


解释这个 Workflow



---

## Teach Concept


例如：


什么是 Latent？



---

## Suggest Improvement


例如：


如何提高图片质量？



---

# 13. v1.0 - Personal ComfyUI Expert


最终目标。


AI 具备：


## Workflow Understanding


理解任何 Workflow。


---

## Knowledge Memory


记住用户经验。


---

## Optimization Ability


提出改进建议。


---

## Creative Assistance


帮助设计新的 Workflow。


---

# 14. Future Vision


未来系统：

```
User

    |

    v

AI ComfyUI Expert

    |

    +----------------+

    |                |

Knowledge        Experience

    |                |

Patterns        Experiments

    |                |

Workflows        Improvements
```


---

# 15. Contribution Direction


社区可以贡献：


## Workflow Collection


提供：

- 优秀 Workflow
- 实验案例


---

## Knowledge Writing


贡献：

- Node Explanation
- Model Guide
- Optimization Tips


---

## Pattern Discovery


帮助发现：

- 新 Pipeline
- 新方法


---

# 16. Design Principle


项目长期原则：


> 不只是管理 Workflow，而是让 Workflow 成为可以学习和进化的知识。


最终目标：

建立一个持续成长的 ComfyUI AI Learning Ecosystem。
