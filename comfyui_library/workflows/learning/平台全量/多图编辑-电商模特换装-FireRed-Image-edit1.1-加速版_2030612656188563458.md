---
key: 平台全量/多图编辑-电商模特换装-FireRed-Image-edit1.1-加速版_2030612656188563458.json
name: 多图编辑-电商模特换装-FireRed-Image-edit1.1-加速版_2030612656188563458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/多图编辑-电商模特换装-FireRed-Image-edit1.1-加速版_2030612656188563458.json
hash: ae17fc696c4ddc96
coverage: 0.774194
learned_at: 2026-11-14 01:57:38
nodes: [ModelSamplingAuraFlow, ImageConcatMulti, ImageConcatMulti, UNETLoader, CLIPLoader, VAELoader, CFGNorm, FluxKontextImageScale, FluxKontextImageScale, KOOK_SaveJPGImage, Reroute, AddLabel, SaveImage, VAEDecode, Reroute, Image Comparer (rgthree), Reroute, Reroute, Reroute, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, KSampler, LoraLoaderModelOnly, easy int, LoadImage, LoadImage, LoadImage, CR Prompt Text, Reroute]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1075186128515839, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/多图编辑-电商模特换装-FireRed-Image-edit1.1-加速版_2030612656188563458.json

> 来源文件 `comfyui_library/workflows/平台全量/多图编辑-电商模特换装-FireRed-Image-edit1.1-加速版_2030612656188563458.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `ModelSamplingAuraFlow`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `KOOK_SaveJPGImage`
- `Reroute`
- `AddLabel`
- `SaveImage`
- `VAEDecode` ★核心
- `Reroute`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `Reroute`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1075186128515839`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`ModelSamplingAuraFlow`、`ImageConcatMulti`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`FluxKontextImageScale`、`KOOK_SaveJPGImage`、`AddLabel`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`LoraLoaderModelOnly`、`easy int`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
