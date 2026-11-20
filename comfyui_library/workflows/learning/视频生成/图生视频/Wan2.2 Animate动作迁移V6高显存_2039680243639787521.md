---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移V6高显存_2039680243639787521.json
name: Wan2.2 Animate动作迁移V6高显存_2039680243639787521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移V6高显存_2039680243639787521.json
hash: 9b7e020a6ea1c83a
coverage: 0.496
learned_at: 2026-10-30 17:58:57
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, YOLOModelLoader, Note, Note, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoLoraSelectMulti, VRAMReserver, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, DownloadAndLoadNLFModel, DrawViTPose, SetNode, WanVideoContextOptions, SetNode, Note, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeCached, SDPoseOODProcessor, easy mathInt, GetNode, RenderNLFPoses, easy anythingIndexSwitch, MemoryCleaner, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, Note, ImpactSwitch, WanVideoBlockSwap, GetNode, MemoryCleaner, easy float, Note, easy int, easy int, LoadImage, easy imageSize, easy int, CR Text, easy compare, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LazySwitch1way, VHS_VideoCombine, GetNode, WanVideoSampler, WanVideoDecode, easy float, Note, WanVideoAnimateEmbeds, easy float, easy boolean, GetNode, GetNode, PoseAndFaceDetection, easy mathInt, ImageFromBatch, ImageBatch, GetNode, BatchCount+, RepeatImageBatch, SetNode, SetNode, SetNode, BatchCount+, RHHiddenNodes, GetNode, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移V6高显存_2039680243639787521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移V6高显存_2039680243639787521.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（125 个）：
- `GetNode`
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
- `GetNode`
- `SDPoseOODLoader`
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
- `MemoryCleaner`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `YOLOModelLoader`
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
- `WanVideoLoraSelectMulti`
- `VRAMReserver`
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
- `WanVideoContextOptions`
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
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy int`
- `Note`
- `ImpactSwitch`
- `WanVideoBlockSwap`
- `GetNode`
- `MemoryCleaner`
- `easy float`
- `Note`
- `easy int`
- `easy int`
- `LoadImage`
- `easy imageSize`
- `easy int`
- `CR Text`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `LazySwitch1way`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy float`
- `Note`
- `WanVideoAnimateEmbeds`
- `easy float`
- `easy boolean`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `easy mathInt`
- `ImageFromBatch`
- `ImageBatch`
- `GetNode`
- `BatchCount+`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `BatchCount+`
- `RHHiddenNodes`
- `GetNode`
- `VHS_LoadVideo`

## 知识

覆盖率 **50%**（62/125）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`SDPoseOODLoader`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`MemoryCleaner`、`ImageResizeKJv2`、`YOLOModelLoader`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoLoraSelectMulti`、`VRAMReserver`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`SDPoseOODProcessor`、`easy mathInt`、`RenderNLFPoses`、`easy anythingIndexSwitch`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`WanVideoBlockSwap`、`easy float`、`LoadImage`、`easy imageSize`、`CR Text`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`easy boolean`、`ImageBatch`、`BatchCount+`、`RHHiddenNodes`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
