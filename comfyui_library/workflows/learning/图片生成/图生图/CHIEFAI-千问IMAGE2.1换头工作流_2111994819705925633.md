---
key: 图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json
name: CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json
hash: 7652a730cbd64f3b
coverage: 0.916667
learned_at: 2026-10-23 10:51:49
nodes: [LoraLoaderModelOnly, VAEDecode, UNETLoader, KSampler, SaveImage, LoadImage, VAELoader, CLIPLoader, PrimitiveStringMultiline, TextEncodeQwenImage21, LoadImage, Get resolution [Crystools]]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 860467842800150, "steps": 25}
---

# 图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `LoadImage`
- `Get resolution [Crystools]`

## 关键参数

- `seed` = `860467842800150`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`KSampler`、`SaveImage`、`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`Get resolution [Crystools]`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
