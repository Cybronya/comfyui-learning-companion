---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1 文字排版_2029759015185551362.json
name: 小红书FireRed-Image-edit1.1 文字排版_2029759015185551362
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 文字排版_2029759015185551362.json
hash: a3ac1d5ef787ea4d
coverage: 0.846154
learned_at: 2026-10-23 12:49:14
nodes: [FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), Any Switch (rgthree), FluxKontextImageScale, Any Switch (rgthree), TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, VAELoader, ModelSamplingAuraFlow, CFGNorm, easy cleanGpuUsed, LoraLoaderModelOnly, LoraLoaderModelOnly, easy int, SaveImage, CLIPLoader, UNETLoader, LoadImage, VAEEncode, PreviewImage, SaveImage, CR Prompt Text, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 543885315746821, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1 文字排版_2029759015185551362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 文字排版_2029759015185551362.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `Any Switch (rgthree)`
- `FluxKontextImageScale`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `SaveImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `PreviewImage`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `543885315746821`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`FluxKontextImageScale`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`easy int`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`VAEEncode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
