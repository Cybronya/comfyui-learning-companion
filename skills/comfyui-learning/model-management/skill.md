# Model Management Skill


## Skill Purpose


Model Management Skill 用于让 AI Agent 理解 ComfyUI 模型生态。


负责：

- 扫描模型文件
- 分类模型类型
- 建立模型数据库
- 分析模型依赖


---


# Core Ability


Agent 可以回答：


用户：

> 我的 Workflow 缺少什么模型？


Agent：


检查：

workflow_manifest + model_database


返回：

```
Missing:
Wan2.1_VAE

Location:
models/vae/
```



---


# Supported Models


主要管理：


## Checkpoint


路径：


models/checkpoints/


例如：


SD1.5

SDXL

Flux



---


## Diffusion Models


路径：


models/diffusion_models/


例如：


Wan

HunyuanVideo

LTX



---


## VAE


路径：


models/vae/



---


## Text Encoder


路径：


models/text_encoders/



---


## LoRA


路径：


models/loras/



---


## ControlNet


路径：


models/controlnet/



---


# Pipeline

```
models/

    ↓

scan

    ↓

identify

    ↓

metadata

    ↓

database

    ↓

Agent Search
```



---


# Design Principle


自动扫描：

负责：

- 文件发现
- 类型判断
- 基础信息


人工确认：

负责：

- 质量评价
- 推荐用途
- 风格标签
