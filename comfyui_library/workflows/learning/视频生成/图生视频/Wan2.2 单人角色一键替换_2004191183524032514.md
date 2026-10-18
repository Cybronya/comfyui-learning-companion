---
key: 视频生成/图生视频/Wan2.2 单人角色一键替换_2004191183524032514.json
name: Wan2.2 单人角色一键替换_2004191183524032514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 单人角色一键替换_2004191183524032514.json
hash: b01a39c9b2f2a2d0
coverage: 0.453608
learned_at: 2026-10-15 22:33:53
nodes: [WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, SetNode, WanVideoVAELoader, SetNode, CLIPVisionLoader, SetNode, LoadWanVideoT5TextEncoder, PrimitiveString, SetNode, GetImageSize, GetNode, WanVideoClipVisionEncode, WanVideoTextEncode, GetNode, DownloadAndLoadSAM2Model, GetNode, GetImageSize, SetNode, SetNode, easy int, SetNode, SetNode, easy seed, PrimitiveStringMultiline, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GetNode, GetImageSize, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, GetNode, GetImageSizeAndCount, GetNode, ImageConcatMulti, PrimitiveString, StringConcatenate, StringConcatenate, PrimitiveString, SetNode, PreviewAny, OnnxDetectionModelLoader, GetNode, PoseAndFaceDetection, DrawViTPose, SetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, PreviewImage, ImageFromBatch, GetNode, GetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), DrawMaskOnImage, BlockifyMask, Sam2Segmentation, GrowMask, GetNode, GetImageSize+, easy clearCacheAll, easy cleanGpuUsed, ResizeMask, LoadImage, VHS_VideoCombine, VHS_LoadVideo, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 单人角色一键替换_2004191183524032514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004191183524032514.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（97 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveString`
- `SetNode`
- `GetImageSize`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `easy int`
- `SetNode`
- `SetNode`
- `easy seed`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `PrimitiveString`
- `StringConcatenate`
- `StringConcatenate`
- `PrimitiveString`
- `SetNode`
- `PreviewAny`
- `OnnxDetectionModelLoader`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `DrawMaskOnImage`
- `BlockifyMask`
- `Sam2Segmentation`
- `GrowMask`
- `GetNode`
- `GetImageSize+`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `ResizeMask`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`

## 知识

覆盖率 **45%**（44/97）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`GetImageSize`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`DownloadAndLoadSAM2Model`、`easy int`、`easy seed`、`VHS_VideoInfo`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`StringConcatenate`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageFromBatch`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`DrawMaskOnImage`、`BlockifyMask`、`Sam2Segmentation`、`GrowMask`、`GetImageSize+`、`easy clearCacheAll`、`easy cleanGpuUsed`、`ResizeMask`、`LoadImage`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
