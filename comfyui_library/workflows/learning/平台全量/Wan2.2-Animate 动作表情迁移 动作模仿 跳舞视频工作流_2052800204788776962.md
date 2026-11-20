---
key: 平台全量/Wan2.2-Animate 动作表情迁移 动作模仿 跳舞视频工作流_2052800204788776962.json
name: Wan2.2-Animate 动作表情迁移 动作模仿 跳舞视频工作流_2052800204788776962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Animate 动作表情迁移 动作模仿 跳舞视频工作流_2052800204788776962.json
hash: 5bb0a6a31671a6df
coverage: 0.492754
learned_at: 2026-11-14 01:05:53
nodes: [WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, GetNode, SetNode, easy cleanGpuUsed, WanVideoSetBlockSwap, ImageResizeKJv2, GetNode, GetNode, GetNode, Switch image [Crystools], FaceMaskFromPoseKeypoints, GetNode, SetNode, GetNode, GetNode, ImageCropByMaskAndResize, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoDecode, GetNode, GetNode, WanVideoAnimateEmbeds, GetImageSizeAndCount, easy showAnything, GetNode, VHS_VideoCombine, WanVideoSampler, GetNode, SetNode, SetNode, VHS_VideoInfoLoaded, SetNode, SetNode, easy showAnything, SetNode, SetNode, SetNode, ImageResizeKJv2, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, INTConstant, INTConstant, SetNode, VHS_LoadVideo, WanVideoModelLoader, SetNode, VHS_VideoCombine, SetNode, VHS_VideoCombine, DWPreprocessor, PixelPerfectResolution, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Animate 动作表情迁移 动作模仿 跳舞视频工作流_2052800204788776962.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Animate 动作表情迁移 动作模仿 跳舞视频工作流_2052800204788776962.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（69 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `Switch image [Crystools]`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageCropByMaskAndResize`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetImageSizeAndCount`
- `easy showAnything`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `PixelPerfectResolution`
- `LoadImage`

## 知识

覆盖率 **49%**（34/69）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`ImageResizeKJv2`、`Switch image [Crystools]`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoSampler`、`VHS_VideoInfoLoaded`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`INTConstant`、`VHS_LoadVideo`、`WanVideoModelLoader`、`DWPreprocessor`、`PixelPerfectResolution`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
