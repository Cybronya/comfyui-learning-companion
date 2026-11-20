---
key: 平台全量/Wan2.2表情+动作迁移、模仿V5优化版_1998815533208363010.json
name: Wan2.2表情+动作迁移、模仿V5优化版_1998815533208363010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2表情+动作迁移、模仿V5优化版_1998815533208363010.json
hash: ffd0f964a5915405
coverage: 0.491071
learned_at: 2026-11-14 01:06:23
nodes: [SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, SetNode, easy seed, GetNode, SetNode, PrimitiveString, SetNode, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), GetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, VHS_VideoInfo, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, SetNode, LoadWanVideoT5TextEncoder, MarkdownNote, GetNode, ImageFromBatch, PreviewImage, DownloadAndLoadSAM2Model, GetNode, GetImageSize+, Mute / Bypass Repeater (rgthree), DrawMaskOnImage, StringConcatenate, GetNode, StringConcatenate, PrimitiveString, PrimitiveString, PreviewAny, SetNode, Sam2Segmentation, Mute / Bypass Relay (rgthree), GetNode, BlockifyMask, GrowMask, ResizeMask, easy cleanGpuUsed, easy clearCacheAll, SetNode, SetNode, GetNode, GetNode, GetImageSize, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, SetNode, SetNode, SetNode, GetImageSize, GetNode, ImageResizeKJv2, GetNode, SetNode, ImageConcatMulti, PreviewImage, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetImageSize, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoTextEncode, WanVideoAnimateEmbeds, easy int, WanVideoModelLoader, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.2表情+动作迁移、模仿V5优化版_1998815533208363010.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2表情+动作迁移、模仿V5优化版_1998815533208363010.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（112 个）：
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy seed`
- `GetNode`
- `SetNode`
- `PrimitiveString`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `MarkdownNote`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `GetImageSize+`
- `Mute / Bypass Repeater (rgthree)`
- `DrawMaskOnImage`
- `StringConcatenate`
- `GetNode`
- `StringConcatenate`
- `PrimitiveString`
- `PrimitiveString`
- `PreviewAny`
- `SetNode`
- `Sam2Segmentation`
- `Mute / Bypass Relay (rgthree)`
- `GetNode`
- `BlockifyMask`
- `GrowMask`
- `ResizeMask`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoAnimateEmbeds`
- `easy int`
- `WanVideoModelLoader`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **49%**（55/112）

**有卡**：`ImageResizeKJv2`、`easy seed`、`Label (rgthree)`、`VHS_VideoCombine`、`VHS_VideoInfo`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`ImageFromBatch`、`DownloadAndLoadSAM2Model`、`GetImageSize+`、`Mute / Bypass Repeater (rgthree)`、`DrawMaskOnImage`、`StringConcatenate`、`Sam2Segmentation`、`Mute / Bypass Relay (rgthree)`、`BlockifyMask`、`GrowMask`、`ResizeMask`、`easy cleanGpuUsed`、`easy clearCacheAll`、`GetImageSize`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoAnimateEmbeds`、`easy int`、`WanVideoModelLoader`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
