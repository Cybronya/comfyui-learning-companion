---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json
name: Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json
hash: 538d4a338f0a6e4e
coverage: 0.519231
learned_at: 2026-10-15 22:31:48
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, Reroute, SetNode, ImageConcatMulti, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GetNode, GetNode, WanVideoBlockSwap, CLIPVisionLoader, WanVideoModelLoader, SetNode, GetNode, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, SetNode, VHS_VideoCombine, LoadImage, ImageResizeKJv2, SetNode, SetNode, SetNode, JWInteger, JWInteger, SetNode, VHS_LoadVideo, WanVideoSampler, SetNode, VHS_VideoCombine, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, GetImageSizeAndCount, GetNode, GetNode, WanVideoDecode, WanVideoVAELoader, PrimitiveStringMultiline, SetNode, ImageCropByMaskAndResize, PixelPerfectResolution, FaceMaskFromPoseKeypoints, DWPreprocessor, WanVideoTextEncodeCached, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969252099450150913.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（52 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `SetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `PrimitiveStringMultiline`
- `SetNode`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `WanVideoTextEncodeCached`
- `MarkdownNote`

## 知识

覆盖率 **52%**（27/52）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`JWInteger`、`VHS_LoadVideo`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
