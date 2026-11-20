---
key: 平台全量/Wan2.2 Animate 多人视频人物精准替换_1977741311920984065.json
name: Wan2.2 Animate 多人视频人物精准替换_1977741311920984065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 多人视频人物精准替换_1977741311920984065.json
hash: 3cf1f5e2a54dac8c
coverage: 0.888889
learned_at: 2026-11-14 01:04:59
nodes: [WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoDecode, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJv2, DWPreprocessor, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, INTConstant, PixelPerfectResolution, WanVideoBlockSwap, WanVideoSetBlockSwap, SimpleMath+, INTConstant, INTConstant, Note, Note, VHS_LoadVideo, LoadImage, PointsEditor, Fast Groups Muter (rgthree), VHS_VideoCombine, VHS_VideoCombine, FaceMaskFromPoseKeypoints, Note, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoSampler, ImageCropByMaskAndResize, VHS_VideoCombine, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 多人视频人物精准替换_1977741311920984065.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 多人视频人物精准替换_1977741311920984065.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `INTConstant`
- `PixelPerfectResolution`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `PointsEditor`
- `Fast Groups Muter (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FaceMaskFromPoseKeypoints`
- `Note`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`DWPreprocessor`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`INTConstant`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`SimpleMath+`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`、`VHS_VideoCombine`、`FaceMaskFromPoseKeypoints`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`ImageCropByMaskAndResize`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader
