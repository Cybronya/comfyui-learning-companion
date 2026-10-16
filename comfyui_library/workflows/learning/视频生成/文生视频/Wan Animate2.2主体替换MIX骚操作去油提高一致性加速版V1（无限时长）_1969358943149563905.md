---
key: 视频生成/文生视频/Wan Animate2.2主体替换MIX骚操作去油提高一致性加速版V1（无限时长）_1969358943149563905.json
name: Wan Animate2.2主体替换MIX骚操作去油提高一致性加速版V1（无限时长）_1969358943149563905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1969358943149563905.json
hash: ee717238039e6a61
coverage: 0.555556
learned_at: 2026-10-15 22:43:46
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, SetNode, SetNode, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, ImageResizeKJv2, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, WanVideoTextEncodeCached, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, PointsEditor, Note, WanVideoContextOptions, GetNode, VHS_LoadVideo, WanVideoUni3C_embeds, Note, Note, WanVideoModelLoader, SetNode, PixelPerfectResolution, Note, Note, Note, JWInteger, JWInteger, JWInteger, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, VHS_LoadVideo, SetNode, CR Prompt Text, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan Animate2.2主体替换MIX骚操作去油提高一致性加速版V1（无限时长）_1969358943149563905.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969358943149563905.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（81 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `SetNode`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `DWPreprocessor`
- `Sam2Segmentation`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoClipVisionEncode`
- `PointsEditor`
- `Note`
- `WanVideoContextOptions`
- `GetNode`
- `VHS_LoadVideo`
- `WanVideoUni3C_embeds`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `SetNode`
- `PixelPerfectResolution`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `SetNode`
- `CR Prompt Text`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（45/81）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`PointsEditor`、`WanVideoContextOptions`、`VHS_LoadVideo`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`PixelPerfectResolution`、`JWInteger`、`WanVideoUni3C_ControlnetLoader`、`WanVideoSampler`、`CR Prompt Text`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
