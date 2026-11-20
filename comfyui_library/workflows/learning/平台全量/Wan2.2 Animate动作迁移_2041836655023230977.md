---
key: 平台全量/Wan2.2 Animate动作迁移_2041836655023230977.json
name: Wan2.2 Animate动作迁移_2041836655023230977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移_2041836655023230977.json
hash: f0873e9c1af21e6d
coverage: 0.434211
learned_at: 2026-11-14 01:05:19
nodes: [LazySwitch1way, GetNode, GetNode, GetNode, Note, Note, Note, easy int, easy int, SetNode, SetNode, SetNode, SetNode, easy float, SetNode, SetNode, ImpactSwitch, CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, SetNode, SetNode, Note, Note, easy boolean, easy float, Note, Note, easy int, easy boolean, SetNode, easy int, Note, SetNode, GetNode, GetNode, SetNode, SetNode, CLIPVisionLoader, MemoryCleaner, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, NLFPredict, PoseAndFaceDetection, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, Reroute, RenderNLFPoses, GetNode, GetNode, LazySwitch1way, GetNode, DrawViTPose, BBoxYOLO, YOLOModelLoader, CheckpointLoaderSimple, GetNode, easy anythingIndexSwitch, MemoryCleaner, SetNode, easy mathInt, DownloadAndLoadNLFModel, OnnxDetectionModelLoader, PoseAndFaceDetection, WanVideoContextOptions, WanVideoSetBlockSwap, Note, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, SetNode, SetNode, WanVideoClipVisionEncode, GetNode, SDPoseDrawKeypoints, SDPoseKeypointExtractor, OnnxDetectionModelLoader, ImageFromBatch, Note, WanVideoVAELoader, SetNode, GetNode, GetNode, WanVideoLoraSelectMulti, easy compare, GetNode, SetNode, SetNode, SetNode, MemoryCleaner, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, SetNode, PreviewImage, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, GetNode, RepeatImageBatch, ImageBatch, GetNode, GetNode, SetNode, GetNode, BatchCount+, SetNode, RepeatImageBatch, SetNode, Note, Note, GetNode, GetNode, GetNode, ImageFromBatch, WanVideoDecode, SetNode, BatchCount+, SetNode, GetNode, Note, VHS_VideoInfo, easy mathInt, RHHiddenNodes, GetNode, Note, easy imageSize, Note, Note, Note, easy int, SetNode, easy float, LoadImage, GetNode, GetNode, GetNode, SetNode, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2 Animate动作迁移_2041836655023230977.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移_2041836655023230977.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（152 个）：
- `LazySwitch1way`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `Note`
- `easy int`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy float`
- `SetNode`
- `SetNode`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `easy boolean`
- `easy float`
- `Note`
- `Note`
- `easy int`
- `easy boolean`
- `SetNode`
- `easy int`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `MemoryCleaner`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `NLFPredict`
- `PoseAndFaceDetection`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `Reroute`
- `RenderNLFPoses`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `GetNode`
- `DrawViTPose`
- `BBoxYOLO`
- `YOLOModelLoader`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `easy anythingIndexSwitch`
- `MemoryCleaner`
- `SetNode`
- `easy mathInt`
- `DownloadAndLoadNLFModel`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `WanVideoContextOptions`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `OnnxDetectionModelLoader`
- `ImageFromBatch`
- `Note`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `easy compare`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `RepeatImageBatch`
- `ImageBatch`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `BatchCount+`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `WanVideoDecode`
- `SetNode`
- `BatchCount+`
- `SetNode`
- `GetNode`
- `Note`
- `VHS_VideoInfo`
- `easy mathInt`
- `RHHiddenNodes`
- `GetNode`
- `Note`
- `easy imageSize`
- `Note`
- `Note`
- `Note`
- `easy int`
- `SetNode`
- `easy float`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **43%**（66/152）

**有卡**：`LazySwitch1way`、`easy int`、`easy float`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`easy boolean`、`CLIPVisionLoader`、`MemoryCleaner`、`WanVideoAnimateEmbeds`、`NLFPredict`、`PoseAndFaceDetection`、`PoseDetectionVitPoseToDWPose`、`RenderNLFPoses`、`DrawViTPose`、`BBoxYOLO`、`YOLOModelLoader`、`CheckpointLoaderSimple`、`easy anythingIndexSwitch`、`easy mathInt`、`DownloadAndLoadNLFModel`、`OnnxDetectionModelLoader`、`WanVideoContextOptions`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`SDPoseDrawKeypoints`、`SDPoseKeypointExtractor`、`ImageFromBatch`、`WanVideoVAELoader`、`easy compare`、`VHS_VideoCombine`、`WanVideoSampler`、`ImageResizeKJv2`、`RepeatImageBatch`、`ImageBatch`、`BatchCount+`、`WanVideoDecode`、`VHS_VideoInfo`、`RHHiddenNodes`、`easy imageSize`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader
