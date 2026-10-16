---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移（姿势面部胸部幅度大小可调节）（自动尺寸）_2039936284520615937.json
name: Wan2.2 Animate动作迁移（姿势面部胸部幅度大小可调节）（自动尺寸）_2039936284520615937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039936284520615937.json
hash: 050c06197b12da38
coverage: 0.5
learned_at: 2026-10-15 22:36:12
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, easy float, Note, SetNode, easy boolean, Note, easy int, easy float, Note, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, BatchCount+, ImageBatch, ImageFromBatch, easy mathInt, VHS_VideoInfo, SetNode, SetNode, SetNode, SetNode, LazySwitch2way, LayerUtility: ImageScaleByAspectRatio V2, easy compare, CR Text, easy imageSize, CR Text, LazySwitch1way, SetNode, SetNode, easy int, easy int, Note, Note, easy int, easy int, Note, Note, easy float, SetNode, VHS_VideoCombine, SetNode, ImpactSwitch, Note, MemoryCleaner, ImageResizeKJv2, PreviewImage, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, MemoryCleaner, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, WanVideoDecode, WanVideoLoraSelectMulti, GetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoSetBlockSwap, Reroute, easy anythingIndexSwitch, BBoxYOLO, SDPoseKeypointExtractor, YOLOModelLoader, DrawViTPose, MemoryCleaner, SetNode, GetNode, GetNode, DownloadAndLoadNLFModel, NLFPredict, RepeatImageBatch, LazySwitch1way, GetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, OnnxDetectionModelLoader, CheckpointLoaderSimple, easy mathInt, RenderNLFPoses, SDPoseDrawKeypoints, PoseDetectionVitPoseToDWPose, SetNode, PoseAndFaceDetection, PoseDetectionVitPoseToDWPose, Note, easy boolean, easy int, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoContextOptions, WanVideoBlockSwap, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移（姿势面部胸部幅度大小可调节）（自动尺寸）_2039936284520615937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039936284520615937.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（134 个）：
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
- `SetNode`
- `Note`
- `easy float`
- `Note`
- `SetNode`
- `easy boolean`
- `Note`
- `easy int`
- `easy float`
- `Note`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `BatchCount+`
- `BatchCount+`
- `ImageBatch`
- `ImageFromBatch`
- `easy mathInt`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LazySwitch2way`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy compare`
- `CR Text`
- `easy imageSize`
- `CR Text`
- `LazySwitch1way`
- `SetNode`
- `SetNode`
- `easy int`
- `easy int`
- `Note`
- `Note`
- `easy int`
- `easy int`
- `Note`
- `Note`
- `easy float`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `ImpactSwitch`
- `Note`
- `MemoryCleaner`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `MemoryCleaner`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `Reroute`
- `easy anythingIndexSwitch`
- `BBoxYOLO`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `DrawViTPose`
- `MemoryCleaner`
- `SetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadNLFModel`
- `NLFPredict`
- `RepeatImageBatch`
- `LazySwitch1way`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `CheckpointLoaderSimple` ★核心
- `easy mathInt`
- `RenderNLFPoses`
- `SDPoseDrawKeypoints`
- `PoseDetectionVitPoseToDWPose`
- `SetNode`
- `PoseAndFaceDetection`
- `PoseDetectionVitPoseToDWPose`
- `Note`
- `easy boolean`
- `easy int`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **50%**（67/134）

**有卡**：`easy float`、`easy boolean`、`easy int`、`RepeatImageBatch`、`RHHiddenNodes`、`BatchCount+`、`ImageBatch`、`ImageFromBatch`、`easy mathInt`、`VHS_VideoInfo`、`LazySwitch2way`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy compare`、`CR Text`、`easy imageSize`、`LazySwitch1way`、`VHS_VideoCombine`、`MemoryCleaner`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`easy anythingIndexSwitch`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`YOLOModelLoader`、`DrawViTPose`、`DownloadAndLoadNLFModel`、`NLFPredict`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`CheckpointLoaderSimple`、`RenderNLFPoses`、`SDPoseDrawKeypoints`、`PoseDetectionVitPoseToDWPose`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
