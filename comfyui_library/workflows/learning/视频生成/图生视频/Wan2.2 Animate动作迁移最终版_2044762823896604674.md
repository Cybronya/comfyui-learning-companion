---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移最终版_2044762823896604674.json
name: Wan2.2 Animate动作迁移最终版_2044762823896604674.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移最终版_2044762823896604674.json
hash: 7b8004879757863b
coverage: 0.484127
learned_at: 2026-10-15 22:36:40
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, ImageFromBatch, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, BatchCount+, ImageBatch, RepeatImageBatch, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, MemoryCleaner, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, YOLOModelLoader, WanVideoVAELoader, Note, Note, Note, Note, RHHiddenNodes, easy mathInt, BatchCount+, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, WanVideoTextEncodeCached, Note, Note, WanVideoDecode, GetNode, VHS_VideoCombine, SetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, PoseAndFaceDetection, RenderNLFPoses, VRAMReserver, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy boolean, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, Note, Note, Note, SetNode, DownloadAndLoadNLFModel, WanVideoContextOptions, WanVideoContextOptions, LazySwitch1way, SetNode, easy float, WanVideoBlockSwap, easy int, easy float, easy anythingIndexSwitch, DrawViTPose, easy mathInt, SDPoseOODProcessor, LazySwitch1way, MemoryCleaner, Note, VHS_VideoCombine, easy boolean, VHS_LoadVideo, LoadImage, easy int, easy int, easy int, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移最终版_2044762823896604674.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044762823896604674.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（126 个）：
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
- `BatchCount+`
- `ImageBatch`
- `RepeatImageBatch`
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
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
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
- `Note`
- `Note`
- `Note`
- `RHHiddenNodes`
- `easy mathInt`
- `BatchCount+`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `PoseAndFaceDetection`
- `RenderNLFPoses`
- `VRAMReserver`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy boolean`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `DownloadAndLoadNLFModel`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `LazySwitch1way`
- `SetNode`
- `easy float`
- `WanVideoBlockSwap`
- `easy int`
- `easy float`
- `easy anythingIndexSwitch`
- `DrawViTPose`
- `easy mathInt`
- `SDPoseOODProcessor`
- `LazySwitch1way`
- `MemoryCleaner`
- `Note`
- `VHS_VideoCombine`
- `easy boolean`
- `VHS_LoadVideo`
- `LoadImage`
- `easy int`
- `easy int`
- `easy int`
- `easy int`

## 知识

覆盖率 **48%**（61/126）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`WanVideoClipVisionEncode`、`SDPoseOODLoader`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoAnimateEmbeds`、`MemoryCleaner`、`WanVideoSampler`、`ImageResizeKJv2`、`YOLOModelLoader`、`WanVideoVAELoader`、`RHHiddenNodes`、`easy mathInt`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`RenderNLFPoses`、`VRAMReserver`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy boolean`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`WanVideoContextOptions`、`easy float`、`WanVideoBlockSwap`、`easy int`、`easy anythingIndexSwitch`、`DrawViTPose`、`SDPoseOODProcessor`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
