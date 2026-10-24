---
key: 图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json
name: Wan2.2 animate 视频人物替换_1976938900721672193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json
hash: dacf7ab772f2ecb3
coverage: 0.914286
learned_at: 2026-10-23 11:28:00
nodes: [WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJv2, DWPreprocessor, FaceMaskFromPoseKeypoints, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, VHS_VideoCombine, DrawMaskOnImage, VHS_VideoCombine, LoadImage, WanVideoAnimateEmbeds, INTConstant, PixelPerfectResolution, ImageCropByMaskAndResize, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoSetBlockSwap, VHS_VideoCombine, VHS_LoadVideo, SimpleMath+, PointsEditor, Fast Groups Muter (rgthree), INTConstant, INTConstant, Note, Note, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
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
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoAnimateEmbeds`
- `INTConstant`
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SimpleMath+`
- `PointsEditor`
- `Fast Groups Muter (rgthree)`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`VHS_VideoCombine`、`DrawMaskOnImage`、`LoadImage`、`WanVideoAnimateEmbeds`、`INTConstant`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`VHS_LoadVideo`、`SimpleMath+`、`PointsEditor`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelectMulti、CLIPVisionLoader
