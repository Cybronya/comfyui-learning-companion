---
key: 图片生成/图生图/FireRed-Image-edit1.1--模特换姿势_2029768783438553089.json
name: FireRed-Image-edit1.1--模特换姿势_2029768783438553089
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--模特换姿势_2029768783438553089.json
hash: 67934ccfebc75367
coverage: 0.88
learned_at: 2026-10-23 10:55:50
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, VAEDecode, LoraLoaderModelOnly, easy int, TextEncodeQwenImageEditPlus, PreviewImage, SaveImage, KSampler, easy cleanGpuUsed, Image Comparer (rgthree), LoadImage, FluxKontextImageScale, Any Switch (rgthree), SaveImage, UNETLoader, FluxKontextImageScale, LoadImage, OpenposePreprocessor, CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 600512916722824, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1--模特换姿势_2029768783438553089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--模特换姿势_2029768783438553089.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `LoadImage`
- `FluxKontextImageScale`
- `Any Switch (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `FluxKontextImageScale`
- `LoadImage`
- `OpenposePreprocessor`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `600512916722824`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`LoraLoaderModelOnly`、`easy int`、`SaveImage`、`KSampler`、`easy cleanGpuUsed`、`LoadImage`、`FluxKontextImageScale`、`UNETLoader`、`OpenposePreprocessor`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、OpenposePreprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
