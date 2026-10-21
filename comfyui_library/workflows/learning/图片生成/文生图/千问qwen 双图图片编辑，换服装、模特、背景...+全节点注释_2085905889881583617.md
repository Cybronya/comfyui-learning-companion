---
key: 图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json
name: 千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json
hash: de0ace932de51b6d
coverage: 0.52381
learned_at: 2026-10-20 01:00:28
nodes: [VAEDecode, UNETLoader, CLIPLoader, KSampler, LoraLoaderModelOnly, VAELoader, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, Seed (rgthree), SaveImage, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEdit, ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, Int, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, Note, TextInput_]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 586425941126160, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Seed (rgthree)`
- `SaveImage`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEdit`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `Int`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`
- `TextInput_`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `586425941126160`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **52%**（22/42）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Seed (rgthree)`、`SaveImage`、`FluxKontextMultiReferenceLatentMethod`、`TextEncodeQwenImageEdit`、`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`Int`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
