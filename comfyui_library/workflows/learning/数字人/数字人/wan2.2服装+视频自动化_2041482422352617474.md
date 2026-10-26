---
key: 数字人/数字人/wan2.2服装+视频自动化_2041482422352617474.json
name: wan2.2服装+视频自动化_2041482422352617474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2服装+视频自动化_2041482422352617474.json
hash: cb87bee556c6e786
coverage: 0.491935
learned_at: 2026-10-26 01:59:29
nodes: [GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, ImageFromBatch, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, BatchCount+, ImageBatch, RepeatImageBatch, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, MemoryCleaner, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, YOLOModelLoader, WanVideoVAELoader, Note, Note, Note, Note, easy mathInt, BatchCount+, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, Note, WanVideoDecode, GetNode, SetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, PoseAndFaceDetection, RenderNLFPoses, VRAMReserver, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy boolean, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, easy int, easy int, Note, Note, Note, SetNode, DownloadAndLoadNLFModel, WanVideoContextOptions, WanVideoContextOptions, LazySwitch1way, SetNode, easy float, WanVideoBlockSwap, easy int, easy float, easy anythingIndexSwitch, DrawViTPose, easy mathInt, SDPoseOODProcessor, LazySwitch1way, MemoryCleaner, Note, VHS_VideoCombine, easy boolean, RHHiddenNodes, WanVideoTextEncodeCached, VHS_VideoCombine, GetNode, VHS_LoadVideo, LoadImage, easy int, easy int]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2服装+视频自动化_2041482422352617474.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2服装+视频自动化_2041482422352617474.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（124 个）：
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
- `Note`
- `WanVideoDecode`
- `GetNode`
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
- `easy int`
- `easy int`
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
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `easy int`
- `easy int`

## 知识

覆盖率 **49%**（61/124）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`WanVideoClipVisionEncode`、`SDPoseOODLoader`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoAnimateEmbeds`、`MemoryCleaner`、`WanVideoSampler`、`ImageResizeKJv2`、`YOLOModelLoader`、`WanVideoVAELoader`、`easy mathInt`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`RenderNLFPoses`、`VRAMReserver`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy boolean`、`VHS_VideoInfo`、`easy int`、`DownloadAndLoadNLFModel`、`WanVideoContextOptions`、`easy float`、`WanVideoBlockSwap`、`easy anythingIndexSwitch`、`DrawViTPose`、`SDPoseOODProcessor`、`VHS_VideoCombine`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
