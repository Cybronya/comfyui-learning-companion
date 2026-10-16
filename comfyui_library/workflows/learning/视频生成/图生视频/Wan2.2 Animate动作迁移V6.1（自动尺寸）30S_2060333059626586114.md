---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1（自动尺寸）30S_2060333059626586114.json
name: Wan2.2 Animate动作迁移V6.1（自动尺寸）30S_2060333059626586114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2060333059626586114.json
hash: f5a4ca976174eccd
coverage: 0.49635
learned_at: 2026-10-15 22:38:47
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, Note, SetNode, SetNode, SetNode, SetNode, WanVideoSampler, MemoryCleaner, SetNode, SetNode, SetNode, Note, Note, Note, SetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoDecode, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, DrawViTPose, LazySwitch1way, CR Text, Note, easy int, easy float, SetNode, Note, easy mathInt, GetNode, RenderNLFPoses, MemoryCleaner, VHS_VideoCombine, SetNode, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, easy float, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, Note, GetNode, MemoryCleaner, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, Note, Note, Note, Note, easy int, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, CheckpointLoaderSimple, SDPoseKeypointExtractor, ImpactSwitch, easy int, easy int, easy int, CLIPVisionLoader, WanVideoClipVisionEncode, PreviewImage, WanVideoBlockSwap, SDPoseDrawKeypoints, WanVideoSetLoRAs, WanVideoVAELoader, GetNode, PoseAndFaceDetection, DownloadAndLoadNLFModel, WanVideoTextEncodeCached, SetNode, WanVideoModelLoader, ImageResizeKJv2, GetNode, SimpleMath+, easy boolean, Int, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, GetNode, SetNode, easy boolean, VHS_LoadVideo, LoadImage, WanVideoContextOptions]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1（自动尺寸）30S_2060333059626586114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060333059626586114.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（137 个）：
- `GetNode`
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
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `MemoryCleaner`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `Note`
- `WanVideoDecode`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `DrawViTPose`
- `LazySwitch1way`
- `CR Text`
- `Note`
- `easy int`
- `easy float`
- `SetNode`
- `Note`
- `easy mathInt`
- `GetNode`
- `RenderNLFPoses`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoSetBlockSwap`
- `easy int`
- `WanVideoAnimateEmbeds`
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
- `GetNode`
- `MemoryCleaner`
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy int`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `ImpactSwitch`
- `easy int`
- `easy int`
- `easy int`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `PreviewImage`
- `WanVideoBlockSwap`
- `SDPoseDrawKeypoints`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `GetNode`
- `PoseAndFaceDetection`
- `DownloadAndLoadNLFModel`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `GetNode`
- `SimpleMath+`
- `easy boolean`
- `Int`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `SetNode`
- `easy boolean`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoContextOptions`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **50%**（68/137）

**有卡**：`ImageFromBatch`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoSampler`、`MemoryCleaner`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`DrawViTPose`、`CR Text`、`easy int`、`easy float`、`easy mathInt`、`RenderNLFPoses`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`SDPoseDrawKeypoints`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`DownloadAndLoadNLFModel`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`ImageResizeKJv2`、`SimpleMath+`、`easy boolean`、`Int`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`LoadImage`、`WanVideoContextOptions`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
