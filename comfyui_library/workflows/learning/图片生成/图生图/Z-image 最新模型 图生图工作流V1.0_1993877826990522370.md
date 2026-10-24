---
key: 图片生成/图生图/Z-image 最新模型 图生图工作流V1.0_1993877826990522370.json
name: Z-image 最新模型 图生图工作流V1.0_1993877826990522370
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image 最新模型 图生图工作流V1.0_1993877826990522370.json
hash: 8566519b0e252b81
coverage: 0.916667
learned_at: 2026-10-23 11:30:27
nodes: [ConditioningZeroOut, UNETLoader, CLIPLoader, VAEDecode, VAELoader, EmptyLatentImage, CLIPTextEncode, SaveImage, easy showAnything, KSampler, LoadImage, AILab_QwenVL]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 683187181284474, "steps": 10, "width": 1080}
---

# 图片生成/图生图/Z-image 最新模型 图生图工作流V1.0_1993877826990522370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image 最新模型 图生图工作流V1.0_1993877826990522370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy showAnything`
- `KSampler` ★核心
- `LoadImage`
- `AILab_QwenVL`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `683187181284474`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`SaveImage`、`KSampler`、`LoadImage`、`AILab_QwenVL`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
