---
key: 图片生成/图生图/FireRed-Image-edit1.1 跨次元换装_2029765859891224577.json
name: FireRed-Image-edit1.1 跨次元换装_2029765859891224577
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1 跨次元换装_2029765859891224577.json
hash: c1566461c4404323
coverage: 0.875
learned_at: 2026-10-23 10:55:49
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), TextEncodeQwenImageEditPlus, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, FluxKontextImageScale, FluxKontextImageScale, KSampler, CR Prompt Text, Image Comparer (rgthree), VAEDecode, easy cleanGpuUsed, SaveImage, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 67394414914265, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1 跨次元换装_2029765859891224577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1 跨次元换装_2029765859891224577.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
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
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `67394414914265`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`FluxKontextImageScale`、`KSampler`、`CR Prompt Text`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
