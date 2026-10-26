---
key: 图片生成/图生图/Qwen_2.1_抠图_2114260916647841794.json
name: Qwen_2.1_抠图_2114260916647841794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_2.1_抠图_2114260916647841794.json
hash: 3a288d6e655bd42b
coverage: 0.888889
learned_at: 2026-10-26 22:03:32
nodes: [CLIPLoader, VAELoader, KSampler, Seed (rgthree), ResolutionSelector, EmptyLatentImage, ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenImage21Cache, YUAN_TXTConvertAny, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, ImageInvert, GrowMask, SaveImage, ImageUpscaleWithModel, ImageUpscaleWithModel, ImageUpscaleWithModel, Upscale Model Loader, PreviewImage, LayerMask: BiRefNetUltraV2, JoinImageWithAlpha, InvertMask, YUAN_TXTConvertAny, Text Multiline, LayerUtility: ImageScaleByAspectRatio, Image Comparer (rgthree), LoadImage, ImageConcanate, SaveImageAdvanced, SaveImage, VAEDecode, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 67494841199994, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen_2.1_抠图_2114260916647841794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_2.1_抠图_2114260916647841794.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Seed (rgthree)`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `YUAN_TXTConvertAny`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: BiRefNetUltraV2`
- `ImageInvert`
- `GrowMask`
- `SaveImage`
- `ImageUpscaleWithModel`
- `ImageUpscaleWithModel`
- `ImageUpscaleWithModel`
- `Upscale Model Loader`
- `PreviewImage`
- `LayerMask: BiRefNetUltraV2`
- `JoinImageWithAlpha`
- `InvertMask`
- `YUAN_TXTConvertAny`
- `Text Multiline`
- `LayerUtility: ImageScaleByAspectRatio`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ImageConcanate`
- `SaveImageAdvanced`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `67494841199994`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`Seed (rgthree)`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`YUAN_TXTConvertAny`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`ImageInvert`、`GrowMask`、`SaveImage`、`ImageUpscaleWithModel`、`Upscale Model Loader`、`JoinImageWithAlpha`、`InvertMask`、`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio`、`LoadImage`、`ImageConcanate`、`SaveImageAdvanced`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
