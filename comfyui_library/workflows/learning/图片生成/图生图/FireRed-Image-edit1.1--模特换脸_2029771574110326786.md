---
key: 图片生成/图生图/FireRed-Image-edit1.1--模特换脸_2029771574110326786.json
name: FireRed-Image-edit1.1--模特换脸_2029771574110326786
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--模特换脸_2029771574110326786.json
hash: 729e7626fd966e11
coverage: 0.875
learned_at: 2026-10-23 10:55:50
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, VAEDecode, easy int, TextEncodeQwenImageEditPlus, PreviewImage, SaveImage, easy cleanGpuUsed, Image Comparer (rgthree), FluxKontextImageScale, FluxKontextImageScale, Any Switch (rgthree), SaveImage, LoadImage, CR Prompt Text, UNETLoader, LoraLoaderModelOnly, KSampler, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 750273839947369, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1--模特换脸_2029771574110326786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--模特换脸_2029771574110326786.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `easy int`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `SaveImage`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `Any Switch (rgthree)`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `750273839947369`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`easy int`、`SaveImage`、`easy cleanGpuUsed`、`FluxKontextImageScale`、`LoadImage`、`CR Prompt Text`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
