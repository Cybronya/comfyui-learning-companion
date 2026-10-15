---
key: 图片生成/文生图/wan2.1单帧文生图_1944002361066946562.json
name: wan2.1单帧文生图_1944002361066946562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1单帧文生图_1944002361066946562.json
hash: 81590fee0fcd96e0
coverage: 0.75
learned_at: 2026-10-10 20:59:26
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CLIPTextEncode, UNETLoader, LoraLoader, LoraLoader, CLIPLoader, EmptyHunyuanLatentVideo, VAELoader, LoraLoader, VAEDecode, KSampler, SaveImage, CLIPTextEncode]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 212387878880387, "steps": 10, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 图片生成/文生图/wan2.1单帧文生图_1944002361066946562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1单帧文生图_1944002361066946562.json`

## 结构

**节点**（16 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode`
- `UNETLoader`
- `LoraLoader`
- `LoraLoader`
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `LoraLoader`
- `VAEDecode`
- `KSampler`
- `SaveImage`
- `CLIPTextEncode`

**识别到的模式**：lora

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `212387878880387`
- `steps` = `10`
- `strength_clip` = `1.0000000000000002`
- `strength_model` = `1.0000000000000002`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`MarkdownNote`、`CLIPTextEncode`、`UNETLoader`、`LoraLoader`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`VAELoader`
