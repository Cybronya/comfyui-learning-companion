---
key: 平台全量/极速版高清修复 细节增强 去AI感 照片修复+图片高清放大 FLUX.2-klein 高清修复细节_2032256864158748674.json
name: 极速版高清修复 细节增强 去AI感 照片修复+图片高清放大 FLUX.2-klein 高清修复细节_2032256864158748674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/极速版高清修复 细节增强 去AI感 照片修复+图片高清放大 FLUX.2-klein 高清修复细节_2032256864158748674.json
hash: 61e0fe02bc10c7b1
coverage: 0.553191
learned_at: 2026-11-14 02:17:52
nodes: [Reroute, GetNode, SetNode, ReferenceLatent, UNETLoader, VAELoader, SetNode, SetNode, SetNode, SetNode, GetNode, ReferenceLatent, CLIPTextEncode, GetNode, Reroute, GetNode, GetNode, VAEEncode, UpscaleModelLoader, ImageScaleBy, SetNode, GetNode, CLIPLoader, GetNode, GetNode, Image Comparer (rgthree), VAEEncode, ImageUpscaleWithModel, VAEDecode, GetNode, SetNode, KSampler, GetNode, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, easy imageConcat, SaveImage, LoadImage, GetNode, ModelSamplingFlux, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, TextBox1, KSampler, easy imageColorMatch, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 133, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/极速版高清修复 细节增强 去AI感 照片修复+图片高清放大 FLUX.2-klein 高清修复细节_2032256864158748674.json

> 来源文件 `comfyui_library/workflows/平台全量/极速版高清修复 细节增强 去AI感 照片修复+图片高清放大 FLUX.2-klein 高清修复细节_2032256864158748674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `Reroute`
- `GetNode`
- `SetNode`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `ImageScaleBy`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `KSampler` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageConcat`
- `SaveImage`
- `LoadImage`
- `GetNode`
- `ModelSamplingFlux`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextBox1`
- `KSampler` ★核心
- `easy imageColorMatch`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `133`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **55%**（26/47）

**有卡**：`ReferenceLatent`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`UpscaleModelLoader`、`ImageScaleBy`、`CLIPLoader`、`ImageUpscaleWithModel`、`VAEDecode`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageConcat`、`SaveImage`、`LoadImage`、`ModelSamplingFlux`、`TextBox1`、`easy imageColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、ReferenceLatent

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
