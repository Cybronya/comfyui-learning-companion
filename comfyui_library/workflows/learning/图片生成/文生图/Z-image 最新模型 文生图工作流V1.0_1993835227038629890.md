---
key: 图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json
name: Z-image 最新模型 文生图工作流V1.0_1993835227038629890
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json
hash: a6e24db0a8130e71
coverage: 1
learned_at: 2026-10-19 21:32:57
nodes: [ConditioningZeroOut, UNETLoader, CLIPLoader, EmptyLatentImage, VAEDecode, KSampler, CLIPTextEncode, VAELoader, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 878193908036932, "steps": 20, "width": 1920}
---

# 图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（9 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `878193908036932`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
