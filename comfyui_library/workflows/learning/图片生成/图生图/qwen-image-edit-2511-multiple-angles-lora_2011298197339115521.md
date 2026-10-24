---
key: 图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2011298197339115521.json
name: qwen-image-edit-2511-multiple-angles-lora_2011298197339115521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2011298197339115521.json
hash: b0bd39dfc0a06978
coverage: 0.842105
learned_at: 2026-10-23 11:42:48
nodes: [LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, easy imageSize, EmptyLatentImage, TextEncodeQwenImageEditPlus, GetNode, LoadImage, VAEDecode, SetNode, SaveImage, QwenMultiangleCameraNode, easy showAnything, JoinStringMulti, ConditioningZeroOut, KepStringLiteral]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 273934534207900, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2011298197339115521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2011298197339115521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy imageSize`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `LoadImage`
- `VAEDecode` ★核心
- `SetNode`
- `SaveImage`
- `QwenMultiangleCameraNode`
- `easy showAnything`
- `JoinStringMulti`
- `ConditioningZeroOut`
- `KepStringLiteral`

## 关键参数

- `seed` = `273934534207900`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy imageSize`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`VAEDecode`、`SaveImage`、`QwenMultiangleCameraNode`、`JoinStringMulti`、`ConditioningZeroOut`、`KepStringLiteral`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
