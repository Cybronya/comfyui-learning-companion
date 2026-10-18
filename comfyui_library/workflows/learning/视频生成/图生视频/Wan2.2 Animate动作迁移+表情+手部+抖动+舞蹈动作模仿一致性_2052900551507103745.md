---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部+抖动+舞蹈动作模仿一致性_2052900551507103745.json
name: Wan2.2 Animate动作迁移+表情+手部+抖动+舞蹈动作模仿一致性_2052900551507103745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部+抖动+舞蹈动作模仿一致性_2052900551507103745.json
hash: 26d8732a3947b534
coverage: 0.510791
learned_at: 2026-10-15 22:37:33
nodes: [GetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, SetNode, SetNode, ImageResizeKJv2, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, LazySwitch1way, CR Text, WanVideoLoraSelectMulti, GetNode, MemoryCleaner, SetNode, easy int, ImageFromBatch, ImageBatch, GetNode, easy mathInt, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, LazySwitch2way, easy int, Note, Reroute, YOLOModelLoader, BBoxYOLO, WanVideoContextOptions, CheckpointLoaderSimple, SetNode, easy float, WanVideoLoraSelectMulti, easy float, easy mathInt, RenderNLFPoses, DrawViTPose, DownloadAndLoadNLFModel, easy anythingIndexSwitch, SDPoseDrawKeypoints, BatchCount+, GetNode, BatchCount+, SDPoseKeypointExtractor, easy int, easy int, SetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, MemoryCleaner, MemoryCleaner, WanVideoDecode, GetNode, GetNode, CLIPVisionLoader, SetNode, SetNode, WanVideoClipVisionEncode, SetNode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoTextEncodeCached, SetNode, Note, WanVideoSampler, Note, VHS_VideoCombine, Note, easy boolean, easy int, Note, LoadImage, ImpactSwitch, Note, Note, easy boolean, Note, Note, easy float, Note, Note, WanVideoBlockSwap, Primitive integer [Crystools], Primitive integer [Crystools], SimpleMath+, easy int, easy compare, CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, VHS_LoadVideo, LoadImage, SetNode]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部+抖动+舞蹈动作模仿一致性_2052900551507103745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052900551507103745.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（139 个）：
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
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `LazySwitch1way`
- `CR Text`
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
- `LazySwitch2way`
- `easy int`
- `Note`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `WanVideoContextOptions`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `easy float`
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
- `easy int`
- `easy int`
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
- `Note`
- `VHS_VideoCombine`
- `Note`
- `easy boolean`
- `easy int`
- `Note`
- `LoadImage`
- `ImpactSwitch`
- `Note`
- `Note`
- `easy boolean`
- `Note`
- `Note`
- `easy float`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `easy int`
- `easy compare`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `VHS_LoadVideo`
- `LoadImage`
- `SetNode`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **51%**（71/139）

**有卡**：`ImageFromBatch`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoInfo`、`CR Text`、`WanVideoLoraSelectMulti`、`MemoryCleaner`、`easy int`、`ImageBatch`、`easy mathInt`、`RHHiddenNodes`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`WanVideoContextOptions`、`CheckpointLoaderSimple`、`easy float`、`RenderNLFPoses`、`DrawViTPose`、`DownloadAndLoadNLFModel`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`BatchCount+`、`SDPoseKeypointExtractor`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`VHS_VideoCombine`、`easy boolean`、`LoadImage`、`WanVideoBlockSwap`、`Primitive integer [Crystools]`、`SimpleMath+`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSize`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
