---
key: 数字人/数字人/Wan Animate2.2换脸V1_2000858355855917057.json
name: Wan Animate2.2换脸V1_2000858355855917057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan Animate2.2换脸V1_2000858355855917057.json
hash: f5a14ca869a0c8d4
coverage: 0.507246
learned_at: 2026-10-26 01:57:43
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, LoadImage, JWInteger, PixelPerfectResolution, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, DWPreprocessor, ImageCropByMaskAndResize, SetNode, VHS_VideoCombine, SetNode, JWInteger, ImageResizeKJv2, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, easy cleanGpuUsed, VHS_VideoCombine, SetNode, GetNode, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, SetNode, Note, GetNode, DrawMaskOnImage, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, PointsEditor, Note, Note, WanVideoSampler, WanVideoTextEncodeCached, ImageConcatMulti, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/Wan Animate2.2换脸V1_2000858355855917057.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan Animate2.2换脸V1_2000858355855917057.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（69 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `LoadImage`
- `JWInteger`
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `ImageCropByMaskAndResize`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `JWInteger`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `Note`
- `GetNode`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PointsEditor`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `VHS_LoadVideo`

## 知识

覆盖率 **51%**（35/69）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageConcatMulti`、`LoadImage`、`JWInteger`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`PointsEditor`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
