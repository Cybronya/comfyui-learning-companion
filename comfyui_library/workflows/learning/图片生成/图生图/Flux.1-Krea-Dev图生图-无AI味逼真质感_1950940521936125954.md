---
key: 图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味逼真质感_1950940521936125954.json
name: Flux.1-Krea-Dev图生图-无AI味逼真质感_1950940521936125954
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味逼真质感_1950940521936125954.json
hash: c409442901ddb3a2
coverage: 0.85
learned_at: 2026-10-23 10:58:42
nodes: [VAELoader, DualCLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, KSampler, RepeatLatentBatch, VAEEncode, VAEDecode, SaveImage, SaveImage, ImageStitch, ConditioningZeroOut, CLIPTextEncode, Text Concatenate, Text Multiline, ImageScaleDownToSize, RH_Captioner, easy showAnything, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 401297364299437, "steps": 20}
---

# 图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味逼真质感_1950940521936125954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味逼真质感_1950940521936125954.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `RepeatLatentBatch`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `Text Multiline`
- `ImageScaleDownToSize`
- `RH_Captioner`
- `easy showAnything`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `401297364299437`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`KSampler`、`RepeatLatentBatch`、`VAEEncode`、`VAEDecode`、`SaveImage`、`ImageStitch`、`ConditioningZeroOut`、`CLIPTextEncode`、`Text Concatenate`、`Text Multiline`、`ImageScaleDownToSize`、`RH_Captioner`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、RepeatLatentBatch
