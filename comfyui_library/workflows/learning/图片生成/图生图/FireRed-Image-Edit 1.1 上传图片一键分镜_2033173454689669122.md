---
key: 图片生成/图生图/FireRed-Image-Edit 1.1 上传图片一键分镜_2033173454689669122.json
name: FireRed-Image-Edit 1.1 上传图片一键分镜_2033173454689669122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 上传图片一键分镜_2033173454689669122.json
hash: c4a2322b52a34b6e
coverage: 0.735294
learned_at: 2026-10-23 10:55:31
nodes: [TextEncodeQwenImageEditPlusAdvance_lrzjason, ModelSamplingAuraFlow, LoraLoaderModelOnly, SetNode, GetNode, GetNode, JDCN_StringToList, TextEncodeQwenImageEditPlus, VAEDecode, SetNode, Note, Note, UNETLoader, KSampler, ProcessString, LoadImage, LoraLoaderModelOnly, CFGNorm, VAELoader, CLIPLoader, Anything Everywhere3, RH_LLMAPI_NODE, CR Text, SaveImage, GetNode, Text, Text, ttN concat, SetNode, MultiTextConcatenate, CR Text, Text, CustomAddLabel, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 572107975621072, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1 上传图片一键分镜_2033173454689669122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 上传图片一键分镜_2033173454689669122.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（34 个）：
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `JDCN_StringToList`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `SetNode`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ProcessString`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `RH_LLMAPI_NODE`
- `CR Text`
- `SaveImage`
- `GetNode`
- `Text`
- `Text`
- `ttN concat`
- `SetNode`
- `MultiTextConcatenate`
- `CR Text`
- `Text`
- `CustomAddLabel`
- `SaveImage`

## 关键参数

- `seed` = `572107975621072`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`UNETLoader`、`KSampler`、`ProcessString`、`LoadImage`、`CFGNorm`、`VAELoader`、`CLIPLoader`、`RH_LLMAPI_NODE`、`CR Text`、`SaveImage`、`Text`、`ttN concat`、`MultiTextConcatenate`、`CustomAddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
