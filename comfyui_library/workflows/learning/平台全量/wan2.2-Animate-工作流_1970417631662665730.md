---
key: 平台全量/wan2.2-Animate-工作流_1970417631662665730.json
name: wan2.2-Animate-工作流_1970417631662665730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-Animate-工作流_1970417631662665730.json
hash: 655096050458ff67
coverage: 0.857143
learned_at: 2026-11-14 01:19:26
nodes: [INTConstant, INTConstant, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, WanVideoVAELoader, PixelPerfectResolution, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, VHS_VideoCombine, SetNode, SetNode, INTConstant, WanVideoTextEncodeCached, DownloadAndLoadSAM2Model, Sam2Segmentation, Reroute, GrowMask, BlockifyMask, DrawMaskOnImage, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, Reroute, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, LoadImage, VHS_LoadVideo, PointsEditor, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/wan2.2-Animate-工作流_1970417631662665730.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-Animate-工作流_1970417631662665730.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `INTConstant`
- `INTConstant`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Reroute`
- `WanVideoVAELoader`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `Reroute`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `Reroute`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `PointsEditor`
- `WanVideoModelLoader`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`ImageConcatMulti`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`、`PointsEditor`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
