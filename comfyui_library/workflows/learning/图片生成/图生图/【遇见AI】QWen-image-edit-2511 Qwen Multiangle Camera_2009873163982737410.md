---
key: 图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json
name: 【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json
hash: fcbc41b749d3eb7b
coverage: 1
learned_at: 2026-10-23 11:52:07
nodes: [CFGNorm, KSampler, CLIPLoader, VAELoader, LoraLoader, UNETLoader, ConditioningZeroOut, TextEncodeQwenImageEditPlus, QwenMultiangleCameraNode, ModelSamplingAuraFlow, SaveImage, VAEDecode, LoadImage, VAEEncode, ImageConcanate]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Qwen-Image-Edit-2511-Lightning-4steps-V1-bf16.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 253567043240188, "steps": 4, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CFGNorm`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `QwenMultiangleCameraNode`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `ImageConcanate`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `253567043240188`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Qwen-Image-Edit-2511-Lightning-4steps-V1-bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`CFGNorm`、`KSampler`、`CLIPLoader`、`VAELoader`、`LoraLoader`、`UNETLoader`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`QwenMultiangleCameraNode`、`ModelSamplingAuraFlow`、`SaveImage`、`VAEDecode`、`LoadImage`、`VAEEncode`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
