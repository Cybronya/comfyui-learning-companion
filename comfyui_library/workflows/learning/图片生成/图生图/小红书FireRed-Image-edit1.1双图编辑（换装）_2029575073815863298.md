---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑（换装）_2029575073815863298.json
name: 小红书FireRed-Image-edit1.1双图编辑（换装）_2029575073815863298
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑（换装）_2029575073815863298.json
hash: 1547102f3bc788c4
coverage: 0.857143
learned_at: 2026-10-23 12:49:17
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), TextEncodeQwenImageEditPlus, LoadImage, Fast Groups Muter (rgthree), FluxKontextImageScale, PreviewImage, SaveImage, LoadImage, TextEncodeQwenImageEditPlus, LoadImage, FluxKontextImageScale, FluxKontextImageScale, KSampler, CR Prompt Text, Image Comparer (rgthree), VAEDecode, easy cleanGpuUsed, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 541959783320233, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑（换装）_2029575073815863298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑（换装）_2029575073815863298.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `FluxKontextImageScale`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `541959783320233`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`FluxKontextImageScale`、`SaveImage`、`KSampler`、`CR Prompt Text`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
