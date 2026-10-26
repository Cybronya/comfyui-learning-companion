---
key: 数字人/数字人/多角色替换-Wan2.2Animate-SAM3.1_new_2061645211851378690.json
name: 多角色替换-Wan2.2Animate-SAM3.1_new_2061645211851378690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/多角色替换-Wan2.2Animate-SAM3.1_new_2061645211851378690.json
hash: 8fe5810afa56e3f4
coverage: 0.321656
learned_at: 2026-10-26 02:01:31
nodes: [Note, GetNode, GetNode, YOLOModelLoader, Note, BodyRatioMapperSDPoseRender, LoadImage, ImageResizeKJv2, VHS_VideoCombine, GetNode, Note, LoadImage, ImageBatch, GetNode, GetNode, Note, SetNode, SetNode, SetNode, SetNode, Note, PreviewImage, SetNode, INTConstant, MarkdownNote, SetNode, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, Note, Note, Note, GetNode, GetNode, CheckpointLoaderSimple, CLIPTextEncode, SAM3_VideoTrack, BodyRatioMapperProportionTransfer, GetNode, GetNode, PreviewImage, BodyRatioMapperSDPoseRender, Note, GetNode, GetNode, GetNode, GetNode, GetNode, Note, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DrawMaskOnImage, GetNode, SAM3_TrackToMask, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, CLIPVisionEncode, BBoxYOLO, YOLOModelLoader, BBoxYOLO, GetNode, GetNode, GetNode, SDPoseKeypointExtractor, GetNode, SetNode, GetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, GetNode, GrowMask, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BlockifyMask, MaskToImage, SetNode, SetNode, SAM3_TrackToMask, GetNode, SetNode, SetNode, INTConstant, INTConstant, SetNode, VAELoader, GetNode, GrowMask, BlockifyMask, MaskToImage, GetNode, SetNode, GetNode, GetNode, InvertMask, GetNode, GetNode, Note, OnnxDetectionModelLoader, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, DrawMaskOnImage, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, VHS_VideoCombine, GetNode, InvertMask, DrawMaskOnImage, PoseAndFaceDetection, SetNode, SetNode, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, GetNode, GetNode, ImageFromBatch, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, GetNode, GetNode, WanAnimateToVideo, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageFromBatch, SetNode, GetNode, GetNode, BatchImagesNode, SetNode, ImageBatch, ImageResizeKJv2, SetNode, GetNode, GetNode, LoadImage, GetNode, SetNode, SetNode, GetNode, SAM3_TrackPreview, GetNode, Note, GetNode, TrimVideoLatent, VAEDecode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, VAEDecode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, VAEDecode, GetNode, ImageFromBatch, WanAnimateToVideo, SetNode, SetNode, SetNode, WanAnimateToVideo, GetNode, GetNode, SetNode, SetNode, GetNode, WanAnimateToVideo, GetNode, SetNode, GetNode, GetNode, GetNode, BatchImagesNode, SetNode, GetNode, GetNode, GetNode, KSampler, KSampler, KSampler, KSampler, KSampler, VHS_VideoCombine, CLIPVisionLoader, Note, LoadImage, VHS_VideoInfoLoaded, SetNode, CheckpointLoaderSimple, PreviewImage, BodyRatioMapperSDPoseRender, SDPoseKeypointExtractor, Note, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, WanAnimateToVideo, GetNode, GetNode, TrimVideoLatent, VAEDecode, GetNode, KSampler, WanAnimateToVideo, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, DrawMaskOnImage, PoseAndFaceDetection, SetNode, CLIPLoader, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1028228345876161, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/多角色替换-Wan2.2Animate-SAM3.1_new_2061645211851378690.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/多角色替换-Wan2.2Animate-SAM3.1_new_2061645211851378690.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（314 个）：
- `Note`
- `GetNode`
- `GetNode`
- `YOLOModelLoader`
- `Note`
- `BodyRatioMapperSDPoseRender`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `GetNode`
- `Note`
- `LoadImage`
- `ImageBatch`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `PreviewImage`
- `SetNode`
- `INTConstant`
- `MarkdownNote`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `BodyRatioMapperProportionTransfer`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `BodyRatioMapperSDPoseRender`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SAM3_TrackToMask`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `CLIPVisionEncode`
- `BBoxYOLO`
- `YOLOModelLoader`
- `BBoxYOLO`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseKeypointExtractor`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `MaskToImage`
- `SetNode`
- `SetNode`
- `SAM3_TrackToMask`
- `GetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GrowMask`
- `BlockifyMask`
- `MaskToImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `InvertMask`
- `GetNode`
- `GetNode`
- `Note`
- `OnnxDetectionModelLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `InvertMask`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `BatchImagesNode`
- `SetNode`
- `ImageBatch`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SAM3_TrackPreview`
- `GetNode`
- `Note`
- `GetNode`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `GetNode`
- `ImageFromBatch`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `GetNode`
- `ImageFromBatch`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `GetNode`
- `ImageFromBatch`
- `WanAnimateToVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanAnimateToVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanAnimateToVideo`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BatchImagesNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `Note`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `BodyRatioMapperSDPoseRender`
- `SDPoseKeypointExtractor`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `GetNode`
- `KSampler` ★核心
- `WanAnimateToVideo`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `SetNode`
- `CLIPLoader`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`
- `seed` = `1028228345876161`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **32%**（101/314）

**有卡**：`YOLOModelLoader`、`BodyRatioMapperSDPoseRender`、`LoadImage`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ImageBatch`、`INTConstant`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`SAM3_VideoTrack`、`BodyRatioMapperProportionTransfer`、`CLIPVisionEncode`、`DrawMaskOnImage`、`SAM3_TrackToMask`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`GrowMask`、`BlockifyMask`、`MaskToImage`、`VAELoader`、`InvertMask`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`TrimVideoLatent`、`VAEDecode`、`ImageFromBatch`、`WanAnimateToVideo`、`BatchImagesNode`、`SAM3_TrackPreview`、`KSampler`、`CLIPVisionLoader`、`VHS_VideoInfoLoaded`、`CLIPLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 6 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
