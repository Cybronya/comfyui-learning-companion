---
key: 图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json
name: Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json
hash: 411ed249de7625f4
coverage: 0.529412
learned_at: 2026-10-19 23:02:26
nodes: [LoraLoaderModelOnly, VAELoader, ConditioningZeroOut, VAEEncode, VAEDecode, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, LoraLoaderModelOnly, UNETLoader, SaveImage, LoadImage, RH_LLMAPI_Pro_Node, Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, RHHiddenNodes]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 501131000597717, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `Text`
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
- `TextEncodeQwenImageEditPlus`
- `RHHiddenNodes`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `501131000597717`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **53%**（18/34）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`ConditioningZeroOut`、`VAEEncode`、`VAEDecode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`UNETLoader`、`SaveImage`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`Text`、`TextEncodeQwenImageEditPlus`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
