---
key: 视频生成/图生视频/Wan2.2 动作迁移V6.1+抖动（动作表情一致性强）_2041459050583433217.json
name: Wan2.2 动作迁移V6.1+抖动（动作表情一致性强）_2041459050583433217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 动作迁移V6.1+抖动（动作表情一致性强）_2041459050583433217.json
hash: 086e9801c2190d96
coverage: 0.5
learned_at: 2026-10-15 22:36:20
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoDecode, WanVideoLoraSelectMulti, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy int, easy float, easy float, easy boolean, SetNode, Note, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, GetNode, RenderNLFPoses, MemoryCleaner, VHS_VideoCombine, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, easy float, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, GetNode, MemoryCleaner, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy int, easy int, Note, Note, Note, Note, easy boolean, easy int, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, ImpactSwitch, WanVideoBlockSwap, WanVideoContextOptions, easy int, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 动作迁移V6.1+抖动（动作表情一致性强）_2041459050583433217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041459050583433217.json`

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
- `GetNode`
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
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `ImpactSwitch`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `easy int`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **50%**（67/134）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoSampler`、`MemoryCleaner`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy int`、`easy float`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoBlockSwap`、`WanVideoContextOptions`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
