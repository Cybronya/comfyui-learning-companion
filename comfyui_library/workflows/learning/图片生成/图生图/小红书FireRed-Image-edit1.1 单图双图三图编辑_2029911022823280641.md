---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1 单图双图三图编辑_2029911022823280641.json
name: 小红书FireRed-Image-edit1.1 单图双图三图编辑_2029911022823280641
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 单图双图三图编辑_2029911022823280641.json
hash: bb44e6a5ae86f409
coverage: 0.857143
learned_at: 2026-10-23 12:49:11
nodes: [TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, Any Switch (rgthree), VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, FluxKontextImageScale, easy int, TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, CFGNorm, FluxKontextImageScale, LoadImage, UNETLoader, VAEDecode, easy cleanGpuUsed, Image Comparer (rgthree), SaveImage, PreviewImage, Any Switch (rgthree), FluxKontextImageScale, LoadImage, LoadImage, CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 996950051578151, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1 单图双图三图编辑_2029911022823280641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 单图双图三图编辑_2029911022823280641.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Any Switch (rgthree)`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `FluxKontextImageScale`
- `easy int`
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `FluxKontextImageScale`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `Any Switch (rgthree)`
- `FluxKontextImageScale`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `996950051578151`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`KSampler`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`FluxKontextImageScale`、`easy int`、`ModelSamplingAuraFlow`、`CFGNorm`、`LoadImage`、`UNETLoader`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
