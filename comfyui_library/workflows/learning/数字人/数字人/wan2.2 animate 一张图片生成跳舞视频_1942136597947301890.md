---
key: 数字人/数字人/wan2.2 animate 一张图片生成跳舞视频_1942136597947301890.json
name: wan2.2 animate 一张图片生成跳舞视频_1942136597947301890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2 animate 一张图片生成跳舞视频_1942136597947301890.json
hash: 657a146eb6ed92a7
coverage: 0.529412
learned_at: 2026-10-26 01:59:25
nodes: [GetNode, GetNode, GetNode, Reroute, GetNode, GetNode, WanVideoTorchCompileSettings, ImageConcatMulti, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, PixelPerfectResolution, FaceMaskFromPoseKeypoints, Note, WanVideoBlockSwap, DWPreprocessor, WanVideoAnimateEmbeds, GetNode, WanVideoModelLoader, GetNode, GetNode, GetNode, GetNode, WanVideoVAELoader, SetNode, ImageResizeKJv2, WanVideoTextEncodeCached, GetNode, SetNode, SetNode, SetNode, PreviewImage, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, SetNode, Note, GetNode, SetNode, DrawMaskOnImage, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, SetNode, ImageConcatMulti, GetImageSizeAndCount, SetNode, ImageCropByMaskAndResize, WanVideoSampler, WanVideoDecode, GetNode, PointsEditor, WanVideoLoraSelectMulti, WanVideoClipVisionEncode, INTConstant, INTConstant, SetNode, VHS_VideoCombine, LoadImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, GetNode, CLIPVisionLoader, GetNode]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2 animate 一张图片生成跳舞视频_1942136597947301890.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2 animate 一张图片生成跳舞视频_1942136597947301890.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（68 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `Note`
- `WanVideoBlockSwap`
- `DWPreprocessor`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageCropByMaskAndResize`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `PointsEditor`
- `WanVideoLoraSelectMulti`
- `WanVideoClipVisionEncode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`

## 知识

覆盖率 **53%**（36/68）

**有卡**：`WanVideoTorchCompileSettings`、`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`WanVideoBlockSwap`、`DWPreprocessor`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`WanVideoDecode`、`PointsEditor`、`WanVideoLoraSelectMulti`、`WanVideoClipVisionEncode`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
