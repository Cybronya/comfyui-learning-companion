---
key: 数字人/数字人/Wan2.2 Animate动作迁移V7（自动尺寸）_2052646498596343809.json
name: Wan2.2 Animate动作迁移V7（自动尺寸）_2052646498596343809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate动作迁移V7（自动尺寸）_2052646498596343809.json
hash: c9a5e61853fa829c
coverage: 0.509202
learned_at: 2026-10-26 01:57:52
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, Note, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy int, SetNode, Note, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, RenderNLFPoses, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, Note, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy int, easy int, Note, Note, Note, easy boolean, easy int, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoContextOptions, GetNode, GetNode, ImageFromBatch, Bool, Bool, Bool, easy anythingIndexSwitch, easy mathInt, easy anythingIndexSwitch, ImpactSwitch, VideoCombineNode, ZML_AnyTypeSwitchFiveBoolean, CompressImages, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, SetNode, SetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, VHS_VideoCombine, easy cleanGpuUsed, GetNode, GetNode, GetNode, easy cleanGpuUsed, Note, WanVideoDecode, WanVideoLoraSelectMulti, easy float, SetNode, WanVideoSampler, WanVideoEncode, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoUni3C_embeds, LazySwitch1way, ImpactSwitch, easy boolean, ImageResizeKJv2, Note, easy boolean, easy float, easy float, VHS_VideoInfo, VHS_LoadVideo, easy float, LoadImage, easy int]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 数字人/数字人/Wan2.2 Animate动作迁移V7（自动尺寸）_2052646498596343809.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate动作迁移V7（自动尺寸）_2052646498596343809.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（163 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
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
- `SetNode`
- `DownloadAndLoadNLFModel`
- `DrawViTPose`
- `SetNode`
- `LazySwitch1way`
- `CR Text`
- `Note`
- `easy int`
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
- `easy int`
- `easy int`
- `Note`
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
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `Note`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `easy float`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoUni3C_embeds`
- `LazySwitch1way`
- `ImpactSwitch`
- `easy boolean`
- `ImageResizeKJv2`
- `Note`
- `easy boolean`
- `easy float`
- `easy float`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `easy float`
- `LoadImage`
- `easy int`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **51%**（83/163）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy int`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`easy boolean`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoContextOptions`、`Bool`、`VideoCombineNode`、`ZML_AnyTypeSwitchFiveBoolean`、`CompressImages`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`WanVideoDecode`、`easy float`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoBlockSwap`、`WanVideoUni3C_embeds`、`ImageResizeKJv2`、`VHS_VideoInfo`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
