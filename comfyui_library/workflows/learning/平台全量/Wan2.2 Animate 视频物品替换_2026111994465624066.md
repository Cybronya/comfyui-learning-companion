---
key: 平台全量/Wan2.2 Animate 视频物品替换_2026111994465624066.json
name: Wan2.2 Animate 视频物品替换_2026111994465624066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 视频物品替换_2026111994465624066.json
hash: 745062651086cfa1
coverage: 0.871795
learned_at: 2026-11-14 01:05:04
nodes: [Note, INTConstant, PixelPerfectResolution, WanVideoSetBlockSwap, INTConstant, WanVideoBlockSwap, CLIPVisionLoader, WanVideoTorchCompileSettings, SimpleMath+, INTConstant, Note, ImageResizeKJv2, InspyrenetRembg, PreviewImage, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, Fast Groups Muter (rgthree), PreviewImage, WanVideoClipVisionEncode, WanVideoVAELoader, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, PointsEditor, VHS_LoadVideo, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, LoadImage, VHS_VideoCombine, DrawMaskOnImage, WanVideoDecode, WanVideoTextEncodeCached, VHS_VideoCombine, WanVideoSampler, CR Upscale Image, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 视频物品替换_2026111994465624066.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 视频物品替换_2026111994465624066.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `Note`
- `INTConstant`
- `PixelPerfectResolution`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoTorchCompileSettings`
- `SimpleMath+`
- `INTConstant`
- `Note`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `PreviewImage`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `PointsEditor`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `LoadImage`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `CR Upscale Image`
- `VHS_VideoCombine`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`INTConstant`、`PixelPerfectResolution`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`ImageResizeKJv2`、`InspyrenetRembg`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`PointsEditor`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`LoadImage`、`VHS_VideoCombine`、`DrawMaskOnImage`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`CR Upscale Image`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CR Upscale Image
