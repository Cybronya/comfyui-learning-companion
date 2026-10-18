---
key: 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json
name: Wan2.2 Animate-动作迁移_2011439752528011266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json
hash: 1918fd5be8d5fddc
coverage: 0.964286
learned_at: 2026-10-15 22:34:23
nodes: [ImageConcatMulti, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, JWInteger, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, RHHiddenNodes, JWInteger, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, Text, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, LoadImage, PixelPerfectResolution]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011439752528011266.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `ImageConcatMulti`
- `DWPreprocessor`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `JWInteger`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `RHHiddenNodes`
- `JWInteger`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`
- `PixelPerfectResolution`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ImageConcatMulti`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`JWInteger`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`Text`、`VHS_VideoCombine`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`PixelPerfectResolution`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
