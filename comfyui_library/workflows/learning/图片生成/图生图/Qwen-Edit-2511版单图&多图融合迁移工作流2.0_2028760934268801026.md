---
key: 图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json
name: Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json
hash: 0cd08a4e8173e53e
coverage: 0.915493
learned_at: 2026-10-23 11:15:56
nodes: [CLIPLoader, CFGNorm, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, VAEDecode, Image Comparer (rgthree), KSampler, CLIPLoader, CFGNorm, ModelSamplingAuraFlow, VAELoader, ImageScaleToTotalPixels, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus, VAEDecode, Image Comparer (rgthree), KSampler, VAEEncode, ImageScaleToTotalPixels, VAELoader, FluxKontextMultiReferenceLatentMethod, SaveImage, SaveImage, Note, Note, CLIPLoader, CFGNorm, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, VAEDecode, Image Comparer (rgthree), KSampler, ImageScaleToTotalPixels, VAELoader, FluxKontextMultiReferenceLatentMethod, CLIPLoader, CFGNorm, ModelSamplingAuraFlow, VAEDecode, Image Comparer (rgthree), KSampler, VAEEncode, ImageScaleToTotalPixels, VAELoader, FluxKontextMultiReferenceLatentMethod, SaveImage, SaveImage, EmptySD3LatentImage, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LoadImage, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, UNETLoader, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 306946835703427, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `CLIPLoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `CLIPLoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `SaveImage`
- `SaveImage`
- `Note`
- `Note`
- `CLIPLoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `CLIPLoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `SaveImage`
- `SaveImage`
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `306946835703427`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（65/71）

**有卡**：`CLIPLoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`KSampler`、`VAELoader`、`ImageScaleToTotalPixels`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`SaveImage`、`EmptySD3LatentImage`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
