---
key: 图片生成/图生图/FireRed-Image-edit1.1--模特换装_2029765744128434177.json
name: FireRed-Image-edit1.1--模特换装_2029765744128434177
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--模特换装_2029765744128434177.json
hash: 60156f49b1e2ed20
coverage: 0.875
learned_at: 2026-10-23 10:55:50
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, VAEDecode, LoraLoaderModelOnly, easy int, TextEncodeQwenImageEditPlus, PreviewImage, SaveImage, KSampler, easy cleanGpuUsed, UNETLoader, Image Comparer (rgthree), LoadImage, LoadImage, CR Prompt Text, FluxKontextImageScale, FluxKontextImageScale, Any Switch (rgthree), SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 712683276114293, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1--模特换装_2029765744128434177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1--模特换装_2029765744128434177.json`

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
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `Any Switch (rgthree)`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `712683276114293`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`LoraLoaderModelOnly`、`easy int`、`SaveImage`、`KSampler`、`easy cleanGpuUsed`、`UNETLoader`、`LoadImage`、`CR Prompt Text`、`FluxKontextImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
