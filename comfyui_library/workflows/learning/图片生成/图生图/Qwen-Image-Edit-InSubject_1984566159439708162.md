---
key: 图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json
name: Qwen-Image-Edit-InSubject_1984566159439708162
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json
hash: c975e870935ba8b2
coverage: 0.8
learned_at: 2026-10-23 11:16:57
nodes: [VAEEncode, KSampler, ImageScaleToTotalPixels, easy imageSize, CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPLoader, UNETLoader, VAELoader, Note, LoadImage, TextEncodeQwenImageEditPlus, PreviewImage, LoraLoaderModelOnly, Image Comparer (rgthree), VAEDecode, SaveImage, TextEncodeQwenImageEditPlus, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 850215911203007, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Note`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `850215911203007`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`VAEEncode`、`KSampler`、`ImageScaleToTotalPixels`、`easy imageSize`、`CFGNorm`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
