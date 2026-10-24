---
key: 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json
name: 固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json
hash: 876dc8ed95366502
coverage: 0.875
learned_at: 2026-10-23 12:37:39
nodes: [CLIPLoader, VAELoader, VAEDecode, TextEncodeQwenImageEdit, ShowText|pysssss, TextEncodeQwenImageEditPlusAdvance_lrzjason, EmptySD3LatentImage, ModelSamplingAuraFlow, JDCN_StringToList, AILab_QwenVL, RH_LLMAPI_NODE, ProcessString, CR Text Replace, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CR Text, CR Text, Note, Note, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "kl_optimal", "seed": 129990221464770, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEdit`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `JDCN_StringToList`
- `AILab_QwenVL`
- `RH_LLMAPI_NODE`
- `ProcessString`
- `CR Text Replace`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CR Text`
- `CR Text`
- `Note`
- `Note`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `129990221464770`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `kl_optimal`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImageEdit`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`JDCN_StringToList`、`AILab_QwenVL`、`RH_LLMAPI_NODE`、`ProcessString`、`CR Text Replace`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CR Text`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
