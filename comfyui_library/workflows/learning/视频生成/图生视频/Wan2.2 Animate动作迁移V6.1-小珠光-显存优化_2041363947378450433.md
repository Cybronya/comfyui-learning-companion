---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1-小珠光-显存优化_2041363947378450433.json
name: Wan2.2 Animate动作迁移V6.1-小珠光-显存优化_2041363947378450433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移V6.1-小珠光-显存优化_2041363947378450433.json
hash: c22202ee68ed28c8
coverage: 0.489051
learned_at: 2026-10-15 22:36:19
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoDecode, WanVideoLoraSelectMulti, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy int, easy float, easy float, easy boolean, SetNode, Note, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, GetNode, RenderNLFPoses, MemoryCleaner, VHS_VideoCombine, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, easy int, easy float, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, Note, easy int, MemoryCleaner, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy int, easy int, Note, Note, Note, Note, easy boolean, easy int, VHS_LoadVideo, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, ImpactSwitch, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, WanVideoSampler, WanVideoContextOptions, WanVideoAnimateEmbeds, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1-小珠光-显存优化_2041363947378450433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041363947378450433.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（137 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
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
- `RepeatImageBatch`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `GetNode`
- `PreviewImage`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MemoryCleaner`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `Note`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `DownloadAndLoadNLFModel`
- `DrawViTPose`
- `SetNode`
- `LazySwitch1way`
- `CR Text`
- `Note`
- `easy int`
- `easy float`
- `easy float`
- `easy boolean`
- `SetNode`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `easy mathInt`
- `GetNode`
- `RenderNLFPoses`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `easy int`
- `easy float`
- `Note`
- `ImageFromBatch`
- `ImageBatch`
- `GetNode`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `BatchCount+`
- `Note`
- `easy int`
- `MemoryCleaner`
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `easy int`
- `easy int`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy boolean`
- `easy int`
- `VHS_LoadVideo`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `ImpactSwitch`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **49%**（67/137）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`MemoryCleaner`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy int`、`easy float`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`VHS_LoadVideo`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
