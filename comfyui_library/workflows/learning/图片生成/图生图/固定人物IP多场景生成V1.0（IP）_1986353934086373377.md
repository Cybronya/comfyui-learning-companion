---
key: 图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json
name: 固定人物IP多场景生成V1.0（IP）_1986353934086373377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json
hash: 31e6c383b0b2cfeb
coverage: 0.9
learned_at: 2026-10-23 12:37:37
nodes: [JDCN_StringToList, TextEncodeQwenImageEditPlusAdvance_lrzjason, CLIPLoader, VAELoader, UNETLoader, VAEDecode, TextEncodeQwenImageEdit, ShowText|pysssss, LoraLoaderModelOnly, LoraLoaderModelOnly, ProcessString, AILab_QwenVL, KSampler, ModelSamplingAuraFlow, CR Text Replace, CR Text, SaveImage, LoadImage, CR Text, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 450407586602787, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（20 个）：
- `JDCN_StringToList`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEdit`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ProcessString`
- `AILab_QwenVL`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CR Text Replace`
- `CR Text`
- `SaveImage`
- `LoadImage`
- `CR Text`
- `Note`

## 关键参数

- `seed` = `450407586602787`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`JDCN_StringToList`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`TextEncodeQwenImageEdit`、`LoraLoaderModelOnly`、`ProcessString`、`AILab_QwenVL`、`KSampler`、`ModelSamplingAuraFlow`、`CR Text Replace`、`CR Text`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
