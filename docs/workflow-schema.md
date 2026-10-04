# ComfyUI Workflow Knowledge Schema

Version: v0.4

---

# 1. 概述


ComfyUI Learning Companion 使用标准化 Workflow Schema 管理和理解 ComfyUI Workflow。


一个原始 ComfyUI Workflow JSON 只是节点数据。


本项目会进一步扩展为完整 Knowledge Object。


目标：

将：


Workflow File


转换为：


Workflow Knowledge Object



包含：

- Workflow Metadata
- Node Information
- Model Information
- Execution Flow
- Analysis Result
- Pattern Information
- Learning Notes


---

# 2. Workflow Knowledge Structure


标准结构：

```
workflow

├── workflow.json
├── metadata.json
├── analysis.md
├── pattern.json
└── notes.md
```


说明：

| 文件 | 作用 |
|-|-|
| workflow.json | 原始 ComfyUI Workflow |
| metadata.json | 基础信息和标签 |
| analysis.md | AI 分析结果 |
| pattern.json | Workflow Pattern 信息 |
| notes.md | 人工学习记录 |


---

# 3. workflow.json


## 3.1 定义


workflow.json 保存原始 ComfyUI Workflow。


来源：

- ComfyUI Export
- Community Workflow
- User Experiment


示例：

```json
{
  "nodes": [],
  "links": [],
  "groups": []
}
```


该文件保持原始格式。

系统不会修改原始 Workflow。


---

# 4. metadata.json

metadata.json 保存 Workflow 的基础描述信息。

示例：

```json
{
  "name": "Flux Basic Text To Image",
  "category": "text-to-image",
  "model_family": "Flux",
  "difficulty": "beginner",
  "tags": [
    "Flux",
    "txt2img",
    "basic"
  ],
  "author": "",
  "source": "",
  "created": "",
  "updated": ""
}
```


---

# 5. Metadata 字段说明

**name**

Workflow 名称。

示例：

Flux Cinematic Portrait Workflow

**category**

Workflow 类型。

常见分类：

- text-to-image
- image-to-image
- video-generation
- upscaling
- control
- animation
- training

**model_family**

使用的主要 Model。

例如：

- SDXL
- Flux
- Wan
- Stable Diffusion

**difficulty**

学习难度。

标准：

- beginner
- intermediate
- advanced
- expert

**tags**

用于 Knowledge Retrieval 的关键词。

例如：

```json
[
  "portrait",
  "cinematic",
  "controlnet"
]
```


---

# 6. analysis.md

analysis.md 保存 AI 对 Workflow 的理解。

格式建议：

```markdown
# Workflow Analysis

## Purpose

Text to Image generation

## Model

Flux.1

## Pipeline

Text Encoder

    ↓

Sampler

    ↓

VAE Decode

## Important Nodes

- CLIP Text Encode
- KSampler
- VAE Decode

## Optimization

Possible VRAM optimization:

- Reduce resolution
- Use low memory mode
```


---

# 7. Workflow Analysis 内容规范

Analysis 至少包含：

**Purpose**

说明 Workflow 用途。

例如：

用于生成人物肖像图片

**Pipeline**

描述执行流程。

例如：

```
Prompt

    ↓

Conditioning

    ↓

Sampling

    ↓

Decode

    ↓

Output
```


**Important Nodes**

记录关键 Node。

例如：

- KSampler
- ControlNet
- VAE Decode

**Model Usage**

说明 Model 组合。

例如：

```
Base Model:
SDXL

Additional:
ControlNet Depth
```


**Optimization**

记录优化经验。

例如：

```
High VRAM usage detected.

Recommendation:
Use tiled VAE Decode.
```


---

# 8. pattern.json

pattern.json 用于描述 Workflow Pattern。

示例：

```json
{
  "pattern_name": "Basic SDXL Generation",
  "category": "text-to-image",
  "frequency": 85,
  "structure": [
    "Model Loader",
    "Text Encoder",
    "Sampler",
    "VAE Decode"
  ]
}
```


---

# 9. Pattern 字段说明

**pattern_name**

Pattern 名称。

例如：

Basic Flux Pipeline

**category**

Pattern 类型。

例如：

- image-generation
- video-generation
- control
- upscale

**frequency**

该 Pattern 出现频率。

例如：

85

表示：

100 个 Workflow 中约 85 个包含类似结构。

**structure**

Pattern 的核心 Node Flow。

例如：

```
Load Model

    ↓

Encode Prompt

    ↓

Sampling

    ↓

Decode
```


---

# 10. notes.md

notes.md 保存人工学习记录。

例如：

```markdown
# Learning Notes

## Experiment

Tested Flux workflow.

## Result

Good quality portrait generation.

## Problem

High VRAM usage.

## Solution

Reduced resolution.
```


---

# 11. Workflow 生命周期


一个 Workflow 的生命周期：

```
Raw Workflow

      |

      v

Metadata Creation

      |

      v

AI Analysis

      |

      v

Pattern Detection

      |

      v

Knowledge Storage

      |

      v

AI Retrieval
```


---

# 12. Future Extension

未来 Workflow Schema 将支持：


## Semantic Search

通过自然语言搜索 Workflow。

例如：

寻找适合低显存生成动漫图片的 Workflow


---

## Knowledge Graph

建立关系：

```
Workflow

   |

uses

   |

Model

   |

contains

   |

Node

   |

belongs_to

   |

Pattern
```


---

## Automatic Learning

系统自动从大量 Workflow 中学习：

```
1000 Workflows

    ↓

Common Structures

    ↓

Reusable Patterns

    ↓

Expert Knowledge
```


---

# 13. Design Principle

Workflow Schema 的核心原则：


> Workflow 不只是文件，而是一份可学习、可检索、可积累的知识。
