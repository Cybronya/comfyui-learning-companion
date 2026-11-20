---
key: 平台全量/文生IP人物固定场景写真V1.0_1998319708766134274.json
name: 文生IP人物固定场景写真V1.0_1998319708766134274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/文生IP人物固定场景写真V1.0_1998319708766134274.json
hash: 58f265b029562e87
coverage: 0.681818
learned_at: 2026-11-14 02:10:58
nodes: [CLIPLoader, VAELoader, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingAuraFlow, ConditioningZeroOut, CLIPTextEncode, KSamplerAdvanced, VAEDecode, UNETLoader, CR Text Replace, JDCN_StringToList, ProcessString, CR Text, AILab_QwenVL, TextEncodeQwenImageEdit, ShowText|pysssss, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAEDecode, KSampler, SetNode, SetNode, GetNode, SetNode, CR Text, SaveImage, Note, Note, Note, EmptySD3LatentImage, CR Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 470826141524296, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/文生IP人物固定场景写真V1.0_1998319708766134274.json

> 来源文件 `comfyui_library/workflows/平台全量/文生IP人物固定场景写真V1.0_1998319708766134274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CR Text Replace`
- `JDCN_StringToList`
- `ProcessString`
- `CR Text`
- `AILab_QwenVL`
- `TextEncodeQwenImageEdit`
- `ShowText|pysssss`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `CR Text`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `EmptySD3LatentImage`
- `CR Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImage`

## 关键参数

- `seed` = `470826141524296`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **68%**（30/44）

**有卡**：`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`UNETLoader`、`CR Text Replace`、`JDCN_StringToList`、`ProcessString`、`CR Text`、`AILab_QwenVL`、`TextEncodeQwenImageEdit`、`KSampler`、`SaveImage`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
