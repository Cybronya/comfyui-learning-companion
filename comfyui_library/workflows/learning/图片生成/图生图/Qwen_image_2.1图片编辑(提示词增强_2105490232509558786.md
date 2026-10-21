---
key: 图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105490232509558786.json
name: Qwen_image_2.1图片编辑(提示词增强_2105490232509558786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105490232509558786.json
hash: 82b5108e768795cc
coverage: 0.903226
learned_at: 2026-10-21 00:44:02
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, VAELoader, UNETLoader, QwenImage21Cache, LoadImage, BatchImagesNode, ComfySwitchNode, KSampler, ImageConcatMulti, ImageConcatMulti, SaveImageAdvanced, easy showAnything, VAEDecode, SaveImage, ResolutionSelector, LoadImage, LoadImage, CLIPLoader, EmptyLatentImage, Image Comparer (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105490232509558786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105490232509558786.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `BatchImagesNode`
- `ComfySwitchNode`
- `KSampler` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `easy showAnything`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`BatchImagesNode`、`KSampler`、`ImageConcatMulti`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
