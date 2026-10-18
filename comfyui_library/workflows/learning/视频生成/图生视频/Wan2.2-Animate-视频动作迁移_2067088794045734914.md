---
key: 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2067088794045734914.json
name: Wan2.2-Animate-视频动作迁移_2067088794045734914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2067088794045734914.json
hash: a9a81997f54880ea
coverage: 0.964286
learned_at: 2026-10-15 22:39:56
nodes: [ImageConcatMulti, PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, RHHiddenNodes, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, LoadImage, Text, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2067088794045734914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067088794045734914.json`

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
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`
- `Text`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ImageConcatMulti`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`Text`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
