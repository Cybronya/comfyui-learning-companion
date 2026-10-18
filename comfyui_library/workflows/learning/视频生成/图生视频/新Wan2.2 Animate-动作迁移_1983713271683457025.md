---
key: 视频生成/图生视频/新Wan2.2 Animate-动作迁移_1983713271683457025.json
name: 新Wan2.2 Animate-动作迁移_1983713271683457025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/新Wan2.2 Animate-动作迁移_1983713271683457025.json
hash: 84bae83da39db634
coverage: 0.964286
learned_at: 2026-10-15 22:32:45
nodes: [WanVideoSetBlockSwap, MarkdownNote, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, WanVideoModelLoader, ImageResizeKJv2, VHS_VideoCombine, LoadImage, WanVideoBlockSwap, CLIPVisionLoader, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, Text, PixelPerfectResolution, ImageCropByMaskAndResize, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoSampler, RHHiddenNodes, JWInteger, JWInteger, DWPreprocessor, VHS_LoadVideo, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/新Wan2.2 Animate-动作迁移_1983713271683457025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983713271683457025.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoSetBlockSwap`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `FaceMaskFromPoseKeypoints`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `Text`
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `JWInteger`
- `JWInteger`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`WanVideoModelLoader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`LoadImage`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`Text`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`RHHiddenNodes`、`JWInteger`、`DWPreprocessor`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
