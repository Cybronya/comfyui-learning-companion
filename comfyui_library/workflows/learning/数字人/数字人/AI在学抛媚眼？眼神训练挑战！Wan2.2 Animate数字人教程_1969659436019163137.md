---
key: 数字人/数字人/AI在学抛媚眼？眼神训练挑战！Wan2.2 Animate数字人教程_1969659436019163137.json
name: AI在学抛媚眼？眼神训练挑战！Wan2.2 Animate数字人教程_1969659436019163137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI在学抛媚眼？眼神训练挑战！Wan2.2 Animate数字人教程_1969659436019163137.json
hash: cb3a7e40654d8783
coverage: 0.568627
learned_at: 2026-10-26 01:53:40
nodes: [SetNode, GetNode, GetNode, SetNode, GetNode, PixelPerfectResolution, SetNode, Reroute, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, INTConstant, INTConstant, WanVideoVAELoader, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageResizeKJv2, PreviewImage, WanVideoDecode, Bjornulf_ShowInt, GetNode, WanVideoSampler, DWPreprocessor, LoadImage, WanVideoAnimateEmbeds, VHS_LoadVideo, SetNode, SetNode, SetNode, Bjornulf_ShowInt, Note, WanVideoTextEncodeCached, GetImageSizeAndCount, VHS_VideoCombine, GetNode, VHS_VideoCombine, GetImageRangeFromBatch, Label (rgthree)]
patterns: []
missing: []
---

# 数字人/数字人/AI在学抛媚眼？眼神训练挑战！Wan2.2 Animate数字人教程_1969659436019163137.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI在学抛媚眼？眼神训练挑战！Wan2.2 Animate数字人教程_1969659436019163137.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PixelPerfectResolution`
- `SetNode`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoDecode`
- `Bjornulf_ShowInt`
- `GetNode`
- `WanVideoSampler` ★核心
- `DWPreprocessor`
- `LoadImage`
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `Bjornulf_ShowInt`
- `Note`
- `WanVideoTextEncodeCached`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `Label (rgthree)`

## 知识

覆盖率 **57%**（29/51）

**有卡**：`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`WanVideoDecode`、`Bjornulf_ShowInt`、`WanVideoSampler`、`DWPreprocessor`、`LoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
