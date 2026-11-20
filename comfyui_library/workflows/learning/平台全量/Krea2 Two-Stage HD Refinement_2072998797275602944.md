---
key: 平台全量/Krea2 Two-Stage HD Refinement_2072998797275602944.json
name: Krea2 Two-Stage HD Refinement_2072998797275602944
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Krea2 Two-Stage HD Refinement_2072998797275602944.json
hash: 087d7ac6864ad02c
coverage: 0.928571
learned_at: 2026-11-14 00:36:10
nodes: [UNETLoader, ConditioningZeroOut, KSampler, ConditioningKrea2Rebalance, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, LatentUpscaleBy, FluxResolutionNode, SaveImage, VAEDecode, CLIPTextEncode, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 20260630, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Krea2 Two-Stage HD Refinement_2072998797275602944.json

> 来源文件 `comfyui_library/workflows/平台全量/Krea2 Two-Stage HD Refinement_2072998797275602944.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ConditioningKrea2Rebalance`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LatentUpscaleBy`
- `FluxResolutionNode`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `20260630`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`KSampler`、`ConditioningKrea2Rebalance`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LatentUpscaleBy`、`FluxResolutionNode`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
