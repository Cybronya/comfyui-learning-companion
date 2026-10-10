---
key: WAN2.1文生图_1946266988476030978.json
name: WAN2.1文生图_1946266988476030978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.1文生图_1946266988476030978.json
hash: 7bd1c759b2bd2144
coverage: 0.923077
learned_at: 2026-10-10 20:59:13
nodes: [CLIPLoader, LoraLoader, LoraLoader, LoraLoader, CLIPTextEncode, VAELoader, EmptyHunyuanLatentVideo, KSampler, SaveImage, UNETLoader, CLIPTextEncode, VAEDecode, easy cleanGpuUsed]
patterns: [lora]
missing: [easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.1_BaldursGate3Style_v1_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 524865607552228, "steps": 8, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# WAN2.1文生图_1946266988476030978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.1文生图_1946266988476030978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `WAN2.1_BaldursGate3Style_v1_by-AI_Characters.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `524865607552228`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`LoraLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyHunyuanLatentVideo`、`KSampler`、`SaveImage`、`UNETLoader`、`VAEDecode`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
