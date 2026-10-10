---
key: wan2.1单帧文生图_1944002361066946562.json
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

# wan2.1单帧文生图_1944002361066946562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1单帧文生图_1944002361066946562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `212387878880387`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`LoraLoader`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`VAELoader`、`VAEDecode`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、LoraLoader
