---
key: 图片生成/文生图/rebalancev1+Qwen3VL-Supermate（本地实测）_1983970835247628289.json
name: rebalancev1+Qwen3VL-Supermate（本地实测）_1983970835247628289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/rebalancev1+Qwen3VL-Supermate（本地实测）_1983970835247628289.json
hash: f53007a137da9def
coverage: 0.777778
learned_at: 2026-10-09 20:05:46
nodes: [VAELoader, CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, CheckpointLoaderSimple, LoadDiffusionModelShared //Inspire, Qwen3_VQA, Note, Bjornulf_AnythingToText, CLIPTextEncode, ShowText, EmptySD3LatentImage, SaveImage, KSampler, VAEDecode, AILab_QwenVL, Note, Note]
patterns: []
missing: [LoadDiffusionModelShared //Inspire]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Rebalance_beta_00001_.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 770157070215727, "steps": 8}
discoveries: [次要节点 `LoadDiffusionModelShared //Inspire` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/rebalancev1+Qwen3VL-Supermate（本地实测）_1983970835247628289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1983970835247628289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `CheckpointLoaderSimple` ★核心
- `LoadDiffusionModelShared //Inspire`
- `Qwen3_VQA`
- `Note`
- `Bjornulf_AnythingToText`
- `CLIPTextEncode` ★核心
- `ShowText`
- `EmptySD3LatentImage`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `AILab_QwenVL`
- `Note`
- `Note`

## 关键参数

- `checkpoint` = `Rebalance_beta_00001_.safetensors`
- `seed` = `770157070215727`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`Qwen3_VQA`、`Bjornulf_AnythingToText`、`CLIPTextEncode`、`ShowText`、`EmptySD3LatentImage`、`SaveImage`、`KSampler`、`VAEDecode`、`AILab_QwenVL`

**缺卡**（1）：`LoadDiffusionModelShared //Inspire`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LoadDiffusionModelShared //Inspire` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
