---
key: 图片生成/图生图/小红书 FireRed image-Edit-1.1 老照片修复重新上色_2033805219217281026.json
name: 小红书 FireRed image-Edit-1.1 老照片修复重新上色_2033805219217281026
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书 FireRed image-Edit-1.1 老照片修复重新上色_2033805219217281026.json
hash: 852b63001effea8d
coverage: 0.894737
learned_at: 2026-10-23 12:49:00
nodes: [KSampler, LoraLoaderModelOnly, VAELoader, ImageScaleToTotalPixels, CLIPLoader, VAEDecode, Image Comparer (rgthree), CFGNorm, Seed Generator, ModelSamplingAuraFlow, ReferenceLatent, ReferenceLatent, SaveImage, VAEEncode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, Note, LoadImage, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 301452201711341, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书 FireRed image-Edit-1.1 老照片修复重新上色_2033805219217281026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书 FireRed image-Edit-1.1 老照片修复重新上色_2033805219217281026.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `CFGNorm`
- `Seed Generator`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `ReferenceLatent`
- `SaveImage`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `LoadImage`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `301452201711341`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`ImageScaleToTotalPixels`、`CLIPLoader`、`VAEDecode`、`CFGNorm`、`Seed Generator`、`ModelSamplingAuraFlow`、`ReferenceLatent`、`SaveImage`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
