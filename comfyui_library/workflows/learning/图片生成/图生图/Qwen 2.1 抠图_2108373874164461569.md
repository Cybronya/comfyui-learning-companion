---
key: 图片生成/图生图/Qwen 2.1 抠图_2108373874164461569.json
name: Qwen 2.1 抠图_2108373874164461569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1 抠图_2108373874164461569.json
hash: 689431f7c7b2c828
coverage: 0.911765
learned_at: 2026-10-21 00:41:58
nodes: [CLIPLoader, VAELoader, KSampler, Seed (rgthree), ResolutionSelector, EmptyLatentImage, ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenImage21Cache, YUAN_TXTConvertAny, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, ImageInvert, GrowMask, SaveImage, ImageUpscaleWithModel, ImageUpscaleWithModel, ImageUpscaleWithModel, Upscale Model Loader, PreviewImage, LayerMask: BiRefNetUltraV2, JoinImageWithAlpha, InvertMask, YUAN_TXTConvertAny, Text Multiline, LayerUtility: ImageScaleByAspectRatio, Image Comparer (rgthree), LoadImage, ImageConcanate, SaveImageAdvanced, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 723018564233342, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen 2.1 抠图_2108373874164461569.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1 抠图_2108373874164461569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
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

## 关键参数

- `seed` = `723018564233342`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`Seed (rgthree)`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`YUAN_TXTConvertAny`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`ImageInvert`、`GrowMask`、`SaveImage`、`ImageUpscaleWithModel`、`Upscale Model Loader`、`JoinImageWithAlpha`、`InvertMask`、`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio`、`LoadImage`、`ImageConcanate`、`SaveImageAdvanced`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
