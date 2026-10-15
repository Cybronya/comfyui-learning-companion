---
key: 图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json
name: Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json
hash: c631dbaf6d63c6ee
coverage: 0.870968
learned_at: 2026-10-10 21:27:51
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, VAELoader, UNETLoader, QwenImage21Cache, LoadImage, BatchImagesNode, ComfySwitchNode, KSampler, ImageConcatMulti, ImageConcatMulti, SaveImageAdvanced, VAEDecode, SaveImage, ResolutionSelector, ImageResizeKJv2, LoadImage, LoadImage, CLIPLoader, EmptyLatentImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, TextGenerateLTX2Prompt, easy showAnything]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json`

## 结构

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
- `UNETLoader`
- `QwenImage21Cache`
- `LoadImage`
- `BatchImagesNode`
- `ComfySwitchNode`
- `KSampler`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `VAEDecode`
- `SaveImage`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `easy showAnything`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `999`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`BatchImagesNode`、`ComfySwitchNode`、`KSampler`、`ImageConcatMulti`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`ImageResizeKJv2`、`EmptyLatentImage`、`Image Comparer (rgthree)`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
