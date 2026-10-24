---
key: 图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080120148148703234.json
name: 动漫转写实真人（AnythingtoRealCharacters）V1_2080120148148703234
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080120148148703234.json
hash: 8db03d34ee086828
coverage: 0.6
learned_at: 2026-10-23 12:25:32
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, TextEncodeQwenImageEdit, GetNode, GetNode, SetNode, VAEEncode, CFGNorm, ModelSamplingAuraFlow, VAELoader, Note, VAEDecode, SetNode, KSampler, LoraLoaderModelOnly, CLIPLoader, ImageScaleByAspectRatio_UTK, TextEncodeQwenImageEditPlus, SaveImage, LoadImage, UnetLoaderGGUF, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 581749362240971, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080120148148703234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080120148148703234.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEEncode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `Note`
- `VAEDecode` ★核心
- `SetNode`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ImageScaleByAspectRatio_UTK`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `581749362240971`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **60%**（15/25）

**有卡**：`TextEncodeQwenImageEdit`、`VAEEncode`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAELoader`、`VAEDecode`、`KSampler`、`LoraLoaderModelOnly`、`CLIPLoader`、`ImageScaleByAspectRatio_UTK`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`LoadImage`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
