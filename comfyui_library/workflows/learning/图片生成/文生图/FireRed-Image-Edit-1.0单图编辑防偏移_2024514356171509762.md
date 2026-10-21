---
key: 图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json
name: FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json
hash: 402250b74031041b
coverage: 0.896552
learned_at: 2026-10-19 22:29:39
nodes: [CLIPLoader, ModelSamplingAuraFlow, CFGNorm, MarkdownNote, VAELoader, VAEDecode, GetImageSize+, EmptySD3LatentImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, VAEEncode, ReferenceLatent, LoadImage, LoadImage, Note, ImageScaleToTotalPixels, ReferenceLatent, LoadImage, TextEncodeQwenImageEditPlus, KSampler, Seed Generator, VAEDecodeTiled, LoadImage, String Literal, Image Comparer (rgthree), UNETLoader, LoraLoaderModelOnly, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 301452201711341, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `MarkdownNote`
- `VAELoader`
- `VAEDecode` ★核心
- `GetImageSize+`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `Note`
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `Seed Generator`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `String Literal`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `301452201711341`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAELoader`、`VAEDecode`、`GetImageSize+`、`EmptySD3LatentImage`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ReferenceLatent`、`LoadImage`、`KSampler`、`Seed Generator`、`VAEDecodeTiled`、`String Literal`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
