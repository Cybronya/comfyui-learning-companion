---
key: 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 一键换背景_1971395067741192193.json
name: 一键运行：Flux-dev-fp8-ControlNet-Inpainting 一键换背景_1971395067741192193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 一键换背景_1971395067741192193.json
hash: d3c85f1d98d6cfa7
coverage: 0.826087
learned_at: 2026-11-14 01:30:05
nodes: [PreviewImage, ModelSamplingAuraFlow, Prompts Everywhere, PreviewImage, ControlNetInpaintingAliMamaApply, ImageConcanate, Anything Everywhere, GetImageSize, InvertMask, UNETLoader, KSampler (Efficient), CLIPTextEncode, LoadImage, ApplyFBCacheOnModel, VAELoader, CLIPTextEncode, ControlNetLoader, MarkdownNote, EmptyLatentImage, DualCLIPLoader, BiRefNet_Hugo, SaveImage, LayerFilter: HDREffects]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 417849632579646, "steps": 8, "width": 512}
---

# 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 一键换背景_1971395067741192193.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 一键换背景_1971395067741192193.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Process → Output → Other

**节点**（23 个）：
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `Prompts Everywhere`
- `PreviewImage`
- `ControlNetInpaintingAliMamaApply`
- `ImageConcanate`
- `Anything Everywhere`
- `GetImageSize`
- `InvertMask`
- `UNETLoader` ★核心
- `KSampler (Efficient)` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ApplyFBCacheOnModel`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `DualCLIPLoader`
- `BiRefNet_Hugo`
- `SaveImage`
- `LayerFilter: HDREffects`

## 关键参数

- `seed` = `417849632579646`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`ModelSamplingAuraFlow`、`Prompts Everywhere`、`ControlNetInpaintingAliMamaApply`、`ImageConcanate`、`GetImageSize`、`InvertMask`、`UNETLoader`、`KSampler (Efficient)`、`CLIPTextEncode`、`LoadImage`、`ApplyFBCacheOnModel`、`VAELoader`、`ControlNetLoader`、`EmptyLatentImage`、`DualCLIPLoader`、`BiRefNet_Hugo`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、ControlNetInpaintingAliMamaApply、ControlNetLoader、KSampler (Efficient)
