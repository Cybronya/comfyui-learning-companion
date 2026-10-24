---
key: 图片生成/图生图/星绘一键多机位角度调整（Multi-camera angle adjustment）_2010704541276180482.json
name: 星绘一键多机位角度调整（Multi-camera angle adjustment）_2010704541276180482
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/星绘一键多机位角度调整（Multi-camera angle adjustment）_2010704541276180482.json
hash: c57a55f7c579a0fa
coverage: 0.92
learned_at: 2026-10-23 13:04:53
nodes: [LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPLoader, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, KSampler, VAELoader, LoraLoaderModelOnly, CheckpointLoaderSimple, CFGNorm, QwenMultiangleCameraNode, QwenMultiangleCameraNode, TextEncodeQwenImageEditPlus, easy promptList, easy showAnything, Note, VAEDecode, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v18.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 966466706425578, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/星绘一键多机位角度调整（Multi-camera angle adjustment）_2010704541276180482.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/星绘一键多机位角度调整（Multi-camera angle adjustment）_2010704541276180482.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `KSampler` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `CFGNorm`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `TextEncodeQwenImageEditPlus`
- `easy promptList`
- `easy showAnything`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `966466706425578`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v18.safetensors`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`QwenMultiangleCameraNode`、`KSampler`、`VAELoader`、`CheckpointLoaderSimple`、`CFGNorm`、`easy promptList`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
