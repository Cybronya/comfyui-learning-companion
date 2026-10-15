---
key: 图片生成/文生图/Wan2.2 单模低噪写实文生图_1950729804771430402.json
name: Wan2.2 单模低噪写实文生图_1950729804771430402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 单模低噪写实文生图_1950729804771430402.json
hash: 9973aa3d98d7d37d
coverage: 0.730769
learned_at: 2026-10-15 22:27:35
nodes: [CLIPTextEncode, VAEDecode, LoraLoader, LoraLoader, MarkdownNote, MarkdownNote, CLIPLoader, VAELoader, LoraLoader, MarkdownNote, KSampler, CLIPTextEncode, EmptyHunyuanLatentVideo, ImpactInt, CFGZeroStarAndInit, CR Text, ImpactSwitch, ImpactInt, CR Text Concatenate, easy showAnything, Note, SaveImage, CR Text, UNETLoader, RH_LLMAPI_NODE, MarkdownNote]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 66067103546342, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2 单模低噪写实文生图_1950729804771430402.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 单模低噪写实文生图_1950729804771430402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `CFGZeroStarAndInit`
- `CR Text`
- `ImpactSwitch`
- `ImpactInt`
- `CR Text Concatenate`
- `easy showAnything`
- `Note`
- `SaveImage`
- `CR Text`
- `UNETLoader` ★核心
- `RH_LLMAPI_NODE`
- `MarkdownNote`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `66067103546342`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`LoraLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`EmptyHunyuanLatentVideo`、`ImpactInt`、`CFGZeroStarAndInit`、`CR Text`、`CR Text Concatenate`、`SaveImage`、`UNETLoader`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
