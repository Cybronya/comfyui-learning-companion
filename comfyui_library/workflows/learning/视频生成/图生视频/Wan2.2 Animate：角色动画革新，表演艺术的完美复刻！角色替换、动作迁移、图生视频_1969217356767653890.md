---
key: 视频生成/图生视频/Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json
name: Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json
hash: d311c12504887940
coverage: 0.964286
learned_at: 2026-10-15 22:31:48
nodes: [ImageConcatMulti, PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoSetLoRAs, ImageResizeKJv2, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, Text, LoadImage, JWInteger, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, RHHiddenNodes, JWInteger, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969217356767653890.json`

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
- `ImageResizeKJv2`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `Text`
- `LoadImage`
- `JWInteger`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `JWInteger`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ImageConcatMulti`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`Text`、`LoadImage`、`JWInteger`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
