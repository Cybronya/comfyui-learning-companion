---
key: 平台全量/Wan2.2 animate 视频人物、背景更换_1977377943250968578.json
name: Wan2.2 animate 视频人物、背景更换_1977377943250968578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 animate 视频人物、背景更换_1977377943250968578.json
hash: 2bba13be08e28167
coverage: 0.916667
learned_at: 2026-11-14 01:05:38
nodes: [Note, WanVideoTorchCompileSettings, WanVideoVAELoader, CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, PixelPerfectResolution, WanVideoClipVisionEncode, WanVideoSampler, WanVideoAnimateEmbeds, ImageResizeKJv2, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, Fast Groups Muter (rgthree), INTConstant, VHS_LoadVideo, SimpleMath+, LoadImage, VHS_VideoCombine, VHS_LoadVideo, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, WanVideoDecode, PointsEditor, INTConstant, INTConstant, VHS_VideoCombine, VHS_VideoCombine, DrawMaskOnImage, ImageCropByMaskAndResize, Note, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 平台全量/Wan2.2 animate 视频人物、背景更换_1977377943250968578.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 animate 视频人物、背景更换_1977377943250968578.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `Fast Groups Muter (rgthree)`
- `INTConstant`
- `VHS_LoadVideo`
- `SimpleMath+`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoDecode`
- `PointsEditor`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `ImageCropByMaskAndResize`
- `Note`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`CLIPVisionLoader`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`INTConstant`、`VHS_LoadVideo`、`SimpleMath+`、`LoadImage`、`VHS_VideoCombine`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`WanVideoDecode`、`PointsEditor`、`DrawMaskOnImage`、`ImageCropByMaskAndResize`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader
