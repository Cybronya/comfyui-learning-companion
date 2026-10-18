---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移001_2052699613496397825.json
name: Wan2.2 Animate动作迁移001_2052699613496397825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移001_2052699613496397825.json
hash: 7bedcf65da9bb978
coverage: 0.5125
learned_at: 2026-10-15 22:37:31
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoDecode, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, easy float, easy boolean, SetNode, Note, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, RenderNLFPoses, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, BatchCount+, GetNode, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, ImpactSwitch, WanVideoContextOptions, GetNode, GetNode, ImageFromBatch, Bool, Bool, Bool, easy anythingIndexSwitch, easy mathInt, easy anythingIndexSwitch, ImpactSwitch, VideoCombineNode, ZML_AnyTypeSwitchFiveBoolean, CompressImages, WanVideoEncode, easy cleanGpuUsed, SetNode, WanVideoSampler, easy cleanGpuUsed, WanVideoBlockSwap, SetNode, easy float, SetNode, GetNode, GetNode, Note, SetNode, WanVideoUni3C_embeds, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy float, VHS_VideoCombine, easy cleanGpuUsed, GetNode, easy float, CLIPVisionLoader, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, easy int, VHS_VideoCombine, RHHiddenNodes, easy int, easy int, Note, Note, Note, easy int, easy boolean, easy int, Note, Note, Note, Note, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移001_2052699613496397825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052699613496397825.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（160 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `LazySwitch1way`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
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
- `WanVideoDecode`
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
- `easy float`
- `easy boolean`
- `SetNode`
- `Note`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `easy mathInt`
- `RenderNLFPoses`
- `SetNode`
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
- `BatchCount+`
- `GetNode`
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `ImpactSwitch`
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
- `WanVideoEncode`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `SetNode`
- `easy float`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy float`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `GetNode`
- `easy float`
- `CLIPVisionLoader`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `easy int`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `easy int`
- `easy int`
- `Note`
- `Note`
- `Note`
- `easy int`
- `easy boolean`
- `easy int`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **51%**（82/160）

**有卡**：`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy float`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`WanVideoAnimateEmbeds`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoContextOptions`、`Bool`、`VideoCombineNode`、`ZML_AnyTypeSwitchFiveBoolean`、`CompressImages`、`WanVideoEncode`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoUni3C_embeds`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`RHHiddenNodes`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
