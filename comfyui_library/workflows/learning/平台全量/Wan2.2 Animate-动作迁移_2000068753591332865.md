---
key: 平台全量/Wan2.2 Animate-动作迁移_2000068753591332865.json
name: Wan2.2 Animate-动作迁移_2000068753591332865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate-动作迁移_2000068753591332865.json
hash: b2c070c20be94907
coverage: 0.964286
learned_at: 2026-11-14 01:05:05
nodes: [ImageConcatMulti, PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, JWInteger, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, RHHiddenNodes, JWInteger, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, Text, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate-动作迁移_2000068753591332865.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate-动作迁移_2000068753591332865.json`

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

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ImageConcatMulti`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`JWInteger`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`Text`、`VHS_VideoCombine`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
