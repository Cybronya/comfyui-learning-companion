---
key: 图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json
name: Qwen image2.1-多功能图像编辑_2104767444010225665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json
hash: b6bfe656e3390a3f
coverage: 0.823529
learned_at: 2026-10-21 00:43:02
nodes: [LoadImage, QwenImage21Cache, LoraLoaderModelOnly, CLIPLoader, TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, VAELoader, UNETLoader, Note, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SaveImage, PreviewImage, VAEDecode, Image Comparer (rgthree), Seed (rgthree), ComfySwitchNode, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 153485762872202, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoadImage`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Seed (rgthree)`
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `153485762872202`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`LoadImage`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`CLIPLoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`SaveImage`、`VAEDecode`、`Seed (rgthree)`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
