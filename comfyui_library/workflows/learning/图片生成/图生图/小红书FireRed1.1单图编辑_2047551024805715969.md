---
key: 图片生成/图生图/小红书FireRed1.1单图编辑_2047551024805715969.json
name: 小红书FireRed1.1单图编辑_2047551024805715969
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed1.1单图编辑_2047551024805715969.json
hash: 170799669fc5114f
coverage: 0.85
learned_at: 2026-10-23 12:49:20
nodes: [VAELoader, CLIPLoader, ModelSamplingAuraFlow, LoraLoaderModelOnly, CFGNorm, KSampler, VAEDecode, easy cleanGpuUsed, UNETLoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, Image Comparer (rgthree), SaveImage, Note, Note, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, Int, VAEEncode, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 160528759176842, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed1.1单图编辑_2047551024805715969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed1.1单图编辑_2047551024805715969.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Note`
- `Note`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `VAEEncode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `160528759176842`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CFGNorm`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`VAEEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
