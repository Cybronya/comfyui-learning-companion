---
key: 视频生成/文生视频/Wan Animate2.2非人类主体混合mix魔改加速版V3（无限时长）_1969373357202436097.json
name: Wan Animate2.2非人类主体混合mix魔改加速版V3（无限时长）_1969373357202436097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1969373357202436097.json
hash: d10b2cd7d33dff95
coverage: 0.560976
learned_at: 2026-10-15 22:43:46
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, DownloadAndLoadSAM2Model, SetNode, SetNode, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, PointsEditor, Note, WanVideoContextOptions, WanVideoSampler, VHS_LoadVideo, WanVideoUni3C_embeds, Note, Note, WanVideoModelLoader, VHS_VideoCombine, SetNode, JWInteger, JWInteger, PixelPerfectResolution, Note, Note, WanVideoTextEncodeCached, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, CR Prompt Text, JWInteger, Note, EmptyImage, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan Animate2.2非人类主体混合mix魔改加速版V3（无限时长）_1969373357202436097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969373357202436097.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（82 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
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
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoClipVisionEncode`
- `PointsEditor`
- `Note`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `WanVideoUni3C_embeds`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `PixelPerfectResolution`
- `Note`
- `Note`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `Note`
- `EmptyImage`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`PointsEditor`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`JWInteger`、`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`LoadImage`、`CR Prompt Text`、`EmptyImage`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
