---
key: 数字人/数字人/wan2.2服装+视频自动化_2041447047198412802.json
name: wan2.2服装+视频自动化_2041447047198412802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2服装+视频自动化_2041447047198412802.json
hash: 775fe7375f0b69bf
coverage: 0.483871
learned_at: 2026-10-26 01:59:29
nodes: [GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, ImageFromBatch, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, BatchCount+, ImageBatch, RepeatImageBatch, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseOODLoader, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, MemoryCleaner, WanVideoSampler, MemoryCleaner, SetNode, ImageResizeKJv2, SetNode, SetNode, YOLOModelLoader, WanVideoVAELoader, easy int, Note, Note, Note, Note, easy mathInt, BatchCount+, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, GetNode, Note, Note, WanVideoDecode, GetNode, SetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, PoseAndFaceDetection, RenderNLFPoses, VRAMReserver, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy boolean, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, easy int, easy int, Note, Note, Note, SetNode, DownloadAndLoadNLFModel, WanVideoContextOptions, WanVideoContextOptions, LazySwitch1way, SetNode, easy float, WanVideoBlockSwap, easy int, easy float, easy anythingIndexSwitch, DrawViTPose, easy mathInt, SDPoseOODProcessor, LazySwitch1way, MemoryCleaner, Note, VHS_VideoCombine, easy int, easy boolean, RHHiddenNodes, WanVideoTextEncodeCached, GetNode, VHS_LoadVideo, VHS_VideoCombine, GetNode]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2服装+视频自动化_2041447047198412802.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2服装+视频自动化_2041447047198412802.json`

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
- `easy int`
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
- `easy int`
- `easy boolean`
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `GetNode`

## 知识

覆盖率 **48%**（60/124）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`WanVideoClipVisionEncode`、`SDPoseOODLoader`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`WanVideoAnimateEmbeds`、`MemoryCleaner`、`WanVideoSampler`、`ImageResizeKJv2`、`YOLOModelLoader`、`WanVideoVAELoader`、`easy int`、`easy mathInt`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`RenderNLFPoses`、`VRAMReserver`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy boolean`、`VHS_VideoInfo`、`DownloadAndLoadNLFModel`、`WanVideoContextOptions`、`easy float`、`WanVideoBlockSwap`、`easy anythingIndexSwitch`、`DrawViTPose`、`SDPoseOODProcessor`、`VHS_VideoCombine`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti、CLIPVisionLoader
