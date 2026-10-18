---
key: 视频生成/图生视频/wan2.2-Animate动作迁移v1_2101930049103548418.json
name: wan2.2-Animate动作迁移v1_2101930049103548418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Animate动作迁移v1_2101930049103548418.json
hash: 93ddfb7c70610393
coverage: 0.593583
learned_at: 2026-10-17 02:29:35
nodes: [GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, LazySwitch1way, SetNode, SetNode, PoseAndFaceDetection, PoseAndFaceDetection, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, Note, GetNode, GetNode, Bool, Bool, easy anythingIndexSwitch, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoDecode, WanVideoSampler, WanVideoEncode, WanVideoSampler, easy cleanGpuUsed, WanVideoUni3C_embeds, LazySwitch1way, WanVideoClipVisionEncode, GetNode, GetNode, SetNode, DrawViTPose, easy mathInt, GetNode, YOLOModelLoader, BBoxYOLO, ImageResizeKJv2, BBoxYOLO, easy anythingIndexSwitch, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseKeypointExtractor, WanVideoLoraSelectMulti, SDPoseDrawKeypoints, ImpactSwitch, Bool, easy mathInt, easy anythingIndexSwitch, ZML_AnyTypeSwitchFiveBoolean, VideoCombineNode, CompressImages, GetNode, easy cleanGpuUsed, SDPoseKeypointExtractor, YOLOModelLoader, easy int, BodyRatioMapperSDPoseRender, WanVideoBlockSwap, WanVideoBlockSwap, easy anythingIndexSwitch, WanVideoContextOptions, WanVideoContextOptions, WanVideoContextOptions, WanVideoBlockSwap, easy mathInt, LayerUtility: ColorImage V2, LazySwitch1way, easy compare, CR Text, CR Text, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, easy mathInt, easy anythingIndexSwitch, easy float, easy int, easy int, easy anythingIndexSwitch, easy int, SetNode, SetNode, SetNode, ImageResizeKJv2, easy imageSize, easy imageSize, LazySwitch2way, easy showAnything, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy float, easy float, 孤海注释, ImpactSwitch, SetNode, SetNode, easy float, 孤海注释, 孤海注释, SetNode, easy float, SetNode, 孤海注释, 孤海注释, easy float, ImageScaleToTotalPixels, 孤海注释, easy int, easy int, easy int, 孤海注释, 孤海注释, 孤海注释, easy int, easy int, 孤海注释, 孤海注释, Note, easy anythingIndexSwitch, ImageFromBatch, VHS_VideoCombine, easy int, easy compare, easy int, LazySwitch1way, easy showAnything, ImpactSwitch, easy int, easy boolean, easy boolean, BodyRatioMapperProportionTransfer, easy boolean, 孤海注释, VHS_LoadVideo, LoadImage, easy boolean, SetNode, easy float, 孤海注释, 孤海注释, 孤海注释]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/wan2.2-Animate动作迁移v1_2101930049103548418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2-Animate动作迁移v1_2101930049103548418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（187 个）：
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
- `easy int`
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
- `GetNode`
- `Bool`
- `Bool`
- `easy anythingIndexSwitch`
- `SetNode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoUni3C_embeds`
- `LazySwitch1way`
- `WanVideoClipVisionEncode`
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
- `GetNode`
- `easy cleanGpuUsed`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `easy int`
- `BodyRatioMapperSDPoseRender`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `easy anythingIndexSwitch`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `easy mathInt`
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
- `WanVideoAnimateEmbeds`
- `easy mathInt`
- `easy anythingIndexSwitch`
- `easy float`
- `easy int`
- `easy int`
- `easy anythingIndexSwitch`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `easy imageSize`
- `easy imageSize`
- `LazySwitch2way`
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy float`
- `easy float`
- `孤海注释`
- `ImpactSwitch`
- `SetNode`
- `SetNode`
- `easy float`
- `孤海注释`
- `孤海注释`
- `SetNode`
- `easy float`
- `SetNode`
- `孤海注释`
- `孤海注释`
- `easy float`
- `ImageScaleToTotalPixels`
- `孤海注释`
- `easy int`
- `easy int`
- `easy int`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `easy int`
- `easy int`
- `孤海注释`
- `孤海注释`
- `Note`
- `easy anythingIndexSwitch`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `easy int`
- `easy compare`
- `easy int`
- `LazySwitch1way`
- `easy showAnything`
- `ImpactSwitch`
- `easy int`
- `easy boolean`
- `easy boolean`
- `BodyRatioMapperProportionTransfer`
- `easy boolean`
- `孤海注释`
- `VHS_LoadVideo`
- `LoadImage`
- `easy boolean`
- `SetNode`
- `easy float`
- `孤海注释`
- `孤海注释`
- `孤海注释`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **59%**（111/187）

**有卡**：`CLIPVisionLoader`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`ImageFromBatch`、`ImageBatch`、`easy mathInt`、`BatchCount+`、`RHHiddenNodes`、`Bool`、`easy anythingIndexSwitch`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoClipVisionEncode`、`DrawViTPose`、`YOLOModelLoader`、`BBoxYOLO`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`SDPoseDrawKeypoints`、`ZML_AnyTypeSwitchFiveBoolean`、`VideoCombineNode`、`CompressImages`、`BodyRatioMapperSDPoseRender`、`WanVideoBlockSwap`、`WanVideoContextOptions`、`LayerUtility: ColorImage V2`、`easy compare`、`CR Text`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`easy float`、`easy imageSize`、`LazySwitch2way`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`VHS_VideoCombine`、`easy boolean`、`BodyRatioMapperProportionTransfer`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
