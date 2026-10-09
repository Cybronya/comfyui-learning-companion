---
key: 图片生成/文生图/rebalancev1+Qwen3VL-workflow_1981298041351208962.json
name: rebalancev1+Qwen3VL-workflow_1981298041351208962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/rebalancev1+Qwen3VL-workflow_1981298041351208962.json
hash: 12804915c14016ef
coverage: 0.916667
learned_at: 2026-10-09 19:56:21
nodes: [EmptySD3LatentImage, VAEDecode, SaveImage, PreviewAny, CheckpointLoaderSimple, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, KSampler, AILab_QwenVL]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Rebalance_beta_00001_.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 774295928468411, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/rebalancev1+Qwen3VL-workflow_1981298041351208962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1981298041351208962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewAny`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `AILab_QwenVL`

## 关键参数

- `checkpoint` = `Rebalance_beta_00001_.safetensors`
- `seed` = `774295928468411`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`KSampler`、`AILab_QwenVL`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
