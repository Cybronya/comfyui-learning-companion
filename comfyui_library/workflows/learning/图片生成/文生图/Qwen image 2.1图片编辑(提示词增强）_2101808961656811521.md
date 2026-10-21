---
key: 图片生成/文生图/Qwen image 2.1图片编辑(提示词增强）_2101808961656811521.json
name: Qwen image 2.1图片编辑(提示词增强）_2101808961656811521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1图片编辑(提示词增强）_2101808961656811521.json
hash: 12c90bfd494ee6d0
coverage: 0.903226
learned_at: 2026-10-20 01:51:11
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, VAELoader, UNETLoader, QwenImage21Cache, LoadImage, BatchImagesNode, ComfySwitchNode, KSampler, ImageConcatMulti, ImageConcatMulti, SaveImageAdvanced, easy showAnything, VAEDecode, SaveImage, ResolutionSelector, ImageResizeKJv2, LoadImage, LoadImage, CLIPLoader, EmptyLatentImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1图片编辑(提示词增强）_2101808961656811521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1图片编辑(提示词增强）_2101808961656811521.json`

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
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`

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

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`BatchImagesNode`、`KSampler`、`ImageConcatMulti`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`ImageResizeKJv2`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
