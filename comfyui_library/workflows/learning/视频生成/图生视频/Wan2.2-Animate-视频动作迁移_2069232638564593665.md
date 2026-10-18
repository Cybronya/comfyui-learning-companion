---
key: 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2069232638564593665.json
name: Wan2.2-Animate-视频动作迁移_2069232638564593665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2069232638564593665.json
hash: be60f621e2685042
coverage: 0.964286
learned_at: 2026-10-15 22:40:26
nodes: [ImageConcatMulti, PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, RHHiddenNodes, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, Text, JWInteger, JWInteger, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2069232638564593665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069232638564593665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `ImageConcatMulti`
- `PixelPerfectResolution`
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
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `Text`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ImageConcatMulti`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`ImageResizeKJv2`、`VHS_LoadVideo`、`Text`、`JWInteger`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
