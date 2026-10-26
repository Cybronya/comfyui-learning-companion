---
key: 数字人/数字人/Wan Animate2.2 主体替换2_1970810037335695361.json
name: Wan Animate2.2 主体替换2_1970810037335695361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan Animate2.2 主体替换2_1970810037335695361.json
hash: 8b274614a8a2e22c
coverage: 0.488889
learned_at: 2026-10-26 01:57:42
nodes: [DownloadAndLoadSAM2Model, GetNode, Sam2Segmentation, GetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, JWInteger, SetNode, JWInteger, SetNode, JWInteger, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, SetNode, FaceMaskFromPoseKeypoints, PixelPerfectResolution, GetNode, SetNode, ImageCropByMaskAndResize, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, SetNode, SetNode, BlockifyMask, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, WanVideoAnimateEmbeds, PreviewImage, SetNode, ImageResizeKJv2, GetNode, VHS_LoadVideo, CR Prompt Text, VHS_VideoCombine, Manual XY Entry Info, VHS_LoadVideo, PointsEditor, PreviewImage, ImageFromBatch+, GetNode, GetNode, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, PreviewImage, LoadImage, VHS_VideoCombine, WanVideoSampler]
patterns: []
missing: []
---

# 数字人/数字人/Wan Animate2.2 主体替换2_1970810037335695361.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan Animate2.2 主体替换2_1970810037335695361.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（90 个）：
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `Sam2Segmentation`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_LoadVideo`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `Manual XY Entry Info`
- `VHS_LoadVideo`
- `PointsEditor`
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `PreviewImage`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **49%**（44/90）

**有卡**：`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`DrawMaskOnImage`、`JWInteger`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`BlockifyMask`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`CR Prompt Text`、`VHS_VideoCombine`、`Manual XY Entry Info`、`PointsEditor`、`ImageFromBatch+`、`WanVideoDecode`、`ImageConcatMulti`、`LoadImage`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
