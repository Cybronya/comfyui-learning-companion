---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移老版本（自动尺寸）V0.016B_2048554524419297281.json
name: Wan2.2 Animate动作迁移老版本（自动尺寸）V0.016B_2048554524419297281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移老版本（自动尺寸）V0.016B_2048554524419297281.json
hash: bd9498a900732e7b
coverage: 0.509434
learned_at: 2026-10-15 22:37:09
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, Note, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, Note, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy boolean, SetNode, Note, WanVideoVAELoader, WanVideoTextEncodeCached, easy mathInt, RenderNLFPoses, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, Note, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, easy imageSize, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch2way, easy int, easy int, Note, Note, Note, Note, easy boolean, easy int, Reroute, YOLOModelLoader, BBoxYOLO, easy anythingIndexSwitch, SDPoseDrawKeypoints, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoContextOptions, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, SetNode, easy float, SetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, easy cleanGpuUsed, Note, WanVideoDecode, WanVideoLoraSelectMulti, easy float, SetNode, WanVideoSampler, WanVideoEncode, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoUni3C_embeds, LazySwitch1way, ImpactSwitch, GetNode, ImageFromBatch, Bool, GetNode, Bool, Bool, easy mathInt, GetNode, ZML_AnyTypeSwitchFiveBoolean, easy anythingIndexSwitch, GetNode, CompressImages, VideoCombineNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy float, easy float, easy int, easy boolean, easy int, VHS_LoadVideo, LoadImage, ImpactSwitch]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移老版本（自动尺寸）V0.016B_2048554524419297281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048554524419297281.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（159 个）：
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
- `RepeatImageBatch`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `GetNode`
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
- `GetNode`
- `ImageFromBatch`
- `Bool`
- `GetNode`
- `Bool`
- `Bool`
- `easy mathInt`
- `GetNode`
- `ZML_AnyTypeSwitchFiveBoolean`
- `easy anythingIndexSwitch`
- `GetNode`
- `CompressImages`
- `VideoCombineNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy float`
- `easy float`
- `easy int`
- `easy boolean`
- `easy int`
- `VHS_LoadVideo`
- `LoadImage`
- `ImpactSwitch`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **51%**（81/159）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy boolean`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy mathInt`、`RenderNLFPoses`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`WanVideoAnimateEmbeds`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`easy imageSize`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`YOLOModelLoader`、`BBoxYOLO`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoContextOptions`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy float`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoBlockSwap`、`WanVideoUni3C_embeds`、`Bool`、`ZML_AnyTypeSwitchFiveBoolean`、`CompressImages`、`VideoCombineNode`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
