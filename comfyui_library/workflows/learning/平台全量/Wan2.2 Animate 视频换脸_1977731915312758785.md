---
key: 平台全量/Wan2.2 Animate 视频换脸_1977731915312758785.json
name: Wan2.2 Animate 视频换脸_1977731915312758785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 视频换脸_1977731915312758785.json
hash: 81c372adae4b74cd
coverage: 0.914286
learned_at: 2026-11-14 01:05:03
nodes: [WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJv2, DWPreprocessor, FaceMaskFromPoseKeypoints, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, INTConstant, PixelPerfectResolution, WanVideoTextEncodeCached, WanVideoSetBlockSwap, INTConstant, INTConstant, Note, SimpleMath+, VHS_LoadVideo, WanVideoBlockSwap, WanVideoModelLoader, LoadImage, Fast Groups Muter (rgthree), PointsEditor, WanVideoAnimateEmbeds, Note, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ImageCropByMaskAndResize, DrawMaskOnImage, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 视频换脸_1977731915312758785.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 视频换脸_1977731915312758785.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `INTConstant`
- `PixelPerfectResolution`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `INTConstant`
- `Note`
- `SimpleMath+`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `PointsEditor`
- `WanVideoAnimateEmbeds`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageCropByMaskAndResize`
- `DrawMaskOnImage`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`INTConstant`、`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`SimpleMath+`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadImage`、`PointsEditor`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`ImageCropByMaskAndResize`、`DrawMaskOnImage`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader
