---
key: 平台全量/FireRed-Image-Edit 1.1 无缝扩图+局部重绘_2045831289651073025.json
name: FireRed-Image-Edit 1.1 无缝扩图+局部重绘_2045831289651073025
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FireRed-Image-Edit 1.1 无缝扩图+局部重绘_2045831289651073025.json
hash: c264f49a6d196b9c
coverage: 0.88
learned_at: 2026-11-14 00:26:42
nodes: [Label (rgthree), PrimitiveNode, TextEncodeQwenImageEditPlus, UNETLoader, LoraLoaderModelOnly, VAELoader, KSampler, SaveImage, CustomAddLabel, SaveImage, EmptyLatentImage, VAEDecode, SeedVR2, CLIPTextEncode, RunningHub Deepcleaner, ImageScaleToTotalPixels, ImagePadForOutpaint, DrawMaskOnImage, GetImageSize, ImageScaleToTotalPixels, PreviewImage, CLIPLoader, JjkText, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 344165114698451, "steps": 8, "width": 2048}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FireRed-Image-Edit 1.1 无缝扩图+局部重绘_2045831289651073025.json

> 来源文件 `comfyui_library/workflows/平台全量/FireRed-Image-Edit 1.1 无缝扩图+局部重绘_2045831289651073025.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Label (rgthree)`
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `CustomAddLabel`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SeedVR2`
- `CLIPTextEncode` ★核心
- `RunningHub Deepcleaner`
- `ImageScaleToTotalPixels`
- `ImagePadForOutpaint`
- `DrawMaskOnImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `CLIPLoader`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `344165114698451`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `2048`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`Label (rgthree)`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`SaveImage`、`CustomAddLabel`、`EmptyLatentImage`、`VAEDecode`、`SeedVR2`、`CLIPTextEncode`、`RunningHub Deepcleaner`、`ImageScaleToTotalPixels`、`ImagePadForOutpaint`、`DrawMaskOnImage`、`GetImageSize`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
