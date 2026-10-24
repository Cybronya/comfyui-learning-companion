---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json
name: 小红书FireRed-Image-edit1.1单图编辑_2033152678896869378
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json
hash: 3e3126810c525b7f
coverage: 0.85
learned_at: 2026-10-23 12:49:14
nodes: [VAEEncode, ModelSamplingAuraFlow, CFGNorm, VAELoader, CLIPLoader, LoadImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, easy cleanGpuUsed, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), UNETLoader, CR Prompt Text, Note, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 653460383585379, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `Note`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `653460383585379`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`VAEEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAELoader`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
