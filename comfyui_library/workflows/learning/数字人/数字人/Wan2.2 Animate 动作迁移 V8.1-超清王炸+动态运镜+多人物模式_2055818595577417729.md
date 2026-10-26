---
key: 数字人/数字人/Wan2.2 Animate 动作迁移 V8.1-超清王炸+动态运镜+多人物模式_2055818595577417729.json
name: Wan2.2 Animate 动作迁移 V8.1-超清王炸+动态运镜+多人物模式_2055818595577417729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 动作迁移 V8.1-超清王炸+动态运镜+多人物模式_2055818595577417729.json
hash: 023cd189459c5f06
coverage: 0.551724
learned_at: 2026-10-26 01:57:49
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, SetNode, ImageResizeKJv2, SetNode, PoseAndFaceDetection, WanVideoVAELoader, SetNode, WanVideoAnimateEmbeds, WanVideoContextOptions, GetNode, GetNode, GetNode, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoClipVisionEncode, GetNode, GetNode, SetNode, DrawViTPose, BBoxYOLO, ImageResizeKJv2, BBoxYOLO, SDPoseKeypointExtractor, SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, SDPoseDrawKeypoints, SDPoseKeypointExtractor, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy imageSize, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, easy imageSize, easy compare, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, WanVideoSampler, GetNode, easy cleanGpuUsed, WanVideoDecode, GetNode, BatchCount+, ImageBatch, ImageFromBatch, easy mathInt, easy mathInt, easy mathInt, SetNode, SetNode, RepeatImageBatch, SetNode, easy mathInt, BatchCount+, SetNode, SetNode, SetNode, GetNode, GetNode, CLIPVisionLoader, Note, GetNode, easy mathInt, Note, easy boolean, easy int, Note, Note, easy int, CR Text, CR Text, LazySwitch1way, SetNode, easy float, SetNode, easy float, SetNode, easy float, Note, Note, SetNode, Note, SetNode, easy float, Note, Note, Note, Note, Note, easy mathInt, easy mathInt, Note, easy int, easy int, easy mathInt, GetNode, WanVideoTextEncodeCached, VHS_VideoCombine, SetNode, easy boolean, CR Text, WanVideoSampler, WanVideoUni3C_ControlnetLoader, GetNode, GetNode, GetNode, WanVideoEncode, WanVideoUni3C_embeds, Reroute, GetNode, VideoCombineNode, GetNode, LazySwitch1way, GetNode, GetNode, easy int, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, OnnxDetectionModelLoader, PoseAndFaceDetection, LoadImage, PreviewImage, Label (rgthree), easy int, GetNode, GetNode, GetNode, GetNode, GetNode, YOLOModelLoader, YOLOModelLoader, easy anythingIndexSwitch, GetNode, GetNode, RepeatImageBatch, easy cleanGpuUsed, BodyRatioMapperProportionTransfer, CheckpointLoaderSimple, easy boolean, Note, easy int, VHS_LoadVideo, ImpactSwitch, CompressImages, ImpactSwitch, easy mathInt, Bool, Bool, easy anythingIndexSwitch, easy anythingIndexSwitch, ZML_AnyTypeSwitchFiveBoolean, ImageFromBatch, Bool, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 数字人/数字人/Wan2.2 Animate 动作迁移 V8.1-超清王炸+动态运镜+多人物模式_2055818595577417729.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 动作迁移 V8.1-超清王炸+动态运镜+多人物模式_2055818595577417729.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（174 个）：
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
- `LazySwitch1way`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PoseAndFaceDetection`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DrawViTPose`
- `BBoxYOLO`
- `ImageResizeKJv2`
- `BBoxYOLO`
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `BodyRatioMapperSDPoseRender`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `easy imageSize`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `easy compare`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `WanVideoSampler` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `GetNode`
- `BatchCount+`
- `ImageBatch`
- `ImageFromBatch`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `SetNode`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `Note`
- `GetNode`
- `easy mathInt`
- `Note`
- `easy boolean`
- `easy int`
- `Note`
- `Note`
- `easy int`
- `CR Text`
- `CR Text`
- `LazySwitch1way`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `Note`
- `Note`
- `SetNode`
- `Note`
- `SetNode`
- `easy float`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy mathInt`
- `easy mathInt`
- `Note`
- `easy int`
- `easy int`
- `easy mathInt`
- `GetNode`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `SetNode`
- `easy boolean`
- `CR Text`
- `WanVideoSampler` ★核心
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `Reroute`
- `GetNode`
- `VideoCombineNode`
- `GetNode`
- `LazySwitch1way`
- `GetNode`
- `GetNode`
- `easy int`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `LoadImage`
- `PreviewImage`
- `Label (rgthree)`
- `easy int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `YOLOModelLoader`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `easy cleanGpuUsed`
- `BodyRatioMapperProportionTransfer`
- `CheckpointLoaderSimple` ★核心
- `easy boolean`
- `Note`
- `easy int`
- `VHS_LoadVideo`
- `ImpactSwitch`
- `CompressImages`
- `ImpactSwitch`
- `easy mathInt`
- `Bool`
- `Bool`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `ZML_AnyTypeSwitchFiveBoolean`
- `ImageFromBatch`
- `Bool`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **55%**（96/174）

**有卡**：`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`WanVideoClipVisionEncode`、`DrawViTPose`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`SDPoseDrawKeypoints`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`easy imageSize`、`ImageScaleToTotalPixels`、`easy compare`、`VHS_VideoInfo`、`WanVideoSampler`、`WanVideoDecode`、`BatchCount+`、`ImageBatch`、`ImageFromBatch`、`easy mathInt`、`RepeatImageBatch`、`CLIPVisionLoader`、`easy boolean`、`easy int`、`CR Text`、`easy float`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`VideoCombineNode`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`OnnxDetectionModelLoader`、`LoadImage`、`Label (rgthree)`、`YOLOModelLoader`、`easy anythingIndexSwitch`、`BodyRatioMapperProportionTransfer`、`CheckpointLoaderSimple`、`VHS_LoadVideo`、`CompressImages`、`Bool`、`ZML_AnyTypeSwitchFiveBoolean`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
