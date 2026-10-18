---
key: 视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json
name: Qwen_image_2.1图片编辑_2104046916651798529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json
hash: 5c91292e427275c6
coverage: 0.903226
learned_at: 2026-10-17 02:29:18
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, ImageConcatMulti, ImageConcatMulti, LoadImage, CLIPLoader, ResolutionSelector, CLIPLoader, BatchImagesNode, easy showAnything, KSampler, SaveImageAdvanced, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImageAdvanced, LoadImage, TextGenerateLTX2Prompt, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_image_2.1图片编辑_2104046916651798529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **90%**（28/31）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageConcatMulti`、`LoadImage`、`CLIPLoader`、`ResolutionSelector`、`BatchImagesNode`、`KSampler`、`SaveImageAdvanced`、`SaveImage`、`TextGenerateLTX2Prompt`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
