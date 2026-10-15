---
key: 图片生成/文生图/wan2.1文生图降维打击——高射炮打蚊子系统四（文生图——放大——修脸完整工作流）_1948383571122749441.json
name: wan2.1文生图降维打击——高射炮打蚊子系统四（文生图——放大——修脸完整工作流）_1948383571122749441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1文生图降维打击——高射炮打蚊子系统四（文生图——放大——修脸完整工作流）_1948383571122749441.json
hash: eb7cf8e447629faa
coverage: 0.479452
learned_at: 2026-10-15 22:27:57
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, VAEEncode, GroundingDinoModelLoader (segment anything), SAMLoader, SetNode, VAEDecode, SetNode, GetNode, GetNode, SaveImage, PreviewImage, ImageCompositeMasked, GetNode, GetNode, KSampler, SetNode, VAEDecode, PreviewImage, VAEDecode, UNETLoader, VAELoader, CLIPLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, SetNode, EmptySD3LatentImage, CLIPTextEncode, SetNode, SetNode, ModelSamplingSD3, WanVideoNAG, ImageUpscaleWithModel, UpscaleModelLoader, GetNode, ImageResizeKJv2, VAEEncode, KSampler, GroundingDinoSAMSegment (segment anything), GrowMask, ImageScaleBy, GroundingDinoSAMSegment (segment anything), GrowMaskWithBlur, PreviewImage, KSampler, SetLatentNoiseMask, MaskPreview, GetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, ImageCrop, MaskBoundingBox+, PreviewImage, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 702073579666166, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1文生图降维打击——高射炮打蚊子系统四（文生图——放大——修脸完整工作流）_1948383571122749441.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1文生图降维打击——高射炮打蚊子系统四（文生图——放大——修脸完整工作流）_1948383571122749441.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEEncode` ★核心
- `GroundingDinoModelLoader (segment anything)`
- `SAMLoader`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `PreviewImage`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `WanVideoNAG`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `GetNode`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `ImageScaleBy`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMaskWithBlur`
- `PreviewImage`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `MaskPreview`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageCrop`
- `MaskBoundingBox+`
- `PreviewImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `702073579666166`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **48%**（35/73）

**有卡**：`VAEEncode`、`GroundingDinoModelLoader (segment anything)`、`SAMLoader`、`VAEDecode`、`SaveImage`、`ImageCompositeMasked`、`KSampler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`WanVideoNAG`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageResizeKJv2`、`GroundingDinoSAMSegment (segment anything)`、`GrowMask`、`ImageScaleBy`、`GrowMaskWithBlur`、`SetLatentNoiseMask`、`MaskPreview`、`ImageCrop`、`MaskBoundingBox+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SetLatentNoiseMask

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
