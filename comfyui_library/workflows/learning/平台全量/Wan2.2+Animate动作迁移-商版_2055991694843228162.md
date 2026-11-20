---
key: 平台全量/Wan2.2+Animate动作迁移-商版_2055991694843228162.json
name: Wan2.2+Animate动作迁移-商版_2055991694843228162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2+Animate动作迁移-商版_2055991694843228162.json
hash: 85aab0a02f90d973
coverage: 0.446154
learned_at: 2026-11-14 01:05:49
nodes: [easy float, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, easy int, GetNode, GetNode, GetNode, easy int, Note, Note, Note, easy int, Note, easy int, Note, Note, ImageFromBatch, RepeatImageBatch, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoInfo, CLIPVisionLoader, GetNode, DownloadAndLoadNLFModel, SetNode, Note, GetNode, BatchCount+, VideoCombineNode, GetNode, GetNode, CompressImages, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, NLFPredict, PoseDetectionVitPoseToDWPose, SetNode, PoseDetectionVitPoseToDWPose, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LazySwitch1way, GetNode, ImageResizeKJv2, SetNode, RenderNLFPoses, GetNode, easy anythingIndexSwitch, SetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, WanVideoLoraSelectMulti, GetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, BatchCount+, GetNode, GetNode, easy float, easy mathInt, CR Text, CR Text, easy imageSize, easy compare, LazySwitch1way, SetNode, SetNode, SetNode, SimpleMath+, easy mathInt, SetNode, Any To Any, Any To Any, ImageBatch, GetNode, WanVideoVAELoader, WanVideoTextEncodeCached, GetNode, OnnxDetectionModelLoader, GetNode, RepeatImageBatch, PoseAndFaceDetection, DrawViTPose, GetNode, easy int, VHS_VideoCombine, SetNode, SetNode, GetNode, LazySwitch2way, SetNode, SetNode, easy boolean, GetNode, SetNode, SetNode, PreviewImage, SetNode, VHS_VideoCombine, easy mathInt, LayerUtility: ImageScaleByAspectRatio V2, easy float, WanVideoModelLoader, Note, easy float, Note, Note, Note, GetNode, CheckpointLoaderSimple, SetNode, GetNode, GetNode, BBoxYOLO, BBoxYOLO, SetNode, Note, ImageFromBatch, SetNode, WanVideoUni3C_embeds, SetNode, WanVideoEncode, GetNode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, GetNode, GetNode, WanVideoContextOptions, WanVideoAnimateEmbeds, GetNode, easy cleanGpuUsed, GetNode, GetNode, WanVideoSampler, GetNode, Note, Fast Groups Bypasser (rgthree), WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoDecode, VHS_VideoCombine, easy boolean, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, BodyRatioMapperSDPoseRender, VHS_LoadVideo, LoadImage, BodyRatioMapperProportionTransfer, YOLOModelLoader, YOLOModelLoader, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, SetNode, SDPoseKeypointExtractor, SetNode, BodyRatioMapperSDPoseRender, GetNode, BodyRatioMapperSDPoseRender, GetNode, ImpactSwitch, easy int]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2+Animate动作迁移-商版_2055991694843228162.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2+Animate动作迁移-商版_2055991694843228162.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（195 个）：
- `easy float`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy int`
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
- `Note`
- `Note`
- `ImageFromBatch`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoInfo`
- `CLIPVisionLoader`
- `GetNode`
- `DownloadAndLoadNLFModel`
- `SetNode`
- `Note`
- `GetNode`
- `BatchCount+`
- `VideoCombineNode`
- `GetNode`
- `GetNode`
- `CompressImages`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `SetNode`
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
- `GetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `BatchCount+`
- `GetNode`
- `GetNode`
- `easy float`
- `easy mathInt`
- `CR Text`
- `CR Text`
- `easy imageSize`
- `easy compare`
- `LazySwitch1way`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `easy mathInt`
- `SetNode`
- `Any To Any`
- `Any To Any`
- `ImageBatch`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `RepeatImageBatch`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `GetNode`
- `easy int`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `LazySwitch2way`
- `SetNode`
- `SetNode`
- `easy boolean`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `easy mathInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy float`
- `WanVideoModelLoader`
- `Note`
- `easy float`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `BBoxYOLO`
- `BBoxYOLO`
- `SetNode`
- `Note`
- `ImageFromBatch`
- `SetNode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `easy boolean`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `BodyRatioMapperSDPoseRender`
- `VHS_LoadVideo`
- `LoadImage`
- `BodyRatioMapperProportionTransfer`
- `YOLOModelLoader`
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
- `BodyRatioMapperSDPoseRender`
- `GetNode`
- `BodyRatioMapperSDPoseRender`
- `GetNode`
- `ImpactSwitch`
- `easy int`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **45%**（87/195）

**有卡**：`easy float`、`easy int`、`ImageFromBatch`、`RepeatImageBatch`、`VHS_VideoInfo`、`CLIPVisionLoader`、`DownloadAndLoadNLFModel`、`BatchCount+`、`VideoCombineNode`、`CompressImages`、`WanVideoClipVisionEncode`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`PoseAndFaceDetection`、`LazySwitch1way`、`ImageResizeKJv2`、`RenderNLFPoses`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy mathInt`、`CR Text`、`easy imageSize`、`easy compare`、`SimpleMath+`、`Any To Any`、`ImageBatch`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`DrawViTPose`、`VHS_VideoCombine`、`LazySwitch2way`、`easy boolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`CheckpointLoaderSimple`、`BBoxYOLO`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoDecode`、`BodyRatioMapperSDPoseRender`、`VHS_LoadVideo`、`LoadImage`、`BodyRatioMapperProportionTransfer`、`YOLOModelLoader`、`SDPoseKeypointExtractor`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
