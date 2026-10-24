---
key: 图片生成/图生图/FireRed Image Edit 1.1单图编辑（效果比qwen强）_2033358154595049474.json
name: FireRed Image Edit 1.1单图编辑（效果比qwen强）_2033358154595049474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1单图编辑（效果比qwen强）_2033358154595049474.json
hash: 3c73710ddb30f2ea
coverage: 0.7
learned_at: 2026-10-23 10:55:25
nodes: [Note, SaveImage, Image Comparer (rgthree), Note, PreviewImage, Note, Note, LoadImage, ImageResize+, KSampler, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, VAEDecode, ImageConcanate, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 740937011537313, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed Image Edit 1.1单图编辑（效果比qwen强）_2033358154595049474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1单图编辑（效果比qwen强）_2033358154595049474.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `Note`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Note`
- `PreviewImage`
- `Note`
- `Note`
- `LoadImage`
- `ImageResize+`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`
- `CR Text`

## 关键参数

- `seed` = `740937011537313`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **70%**（14/20）

**有卡**：`SaveImage`、`LoadImage`、`ImageResize+`、`KSampler`、`TextEncodeQwenImageEditPlus`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageConcanate`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
