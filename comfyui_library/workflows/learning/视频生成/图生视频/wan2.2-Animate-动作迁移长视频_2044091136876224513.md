---
key: 视频生成/图生视频/wan2.2-Animate-动作迁移长视频_2044091136876224513.json
name: wan2.2-Animate-动作迁移长视频_2044091136876224513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Animate-动作迁移长视频_2044091136876224513.json
hash: ef0fc939ed5ae783
coverage: 0.492063
learned_at: 2026-10-15 22:36:36
nodes: [GetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, MemoryCleaner, SetNode, SetNode, SetNode, easy int, easy int, easy int, Note, CR Text, LazySwitch1way, CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy compare, easy imageSize, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, Note, easy int, ImpactSwitch, Note, Note, Note, easy float, Note, easy float, Note, easy float, easy boolean, SetNode, VRAMReserver, SetNode, GetNode, WanVideoAnimateEmbeds, WanVideoSampler, GetNode, MemoryCleaner, WanVideoDecode, GetNode, VHS_VideoCombine, easy mathInt, ImageFromBatch, ImageBatch, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, GetNode, BatchCount+, RHHiddenNodes, SetNode, WanVideoModelLoader, SetNode, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, LazySwitch1way, PoseAndFaceDetection, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, RepeatImageBatch, easy anythingIndexSwitch, DrawViTPose, PoseAndFaceDetection, GetNode, GetNode, GetNode, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SDPoseOODLoader, PoseDetectionVitPoseToDWPose, NLFPredict, DownloadAndLoadNLFModel, GetNode, GetNode, YOLOModelLoader, SDPoseOODProcessor, easy mathInt, MemoryCleaner, SetNode, SetNode, GetNode, LoadImage, Note, Note, SetNode, ImageResizeKJv2, PreviewImage, VHS_LoadVideo, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoContextOptions, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Animate-动作迁移长视频_2044091136876224513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044091136876224513.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（126 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
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
- `GetNode`
- `SetNode`
- `MemoryCleaner`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `easy int`
- `easy int`
- `Note`
- `CR Text`
- `LazySwitch1way`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy compare`
- `easy imageSize`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `Note`
- `easy int`
- `ImpactSwitch`
- `Note`
- `Note`
- `Note`
- `easy float`
- `Note`
- `easy float`
- `Note`
- `easy float`
- `easy boolean`
- `SetNode`
- `VRAMReserver`
- `SetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `GetNode`
- `MemoryCleaner`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `easy mathInt`
- `ImageFromBatch`
- `ImageBatch`
- `BatchCount+`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `GetNode`
- `BatchCount+`
- `RHHiddenNodes`
- `SetNode`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `easy anythingIndexSwitch`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SDPoseOODLoader`
- `PoseDetectionVitPoseToDWPose`
- `NLFPredict`
- `DownloadAndLoadNLFModel`
- `GetNode`
- `GetNode`
- `YOLOModelLoader`
- `SDPoseOODProcessor`
- `easy mathInt`
- `MemoryCleaner`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `Note`
- `Note`
- `SetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_LoadVideo`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`

## 知识

覆盖率 **49%**（62/126）

**有卡**：`ImageFromBatch`、`MemoryCleaner`、`easy int`、`CR Text`、`LazySwitch1way`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy compare`、`easy imageSize`、`VHS_VideoInfo`、`easy float`、`easy boolean`、`VRAMReserver`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`easy mathInt`、`ImageBatch`、`BatchCount+`、`RepeatImageBatch`、`RHHiddenNodes`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`easy anythingIndexSwitch`、`DrawViTPose`、`PoseDetectionVitPoseToDWPose`、`RenderNLFPoses`、`SDPoseOODLoader`、`NLFPredict`、`DownloadAndLoadNLFModel`、`YOLOModelLoader`、`SDPoseOODProcessor`、`LoadImage`、`ImageResizeKJv2`、`VHS_LoadVideo`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
