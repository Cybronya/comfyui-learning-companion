---
key: Wan2.2 文生图_1954733353410949121.json
name: Wan2.2 文生图_1954733353410949121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图_1954733353410949121.json
hash: cd1c9e6026a868cc
coverage: 0.875
learned_at: 2026-10-10 20:59:13
nodes: [PrimitiveInt, PrimitiveInt, VAEDecode, EmptyHunyuanLatentVideo, VAELoader, CFGZeroStarAndInit, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, LoraLoader, LoraLoader, LoraLoader, SaveImage, KSampler]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "Wan2.2-Lightning_T2V-v1.1-A14B-4steps-lora_LOW_fp16.safetensors", "sampler_name": "euler", "scheduler": "bong_tangent", "seed": 222707091458109, "steps": 8, "strength_clip": 0.8000000000000002, "strength_model": 0.8000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Wan2.2 文生图_1954733353410949121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图_1954733353410949121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CFGZeroStarAndInit`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Wan2.2-Lightning_T2V-v1.1-A14B-4steps-lora_LOW_fp16.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `0.8000000000000002`
- `seed` = `222707091458109`
- `steps` = `8`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`VAEDecode`、`EmptyHunyuanLatentVideo`、`VAELoader`、`CFGZeroStarAndInit`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`LoraLoader`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
