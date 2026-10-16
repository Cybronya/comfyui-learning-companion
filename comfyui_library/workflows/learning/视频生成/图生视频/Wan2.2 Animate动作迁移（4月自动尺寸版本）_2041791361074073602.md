---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移（4月自动尺寸版本）_2041791361074073602.json
name: Wan2.2 Animate动作迁移（4月自动尺寸版本）_2041791361074073602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041791361074073602.json
hash: a512c233297a63fe
coverage: 0.5
learned_at: 2026-10-15 22:36:22
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoDecode, WanVideoLoraSelectMulti, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, LazySwitch1way, CR Text, Note, easy float, easy boolean, SetNode, Note, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, GetNode, RenderNLFPoses, MemoryCleaner, VHS_VideoCombine, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, easy int, WanVideoAnimateEmbeds, easy float, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, GetNode, easy imageSize, CR Text, easy compare, LazySwitch2way, Note, Note, Note, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, ImpactSwitch, easy int, easy int, easy int, easy float, SetNode, WanVideoSetBlockSwap, SetNode, LoadImage, MemoryCleaner, easy boolean, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, Note, WanVideoBlockSwap, easy int, WanVideoContextOptions, easy int]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移（4月自动尺寸版本）_2041791361074073602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041791361074073602.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（134 个）：
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
- `WanVideoSampler` ★核心
- `MemoryCleaner`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
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
- `LazySwitch1way`
- `CR Text`
- `Note`
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
- `GetNode`
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LazySwitch2way`
- `Note`
- `Note`
- `Note`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `ImpactSwitch`
- `easy int`
- `easy int`
- `easy int`
- `easy float`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `LoadImage`
- `MemoryCleaner`
- `easy boolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `Note`
- `WanVideoBlockSwap`
- `easy int`
- `WanVideoContextOptions`
- `easy int`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **50%**（67/134）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoSampler`、`MemoryCleaner`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy float`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`easy int`、`WanVideoAnimateEmbeds`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoSetBlockSwap`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`WanVideoContextOptions`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
