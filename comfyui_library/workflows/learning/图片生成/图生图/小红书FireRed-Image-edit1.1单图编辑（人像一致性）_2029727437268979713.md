---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029727437268979713.json
name: 小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029727437268979713
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029727437268979713.json
hash: a8e276c259b071ef
coverage: 0.857143
learned_at: 2026-10-23 12:49:15
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), TextEncodeQwenImageEditPlus, Fast Groups Muter (rgthree), SaveImage, TextEncodeQwenImageEditPlus, FluxKontextImageScale, KSampler, VAEDecode, FluxKontextImageScale, easy cleanGpuUsed, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, FluxKontextImageScale, LoadImage, LoadImage, LoadImage, easy int, CR Prompt Text, PreviewImage, SaveImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 10910002542922, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029727437268979713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029727437268979713.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy int`
- `CR Prompt Text`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `10910002542922`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`FluxKontextImageScale`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`easy int`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
