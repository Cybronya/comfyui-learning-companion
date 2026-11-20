---
key: 平台全量/wan2.2动作迁移、动作模仿_1984949634684633090.json
name: wan2.2动作迁移、动作模仿_1984949634684633090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2动作迁移、动作模仿_1984949634684633090.json
hash: fe20c4d45a0e2fcf
coverage: 0.966667
learned_at: 2026-11-14 01:19:45
nodes: [CLIPVisionLoader, MarkdownNote, JWInteger, Text, VHS_VideoCombine, JWInteger, Switch any [Crystools], LoadImage, ImageResizeKJv2, WanVideoClipVisionEncode, PixelPerfectResolution, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoBlockSwap, RHHiddenNodes, WanVideoSampler, VHS_VideoCombine, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, WanVideoTextEncodeCached, VHS_VideoInfoSource, WanVideoSetLoRAs, VHS_LoadVideo, WanVideoDecode]
patterns: []
missing: []
---

# 平台全量/wan2.2动作迁移、动作模仿_1984949634684633090.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2动作迁移、动作模仿_1984949634684633090.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `CLIPVisionLoader`
- `MarkdownNote`
- `JWInteger`
- `Text`
- `VHS_VideoCombine`
- `JWInteger`
- `Switch any [Crystools]`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `RHHiddenNodes`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoTextEncodeCached`
- `VHS_VideoInfoSource`
- `WanVideoSetLoRAs`
- `VHS_LoadVideo`
- `WanVideoDecode`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`CLIPVisionLoader`、`JWInteger`、`Text`、`VHS_VideoCombine`、`Switch any [Crystools]`、`LoadImage`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`RHHiddenNodes`、`WanVideoSampler`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoTextEncodeCached`、`VHS_VideoInfoSource`、`WanVideoSetLoRAs`、`VHS_LoadVideo`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
