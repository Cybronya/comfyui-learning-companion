---
key: 视频生成/图生视频/Wan Animate2.2 替身出演，形神境随_1969559616474542081.json
name: Wan Animate2.2 替身出演，形神境随_1969559616474542081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan Animate2.2 替身出演，形神境随_1969559616474542081.json
hash: 05689eee168e8c33
coverage: 0.538462
learned_at: 2026-10-15 22:31:49
nodes: [GetNode, GetNode, ImageConcatMulti, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, MathExpression|pysssss, MarkdownNote, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, GetNode, DrawMaskOnImage, GetNode, ColorMatch, GetImageSizeAndCount, PreviewImage, PixelPerfectResolution, DWPreprocessor, FaceMaskFromPoseKeypoints, SetNode, SetNode, WanVideoSetBlockSwap, Sam2Segmentation, GrowMask, BlockifyMask, DownloadAndLoadSAM2Model, SetNode, Reroute, VHS_LoadVideo, INTConstant, INTConstant, ImageCropByMaskAndResize, PreviewImage, Text Multiline, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, GetNode, Reroute, GetNode, GetImageRangeFromBatch, SetNode, SetNode, ImageResizeKJv2, WanVideoSampler, SetNode, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelectMulti, CLIPVisionLoader, GetNode, WanVideoTextEncodeCached, WanVideoContextOptions, WanVideoAnimateEmbeds, Note, VHS_VideoCombine, SetNode, SetNode, PointsEditor, LoadImage, easy showAnything, Note, easy showAnything, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2 替身出演，形神境随_1969559616474542081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969559616474542081.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（78 个）：
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `MathExpression|pysssss`
- `MarkdownNote`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `DrawMaskOnImage`
- `GetNode`
- `ColorMatch`
- `GetImageSizeAndCount`
- `PreviewImage`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `Reroute`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `ImageCropByMaskAndResize`
- `PreviewImage`
- `Text Multiline`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `Note`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `PointsEditor`
- `LoadImage`
- `easy showAnything`
- `Note`
- `easy showAnything`
- `SetNode`

## 知识

覆盖率 **54%**（42/78）

**有卡**：`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoCombine`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`DrawMaskOnImage`、`ColorMatch`、`GetImageSizeAndCount`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`WanVideoSetBlockSwap`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DownloadAndLoadSAM2Model`、`VHS_LoadVideo`、`INTConstant`、`ImageCropByMaskAndResize`、`Text Multiline`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`PointsEditor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
