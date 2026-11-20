---
key: 平台全量/Wan2.2 Animate 视频物品替换_1978055441882173442.json
name: Wan2.2 Animate 视频物品替换_1978055441882173442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 视频物品替换_1978055441882173442.json
hash: d66579e0a39474a4
coverage: 0.891892
learned_at: 2026-11-14 01:05:04
nodes: [Note, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoVAELoader, DWPreprocessor, FaceMaskFromPoseKeypoints, Sam2Segmentation, GrowMask, BlockifyMask, INTConstant, PixelPerfectResolution, WanVideoSetBlockSwap, SimpleMath+, WanVideoLoraSelectMulti, Fast Groups Muter (rgthree), INTConstant, INTConstant, DownloadAndLoadSAM2Model, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, DrawMaskOnImage, ImageCropByMaskAndResize, Note, VHS_LoadVideo, PointsEditor, InspyrenetRembg, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, VHS_VideoCombine, PreviewImage, WanVideoClipVisionEncode, WanVideoBlockSwap, WanVideoModelLoader, ImageResizeKJv2, CLIPVisionLoader, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 视频物品替换_1978055441882173442.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 视频物品替换_1978055441882173442.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `INTConstant`
- `PixelPerfectResolution`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `WanVideoLoraSelectMulti`
- `Fast Groups Muter (rgthree)`
- `INTConstant`
- `INTConstant`
- `DownloadAndLoadSAM2Model`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `ImageCropByMaskAndResize`
- `Note`
- `VHS_LoadVideo`
- `PointsEditor`
- `InspyrenetRembg`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `LoadImage`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoVAELoader`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`INTConstant`、`PixelPerfectResolution`、`WanVideoSetBlockSwap`、`SimpleMath+`、`WanVideoLoraSelectMulti`、`DownloadAndLoadSAM2Model`、`WanVideoDecode`、`VHS_VideoCombine`、`DrawMaskOnImage`、`ImageCropByMaskAndResize`、`VHS_LoadVideo`、`PointsEditor`、`InspyrenetRembg`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`ImageResizeKJv2`、`CLIPVisionLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader
