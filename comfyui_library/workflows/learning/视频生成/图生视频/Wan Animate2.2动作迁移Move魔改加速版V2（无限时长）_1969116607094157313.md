---
key: 视频生成/图生视频/Wan Animate2.2动作迁移Move魔改加速版V2（无限时长）_1969116607094157313.json
name: Wan Animate2.2动作迁移Move魔改加速版V2（无限时长）_1969116607094157313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969116607094157313.json
hash: b7a53507ba9c6823
coverage: 0.555556
learned_at: 2026-10-15 22:31:47
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, SetNode, DownloadAndLoadSAM2Model, SetNode, SetNode, PixelPerfectResolution, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, Note, SetNode, ImageConcatMulti, GetNode, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, ImageResizeKJv2, SetNode, GetNode, GetNode, WanVideoUni3C_embeds, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, SetNode, LoadImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, Note, WanVideoContextOptions, WanVideoSampler, GetNode, VHS_LoadVideo, GetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, DrawMaskOnImage, GetNode, PointsEditor, SetNode, GetNode, Note, Note, VHS_VideoCombine, VHS_VideoCombine, Note, Note, WanVideoModelLoader, JWInteger, JWInteger, JWInteger, Note, WanVideoTextEncodeCached, CR Prompt Text, VHS_VideoCombine, GetImageSizeAndCount, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2动作迁移Move魔改加速版V2（无限时长）_1969116607094157313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969116607094157313.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（81 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `SetNode`
- `PixelPerfectResolution`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `Note`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `DWPreprocessor`
- `Sam2Segmentation`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_embeds`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoClipVisionEncode`
- `Note`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `DrawMaskOnImage`
- `GetNode`
- `PointsEditor`
- `SetNode`
- `GetNode`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetNode`

## 知识

覆盖率 **56%**（45/81）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`WanVideoEncode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoSampler`、`DrawMaskOnImage`、`PointsEditor`、`WanVideoModelLoader`、`JWInteger`、`WanVideoTextEncodeCached`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
