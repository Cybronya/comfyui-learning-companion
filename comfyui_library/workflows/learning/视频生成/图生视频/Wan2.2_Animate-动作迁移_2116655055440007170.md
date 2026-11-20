---
key: 视频生成/图生视频/Wan2.2_Animate-动作迁移_2116655055440007170.json
name: Wan2.2_Animate-动作迁移_2116655055440007170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_Animate-动作迁移_2116655055440007170.json
hash: 2bac7298083db988
coverage: 0.964286
learned_at: 2026-11-02 19:18:46
nodes: [ImageConcatMulti, PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, JWInteger, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, RHHiddenNodes, JWInteger, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, Text, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2_Animate-动作迁移_2116655055440007170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2_Animate-动作迁移_2116655055440007170.json`

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
