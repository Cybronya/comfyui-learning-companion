---
key: 平台全量/Wan2.2 Animate动作迁移_2058121448727859202.json
name: Wan2.2 Animate动作迁移_2058121448727859202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移_2058121448727859202.json
hash: 8d2d3cb6c9bd1640
coverage: 0.527273
learned_at: 2026-11-14 01:05:20
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, LazySwitch1way, PreviewImage, Note, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, Note, Note, Note, PoseAndFaceDetection, Note, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, LazySwitch1way, CR Text, Note, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, Note, easy imageSize, CR Text, easy compare, Note, Note, Note, WanVideoContextOptions, GetNode, GetNode, ImageFromBatch, Bool, Bool, easy anythingIndexSwitch, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, easy float, SetNode, easy float, SetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, Note, WanVideoDecode, easy float, SetNode, WanVideoSampler, WanVideoEncode, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoUni3C_embeds, LazySwitch1way, LazySwitch2way, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, SetNode, ImageScaleToTotalPixels, easy int, easy boolean, WanVideoClipVisionEncode, easy boolean, SetNode, SetNode, easy boolean, GetNode, GetNode, SetNode, DrawViTPose, easy mathInt, GetNode, YOLOModelLoader, BBoxYOLO, ImageResizeKJv2, BBoxYOLO, easy anythingIndexSwitch, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseKeypointExtractor, WanVideoLoraSelectMulti, SDPoseDrawKeypoints, ImpactSwitch, Bool, easy mathInt, easy anythingIndexSwitch, ZML_AnyTypeSwitchFiveBoolean, VideoCombineNode, CompressImages, Note, easy float, easy int, GetNode, VHS_VideoCombine, easy cleanGpuUsed, SDPoseKeypointExtractor, YOLOModelLoader, easy int, easy int, ImpactSwitch, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, Note, VHS_LoadVideo, LoadImage, Note, easy int]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2 Animate动作迁移_2058121448727859202.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移_2058121448727859202.json`

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
- `LazySwitch1way`
- `PreviewImage`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `PoseAndFaceDetection`
- `Note`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `LazySwitch1way`
- `CR Text`
- `Note`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
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
- `Note`
- `Note`
- `Note`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `Bool`
- `Bool`
- `easy anythingIndexSwitch`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `Note`
- `WanVideoDecode`
- `easy float`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoUni3C_embeds`
- `LazySwitch1way`
- `LazySwitch2way`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `SetNode`
- `ImageScaleToTotalPixels`
- `easy int`
- `easy boolean`
- `WanVideoClipVisionEncode`
- `easy boolean`
- `SetNode`
- `SetNode`
- `easy boolean`
- `GetNode`
- `GetNode`
- `SetNode`
- `DrawViTPose`
- `easy mathInt`
- `GetNode`
- `YOLOModelLoader`
- `BBoxYOLO`
- `ImageResizeKJv2`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `WanVideoLoraSelectMulti`
- `SDPoseDrawKeypoints`
- `ImpactSwitch`
- `Bool`
- `easy mathInt`
- `easy anythingIndexSwitch`
- `ZML_AnyTypeSwitchFiveBoolean`
- `VideoCombineNode`
- `CompressImages`
- `Note`
- `easy float`
- `easy int`
- `GetNode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `easy int`
- `easy int`
- `ImpactSwitch`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `Note`
- `easy int`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **53%**（87/165）

**有卡**：`CLIPVisionLoader`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`CR Text`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`WanVideoAnimateEmbeds`、`ImageFromBatch`、`ImageBatch`、`easy mathInt`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`WanVideoContextOptions`、`Bool`、`easy anythingIndexSwitch`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy float`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoBlockSwap`、`WanVideoUni3C_embeds`、`LazySwitch2way`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`easy boolean`、`WanVideoClipVisionEncode`、`DrawViTPose`、`YOLOModelLoader`、`BBoxYOLO`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`SDPoseDrawKeypoints`、`ZML_AnyTypeSwitchFiveBoolean`、`VideoCombineNode`、`CompressImages`、`VHS_VideoCombine`、`BodyRatioMapperProportionTransfer`、`BodyRatioMapperSDPoseRender`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
