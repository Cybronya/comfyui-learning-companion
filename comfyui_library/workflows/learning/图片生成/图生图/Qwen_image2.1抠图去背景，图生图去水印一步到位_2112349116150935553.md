---
key: 图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json
name: Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json
hash: 521fac1ce6dc3a24
coverage: 0.886364
learned_at: 2026-10-23 11:21:27
nodes: [SaveImage, Image Comparer (rgthree), VAELoader, VAEDecode, UNETLoader, PrimitiveStringMultiline, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, QwenImage21Cache, KSampler, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, GetImageSize, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `GetImageSize`
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
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`SaveImage`、`VAELoader`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`QwenImage21Cache`、`KSampler`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`GetImageSize`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
