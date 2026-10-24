---
key: 图片生成/图生图/ywt低价版1.0_2059986818820567041.json
name: ywt低价版1.0_2059986818820567041
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ywt低价版1.0_2059986818820567041.json
hash: 572987c05e42d645
coverage: 0.891892
learned_at: 2026-10-23 11:46:22
nodes: [SaveImage, SaveImage, PreviewImage, PreviewImage, SaveImage, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, CFGNorm, ImageScaleToTotalPixels, VAEEncode, KSampler, VAEDecode, ImageScaleToTotalPixels, VAEEncode, KSampler, VAEDecode, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, VAEEncode, VAEDecode, Image Comparer (rgthree), TextEncodeQwenImageEditPlus, PreviewImage, RH_Nano_Banana_Image2Image, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, RH_Nano_Banana_Image2Image, RH_Nano_Banana_Image2Image, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, CR Text, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.72, "sampler_name": "euler", "scheduler": "simple", "seed": 88888888, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ywt低价版1.0_2059986818820567041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ywt低价版1.0_2059986818820567041.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
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
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `RH_Nano_Banana_Image2Image`
- `RH_Nano_Banana_Image2Image`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `CR Text`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `88888888`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.72`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`SaveImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`ImageScaleToTotalPixels`、`VAEEncode`、`KSampler`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`RH_Nano_Banana_Image2Image`、`LoraLoaderModelOnly`、`CR Text`、`LoadImage`

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
