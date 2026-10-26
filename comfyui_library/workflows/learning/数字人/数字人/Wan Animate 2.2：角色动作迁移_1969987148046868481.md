---
key: 数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json
name: Wan Animate 2.2：角色动作迁移_1969987148046868481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json
hash: 5c3c798adc649c58
coverage: 0.964286
learned_at: 2026-10-26 01:57:41
nodes: [PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, JWInteger, WanVideoBlockSwap, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoModelLoader, JWInteger, Text, VHS_LoadVideo, VHS_VideoCombine, LoadImage, MarkdownNote, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJv2, RHHiddenNodes, WanVideoSampler, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, ImageConcatMulti, WanVideoTextEncodeCached, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `PixelPerfectResolution`
- `DWPreprocessor`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `JWInteger`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `MarkdownNote`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `RHHiddenNodes`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageConcatMulti`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`JWInteger`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`Text`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadImage`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`RHHiddenNodes`、`WanVideoSampler`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
