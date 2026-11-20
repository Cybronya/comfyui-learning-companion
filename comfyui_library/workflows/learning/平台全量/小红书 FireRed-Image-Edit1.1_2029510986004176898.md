---
key: 平台全量/小红书 FireRed-Image-Edit1.1_2029510986004176898.json
name: 小红书 FireRed-Image-Edit1.1_2029510986004176898
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/小红书 FireRed-Image-Edit1.1_2029510986004176898.json
hash: c7e6136ccf86cc34
coverage: 0.851852
learned_at: 2026-11-14 02:01:18
nodes: [TextEncodeQwenImageEditPlus, CFGNorm, KSampler, VAEEncode, TextEncodeQwenImageEditPlus, PreviewImage, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, easy int, FluxKontextImageScale, Note, Any Switch (rgthree), LoadImage, VAEDecode, FluxKontextImageScale, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, ModelSamplingAuraFlow, easy imageConcat, easy imageConcat, PreviewImage, CR Prompt Text, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 344173884378563, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/小红书 FireRed-Image-Edit1.1_2029510986004176898.json

> 来源文件 `comfyui_library/workflows/平台全量/小红书 FireRed-Image-Edit1.1_2029510986004176898.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy int`
- `FluxKontextImageScale`
- `Note`
- `Any Switch (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `ModelSamplingAuraFlow`
- `easy imageConcat`
- `easy imageConcat`
- `PreviewImage`
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `344173884378563`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`TextEncodeQwenImageEditPlus`、`CFGNorm`、`KSampler`、`VAEEncode`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`easy int`、`FluxKontextImageScale`、`LoadImage`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`easy imageConcat`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
