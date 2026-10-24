---
key: 图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json
name: Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json
hash: 7c0b1c198ea34e07
coverage: 0.503876
learned_at: 2026-10-23 11:27:58
nodes: [GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, YOLOModelLoader, Note, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoDecode, GetNode, PoseAndFaceDetection, VRAMReserver, SetNode, SetNode, SetNode, VHS_VideoInfo, DownloadAndLoadNLFModel, DrawViTPose, SetNode, LazySwitch1way, CR Text, Note, easy int, easy float, easy float, LayerUtility: ImageScaleByAspectRatio V2, WanVideoContextOptions, easy boolean, SetNode, Note, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeCached, SDPoseOODProcessor, easy mathInt, GetNode, RenderNLFPoses, easy anythingIndexSwitch, MemoryCleaner, VHS_VideoCombine, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, WanVideoAnimateEmbeds, easy float, Note, Note, WanVideoBlockSwap, ImpactSwitch, GetNode, GetNode, GetNode, GetNode, SetNode, MemoryCleaner, WanVideoLoraSelectMulti, LoadImage, easy int, SetNode, SetNode, CR Text, easy compare, SetNode, easy imageSize, VHS_LoadVideo, ImageFromBatch, GetNode, BatchCount+, BatchCount+, SetNode, SetNode, SetNode, easy mathInt, ImageBatch, RepeatImageBatch, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy int]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（129 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `ImageFromBatch`
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
- `SDPoseOODLoader`
- `RepeatImageBatch`
- `OnnxDetectionModelLoader`
- `GetNode`
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
- `WanVideoSampler` ★核心
- `MemoryCleaner`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `YOLOModelLoader`
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
- `WanVideoDecode`
- `GetNode`
- `PoseAndFaceDetection`
- `VRAMReserver`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `DownloadAndLoadNLFModel`
- `DrawViTPose`
- `SetNode`
- `LazySwitch1way`
- `CR Text`
- `Note`
- `easy int`
- `easy float`
- `easy float`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoContextOptions`
- `easy boolean`
- `SetNode`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `SDPoseOODProcessor`
- `easy mathInt`
- `GetNode`
- `RenderNLFPoses`
- `easy anythingIndexSwitch`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy int`
- `WanVideoAnimateEmbeds`
- `easy float`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MemoryCleaner`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `easy int`
- `SetNode`
- `SetNode`
- `CR Text`
- `easy compare`
- `SetNode`
- `easy imageSize`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `GetNode`
- `BatchCount+`
- `BatchCount+`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `ImageBatch`
- `RepeatImageBatch`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy int`

## 知识

覆盖率 **50%**（65/129）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`SDPoseOODLoader`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoSampler`、`MemoryCleaner`、`ImageResizeKJv2`、`YOLOModelLoader`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`VRAMReserver`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`CR Text`、`easy int`、`easy float`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoContextOptions`、`easy boolean`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`SDPoseOODProcessor`、`easy mathInt`、`RenderNLFPoses`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`LoadImage`、`easy compare`、`easy imageSize`、`VHS_LoadVideo`、`BatchCount+`、`ImageBatch`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
