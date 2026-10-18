---
key: 视频生成/图生视频/Wan2.2+Animate动作迁移-多用途_2056978911422140417.json
name: Wan2.2+Animate动作迁移-多用途_2056978911422140417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Animate动作迁移-多用途_2056978911422140417.json
hash: 72a298669c58e527
coverage: 0.443878
learned_at: 2026-10-15 22:38:07
nodes: [easy float, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, easy int, Note, Note, Note, easy int, Note, easy int, ImageFromBatch, RepeatImageBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, DownloadAndLoadNLFModel, SetNode, Note, GetNode, BatchCount+, WanVideoClipVisionEncode, GetNode, GetNode, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LazySwitch1way, GetNode, ImageResizeKJv2, SetNode, RenderNLFPoses, GetNode, easy anythingIndexSwitch, SetNode, easy cleanGpuUsed, GetNode, GetNode, WanVideoLoraSelectMulti, GetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, GetNode, easy float, easy mathInt, SetNode, SetNode, SetNode, SetNode, Any To Any, ImageBatch, GetNode, WanVideoVAELoader, GetNode, GetNode, RepeatImageBatch, DrawViTPose, GetNode, easy int, SetNode, SetNode, SetNode, easy boolean, GetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, easy mathInt, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, Note, easy float, Note, Note, Note, GetNode, CheckpointLoaderSimple, GetNode, GetNode, BBoxYOLO, BBoxYOLO, SetNode, ImageFromBatch, SetNode, WanVideoUni3C_embeds, SetNode, WanVideoEncode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, GetNode, WanVideoContextOptions, GetNode, easy cleanGpuUsed, GetNode, Note, Fast Groups Bypasser (rgthree), WanVideoLoraSelectMulti, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, BodyRatioMapperSDPoseRender, YOLOModelLoader, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, SetNode, SDPoseKeypointExtractor, SetNode, GetNode, BodyRatioMapperSDPoseRender, GetNode, PreviewImage, easy int, Note, PoseAndFaceDetection, YOLOModelLoader, Note, easy int, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, easy boolean, LazySwitch1way, easy compare, CR Text, CR Text, SetNode, VideoCombineNode, GetNode, GetNode, GetNode, CompressImages, easy float, easy imageSize, LazySwitch2way, SetNode, SetNode, VHS_VideoInfo, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, Note, NLFPredict, ImpactSwitch, WanVideoDecode, Fast Groups Bypasser (rgthree), WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage, GetNode, GetNode, SetNode, SetNode, Any To Any, BatchCount+, SetNode, SimpleMath+, easy mathInt, OnnxDetectionModelLoader, SetNode, WanVideoTextEncodeCached]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2+Animate动作迁移-多用途_2056978911422140417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2056978911422140417.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（196 个）：
- `easy float`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `Note`
- `Note`
- `Note`
- `easy int`
- `Note`
- `easy int`
- `ImageFromBatch`
- `RepeatImageBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `DownloadAndLoadNLFModel`
- `SetNode`
- `Note`
- `GetNode`
- `BatchCount+`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LazySwitch1way`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `RenderNLFPoses`
- `GetNode`
- `easy anythingIndexSwitch`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy float`
- `easy mathInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Any To Any`
- `ImageBatch`
- `GetNode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `DrawViTPose`
- `GetNode`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy boolean`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `easy mathInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `Note`
- `easy float`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `GetNode`
- `BBoxYOLO`
- `BBoxYOLO`
- `SetNode`
- `ImageFromBatch`
- `SetNode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `WanVideoContextOptions`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `BodyRatioMapperSDPoseRender`
- `YOLOModelLoader`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SDPoseKeypointExtractor`
- `SetNode`
- `SDPoseKeypointExtractor`
- `SetNode`
- `GetNode`
- `BodyRatioMapperSDPoseRender`
- `GetNode`
- `PreviewImage`
- `easy int`
- `Note`
- `PoseAndFaceDetection`
- `YOLOModelLoader`
- `Note`
- `easy int`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `easy boolean`
- `LazySwitch1way`
- `easy compare`
- `CR Text`
- `CR Text`
- `SetNode`
- `VideoCombineNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CompressImages`
- `easy float`
- `easy imageSize`
- `LazySwitch2way`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `NLFPredict`
- `ImpactSwitch`
- `WanVideoDecode`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Any To Any`
- `BatchCount+`
- `SetNode`
- `SimpleMath+`
- `easy mathInt`
- `OnnxDetectionModelLoader`
- `SetNode`
- `WanVideoTextEncodeCached`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **44%**（87/196）

**有卡**：`easy float`、`easy int`、`ImageFromBatch`、`RepeatImageBatch`、`CLIPVisionLoader`、`DownloadAndLoadNLFModel`、`BatchCount+`、`WanVideoClipVisionEncode`、`PoseDetectionVitPoseToDWPose`、`PoseAndFaceDetection`、`LazySwitch1way`、`ImageResizeKJv2`、`RenderNLFPoses`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy mathInt`、`Any To Any`、`ImageBatch`、`WanVideoVAELoader`、`DrawViTPose`、`easy boolean`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`CheckpointLoaderSimple`、`BBoxYOLO`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`BodyRatioMapperSDPoseRender`、`YOLOModelLoader`、`SDPoseKeypointExtractor`、`BodyRatioMapperProportionTransfer`、`easy compare`、`CR Text`、`VideoCombineNode`、`CompressImages`、`easy imageSize`、`LazySwitch2way`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`NLFPredict`、`WanVideoDecode`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`SimpleMath+`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
