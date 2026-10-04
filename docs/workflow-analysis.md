# ComfyUI Workflow Analysis System

Version: v0.4

---

## 1. 概述

Workflow Analysis 是 ComfyUI Learning Companion 的核心能力。

它负责将：

ComfyUI Workflow JSON

转换为：

Workflow Knowledge

简单来说，Workflow Analysis 的目标是让 AI 理解：

- 这个 Workflow 做什么
- 使用了哪些 Node
- 使用了哪些 Model
- 数据如何流动
- 为什么这样设计

---

## 2. Analysis Pipeline

完整分析流程（八级流水线）：

```
Workflow JSON
    │
    ▼
Workflow Parser
    │
    ▼
Node Analyzer
    │
    ▼
Connection Analyzer
    │
    ▼
Model Detector
    │
    ▼
Pipeline Recognition
    │
    ▼
Knowledge Extractor
    │
    ▼
Analysis Report
```

各阶段职责速览：

| 阶段 | 模块 | 输出 |
|-|-|-|
| 1 | Workflow Parser | 基础结构（nodes / links） |
| 2 | Node Analyzer | Node 类型与角色分类 |
| 3 | Connection Analyzer | 执行流程与数据关系 |
| 4 | Model Detector | 模型清单（Base / VAE / LoRA …） |
| 5 | Pipeline Recognition | Workflow 类型判定 |
| 6 | Pattern Detection | 相似度匹配结果 |
| 7 | Knowledge Extractor | 结构化知识对象 |
| 8 | Analysis Report | analysis.md 报告 |

---

## 3. 输入数据

Workflow Analysis 的输入：

`workflow.json`

来源：

- ComfyUI Export
- Community Workflow
- User Experiment

---

## 4. Workflow Parser

### 4.1 功能

Workflow Parser 负责读取原始 Workflow。

主要任务：

- 加载 JSON
- 解析 Node
- 解析 Link
- 建立基础结构

### 4.2 输入

```json
{
  "nodes": [],
  "links": []
}
```

### 4.3 输出

内部结构：

```json
{
  "nodes": [
    {
      "id": 1,
      "type": "KSampler"
    }
  ],
  "links": []
}
```

---

## 5. Node Analyzer

### 5.1 功能

Node Analyzer 分析 Workflow 中的 Node。

识别：

- Node Type
- Node Function
- Input
- Output
- Role

### 5.2 Node 分类

Node 可以分为：

**Model Node**

负责加载 Model。

例如：

- Checkpoint Loader
- UNET Loader
- VAE Loader

**Conditioning Node**

负责 Prompt 和条件控制。

例如：

- CLIP Text Encode
- Conditioning Combine

**Sampling Node**

负责生成过程。

例如：

- KSampler
- SamplerCustom

**Processing Node**

负责图像处理。

例如：

- Upscale
- Image Resize
- Face Restore

**Control Node**

负责控制生成。

例如：

- ControlNet
- IPAdapter
- Pose Control

---

## 6. Connection Analyzer

### 6.1 功能

分析 Node 之间的数据关系。

目标：

理解 Workflow 执行流程。

例如，输入：

```
Checkpoint Loader
        │
        ▼
CLIP Encode
        │
        ▼
KSampler
        │
        ▼
VAE Decode
```

转换为：

```
Pipeline:

Model Loading
    ↓
Prompt Encoding
    ↓
Sampling
    ↓
Decoding
```

---

## 7. Model Detector

### 7.1 功能

识别 Workflow 使用的 Model。

包括：

- Base Model
- VAE
- LoRA
- Control Model
- Embedding

### 7.2 Model Information

提取：

```json
{
  "name": "Flux",
  "type": "diffusion-model",
  "usage": "image-generation"
}
```

---

## 8. Pipeline Recognition

### 8.1 功能

根据 Node 组合判断 Workflow 类型。

例如，检测到：

```
Text Encode
    ↓
Sampler
    ↓
VAE Decode
```

识别为：

```
Pipeline:
Text To Image
```

### 8.2 Pipeline 分类

基础分类：

- text-to-image
- image-to-image
- video-generation
- upscaling
- control-generation
- training

---

## 9. Workflow Pattern Detection

Analysis 系统会尝试匹配已有 Pattern。

流程：

```
Workflow Structure
        │
        ▼
Pattern Comparison
        │
        ▼
Similarity Score
        │
        ▼
Pattern Match
```

例如，发现：

```
90% Similarity

with:
Basic SDXL Pipeline
```

结果：

```
Pattern:
SDXL Basic Generation
```

---

## 10. Analysis Report

最终生成：

`analysis.md`

### 10.1 Report Structure

````markdown
# Workflow Analysis

## Overview

Purpose:
Text To Image

## Models

- Flux

## Pipeline

Text Encoder
    ↓
Sampler
    ↓
VAE Decode

## Important Nodes

- KSampler
- VAE Decode

## Pattern

Basic Generation Pipeline

## Optimization

Possible VRAM optimization:

Reduce resolution
````

---

## 11. Analysis Metadata

分析结果可以保存：

```json
{
  "type": "workflow-analysis",
  "version": "0.4",
  "workflow": "",
  "models": [],
  "nodes": [],
  "patterns": []
}
```

---

## 12. Analysis Rules

**Rule 1: 保留原始 Workflow**

分析不能修改：

`workflow.json`

**Rule 2: 分析结果独立保存**

生成：

`analysis.md`

避免污染原始数据。

**Rule 3: 结果必须可解释**

AI 输出必须回答：

- 为什么这样判断
- 根据什么 Node
- 使用什么 Model

---

## 13. Error Handling

Workflow 可能存在：

**Missing Node**

处理：

Unknown Node

记录：

Unrecognized Node Type

**Missing Model**

处理：

Model Reference Missing

**Broken Connection**

处理：

Invalid Link

---

## 14. Future Improvements

**Automatic Workflow Classification**

自动判断：

- Portrait Workflow
- Anime Workflow
- Video Workflow

**Performance Analysis**

分析：

- VRAM Usage
- Execution Time
- Bottleneck Node

**AI Explanation**

生成：

- Beginner Explanation
- Advanced Explanation
- Technical Explanation

---

## 15. Design Principle

Workflow Analysis 的核心原则：

> 先理解 Workflow，再学习 Workflow。

Workflow Analysis 是连接以下链路的核心桥梁：

```
Raw Workflow
    ↓
Knowledge Base
    ↓
AI Assistant
```
