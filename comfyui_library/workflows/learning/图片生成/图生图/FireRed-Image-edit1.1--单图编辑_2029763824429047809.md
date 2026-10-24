---
key: 图片生成/图生图/FireRed-Image-edit1.1--单图编辑_2029763824429047809.json
name: FireRed-Image-edit1.1--单图编辑_2029763824429047809
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--单图编辑_2029763824429047809.json
hash: 2bbdad67def89d9d
coverage: 0.833333
learned_at: 2026-10-23 10:55:49
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, Any Switch (rgthree), TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEDecode, easy int, Note, easy cleanGpuUsed, SaveImage, Image Comparer (rgthree), SaveImage, LoadImage, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, PreviewImage, KSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 739476394883362, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1--单图编辑_2029763824429047809.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--单图编辑_2029763824429047809.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `easy int`
- `Note`
- `easy cleanGpuUsed`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `PreviewImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `739476394883362`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`easy int`、`easy cleanGpuUsed`、`SaveImage`、`LoadImage`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxKontextImageScale`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
