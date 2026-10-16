---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1-自适应调整 显存优化_2038787173708734465.json
name: Wan2.2 Animate动作迁移V6.1-自适应调整 显存优化_2038787173708734465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038787173708734465.json
hash: ec88a0ffc3505a6c
coverage: 0.524138
learned_at: 2026-10-15 22:36:04
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, SetNode, SetNode, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, PoseAndFaceDetection, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, WanVideoLoraSelectMulti, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, GetNode, RenderNLFPoses, MemoryCleaner, SetNode, WanVideoSetLoRAs, MemoryCleaner, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoBlockSwap, GetNode, WanVideoSampler, WanVideoContextOptions, WanVideoAnimateEmbeds, GetNode, ImageBatch, BatchCount+, easy mathInt, ImageFromBatch, easy mathInt, easy mathInt, GetNode, SetNode, SDPoseDrawKeypoints, OnnxDetectionModelLoader, easy int, Note, Note, Note, Note, easy int, Note, Note, SetNode, VHS_VideoCombine, WanVideoDecode, easy mathInt, SetNode, SetNode, BatchCount+, easy mathInt, SetNode, RepeatImageBatch, PreviewImage, PreviewImage, LoadImage, VHS_LoadVideo, easy mathInt, easy int, easy mathInt, easy int, easy int, WanVideoModelLoader, easy boolean, easy int, easy int, SetNode, ImpactSwitch, Note, Note, easy float, Note, SetNode, easy boolean, Note, Note, easy float, easy float, easy float, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, 孤海注释, CR Text, CR Text]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1-自适应调整 显存优化_2038787173708734465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038787173708734465.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（145 个）：
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
- `SetNode`
- `SetNode`
- `MemoryCleaner`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PoseAndFaceDetection`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
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
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `easy mathInt`
- `GetNode`
- `RenderNLFPoses`
- `MemoryCleaner`
- `SetNode`
- `WanVideoSetLoRAs`
- `MemoryCleaner`
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `ImageBatch`
- `BatchCount+`
- `easy mathInt`
- `ImageFromBatch`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `SetNode`
- `SDPoseDrawKeypoints`
- `OnnxDetectionModelLoader`
- `easy int`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy int`
- `Note`
- `Note`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `easy mathInt`
- `SetNode`
- `SetNode`
- `BatchCount+`
- `easy mathInt`
- `SetNode`
- `RepeatImageBatch`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `VHS_LoadVideo`
- `easy mathInt`
- `easy int`
- `easy mathInt`
- `easy int`
- `easy int`
- `WanVideoModelLoader`
- `easy boolean`
- `easy int`
- `easy int`
- `SetNode`
- `ImpactSwitch`
- `Note`
- `Note`
- `easy float`
- `Note`
- `SetNode`
- `easy boolean`
- `Note`
- `Note`
- `easy float`
- `easy float`
- `easy float`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `孤海注释`
- `CR Text`
- `CR Text`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **52%**（76/145）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`MemoryCleaner`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoLoraSelectMulti`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoSetLoRAs`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`ImageBatch`、`BatchCount+`、`SDPoseDrawKeypoints`、`easy int`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadImage`、`VHS_LoadVideo`、`WanVideoModelLoader`、`easy boolean`、`easy float`、`WanVideoSetBlockSwap`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
