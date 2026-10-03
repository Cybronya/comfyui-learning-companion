# Workflow Analysis Rules

Version:

0.3.1


# 文件说明（Purpose）


本文件定义 Agent 如何分析 ComfyUI Workflow。


目标：

不是简单读取 Node 列表。

而是理解：

- Workflow 的设计目的
- Node 之间的数据关系
- 技术方案
- 可复用结构



---

# Workflow 分析原则


分析 Workflow 时：

必须从：

```
Node Graph

    ↓

Data Flow

    ↓

Technical Pipeline

    ↓

Design Intent

    ↓

Knowledge Pattern
```


逐层理解。



---

# 第一阶段：Workflow 基础识别


## 1. 基本信息


提取：


- Workflow Name
- File Name
- Author（如果存在）
- Creation Information（如果存在）


---

## 2. 判断 Workflow 类型


根据 Node 和 Model 判断：


可能类型：


### Image Generation


例如：

- txt2img
- img2img


常见组件：

- Checkpoint Loader
- CLIP Text Encode
- KSampler
- VAE Decode



---

### Video Generation


例如：

- Image To Video
- Text To Video


常见组件：

- Video Model Loader
- Temporal Module
- Video VAE
- Frame Processing



---

### Control Workflow


例如：

- ControlNet
- IPAdapter
- Reference Control


特点：

增加额外条件输入。



---

### Enhancement Workflow


例如：

- Upscale
- Detailer
- Face Restore


特点：

对已有结果进行增强。



---

# 第二阶段：Pipeline 分析


将 Node Graph 转换为 Pipeline。


标准结构：

```
Input

    ↓

Condition

    ↓

Model

    ↓

Sampling

    ↓

Decode

    ↓

Output
```


---

# 1. Input 分析


识别输入来源：


例如：


Image:

- Load Image


Text:

- CLIP Text Encode


Latent:

- Empty Latent Image


Video:

- Load Video



需要说明：

输入数据如何进入 Workflow。



---

# 2. Condition 分析


分析条件控制。


包括：


- Prompt
- Negative Prompt
- ControlNet
- LoRA
- Reference Image



说明：

这些条件如何影响生成结果。



---

# 3. Model 分析


识别：


- Checkpoint
- Diffusion Model
- VAE
- Text Encoder


记录：

Model 家族。

例如：


SDXL

Flux

Wan

HunyuanVideo




---

# 4. Sampling 分析


重点分析：


- Sampler
- Scheduler
- Steps
- CFG
- Denoise


说明：

这些参数如何影响效果。



---

# 5. Output 分析


识别：

- Image Output
- Video Output
- Save Node
- Export Node


说明：

最终结果形式。



---

# 第三阶段：Node 分析规则


不要逐个解释所有 Node。


优先分析：


## 核心 Node


例如：

- Model Loader
- Sampler
- Control Node
- VAE
- Important Custom Node



---

## 每个关键 Node 必须回答：


### Node 名称


是什么？



### Function


作用是什么？



### Why


为什么存在？



### Connection


连接哪些 Node？



### Replace


是否可以替代？



---

# 第四阶段：技术路线总结


分析：

这个 Workflow 使用什么技术方案。


例如：


基础生成:

Checkpoint + CLIP + Sampler + VAE

增强:

ControlNet + LoRA

后处理:

Upscale + Detailer




---

# 第五阶段：学习价值分析


回答：


用户从这个 Workflow 可以学习什么？


例如：


- 学习 Wan I2V 基础结构
- 学习 ControlNet 控制方式
- 学习低显存优化方案



---

# 第六阶段：进入 Pattern 分析


判断：

这个 Workflow 是否属于已有 Pattern。


例如：


Wan I2V Basic Pattern

Flux Control Pattern

SDXL Refiner Pattern




如果没有：

创建新的 Pattern 候选。


---

# 分析输出要求


最终输出必须结构化：


Workflow Summary

Pipeline

Important Nodes

Models

Parameters

Technical Features

Learning Value

Related Patterns
