---
key: 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2113474052353519617.json
name: Qwen-Image-2.1人物换头+图片换脸_2113474052353519617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2113474052353519617.json
hash: 7640f1159390cd7a
coverage: 0.888889
learned_at: 2026-10-26 22:03:23
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, UNETLoader, JjkText, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, SaveImage, LoadImage, TextEncodeQwenImage21, BatchImagesNode, LoadImage, GetImageSize, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 265702111907315, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2113474052353519617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2113474052353519617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `JjkText`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `BatchImagesNode`
- `LoadImage`
- `GetImageSize`
- `ResolutionSelector`

## 关键参数

- `seed` = `265702111907315`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`、`BatchImagesNode`、`GetImageSize`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
