---
key: 平台全量/Wan2.2 Animat V7 动作迁移-多功能版_2047132336252260354.json
name: Wan2.2 Animat V7 动作迁移-多功能版_2047132336252260354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animat V7 动作迁移-多功能版_2047132336252260354.json
hash: bf4d5beea4c375e9
coverage: 0.51875
learned_at: 2026-11-14 01:04:50
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, RenderNLFPoses, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, ImageFromBatch, easy mathInt, RepeatImageBatch, SetNode, SetNode, easy imageSize, CR Text, LazySwitch2way, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoContextOptions, GetNode, GetNode, ImageFromBatch, Bool, Bool, Bool, easy anythingIndexSwitch, easy mathInt, easy anythingIndexSwitch, ImpactSwitch, VideoCombineNode, ZML_AnyTypeSwitchFiveBoolean, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, SetNode, SetNode, GetNode, GetNode, Note, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, easy cleanGpuUsed, Note, WanVideoDecode, WanVideoLoraSelectMulti, SetNode, WanVideoSampler, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, LazySwitch1way, WanVideoEncode, WanVideoUni3C_embeds, GetNode, RHHiddenNodes, SetNode, BatchCount+, GetNode, BatchCount+, ImageBatch, easy compare, LayerUtility: ImageScaleByAspectRatio V2, easy int, easy float, Note, Note, easy float, easy float, Note, Note, easy boolean, easy float, easy boolean, ImpactSwitch, VHS_LoadVideo, SetNode, LoadImage, CompressImages, VHS_VideoCombine, MarkdownNote, easy int, MarkdownNote, easy int, easy int, easy int, easy boolean, MarkdownNote, MarkdownNote, MarkdownNote, Note]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2 Animat V7 动作迁移-多功能版_2047132336252260354.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animat V7 动作迁移-多功能版_2047132336252260354.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（160 个）：
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
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
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
- `SetNode`
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
- `ImageFromBatch`
- `easy mathInt`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `easy imageSize`
- `CR Text`
- `LazySwitch2way`
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
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `Note`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `LazySwitch1way`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `RHHiddenNodes`
- `SetNode`
- `BatchCount+`
- `GetNode`
- `BatchCount+`
- `ImageBatch`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `easy float`
- `Note`
- `Note`
- `easy float`
- `easy float`
- `Note`
- `Note`
- `easy boolean`
- `easy float`
- `easy boolean`
- `ImpactSwitch`
- `VHS_LoadVideo`
- `SetNode`
- `LoadImage`
- `CompressImages`
- `VHS_VideoCombine`
- `MarkdownNote`
- `easy int`
- `MarkdownNote`
- `easy int`
- `easy int`
- `easy int`
- `easy boolean`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Note`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **52%**（83/160）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`WanVideoAnimateEmbeds`、`ImageFromBatch`、`easy imageSize`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoContextOptions`、`Bool`、`VideoCombineNode`、`ZML_AnyTypeSwitchFiveBoolean`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`RHHiddenNodes`、`BatchCount+`、`ImageBatch`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy float`、`easy boolean`、`VHS_LoadVideo`、`LoadImage`、`CompressImages`、`VHS_VideoCombine`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
