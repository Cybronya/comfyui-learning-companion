---
key: 图片生成/图生图/固定人物IP 多张多场景生成V3.0（IP打造）_2031743464865533954.json
name: 固定人物IP 多张多场景生成V3.0（IP打造）_2031743464865533954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/固定人物IP 多张多场景生成V3.0（IP打造）_2031743464865533954.json
hash: eebc89945eab2bef
coverage: 0.875
learned_at: 2026-10-23 12:37:37
nodes: [ShowText|pysssss, ProcessString, CR Text, Note, Note, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, RH_LLMAPI_NODE, JDCN_StringToList, CLIPLoader, VAELoader, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, AILab_QwenVL, GetImageSize, EmptySD3LatentImage, UNETLoader, CR Text Replace, KSampler, CR Text, VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 860954231629159, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/固定人物IP 多张多场景生成V3.0（IP打造）_2031743464865533954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/固定人物IP 多张多场景生成V3.0（IP打造）_2031743464865533954.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ShowText|pysssss`
- `ProcessString`
- `CR Text`
- `Note`
- `Note`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `RH_LLMAPI_NODE`
- `JDCN_StringToList`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `AILab_QwenVL`
- `GetImageSize`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `CR Text Replace`
- `KSampler` ★核心
- `CR Text`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `860954231629159`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`ProcessString`、`CR Text`、`TextEncodeQwenImageEditPlus`、`RH_LLMAPI_NODE`、`JDCN_StringToList`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`AILab_QwenVL`、`GetImageSize`、`EmptySD3LatentImage`、`UNETLoader`、`CR Text Replace`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
