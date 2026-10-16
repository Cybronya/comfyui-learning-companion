---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移002（头发飘动版）_2052701962461818882.json
name: Wan2.2 Animate动作迁移002（头发飘动版）_2052701962461818882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052701962461818882.json
hash: 5c629bae186cbe39
coverage: 0.515528
learned_at: 2026-10-15 22:37:31
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy int, easy boolean, SetNode, Note, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, RenderNLFPoses, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy int, easy int, Note, Note, easy boolean, easy int, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoContextOptions, Bool, Bool, Bool, easy anythingIndexSwitch, easy mathInt, easy anythingIndexSwitch, ImpactSwitch, VideoCombineNode, ZML_AnyTypeSwitchFiveBoolean, CompressImages, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, SetNode, easy float, SetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, Note, ImpactSwitch, WanVideoLoraSelectMulti, easy float, SetNode, WanVideoEncode, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoUni3C_embeds, easy int, WanVideoAnimateEmbeds, easy float, easy float, easy boolean, GetNode, VHS_LoadVideo, LoadImage, VHS_VideoCombine, GetNode, GetNode, ImageFromBatch, GetNode, easy cleanGpuUsed, LazySwitch1way, WanVideoDecode, WanVideoSampler, WanVideoSampler, Note, Note]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移002（头发飘动版）_2052701962461818882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052701962461818882.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（161 个）：
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
- `easy int`
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
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `easy int`
- `easy int`
- `Note`
- `Note`
- `easy boolean`
- `easy int`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `WanVideoContextOptions`
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
- `Note`
- `ImpactSwitch`
- `WanVideoLoraSelectMulti`
- `easy float`
- `SetNode`
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoUni3C_embeds`
- `easy int`
- `WanVideoAnimateEmbeds`
- `easy float`
- `easy float`
- `easy boolean`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `easy cleanGpuUsed`
- `LazySwitch1way`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Note`
- `Note`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **52%**（83/161）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy int`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoContextOptions`、`Bool`、`VideoCombineNode`、`ZML_AnyTypeSwitchFiveBoolean`、`CompressImages`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy float`、`easy cleanGpuUsed`、`WanVideoEncode`、`WanVideoBlockSwap`、`WanVideoUni3C_embeds`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
