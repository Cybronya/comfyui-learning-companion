---
key: 图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2008620397649989633.json
name: 动漫转写实真人（AnythingtoRealCharacters）V1_2008620397649989633
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2008620397649989633.json
hash: 282ca44899e3c170
coverage: 0.592593
learned_at: 2026-10-23 12:25:32
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, TextEncodeQwenImageEdit, GetNode, GetNode, SetNode, VAEEncode, CFGNorm, ModelSamplingAuraFlow, CLIPLoader, VAELoader, Note, VAEDecode, LoraLoaderModelOnly, LoadImage, SetNode, ImageScaleByAspectRatio_UTK, KSampler, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, UNETLoader, SaveImage, LoadImage, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 538257340737513, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2008620397649989633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2008620397649989633.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
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
- `CLIPLoader`
- `VAELoader`
- `Note`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `SetNode`
- `ImageScaleByAspectRatio_UTK`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `538257340737513`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（16/27）

**有卡**：`TextEncodeQwenImageEdit`、`VAEEncode`、`CFGNorm`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`LoraLoaderModelOnly`、`LoadImage`、`ImageScaleByAspectRatio_UTK`、`KSampler`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
