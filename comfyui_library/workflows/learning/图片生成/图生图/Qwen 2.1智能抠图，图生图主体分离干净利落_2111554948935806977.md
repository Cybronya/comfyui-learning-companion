---
key: 图片生成/图生图/Qwen 2.1智能抠图，图生图主体分离干净利落_2111554948935806977.json
name: Qwen 2.1智能抠图，图生图主体分离干净利落_2111554948935806977
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1智能抠图，图生图主体分离干净利落_2111554948935806977.json
hash: 252da14e0b8d1176
coverage: 0.888889
learned_at: 2026-10-23 11:11:35
nodes: [CLIPLoader, VAELoader, KSampler, Seed (rgthree), ResolutionSelector, EmptyLatentImage, ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenImage21Cache, YUAN_TXTConvertAny, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, ImageInvert, GrowMask, SaveImage, ImageUpscaleWithModel, ImageUpscaleWithModel, ImageUpscaleWithModel, Upscale Model Loader, PreviewImage, LayerMask: BiRefNetUltraV2, JoinImageWithAlpha, InvertMask, YUAN_TXTConvertAny, Text Multiline, LayerUtility: ImageScaleByAspectRatio, Image Comparer (rgthree), LoadImage, ImageConcanate, SaveImageAdvanced, SaveImage, VAEDecode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen 2.1智能抠图，图生图主体分离干净利落_2111554948935806977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1智能抠图，图生图主体分离干净利落_2111554948935806977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（56/63）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`Seed (rgthree)`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`YUAN_TXTConvertAny`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`ImageInvert`、`GrowMask`、`SaveImage`、`ImageUpscaleWithModel`、`Upscale Model Loader`、`JoinImageWithAlpha`、`InvertMask`、`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio`、`LoadImage`、`ImageConcanate`、`SaveImageAdvanced`、`VAEDecode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
