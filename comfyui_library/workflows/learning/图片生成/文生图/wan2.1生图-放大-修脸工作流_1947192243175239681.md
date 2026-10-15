---
key: 图片生成/文生图/wan2.1生图-放大-修脸工作流_1947192243175239681.json
name: wan2.1生图-放大-修脸工作流_1947192243175239681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1生图-放大-修脸工作流_1947192243175239681.json
hash: 73c1b810e6426e17
coverage: 0.424658
learned_at: 2026-10-10 20:59:27
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, VAEEncode, GroundingDinoModelLoader (segment anything), SAMLoader, SetNode, VAEDecode, SetNode, GetNode, GetNode, SaveImage, PreviewImage, ImageCompositeMasked, GetNode, GetNode, KSampler, SetNode, VAEDecode, PreviewImage, VAEDecode, UNETLoader, VAELoader, CLIPLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, SetNode, EmptySD3LatentImage, CLIPTextEncode, SetNode, SetNode, ModelSamplingSD3, WanVideoNAG, ImageUpscaleWithModel, UpscaleModelLoader, GetNode, ImageResizeKJv2, VAEEncode, KSampler, GroundingDinoSAMSegment (segment anything), GrowMask, ImageScaleBy, GroundingDinoSAMSegment (segment anything), GrowMaskWithBlur, PreviewImage, KSampler, SetLatentNoiseMask, MaskPreview, GetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, ImageCrop, MaskBoundingBox+, CLIPTextEncode, PreviewImage]
patterns: []
missing: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GroundingDinoSAMSegment (segment anything), MaskBoundingBox+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 409860341308050, "steps": 8}
discoveries: [次要节点 `GroundingDinoModelLoader (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `MaskBoundingBox+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1生图-放大-修脸工作流_1947192243175239681.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1生图-放大-修脸工作流_1947192243175239681.json`

## 结构

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
- `VAEEncode`
- `GroundingDinoModelLoader (segment anything)`
- `SAMLoader`
- `SetNode`
- `VAEDecode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `PreviewImage`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `KSampler`
- `SetNode`
- `VAEDecode`
- `PreviewImage`
- `VAEDecode`
- `UNETLoader`
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `SetNode`
- `EmptySD3LatentImage`
- `CLIPTextEncode`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `WanVideoNAG`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `GetNode`
- `ImageResizeKJv2`
- `VAEEncode`
- `KSampler`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `ImageScaleBy`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMaskWithBlur`
- `PreviewImage`
- `KSampler`
- `SetLatentNoiseMask`
- `MaskPreview`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageCrop`
- `MaskBoundingBox+`
- `CLIPTextEncode`
- `PreviewImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.5000000000000001`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `409860341308050`
- `steps` = `8`

## 知识

覆盖率 **42%**（31/73）

**有卡**：`GetNode`、`SetNode`、`VAEEncode`、`GroundingDinoModelLoader (segment anything)`、`SAMLoader`、`VAEDecode`、`SaveImage`、`PreviewImage`、`ImageCompositeMasked`

**缺卡**（4）：`GroundingDinoModelLoader (segment anything)`、`GroundingDinoSAMSegment (segment anything)`、`GroundingDinoSAMSegment (segment anything)`、`MaskBoundingBox+`

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `GroundingDinoModelLoader (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `MaskBoundingBox+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
