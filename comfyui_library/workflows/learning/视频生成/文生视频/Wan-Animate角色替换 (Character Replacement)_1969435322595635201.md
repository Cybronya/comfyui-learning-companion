---
key: 视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_1969435322595635201.json
name: Wan-Animate角色替换 (Character Replacement)_1969435322595635201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_1969435322595635201.json
hash: 75b1357b6e816065
coverage: 0.535211
learned_at: 2026-10-10 23:06:27
nodes: [ImageConcatMulti, DWPreprocessor, SetNode, SetNode, Sam2Segmentation, DownloadAndLoadSAM2Model, SetNode, Reroute, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, GrowMask, BlockifyMask, Note, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, ImageConcatMulti, GetImageSizeAndCount, WanVideoContextOptions, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, Note, DrawMaskOnImage, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), easy showAnything, WanVideoDecode, WanVideoVAELoader, ImageResizeKJv2, GetImageSize, VHS_VideoCombine, WanVideoSampler, VHS_LoadVideo, PointsEditor, GetNode, LoadImage, SetNode, SetNode, SetNode, PixelPerfectResolution, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_1969435322595635201.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_1969435322595635201.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（71 个）：
- `ImageConcatMulti`
- `DWPreprocessor`
- `SetNode`
- `SetNode`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `GrowMask`
- `BlockifyMask`
- `Note`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `Note`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `GetImageSize`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `PointsEditor`
- `GetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `PixelPerfectResolution`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **54%**（38/71）

**有卡**：`ImageConcatMulti`、`DWPreprocessor`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`GrowMask`、`BlockifyMask`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`ImageResizeKJv2`、`GetImageSize`、`WanVideoSampler`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`、`PixelPerfectResolution`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
