---
key: 图片生成/图生图/QwenEdit-参考图像人物重打光V1.0_2008916789152976898.json
name: QwenEdit-参考图像人物重打光V1.0_2008916789152976898
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit-参考图像人物重打光V1.0_2008916789152976898.json
hash: f079f9d08a52c743
coverage: 0.862069
learned_at: 2026-10-23 11:20:15
nodes: [CFGNorm, VAELoader, CLIPLoader, ModelSamplingAuraFlow, EmptySD3LatentImage, VAEEncode, MarkdownNote, MarkdownNote, MarkdownNote, KSampler, LoraLoaderModelOnly, UNETLoader, SeedVR2LoadVAEModel, VAEDecode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, SaveImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, ImageScaleBy, SaveImage, LoadImage, SeedVR2LoadDiTModel, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 106659619736153, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEdit-参考图像人物重打光V1.0_2008916789152976898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit-参考图像人物重打光V1.0_2008916789152976898.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `SaveImage`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `106659619736153`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`CFGNorm`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`VAEEncode`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`SeedVR2LoadVAEModel`、`VAEDecode`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`LoadImage`、`SeedVR2LoadDiTModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
