---
key: 视频生成/图生视频/动作迁移丨Wan2.2-Animate丨人物替换·自动尺寸_2099797041361805313.json
name: 动作迁移丨Wan2.2-Animate丨人物替换·自动尺寸_2099797041361805313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移丨Wan2.2-Animate丨人物替换·自动尺寸_2099797041361805313.json
hash: 3737d5d6fce3700d
coverage: 0.653409
learned_at: 2026-10-17 01:59:45
nodes: [GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, LazySwitch1way, SetNode, SetNode, PoseAndFaceDetection, PoseAndFaceDetection, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, GetNode, GetNode, SetNode, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoEncode, WanVideoSampler, WanVideoUni3C_embeds, LazySwitch1way, WanVideoClipVisionEncode, GetNode, SetNode, DrawViTPose, GetNode, YOLOModelLoader, BBoxYOLO, BBoxYOLO, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseKeypointExtractor, WanVideoLoraSelectMulti, easy cleanGpuUsed, SDPoseKeypointExtractor, YOLOModelLoader, BodyRatioMapperSDPoseRender, WanVideoBlockSwap, WanVideoBlockSwap, easy anythingIndexSwitch, WanVideoContextOptions, WanVideoContextOptions, WanVideoContextOptions, WanVideoBlockSwap, LayerUtility: ColorImage V2, LazySwitch1way, easy compare, CR Text, CR Text, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, easy mathInt, easy float, SetNode, SetNode, SetNode, easy float, SetNode, easy float, SetNode, easy float, easy int, Note, easy boolean, easy float, easy boolean, BodyRatioMapperProportionTransfer, easy boolean, easy int, WanVideoUni3C_ControlnetLoader, SDPoseDrawKeypoints, WanVideoDecode, easy boolean, GetNode, easy imageSize, easy float, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, SetNode, SetNode, SetNode, easy int, easy int, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, ImageScaleToTotalPixels, easy anythingIndexSwitch, easy float, LazySwitch2way, easy anythingIndexSwitch, easy int, easy int, WanVideoAnimateEmbeds, easy cleanGpuUsed, GetNode, WanVideoSampler, easy anythingIndexSwitch, Note, easy int, AnyBooleanSwitch, easy anythingIndexSwitch, easy int, easy int, easy int, GetNode, GetNode, LazySwitch1way, PrimitiveBoolean, ZML_AnyTypeSwitchFiveBoolean, easy boolean, easy boolean, GetNode, ImageFromBatch, easy int, CompressImages, easy int, easy int, easy mathInt, easy int, easy int, easy compare, easy int, easy int, LazySwitch1way, easy int, ImpactSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, ImpactSwitch, LoadImage, VHS_VideoCombine, VideoCombineNode, ImpactSwitch, VHS_LoadVideo, Note, Note, Note]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/动作迁移丨Wan2.2-Animate丨人物替换·自动尺寸_2099797041361805313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移丨Wan2.2-Animate丨人物替换·自动尺寸_2099797041361805313.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（176 个）：
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
- `RepeatImageBatch`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `PoseAndFaceDetection`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
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
- `GetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoUni3C_embeds`
- `LazySwitch1way`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `DrawViTPose`
- `GetNode`
- `YOLOModelLoader`
- `BBoxYOLO`
- `BBoxYOLO`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `WanVideoLoraSelectMulti`
- `easy cleanGpuUsed`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `BodyRatioMapperSDPoseRender`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `easy anythingIndexSwitch`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `LayerUtility: ColorImage V2`
- `LazySwitch1way`
- `easy compare`
- `CR Text`
- `CR Text`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `easy float`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `easy int`
- `Note`
- `easy boolean`
- `easy float`
- `easy boolean`
- `BodyRatioMapperProportionTransfer`
- `easy boolean`
- `easy int`
- `WanVideoUni3C_ControlnetLoader`
- `SDPoseDrawKeypoints`
- `WanVideoDecode`
- `easy boolean`
- `GetNode`
- `easy imageSize`
- `easy float`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `ImageScaleToTotalPixels`
- `easy anythingIndexSwitch`
- `easy float`
- `LazySwitch2way`
- `easy anythingIndexSwitch`
- `easy int`
- `easy int`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy anythingIndexSwitch`
- `Note`
- `easy int`
- `AnyBooleanSwitch`
- `easy anythingIndexSwitch`
- `easy int`
- `easy int`
- `easy int`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `PrimitiveBoolean`
- `ZML_AnyTypeSwitchFiveBoolean`
- `easy boolean`
- `easy boolean`
- `GetNode`
- `ImageFromBatch`
- `easy int`
- `CompressImages`
- `easy int`
- `easy int`
- `easy mathInt`
- `easy int`
- `easy int`
- `easy compare`
- `easy int`
- `easy int`
- `LazySwitch1way`
- `easy int`
- `ImpactSwitch`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `ImpactSwitch`
- `LoadImage`
- `VHS_VideoCombine`
- `VideoCombineNode`
- `ImpactSwitch`
- `VHS_LoadVideo`
- `Note`
- `Note`
- `Note`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **65%**（115/176）

**有卡**：`CLIPVisionLoader`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ImageFromBatch`、`ImageBatch`、`easy mathInt`、`BatchCount+`、`RHHiddenNodes`、`WanVideoLoraSelectMulti`、`easy cleanGpuUsed`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoClipVisionEncode`、`DrawViTPose`、`YOLOModelLoader`、`BBoxYOLO`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`WanVideoBlockSwap`、`easy anythingIndexSwitch`、`WanVideoContextOptions`、`LayerUtility: ColorImage V2`、`easy compare`、`CR Text`、`VHS_VideoInfo`、`easy float`、`easy int`、`easy boolean`、`BodyRatioMapperProportionTransfer`、`WanVideoUni3C_ControlnetLoader`、`SDPoseDrawKeypoints`、`WanVideoDecode`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`ImageScaleToTotalPixels`、`LazySwitch2way`、`WanVideoAnimateEmbeds`、`AnyBooleanSwitch`、`PrimitiveBoolean`、`ZML_AnyTypeSwitchFiveBoolean`、`CompressImages`、`LoadImage`、`VHS_VideoCombine`、`VideoCombineNode`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
