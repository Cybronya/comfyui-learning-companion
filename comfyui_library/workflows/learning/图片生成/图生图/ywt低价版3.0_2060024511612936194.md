---
key: 图片生成/图生图/ywt低价版3.0_2060024511612936194.json
name: ywt低价版3.0_2060024511612936194
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ywt低价版3.0_2060024511612936194.json
hash: 8de75fc251b30b6d
coverage: 0.888889
learned_at: 2026-10-23 11:46:24
nodes: [SaveImage, SaveImage, PreviewImage, PreviewImage, SaveImage, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, CFGNorm, ImageScaleToTotalPixels, VAEEncode, KSampler, VAEDecode, ImageScaleToTotalPixels, VAEEncode, KSampler, VAEDecode, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, VAEEncode, VAEDecode, TextEncodeQwenImageEditPlus, PreviewImage, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), RH_Nano_Banana_Image2Image, RH_Nano_Banana_Image2Image, RH_RhartImageG2ImageToImage, LoraLoaderModelOnly, LoadImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.72, "sampler_name": "euler", "scheduler": "simple", "seed": 88888888, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ywt低价版3.0_2060024511612936194.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ywt低价版3.0_2060024511612936194.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `RH_Nano_Banana_Image2Image`
- `RH_Nano_Banana_Image2Image`
- `RH_RhartImageG2ImageToImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `88888888`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.72`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`SaveImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`ImageScaleToTotalPixels`、`VAEEncode`、`KSampler`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`RH_Nano_Banana_Image2Image`、`RH_RhartImageG2ImageToImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
