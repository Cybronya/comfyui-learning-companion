---
key: 数字人/数字人/WAN2.2文生图_1985193592358584322.json
name: WAN2.2文生图_1985193592358584322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/WAN2.2文生图_1985193592358584322.json
hash: 5ced54d9daf94116
coverage: 0.555556
learned_at: 2026-10-26 01:57:40
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, Int, Int, PreviewImage, CLIPTextEncode, VAELoader, CLIPLoader, SetNode, GetNode, EmptyHunyuanLatentVideo, GetNode, KSampler, UNETLoader, ModelSamplingSD3, SetNode, CFGZeroStarAndInit, SaveImage, PreviewImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2, VAEDecode, LoraLoader, LoraLoader, ImageScaleBy, Float]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 523069211034295, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/WAN2.2文生图_1985193592358584322.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/WAN2.2文生图_1985193592358584322.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `CFGZeroStarAndInit`
- `SaveImage`
- `PreviewImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `ImageScaleBy`
- `Float`

**识别到的模式**：lora

## 关键参数

- `seed` = `523069211034295`
- `steps` = `8`
- `cfg` = `3.5`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **56%**（20/36）

**有卡**：`CLIPTextEncode`、`Int`、`VAELoader`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`KSampler`、`UNETLoader`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`SaveImage`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2`、`VAEDecode`、`LoraLoader`、`ImageScaleBy`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2、SeedVR2BlockSwap

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
