---
key: 图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json
name: 一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json
hash: b911c7dbccc3c2e9
coverage: 1
learned_at: 2026-10-23 11:56:22
nodes: [CFGNorm, CLIPLoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, LoadImage, LoadImage, LoadImage, UNETLoader, VAEDecode, VAEEncode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, RHHiddenNodes, ImageConcatMulti, ImageConcatMulti, SaveImage, SaveImage, SaveImage, LoadImage, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, LoraLoaderModelOnly, CR Prompt Text, VAELoader, ModelSamplingAuraFlow]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1102601675312153, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CFGNorm`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `RHHiddenNodes`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `VAELoader`
- `ModelSamplingAuraFlow`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1102601675312153`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`CFGNorm`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`KSampler`、`LoadImage`、`UNETLoader`、`VAEDecode`、`VAEEncode`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxKontextMultiReferenceLatentMethod`、`RHHiddenNodes`、`ImageConcatMulti`、`SaveImage`、`LoraLoaderModelOnly`、`CR Prompt Text`、`VAELoader`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
