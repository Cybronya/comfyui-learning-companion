---
key: 数字人/数字人/wan-2.2-动作迁移-V3_2058811529675501570.json
name: wan-2.2-动作迁移-V3_2058811529675501570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan-2.2-动作迁移-V3_2058811529675501570.json
hash: bc2c9219476cedeb
coverage: 0.520548
learned_at: 2026-10-26 01:59:24
nodes: [WanVideoTorchCompileSettings, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, PixelPerfectResolution, easy cleanGpuUsed, ImageResizeKJv2, GetNode, GetNode, GetNode, Switch image [Crystools], FaceMaskFromPoseKeypoints, SetNode, SetNode, DWPreprocessor, GetNode, GetNode, VHS_VideoCombine, ImageCropByMaskAndResize, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoLoraSelectMulti, GetNode, GetImageSizeAndCount, easy showAnything, GetNode, SetNode, GetNode, VHS_VideoInfoLoaded, SetNode, SetNode, SetNode, ImageResizeKJv2, WanVideoLoraSelectMulti, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, INTConstant, INTConstant, easy showAnything, LoadImage, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoModelLoader, WanVideoSampler, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, VHS_VideoCombine, SeedVR2BlockSwap, SeedVR2ExtraArgs, WanVideoDecode, easy cleanGpuUsed, VHS_VideoCombine, SeedVR2, Int, WanVideoBlockSwap, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/wan-2.2-动作迁移-V3_2058811529675501570.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan-2.2-动作迁移-V3_2058811529675501570.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（73 个）：
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `Switch image [Crystools]`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageCropByMaskAndResize`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetImageSizeAndCount`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `easy showAnything`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `VHS_VideoCombine`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SeedVR2`
- `Int`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`

## 知识

覆盖率 **52%**（38/73）

**有卡**：`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`PixelPerfectResolution`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`Switch image [Crystools]`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`VHS_VideoCombine`、`ImageCropByMaskAndResize`、`WanVideoLoraSelectMulti`、`GetImageSizeAndCount`、`VHS_VideoInfoLoaded`、`INTConstant`、`LoadImage`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`WanVideoDecode`、`SeedVR2`、`Int`、`WanVideoBlockSwap`、`VHS_LoadVideo`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
