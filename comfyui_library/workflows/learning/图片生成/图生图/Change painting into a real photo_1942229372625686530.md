---
key: 图片生成/图生图/Change painting into a real photo_1942229372625686530.json
name: Change painting into a real photo_1942229372625686530
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Change painting into a real photo_1942229372625686530.json
hash: c0197c04b1434fa8
coverage: 0.947368
learned_at: 2026-10-23 10:51:54
nodes: [ImageResize, FluxKontextImageScale, VAEEncode, FluxGuidance, ConditioningZeroOut, UNETLoader, DualCLIPLoader, VAEDecode, ImageConcatMulti, SaveImage, ReferenceLatent, CLIPTextEncode, Note, RH_Translator, LoadImage, Text Multiline, SaveImage, VAELoader, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 916173159778222, "steps": 20}
---

# 图片生成/图生图/Change painting into a real photo_1942229372625686530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Change painting into a real photo_1942229372625686530.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ImageResize`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `SaveImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `Note`
- `RH_Translator`
- `LoadImage`
- `Text Multiline`
- `SaveImage`
- `VAELoader`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `916173159778222`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`ImageResize`、`FluxKontextImageScale`、`VAEEncode`、`FluxGuidance`、`ConditioningZeroOut`、`UNETLoader`、`DualCLIPLoader`、`VAEDecode`、`ImageConcatMulti`、`SaveImage`、`ReferenceLatent`、`CLIPTextEncode`、`RH_Translator`、`LoadImage`、`Text Multiline`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
