---
key: 平台全量/Wan2.2 Animate动作迁移V7（自动尺寸）_2046979243996876801.json
name: Wan2.2 Animate动作迁移V7（自动尺寸）_2046979243996876801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移V7（自动尺寸）_2046979243996876801.json
hash: 3b1eae02d99e5b92
coverage: 0.512048
learned_at: 2026-11-14 01:05:17
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy int, easy float, easy boolean, Note, WanVideoVAELoader, WanVideoTextEncodeCached, RenderNLFPoses, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, Note, ImageBatch, easy mathInt, SetNode, RepeatImageBatch, SetNode, RHHiddenNodes, BatchCount+, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy int, Note, Note, Note, Note, easy int, Reroute, BBoxYOLO, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, easy float, SetNode, easy float, SetNode, GetNode, GetNode, Note, SetNode, WanVideoUni3C_embeds, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, LazySwitch1way, easy float, Note, WanVideoDecode, WanVideoSampler, WanVideoSampler, WanVideoLoraSelectMulti, Note, easy boolean, easy mathInt, YOLOModelLoader, easy anythingIndexSwitch, easy int, SetNode, WanVideoContextOptions, ImpactSwitch, easy boolean, WanVideoBlockSwap, VHS_LoadVideo, easy int, LoadImage, Bool, ImpactSwitch, ImageFromBatch, Bool, Bool, easy anythingIndexSwitch, easy mathInt, easy anythingIndexSwitch, GetNode, GetNode, WanVideoEncode, BatchCount+, GetNode, SetNode, ImageFromBatch, GetNode, ZML_AnyTypeSwitchFiveBoolean, VHS_VideoCombine, VideoCombineNode, CompressImages, GetNode]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2 Animate动作迁移V7（自动尺寸）_2046979243996876801.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移V7（自动尺寸）_2046979243996876801.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（166 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
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
- `easy int`
- `easy float`
- `easy boolean`
- `Note`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `RenderNLFPoses`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy int`
- `WanVideoAnimateEmbeds`
- `Note`
- `ImageBatch`
- `easy mathInt`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `RHHiddenNodes`
- `BatchCount+`
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch2way`
- `easy int`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy int`
- `Reroute`
- `BBoxYOLO`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
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
- `SetNode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LazySwitch1way`
- `easy float`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelectMulti`
- `Note`
- `easy boolean`
- `easy mathInt`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `easy int`
- `SetNode`
- `WanVideoContextOptions`
- `ImpactSwitch`
- `easy boolean`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `easy int`
- `LoadImage`
- `Bool`
- `ImpactSwitch`
- `ImageFromBatch`
- `Bool`
- `Bool`
- `easy anythingIndexSwitch`
- `easy mathInt`
- `easy anythingIndexSwitch`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `BatchCount+`
- `GetNode`
- `SetNode`
- `ImageFromBatch`
- `GetNode`
- `ZML_AnyTypeSwitchFiveBoolean`
- `VHS_VideoCombine`
- `VideoCombineNode`
- `CompressImages`
- `GetNode`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **51%**（85/166）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy int`、`easy float`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`RenderNLFPoses`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`ImageBatch`、`easy mathInt`、`RHHiddenNodes`、`BatchCount+`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`BBoxYOLO`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`WanVideoUni3C_embeds`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`、`YOLOModelLoader`、`easy anythingIndexSwitch`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`Bool`、`ImageFromBatch`、`WanVideoEncode`、`ZML_AnyTypeSwitchFiveBoolean`、`VideoCombineNode`、`CompressImages`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
