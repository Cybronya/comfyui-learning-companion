---
key: 视频生成/图生视频/最新 Wan 2.2 Animate 无限循环 自动分割 超长视频_1971391086038040577.json
name: 最新 Wan 2.2 Animate 无限循环 自动分割 超长视频_1971391086038040577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1971391086038040577.json
hash: 0dd7f66d1c035926
coverage: 0.410256
learned_at: 2026-10-15 22:31:56
nodes: [CLIPTextEncode, TrimVideoLatent, VAEDecode, ModelSamplingSD3, KSampler, ImageFromBatch, VAEDecode, WanAnimateToVideo, KSampler, TrimVideoLatent, GrowMask, BlockifyMask, DrawMaskOnImage, PreviewImage, MaskPreview, PixelPerfectResolution, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Reroute, VHS_VideoCombine, easy showAnything, PathchSageAttentionKJ, TorchCompileModel, GroundingDinoSAMSegment (segment anything), SetNode, SetNode, GetNode, GetNode, GetNode, easy forLoopStart, VHS_VideoCombine, GetNode, GetNode, GetNode, MathExpression|pysssss, easy showAnything, easy showAnything, easy showAnything, easy showAnything, ModelSamplingSD3, VHS_GetImageCount, easy showAnything, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, easy showAnything, ImageResizeKJv2, PreviewImage, LoadImageFromPath, CLIPVisionEncode, SetNode, SetNode, Note, MarkdownNote, MarkdownNote, MarkdownNote, GetNode, SetNode, VHS_VideoInfoLoaded, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, CLIPLoader, CLIPVisionLoader, VAELoader, GroundingDinoModelLoader (segment anything), SAMModelLoader (segment anything), ImageBatch, easy forLoopEnd, GetNode, MarkdownNote, GetNode, Note, VHS_LoadVideo, PrimitiveInt, PrimitiveInt, LoadImage, VHS_LoadVideoPath, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, WanAnimateToVideo, DWPreprocessor, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 387378783691198, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/最新 Wan 2.2 Animate 无限循环 自动分割 超长视频_1971391086038040577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971391086038040577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（117 个）：
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
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
- `GetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `CLIPTextEncode` ★核心
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
- `Note`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `VHS_LoadVideoPath`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `WanAnimateToVideo`
- `DWPreprocessor`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `387378783691198`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **41%**（48/117）

**有卡**：`CLIPTextEncode`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`KSampler`、`ImageFromBatch`、`WanAnimateToVideo`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`MaskPreview`、`PixelPerfectResolution`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`TorchCompileModel`、`GroundingDinoSAMSegment (segment anything)`、`easy forLoopStart`、`MathExpression|pysssss`、`VHS_GetImageCount`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`LoadImageFromPath`、`CLIPVisionEncode`、`VHS_VideoInfoLoaded`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`GroundingDinoModelLoader (segment anything)`、`SAMModelLoader (segment anything)`、`ImageBatch`、`easy forLoopEnd`、`VHS_LoadVideo`、`LoadImage`、`VHS_LoadVideoPath`、`DWPreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
