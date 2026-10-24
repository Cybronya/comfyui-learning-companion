---
key: 图片生成/图生图/史上最强-动漫转写实真人2511AnythingtoRealCharacters正式版-高还原_2088249983240851458.json
name: 史上最强-动漫转写实真人2511AnythingtoRealCharacters正式版-高还原_2088249983240851458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/史上最强-动漫转写实真人2511AnythingtoRealCharacters正式版-高还原_2088249983240851458.json
hash: da38ad2803106077
coverage: 0.6
learned_at: 2026-10-23 12:36:12
nodes: [GetNode, SetNode, SetNode, SetNode, Note, MarkdownNote, GetNode, GetNode, SetNode, KSampler, VAELoader, CLIPLoader, UNETLoader, VAEEncode, LoraLoaderModelOnly, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Note, VAEDecode, CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, GetNode, GetNode, LoadImage, TextEncodeQwenImageEdit, FluxKontextMultiReferenceLatentMethod, SaveImage, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 602007262139267, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/史上最强-动漫转写实真人2511AnythingtoRealCharacters正式版-高还原_2088249983240851458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/史上最强-动漫转写实真人2511AnythingtoRealCharacters正式版-高还原_2088249983240851458.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `SetNode`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `VAEDecode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `LoadImage`
- `TextEncodeQwenImageEdit`
- `FluxKontextMultiReferenceLatentMethod`
- `SaveImage`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `602007262139267`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **60%**（18/30）

**有卡**：`KSampler`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEEncode`、`LoraLoaderModelOnly`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`CFGNorm`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEdit`、`FluxKontextMultiReferenceLatentMethod`、`SaveImage`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
