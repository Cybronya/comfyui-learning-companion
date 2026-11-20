---
key: 平台全量/WanVideo SCAIL Context LongLength - SCAIL上下文长视频_2001122624182812674.json
name: WanVideo SCAIL Context LongLength - SCAIL上下文长视频_2001122624182812674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WanVideo SCAIL Context LongLength - SCAIL上下文长视频_2001122624182812674.json
hash: 718febda4df545a7
coverage: 0.626866
learned_at: 2026-11-14 01:07:10
nodes: [LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoEmptyEmbeds, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, SetNode, SetNode, WanVideoScheduler, SetNode, GetNode, FloatConstant, SetNode, GetNode, Note, WanVideoAddSCAILReferenceEmbeds, ImageConcatMulti, VHS_VideoCombine, GetImageSizeAndCount, WanVideoAddSCAILPoseEmbeds, CLIPVisionLoader, WanVideoClipVisionEncode, ImageConcatMulti, NLFPredict, DownloadAndLoadNLFModel, Reroute, SimpleMath+, SimpleMath+, GetNode, GetNode, Note, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, RenderNLFPoses, MarkdownNote, WanVideoSchedulerv2, WanVideoContextOptions, WanVideoSamplerExtraArgs, WanVideoSamplerv2, LoadImage, ImageResizeKJv2, GetNode, GetNode, VHS_LoadVideo, WanVideoTextEncode, WanVideoModelLoader, WanVideoLoraSelect]
patterns: []
missing: []
---

# 平台全量/WanVideo SCAIL Context LongLength - SCAIL上下文长视频_2001122624182812674.json

> 来源文件 `comfyui_library/workflows/平台全量/WanVideo SCAIL Context LongLength - SCAIL上下文长视频_2001122624182812674.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（67 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoEmptyEmbeds`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `GetNode`
- `FloatConstant`
- `SetNode`
- `GetNode`
- `Note`
- `WanVideoAddSCAILReferenceEmbeds`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoAddSCAILPoseEmbeds`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `ImageConcatMulti`
- `NLFPredict`
- `DownloadAndLoadNLFModel`
- `Reroute`
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `Note`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `MarkdownNote`
- `WanVideoSchedulerv2`
- `WanVideoContextOptions`
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoSamplerv2` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`

## 知识

覆盖率 **63%**（42/67）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`ImageResizeKJv2`、`VHS_VideoCombine`、`INTConstant`、`WanVideoScheduler`、`FloatConstant`、`WanVideoAddSCAILReferenceEmbeds`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAddSCAILPoseEmbeds`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`NLFPredict`、`DownloadAndLoadNLFModel`、`SimpleMath+`、`OnnxDetectionModelLoader`、`PoseDetectionVitPoseToDWPose`、`RenderNLFPoses`、`WanVideoSchedulerv2`、`WanVideoContextOptions`、`WanVideoSamplerExtraArgs`、`WanVideoSamplerv2`、`LoadImage`、`VHS_LoadVideo`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoSamplerExtraArgs、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncode
