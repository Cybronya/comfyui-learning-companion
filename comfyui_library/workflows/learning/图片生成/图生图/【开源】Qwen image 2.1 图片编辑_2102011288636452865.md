---
key: 图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json
name: 【开源】Qwen image 2.1 图片编辑_2102011288636452865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json
hash: c8329ecc4392fe12
coverage: 0.96
learned_at: 2026-10-21 00:46:41
nodes: [KSampler, VAEDecode, CLIPLoader, UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, VAELoader, ComfySwitchNode, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, TextGenerateLTX2Prompt, BatchImagesNode, Text, ResolutionSelector, LoadImage, LoadImage, LoadImage, SaveImageAdvanced, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 172093920626591, "steps": 25, "width": 1024}
---

# 图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ComfySwitchNode`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `BatchImagesNode`
- `Text`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `LoadImage`

## 关键参数

- `seed` = `172093920626591`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`KSampler`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAELoader`、`SaveImage`、`LoadImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`Text`、`ResolutionSelector`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
