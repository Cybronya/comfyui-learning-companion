---
key: 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 局部重绘，图像修复_1970306684570791937.json
name: 一键运行：Flux-dev-fp8-ControlNet-Inpainting 局部重绘，图像修复_1970306684570791937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 局部重绘，图像修复_1970306684570791937.json
hash: 6c8f355678367310
coverage: 0.826087
learned_at: 2026-11-14 01:30:05
nodes: [PreviewImage, GetImageSize, PreviewImage, ControlNetInpaintingAliMamaApply, Anything Everywhere, KSampler (Efficient), CLIPTextEncode, Prompts Everywhere, CLIPTextEncode, UNETLoader, GrowMaskWithBlur, ModelSamplingAuraFlow, ApplyFBCacheOnModel, DualCLIPLoader, LoadImage, LoraLoaderModelOnly, ControlNetLoader, VAELoader, EmptyLatentImage, MarkdownNote, ImageConcanate, SaveImage, LayerFilter: HDREffects]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 380920747639698, "steps": 20, "width": 512}
---

# 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 局部重绘，图像修复_1970306684570791937.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 局部重绘，图像修复_1970306684570791937.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Process → Output → Other

**节点**（23 个）：
- `PreviewImage`
- `GetImageSize`
- `PreviewImage`
- `ControlNetInpaintingAliMamaApply`
- `Anything Everywhere`
- `KSampler (Efficient)` ★核心
- `CLIPTextEncode` ★核心
- `Prompts Everywhere`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `GrowMaskWithBlur`
- `ModelSamplingAuraFlow`
- `ApplyFBCacheOnModel`
- `DualCLIPLoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `ImageConcanate`
- `SaveImage`
- `LayerFilter: HDREffects`

## 关键参数

- `seed` = `380920747639698`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`GetImageSize`、`ControlNetInpaintingAliMamaApply`、`KSampler (Efficient)`、`CLIPTextEncode`、`Prompts Everywhere`、`UNETLoader`、`GrowMaskWithBlur`、`ModelSamplingAuraFlow`、`ApplyFBCacheOnModel`、`DualCLIPLoader`、`LoadImage`、`LoraLoaderModelOnly`、`ControlNetLoader`、`VAELoader`、`EmptyLatentImage`、`ImageConcanate`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、ControlNetInpaintingAliMamaApply、ControlNetLoader
