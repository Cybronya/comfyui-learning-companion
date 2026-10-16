---
key: 视频生成/图生视频/Wan Animate2.2动作迁移Move加速版V1_1969195120677580801.json
name: Wan Animate2.2动作迁移Move加速版V1_1969195120677580801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969195120677580801.json
hash: e85fe97e49bd2c26
coverage: 0.509091
learned_at: 2026-10-15 22:31:47
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, Note, Note, LoadImage, JWInteger, PixelPerfectResolution, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, DWPreprocessor, ImageCropByMaskAndResize, SetNode, VHS_VideoCombine, SetNode, JWInteger, VHS_LoadVideo, ImageResizeKJv2, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, easy cleanGpuUsed]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2动作迁移Move加速版V1_1969195120677580801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969195120677580801.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（55 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `Note`
- `Note`
- `LoadImage`
- `JWInteger`
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `ImageCropByMaskAndResize`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `JWInteger`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`

## 知识

覆盖率 **51%**（28/55）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageConcatMulti`、`LoadImage`、`JWInteger`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
