---
key: 图片生成/图生图/Qwen image 2.1图片编辑_2102212076977606658.json
name: Qwen image 2.1图片编辑_2102212076977606658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑_2102212076977606658.json
hash: fa33e3cb5fc1746c
coverage: 0.931034
learned_at: 2026-10-10 20:48:08
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, ImageConcatMulti, ImageConcatMulti, LoadImage, CLIPLoader, ResolutionSelector, CLIPLoader, BatchImagesNode, easy showAnything, KSampler, SaveImageAdvanced, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImageAdvanced, LoadImage, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1图片编辑_2102212076977606658.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑_2102212076977606658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `CLIPLoader`
- `ResolutionSelector`
- `CLIPLoader`
- `BatchImagesNode`
- `easy showAnything`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `LoadImage`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageConcatMulti`、`LoadImage`、`CLIPLoader`、`ResolutionSelector`、`BatchImagesNode`、`KSampler`、`SaveImageAdvanced`、`SaveImage`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
