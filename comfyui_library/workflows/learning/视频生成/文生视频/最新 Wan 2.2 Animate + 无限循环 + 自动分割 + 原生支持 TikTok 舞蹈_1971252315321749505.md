---
key: 视频生成/文生视频/最新 Wan 2.2 Animate + 无限循环 + 自动分割 + 原生支持 TikTok 舞蹈_1971252315321749505.json
name: 最新 Wan 2.2 Animate + 无限循环 + 自动分割 + 原生支持 TikTok 舞蹈_1971252315321749505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/最新 Wan 2.2 Animate + 无限循环 + 自动分割 + 原生支持 TikTok 舞蹈_1971252315321749505.json
hash: 2a5ada22e83f7c82
coverage: 0.353448
learned_at: 2026-10-10 23:13:22
nodes: [CLIPTextEncode, MarkdownNote, TrimVideoLatent, VAEDecode, ModelSamplingSD3, WanAnimateToVideo, KSampler, ImageFromBatch, VAEDecode, WanAnimateToVideo, KSampler, TrimVideoLatent, GrowMask, BlockifyMask, DrawMaskOnImage, PreviewImage, MaskPreview, PixelPerfectResolution, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Reroute, VHS_VideoCombine, easy showAnything, PathchSageAttentionKJ, TorchCompileModel, GroundingDinoSAMSegment (segment anything), SetNode, SetNode, GetNode, GetNode, GetNode, easy forLoopStart, VHS_VideoCombine, GetNode, GetNode, GetNode, MathExpression|pysssss, easy showAnything, easy showAnything, easy showAnything, easy showAnything, ModelSamplingSD3, VHS_GetImageCount, easy showAnything, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, easy showAnything, ImageResizeKJv2, PreviewImage, LoadImageFromPath, CLIPVisionEncode, SetNode, SetNode, Note, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, VHS_LoadVideoPath, GetNode, GetNode, SetNode, VHS_VideoInfoLoaded, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, CLIPVisionLoader, VAELoader, GroundingDinoModelLoader (segment anything), SAMModelLoader (segment anything), ImageBatch, easy forLoopEnd, GetNode, MarkdownNote, GetNode, VHS_VideoCombine, Note, DWPreprocessor, VHS_LoadVideo, PrimitiveInt, PrimitiveInt]
patterns: []
missing: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), MathExpression|pysssss, SAMModelLoader (segment anything), easy forLoopEnd, easy forLoopStart]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 387378783691198, "steps": 6}
discoveries: [次要节点 `GroundingDinoModelLoader (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SAMModelLoader (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/最新 Wan 2.2 Animate + 无限循环 + 自动分割 + 原生支持 TikTok 舞蹈_1971252315321749505.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/最新 Wan 2.2 Animate + 无限循环 + 自动分割 + 原生支持 TikTok 舞蹈_1971252315321749505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（116 个）：
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `ImageFromBatch`
- `VAEDecode` ★核心
- `WanAnimateToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PreviewImage`
- `MaskPreview`
- `PixelPerfectResolution`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `VHS_VideoCombine`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `GroundingDinoSAMSegment (segment anything)`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy forLoopStart`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ModelSamplingSD3`
- `VHS_GetImageCount`
- `easy showAnything`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `easy showAnything`
- `ImageResizeKJv2`
- `PreviewImage`
- `LoadImageFromPath`
- `CLIPVisionEncode`
- `SetNode`
- `SetNode`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `VHS_LoadVideoPath`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `GroundingDinoModelLoader (segment anything)`
- `SAMModelLoader (segment anything)`
- `ImageBatch`
- `easy forLoopEnd`
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `seed` = `387378783691198`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **35%**（41/116）

**有卡**：`CLIPTextEncode`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`WanAnimateToVideo`、`KSampler`、`ImageFromBatch`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`MaskPreview`、`PixelPerfectResolution`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`TorchCompileModel`、`VHS_GetImageCount`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`LoadImageFromPath`、`CLIPVisionEncode`、`LoadImage`、`VHS_LoadVideoPath`、`VHS_VideoInfoLoaded`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`ImageBatch`、`DWPreprocessor`、`VHS_LoadVideo`

**缺卡**（6）：`GroundingDinoModelLoader (segment anything)`、`GroundingDinoSAMSegment (segment anything)`、`MathExpression|pysssss`、`SAMModelLoader (segment anything)`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `GroundingDinoModelLoader (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SAMModelLoader (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
