---
key: 平台全量/FireRed-Image-edit1.1虚拟试衣方法_2029818234802806785.json
name: FireRed-Image-edit1.1虚拟试衣方法_2029818234802806785
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FireRed-Image-edit1.1虚拟试衣方法_2029818234802806785.json
hash: 912e137dd48e69ec
coverage: 0.846154
learned_at: 2026-11-14 00:26:44
nodes: [LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingAuraFlow, CFGNorm, easy int, Any Switch (rgthree), KSampler, FluxKontextImageScale, FluxKontextImageScale, FluxKontextImageScale, easy positive, CLIPLoader, VAELoader, VAEEncode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, Image Comparer (rgthree), PreviewImage, SaveImage, PreviewImage, VAEDecode, SaveImageWebsocket, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 172097341071502, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FireRed-Image-edit1.1虚拟试衣方法_2029818234802806785.json

> 来源文件 `comfyui_library/workflows/平台全量/FireRed-Image-edit1.1虚拟试衣方法_2029818234802806785.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `easy int`
- `Any Switch (rgthree)`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `easy positive`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImageWebsocket`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `172097341071502`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`CFGNorm`、`easy int`、`KSampler`、`FluxKontextImageScale`、`easy positive`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`VAEDecode`、`SaveImageWebsocket`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
