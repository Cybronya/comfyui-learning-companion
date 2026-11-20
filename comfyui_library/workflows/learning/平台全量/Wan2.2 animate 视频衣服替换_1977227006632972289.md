---
key: 平台全量/Wan2.2 animate 视频衣服替换_1977227006632972289.json
name: Wan2.2 animate 视频衣服替换_1977227006632972289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 animate 视频衣服替换_1977227006632972289.json
hash: 2a56488bd986fe3a
coverage: 0.914286
learned_at: 2026-11-14 01:05:38
nodes: [Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJv2, DWPreprocessor, FaceMaskFromPoseKeypoints, Sam2Segmentation, GrowMask, BlockifyMask, WanVideoAnimateEmbeds, INTConstant, PixelPerfectResolution, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoSetBlockSwap, SimpleMath+, Fast Groups Muter (rgthree), INTConstant, INTConstant, DownloadAndLoadSAM2Model, WanVideoDecode, VHS_VideoCombine, LoadImage, PointsEditor, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, DrawMaskOnImage, ImageCropByMaskAndResize, Note, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 平台全量/Wan2.2 animate 视频衣服替换_1977227006632972289.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 animate 视频衣服替换_1977227006632972289.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoAnimateEmbeds`
- `INTConstant`
- `PixelPerfectResolution`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `Fast Groups Muter (rgthree)`
- `INTConstant`
- `INTConstant`
- `DownloadAndLoadSAM2Model`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadImage`
- `PointsEditor`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `ImageCropByMaskAndResize`
- `Note`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`WanVideoAnimateEmbeds`、`INTConstant`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`SimpleMath+`、`DownloadAndLoadSAM2Model`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadImage`、`PointsEditor`、`VHS_LoadVideo`、`DrawMaskOnImage`、`ImageCropByMaskAndResize`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader
