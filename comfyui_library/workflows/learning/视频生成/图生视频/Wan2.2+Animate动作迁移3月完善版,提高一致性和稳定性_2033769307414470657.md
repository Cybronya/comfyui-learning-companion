---
key: 视频生成/图生视频/Wan2.2+Animate动作迁移3月完善版,提高一致性和稳定性_2033769307414470657.json
name: Wan2.2+Animate动作迁移3月完善版,提高一致性和稳定性_2033769307414470657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Animate动作迁移3月完善版,提高一致性和稳定性_2033769307414470657.json
hash: 43e820085b7353e8
coverage: 0.504425
learned_at: 2026-10-15 22:35:41
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, ImageFromBatch, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, ImageBatch, RepeatImageBatch, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, MemoryCleaner, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, YOLOModelLoader, WanVideoVAELoader, Note, easy mathInt, BatchCount+, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, VHS_VideoCombine, WanVideoTextEncodeCached, easy mathInt, easy anythingIndexSwitch, WanVideoDecode, VHS_VideoCombine, SetNode, WanVideoLoraSelectMulti, SDPoseOODProcessor, PoseAndFaceDetection, VRAMReserver, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, VHS_LoadVideo, SetNode, MemoryCleaner, Note, easy int, easy float, easy boolean, Note, Note, WanVideoLoraSelectMulti, WanVideoModelLoader, RHHiddenNodes, SetNode, GetNode, easy int, easy int, easy int, LazySwitch1way, GetNode, RepeatImageBatch, GetNode, BatchCount+, WanVideoSetLoRAs, WanVideoSetBlockSwap, DrawViTPose, GetNode, GetNode, NLFPredict, RenderNLFPoses, DownloadAndLoadNLFModel, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoBlockSwap, PreviewImage, easy int, LoadImage, easy float]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2+Animate动作迁移3月完善版,提高一致性和稳定性_2033769307414470657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033769307414470657.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（113 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `ImageFromBatch`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatch`
- `RepeatImageBatch`
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
- `SDPoseOODLoader`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MemoryCleaner`
- `WanVideoSampler` ★核心
- `MemoryCleaner`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `YOLOModelLoader`
- `WanVideoVAELoader`
- `Note`
- `easy mathInt`
- `BatchCount+`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `easy mathInt`
- `easy anythingIndexSwitch`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `SDPoseOODProcessor`
- `PoseAndFaceDetection`
- `VRAMReserver`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `MemoryCleaner`
- `Note`
- `easy int`
- `easy float`
- `easy boolean`
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `RHHiddenNodes`
- `SetNode`
- `GetNode`
- `easy int`
- `easy int`
- `easy int`
- `LazySwitch1way`
- `GetNode`
- `RepeatImageBatch`
- `GetNode`
- `BatchCount+`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `DrawViTPose`
- `GetNode`
- `GetNode`
- `NLFPredict`
- `RenderNLFPoses`
- `DownloadAndLoadNLFModel`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `PreviewImage`
- `easy int`
- `LoadImage`
- `easy float`

## 知识

覆盖率 **50%**（57/113）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`ImageBatch`、`RepeatImageBatch`、`WanVideoClipVisionEncode`、`SDPoseOODLoader`、`OnnxDetectionModelLoader`、`MemoryCleaner`、`WanVideoSampler`、`ImageResizeKJv2`、`YOLOModelLoader`、`WanVideoVAELoader`、`easy mathInt`、`BatchCount+`、`PoseAndFaceDetection`、`PoseDetectionVitPoseToDWPose`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`easy anythingIndexSwitch`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`SDPoseOODProcessor`、`VRAMReserver`、`VHS_VideoInfo`、`VHS_LoadVideo`、`easy int`、`easy float`、`easy boolean`、`WanVideoModelLoader`、`RHHiddenNodes`、`LazySwitch1way`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`DrawViTPose`、`NLFPredict`、`RenderNLFPoses`、`DownloadAndLoadNLFModel`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
