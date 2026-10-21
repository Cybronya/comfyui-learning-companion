---
key: 图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json
name: Wan2.2 Animate copy2 1-3_2043561252823244802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json
hash: c37821e3cec26291
coverage: 0.484127
learned_at: 2026-10-21 02:55:23
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, ImageFromBatch, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, BatchCount+, ImageBatch, RepeatImageBatch, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, MemoryCleaner, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, YOLOModelLoader, WanVideoVAELoader, Note, Note, Note, Note, RHHiddenNodes, easy mathInt, BatchCount+, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, WanVideoDecode, GetNode, VHS_VideoCombine, SetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, PoseAndFaceDetection, RenderNLFPoses, VRAMReserver, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy boolean, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, Note, Note, Note, SetNode, DownloadAndLoadNLFModel, WanVideoContextOptions, SetNode, WanVideoBlockSwap, easy int, easy anythingIndexSwitch, DrawViTPose, easy mathInt, SDPoseOODProcessor, LazySwitch1way, MemoryCleaner, Note, VHS_VideoCombine, easy int, easy boolean, easy int, easy float, WanVideoContextOptions, LazySwitch1way, easy int, easy int, WanVideoTextEncodeCached, Note, VHS_LoadVideo, easy float, WanVideoLoraSelectMulti, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json`

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
- `Note`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
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
- `SetNode`
- `WanVideoBlockSwap`
- `easy int`
- `easy anythingIndexSwitch`
- `DrawViTPose`
- `easy mathInt`
- `SDPoseOODProcessor`
- `LazySwitch1way`
- `MemoryCleaner`
- `Note`
- `VHS_VideoCombine`
- `easy int`
- `easy boolean`
- `easy int`
- `easy float`
- `WanVideoContextOptions`
- `LazySwitch1way`
- `easy int`
- `easy int`
- `WanVideoTextEncodeCached`
- `Note`
- `VHS_LoadVideo`
- `easy float`
- `WanVideoLoraSelectMulti`
- `LoadImage`

## 知识

覆盖率 **48%**（61/126）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`WanVideoClipVisionEncode`、`SDPoseOODLoader`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoAnimateEmbeds`、`MemoryCleaner`、`WanVideoSampler`、`ImageResizeKJv2`、`YOLOModelLoader`、`WanVideoVAELoader`、`RHHiddenNodes`、`easy mathInt`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`RenderNLFPoses`、`VRAMReserver`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy boolean`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`easy int`、`easy anythingIndexSwitch`、`DrawViTPose`、`SDPoseOODProcessor`、`easy float`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
