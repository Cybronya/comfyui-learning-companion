---
key: 视频生成/图生视频/Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json
name: Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json
hash: 956dc2eb93ab9e9b
coverage: 0.507246
learned_at: 2026-10-15 22:31:48
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, LoadImage, JWInteger, PixelPerfectResolution, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, DWPreprocessor, ImageCropByMaskAndResize, SetNode, VHS_VideoCombine, SetNode, JWInteger, ImageResizeKJv2, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, WanVideoAnimateEmbeds, easy cleanGpuUsed, VHS_VideoCombine, SetNode, GetNode, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, SetNode, Note, GetNode, DrawMaskOnImage, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, PointsEditor, Note, Note, WanVideoSampler, VHS_LoadVideo, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969219198985662465.json`

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
- `ImageConcatMulti`
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
- `VHS_LoadVideo`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **51%**（35/69）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageConcatMulti`、`LoadImage`、`JWInteger`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`PointsEditor`、`WanVideoSampler`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
