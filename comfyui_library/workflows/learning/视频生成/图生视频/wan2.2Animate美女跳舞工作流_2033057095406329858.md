---
key: 视频生成/图生视频/wan2.2Animate美女跳舞工作流_2033057095406329858.json
name: wan2.2Animate美女跳舞工作流_2033057095406329858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033057095406329858.json
hash: 311228a63c6ba022
coverage: 0.777778
learned_at: 2026-10-15 22:35:38
nodes: [WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageResizeKJv2, WanVideoSampler, WanVideoDecode, easy cleanGpuUsed, WanVideoClipVisionEncode, ImageCropByMaskAndResize, PixelPerfectResolution, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoVAELoader, CLIPVisionLoader, GetNode, SetNode, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, ImageConcatMulti, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, INTConstant, INTConstant, LoadImage, VHS_LoadVideo, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2Animate美女跳舞工作流_2033057095406329858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033057095406329858.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `FaceMaskFromPoseKeypoints`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`VHS_VideoCombine`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
