---
key: 平台全量/Wan1.0自动尺寸迁_2051209252705980417.json
name: Wan1.0自动尺寸迁_2051209252705980417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan1.0自动尺寸迁_2051209252705980417.json
hash: 45b70107214cce9d
coverage: 0.515152
learned_at: 2026-11-14 01:04:23
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy boolean, SetNode, Note, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, RenderNLFPoses, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, Note, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, Note, Note, Note, Note, easy boolean, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoContextOptions, GetNode, GetNode, ImageFromBatch, Bool, Bool, Bool, easy anythingIndexSwitch, easy mathInt, easy anythingIndexSwitch, ImpactSwitch, VideoCombineNode, ZML_AnyTypeSwitchFiveBoolean, CompressImages, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, easy float, SetNode, easy float, SetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, easy cleanGpuUsed, Note, ImpactSwitch, WanVideoDecode, WanVideoLoraSelectMulti, easy float, SetNode, WanVideoSampler, WanVideoEncode, WanVideoBlockSwap, LoadImage, WanVideoSampler, easy cleanGpuUsed, WanVideoUni3C_embeds, LazySwitch1way, easy boolean, easy float, VHS_LoadVideo, easy int, easy int, DuckHideNode, SaveImage, GetNode, VHS_VideoCombine, easy int, easy int, easy int]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan1.0自动尺寸迁_2051209252705980417.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan1.0自动尺寸迁_2051209252705980417.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（165 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
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
- `RepeatImageBatch`
- `OnnxDetectionModelLoader`
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
- `easy boolean`
- `SetNode`
- `Note`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `easy mathInt`
- `RenderNLFPoses`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy int`
- `WanVideoAnimateEmbeds`
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
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy boolean`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `Bool`
- `Bool`
- `Bool`
- `easy anythingIndexSwitch`
- `easy mathInt`
- `easy anythingIndexSwitch`
- `ImpactSwitch`
- `VideoCombineNode`
- `ZML_AnyTypeSwitchFiveBoolean`
- `CompressImages`
- `SetNode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `easy float`
- `SetNode`
- `easy float`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `Note`
- `ImpactSwitch`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `easy float`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `LoadImage`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoUni3C_embeds`
- `LazySwitch1way`
- `easy boolean`
- `easy float`
- `VHS_LoadVideo`
- `easy int`
- `easy int`
- `DuckHideNode`
- `SaveImage`
- `GetNode`
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `easy int`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **52%**（85/165）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`WanVideoAnimateEmbeds`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoContextOptions`、`Bool`、`VideoCombineNode`、`ZML_AnyTypeSwitchFiveBoolean`、`CompressImages`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy float`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoUni3C_embeds`、`VHS_LoadVideo`、`DuckHideNode`、`SaveImage`、`VHS_VideoCombine`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
