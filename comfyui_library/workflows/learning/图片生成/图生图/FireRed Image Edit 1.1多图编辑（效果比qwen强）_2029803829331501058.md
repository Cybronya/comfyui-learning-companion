---
key: 图片生成/图生图/FireRed Image Edit 1.1多图编辑（效果比qwen强）_2029803829331501058.json
name: FireRed Image Edit 1.1多图编辑（效果比qwen强）_2029803829331501058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1多图编辑（效果比qwen强）_2029803829331501058.json
hash: b1473ee140f745c7
coverage: 0.655172
learned_at: 2026-10-23 10:55:26
nodes: [Note, SaveImage, Image Comparer (rgthree), Note, PreviewImage, Note, Note, Note, Note, Note, LoadImage, ImageConcanate, ImageConcanate, LoadImage, ImageResize+, ImageResize+, LoadImage, Fast Groups Bypasser (rgthree), CR Text, ImageResize+, KSampler, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1055392030626620, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed Image Edit 1.1多图编辑（效果比qwen强）_2029803829331501058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1多图编辑（效果比qwen强）_2029803829331501058.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Note`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Note`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `ImageConcanate`
- `ImageConcanate`
- `LoadImage`
- `ImageResize+`
- `ImageResize+`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `ImageResize+`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `1055392030626620`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **66%**（19/29）

**有卡**：`SaveImage`、`LoadImage`、`ImageConcanate`、`ImageResize+`、`CR Text`、`KSampler`、`TextEncodeQwenImageEditPlus`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`VAEDecode`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
