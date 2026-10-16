---
key: 视频生成/图生视频/Wan Animate2.2主体混合mix魔改加速版V2（无限时长）_1969110399318716418.json
name: Wan Animate2.2主体混合mix魔改加速版V2（无限时长）_1969110399318716418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969110399318716418.json
hash: 3293f87e695cee9d
coverage: 0.556962
learned_at: 2026-10-15 22:31:47
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, DownloadAndLoadSAM2Model, SetNode, SetNode, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, PointsEditor, Note, WanVideoContextOptions, WanVideoSampler, GetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoUni3C_embeds, Note, Note, WanVideoModelLoader, VHS_VideoCombine, SetNode, JWInteger, JWInteger, PixelPerfectResolution, Note, Note, WanVideoTextEncodeCached, CR Prompt Text, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2主体混合mix魔改加速版V2（无限时长）_1969110399318716418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969110399318716418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（79 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoClipVisionEncode`
- `PointsEditor`
- `Note`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `CR Prompt Text`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（44/79）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`PointsEditor`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`JWInteger`、`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
