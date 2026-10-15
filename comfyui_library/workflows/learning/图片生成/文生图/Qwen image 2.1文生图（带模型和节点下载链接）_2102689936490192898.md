---
key: 图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json
name: Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json
hash: 6b9c3d92270d59f9
coverage: 0.666667
learned_at: 2026-10-15 22:27:07
nodes: [TextGenerate, RegexExtract, Seed (rgthree), UNETLoader, CLIPLoader, VAELoader, SeedVR2LoadVAEModel, SaveImage, SeedVR2LoadDiTModel, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, PreviewImage, VAEDecode, SaveImage, PrimitiveStringMultiline, EmptyLatentImage, PreviewAny, ResolutionSelector, StringConcatenate, TextEncodeQwenImage21, Any Switch (rgthree), PrimitiveStringMultiline, Note, PreviewImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1090322292188015, "steps": 35, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `TextGenerate`
- `RegexExtract`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `ResolutionSelector`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `Any Switch (rgthree)`
- `PrimitiveStringMultiline`
- `Note`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1090322292188015`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（18/27）

**有卡**：`TextGenerate`、`RegexExtract`、`Seed (rgthree)`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`StringConcatenate`、`TextEncodeQwenImage21`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
