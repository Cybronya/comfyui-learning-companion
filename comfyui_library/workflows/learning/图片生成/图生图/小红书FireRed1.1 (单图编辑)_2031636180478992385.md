---
key: 图片生成/图生图/小红书FireRed1.1 (单图编辑)_2031636180478992385.json
name: 小红书FireRed1.1 (单图编辑)_2031636180478992385
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed1.1 (单图编辑)_2031636180478992385.json
hash: a2745ea4358a8a6a
coverage: 1
learned_at: 2026-10-23 12:49:20
nodes: [ModelSamplingAuraFlow, VAEEncode, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSampler, easy cleanGpuUsed, easy int, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, CFGNorm, LoadImage, CR Prompt Text, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 226153885355710, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed1.1 (单图编辑)_2031636180478992385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed1.1 (单图编辑)_2031636180478992385.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `easy int`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `CFGNorm`
- `LoadImage`
- `CR Prompt Text`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `226153885355710`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`ModelSamplingAuraFlow`、`VAEEncode`、`VAEDecode`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`VAELoader`、`KSampler`、`easy cleanGpuUsed`、`easy int`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`CFGNorm`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
