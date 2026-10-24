---
key: 图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2040760101212000257.json
name: qwen-image-edit-2511-multiple-angles-lora_2040760101212000257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2040760101212000257.json
hash: 99549c684f8dc17a
coverage: 0.714286
learned_at: 2026-10-23 11:42:49
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, GetNode, VAEDecode, SetNode, JoinStringMulti, ConditioningZeroOut, LoadImage, VAELoader, EmptyLatentImage, KSampler, PrimitiveNode, PrimitiveNode, PrimitiveNode, TextEncodeQwenImageEditPlus, KepStringLiteral, SaveImage, QwenMultiangleCameraNode, easy showAnything]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 122169260406297, "steps": 8, "width": 1408}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2040760101212000257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2040760101212000257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `JoinStringMulti`
- `ConditioningZeroOut`
- `LoadImage`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `KepStringLiteral`
- `SaveImage`
- `QwenMultiangleCameraNode`
- `easy showAnything`

## 关键参数

- `width` = `1408`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `122169260406297`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`JoinStringMulti`、`ConditioningZeroOut`、`LoadImage`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImageEditPlus`、`KepStringLiteral`、`SaveImage`、`QwenMultiangleCameraNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
