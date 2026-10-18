---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部一致性_2059989559043248130.json
name: Wan2.2 Animate动作迁移+表情+手部一致性_2059989559043248130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部一致性_2059989559043248130.json
hash: 827aaef107eb3398
coverage: 0.50365
learned_at: 2026-10-15 22:38:45
nodes: [GetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, SetNode, SetNode, ImageResizeKJv2, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, PoseAndFaceDetection, SetNode, SetNode, WanVideoLoraSelectMulti, GetNode, MemoryCleaner, SetNode, easy int, ImageFromBatch, ImageBatch, GetNode, easy mathInt, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, Note, Reroute, YOLOModelLoader, BBoxYOLO, WanVideoContextOptions, CheckpointLoaderSimple, Note, easy float, SetNode, Note, WanVideoLoraSelectMulti, easy float, easy mathInt, RenderNLFPoses, DrawViTPose, DownloadAndLoadNLFModel, easy anythingIndexSwitch, SDPoseDrawKeypoints, BatchCount+, GetNode, BatchCount+, SDPoseKeypointExtractor, SetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, MemoryCleaner, MemoryCleaner, WanVideoDecode, GetNode, GetNode, CLIPVisionLoader, SetNode, SetNode, WanVideoClipVisionEncode, SetNode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoTextEncodeCached, SetNode, Note, WanVideoSampler, VHS_VideoCombine, easy int, easy int, Note, easy int, easy int, WanVideoBlockSwap, Note, Note, Note, Note, Note, easy boolean, Note, easy int, ImpactSwitch, easy boolean, easy float, LoadImage, easy compare, VHS_VideoInfo, SetNode, SetNode, SetNode, SetNode, SimpleMath+, LazySwitch2way, CR Text, CR Text, LazySwitch1way, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, SetNode, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部一致性_2059989559043248130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059989559043248130.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（137 个）：
- `GetNode`
- `GetNode`
- `GetNode`
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
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `Note`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `MemoryCleaner`
- `SetNode`
- `easy int`
- `ImageFromBatch`
- `ImageBatch`
- `GetNode`
- `easy mathInt`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `Note`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `WanVideoContextOptions`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `easy float`
- `SetNode`
- `Note`
- `WanVideoLoraSelectMulti`
- `easy float`
- `easy mathInt`
- `RenderNLFPoses`
- `DrawViTPose`
- `DownloadAndLoadNLFModel`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `BatchCount+`
- `GetNode`
- `BatchCount+`
- `SDPoseKeypointExtractor`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `MemoryCleaner`
- `MemoryCleaner`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `SetNode`
- `Note`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `Note`
- `easy int`
- `easy int`
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy boolean`
- `Note`
- `easy int`
- `ImpactSwitch`
- `easy boolean`
- `easy float`
- `LoadImage`
- `easy compare`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `LazySwitch2way`
- `CR Text`
- `CR Text`
- `LazySwitch1way`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `SetNode`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **50%**（69/137）

**有卡**：`ImageFromBatch`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoLoraSelectMulti`、`MemoryCleaner`、`easy int`、`ImageBatch`、`easy mathInt`、`RHHiddenNodes`、`YOLOModelLoader`、`BBoxYOLO`、`WanVideoContextOptions`、`CheckpointLoaderSimple`、`easy float`、`RenderNLFPoses`、`DrawViTPose`、`DownloadAndLoadNLFModel`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`BatchCount+`、`SDPoseKeypointExtractor`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`easy boolean`、`LoadImage`、`easy compare`、`VHS_VideoInfo`、`SimpleMath+`、`LazySwitch2way`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSize`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
