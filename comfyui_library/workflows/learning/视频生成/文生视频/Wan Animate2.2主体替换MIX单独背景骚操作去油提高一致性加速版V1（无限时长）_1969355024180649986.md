---
key: 视频生成/文生视频/Wan Animate2.2主体替换MIX单独背景骚操作去油提高一致性加速版V1（无限时长）_1969355024180649986.json
name: Wan Animate2.2主体替换MIX单独背景骚操作去油提高一致性加速版V1（无限时长）_1969355024180649986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan Animate2.2主体替换MIX单独背景骚操作去油提高一致性加速版V1（无限时长）_1969355024180649986.json
hash: 69712a7f799359ad
coverage: 0.569767
learned_at: 2026-10-15 22:43:46
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, DownloadAndLoadSAM2Model, SetNode, SetNode, PixelPerfectResolution, Reroute, FaceMaskFromPoseKeypoints, SetNode, BlockifyMask, SetNode, ImageConcatMulti, GetNode, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, ImageResizeKJv2, SetNode, GetNode, GetNode, WanVideoUni3C_embeds, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, LoadImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, WanVideoTextEncodeCached, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, Note, WanVideoContextOptions, GetNode, GetNode, PointsEditor, SetNode, GetNode, Note, Note, VHS_VideoCombine, Note, Note, WanVideoModelLoader, Note, LoadImage, GetNode, Note, SetNode, Reroute, GetNode, GrowMask, VHS_LoadVideo, ImageResizeKJv2, SDVN Image Repeat, SetNode, JWInteger, GetNode, DrawMaskOnImage, ImageListToImageBatch, VHS_VideoCombine, SetNode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, JWInteger, JWInteger, VHS_LoadVideo, WanVideoSampler, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan Animate2.2主体替换MIX单独背景骚操作去油提高一致性加速版V1（无限时长）_1969355024180649986.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969355024180649986.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（86 个）：
- `ImageConcatMulti`
- `GetNode`
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
- `BlockifyMask`
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
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_embeds`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoEncode`
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
- `Note`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `PointsEditor`
- `SetNode`
- `GetNode`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `LoadImage`
- `GetNode`
- `Note`
- `SetNode`
- `Reroute`
- `GetNode`
- `GrowMask`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `SDVN Image Repeat`
- `SetNode`
- `JWInteger`
- `GetNode`
- `DrawMaskOnImage`
- `ImageListToImageBatch`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoUni3C_ControlnetLoader`
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`

## 知识

覆盖率 **57%**（49/86）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`BlockifyMask`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`WanVideoEncode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`PointsEditor`、`WanVideoModelLoader`、`GrowMask`、`VHS_LoadVideo`、`SDVN Image Repeat`、`JWInteger`、`DrawMaskOnImage`、`ImageListToImageBatch`、`WanVideoUni3C_ControlnetLoader`、`WanVideoSampler`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
