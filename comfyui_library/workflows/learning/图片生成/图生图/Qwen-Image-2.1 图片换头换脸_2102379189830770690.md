---
key: 图片生成/图生图/Qwen-Image-2.1 图片换头换脸_2102379189830770690.json
name: Qwen-Image-2.1 图片换头换脸_2102379189830770690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图片换头换脸_2102379189830770690.json
hash: 9d5014d9dda87cca
coverage: 0.882353
learned_at: 2026-10-10 20:48:09
nodes: [QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, EmptyLatentImage, TextGenerateLTX2Prompt, BatchImagesNode, ComfySwitchNode, VAEDecode, LoadImage, LoadImage, KSampler, VAELoader, CLIPLoader, UNETLoader, SaveImage, ResolutionSelector, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3824632082122, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 图片换头换脸_2102379189830770690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图片换头换脸_2102379189830770690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `BatchImagesNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `ResolutionSelector`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `3824632082122`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`QwenImage21Cache`、`TextEncodeQwenImage21`、`CLIPLoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`VAEDecode`、`LoadImage`、`KSampler`、`VAELoader`、`UNETLoader`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
