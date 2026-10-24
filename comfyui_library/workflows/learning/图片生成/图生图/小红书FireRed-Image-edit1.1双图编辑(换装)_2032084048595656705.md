---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705.json
name: 小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705.json
hash: 800453115b8ca147
coverage: 0.782609
learned_at: 2026-10-23 12:49:17
nodes: [FluxKontextImageScale, ModelSamplingAuraFlow, CFGNorm, SaveImage, ImageConcanate, Reroute, Image Comparer (rgthree), FluxKontextImageScale, Note, TextEncodeQwenImageEditPlusPro_lrzjason, PreviewImage, VAEDecode, SaveImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlusPro_lrzjason, VAELoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, LoadImage, LoadImage, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 16158214311606, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `FluxKontextImageScale`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SaveImage`
- `ImageConcanate`
- `Reroute`
- `Image Comparer (rgthree)`
- `FluxKontextImageScale`
- `Note`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `16158214311606`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`FluxKontextImageScale`、`ModelSamplingAuraFlow`、`CFGNorm`、`SaveImage`、`ImageConcanate`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
