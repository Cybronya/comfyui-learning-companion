---
key: 平台全量/Wan2.2 Animate动作迁移必须Plus模式运行_2047297085837418498.json
name: Wan2.2 Animate动作迁移必须Plus模式运行_2047297085837418498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移必须Plus模式运行_2047297085837418498.json
hash: a5daca1d830f2f72
coverage: 0.518293
learned_at: 2026-11-14 01:05:21
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy int, easy boolean, SetNode, Note, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, RenderNLFPoses, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, Note, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy int, easy int, Note, Note, Note, Note, easy boolean, easy int, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoContextOptions, GetNode, GetNode, ImageFromBatch, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, easy float, SetNode, easy float, SetNode, GetNode, GetNode, Note, WanVideoUni3C_embeds, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, Note, WanVideoDecode, WanVideoLoraSelectMulti, easy float, SetNode, LazySwitch1way, WanVideoEncode, easy int, LazySwitch1way, WanVideoBlockSwap, ImpactSwitch, easy int, VideoCombineNode, easy anythingIndexSwitch, easy mathInt, GetNode, ImpactSwitch, easy anythingIndexSwitch, Bool, GetNode, Bool, Bool, CompressImages, ZML_AnyTypeSwitchFiveBoolean, easy boolean, easy float, VHS_VideoCombine, GetNode, WanVideoAnimateEmbeds, WanVideoSampler, GetNode, WanVideoSampler, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2 Animate动作迁移必须Plus模式运行_2047297085837418498.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移必须Plus模式运行_2047297085837418498.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（164 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
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
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Note`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `easy float`
- `SetNode`
- `LazySwitch1way`
- `WanVideoEncode`
- `easy int`
- `LazySwitch1way`
- `WanVideoBlockSwap`
- `ImpactSwitch`
- `easy int`
- `VideoCombineNode`
- `easy anythingIndexSwitch`
- `easy mathInt`
- `GetNode`
- `ImpactSwitch`
- `easy anythingIndexSwitch`
- `Bool`
- `GetNode`
- `Bool`
- `Bool`
- `CompressImages`
- `ZML_AnyTypeSwitchFiveBoolean`
- `easy boolean`
- `easy float`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **52%**（85/164）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy int`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoContextOptions`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy float`、`WanVideoUni3C_embeds`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoEncode`、`WanVideoBlockSwap`、`VideoCombineNode`、`Bool`、`CompressImages`、`ZML_AnyTypeSwitchFiveBoolean`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
