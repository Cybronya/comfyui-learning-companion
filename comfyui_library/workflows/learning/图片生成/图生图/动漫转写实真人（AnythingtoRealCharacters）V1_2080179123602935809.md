---
key: 图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080179123602935809.json
name: 动漫转写实真人（AnythingtoRealCharacters）V1_2080179123602935809
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080179123602935809.json
hash: c7afadf7604da4cf
coverage: 0.6
learned_at: 2026-10-23 12:25:34
nodes: [GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, VAELoader, Note, VAEDecode, CLIPLoader, SaveImage, SetNode, ModelSamplingAuraFlow, CFGNorm, LoraLoaderModelOnly, ResizeImageMaskNode, LoraLoaderModelOnly, GetNode, VAEEncode, GetNode, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, LoadImage, KSampler, UnetLoaderGGUF]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 8888, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080179123602935809.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/动漫转写实真人（AnythingtoRealCharacters）V1_2080179123602935809.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（25 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `Note`
- `VAEDecode` ★核心
- `CLIPLoader`
- `SaveImage`
- `SetNode`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `ResizeImageMaskNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `8888`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **60%**（15/25）

**有卡**：`VAELoader`、`VAEDecode`、`CLIPLoader`、`SaveImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`LoraLoaderModelOnly`、`ResizeImageMaskNode`、`VAEEncode`、`TextEncodeQwenImageEdit`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`KSampler`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
