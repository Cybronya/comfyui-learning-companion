---
key: 视频生成/图生视频/SteadyDancer视频动作迁移【1.0】_1995877090840961026.json
name: SteadyDancer视频动作迁移【1.0】_1995877090840961026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1995877090840961026.json
hash: 4665a84745c9cda4
coverage: 0.745455
learned_at: 2026-10-15 22:33:24
nodes: [GetNode, GetNode, GetNode, WanVideoAddSteadyDancerEmbeds, GetNode, WanVideoSetBlockSwap, GetNode, SetNode, WanVideoClipVisionEncode, DrawViTPose, ImageResizeKJv2, SetNode, GetNode, WanVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, PoseAndFaceDetection, WanVideoSamplerFromSettings, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, ImageResizeKJv2, GetNode, WanVideoImageToVideoEncode, SimpleMath+, LoadImage, easy positive, VHS_VideoInfo, WanVideoTextEncodeCached, SetNode, WanVideoContextOptions, WanVideoVAELoader, WanVideoSetLoRAs, SetNode, SetNode, VHS_VideoCombine, WanVideoClipVisionEncode, GetImageRangeFromBatch, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSamplerSettings, ImpactInt, WanVideoBlockSwap, VHS_LoadVideo, easy int, LoadImage, easy int, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/SteadyDancer视频动作迁移【1.0】_1995877090840961026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995877090840961026.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（55 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddSteadyDancerEmbeds`
- `GetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `DrawViTPose`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `WanVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `PoseAndFaceDetection`
- `WanVideoSamplerFromSettings` ★核心
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `LoadImage`
- `easy positive`
- `VHS_VideoInfo`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoContextOptions`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSamplerSettings` ★核心
- `ImpactInt`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `easy int`
- `LoadImage`
- `easy int`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHHiddenNodes`

## 知识

覆盖率 **75%**（41/55）

**有卡**：`WanVideoAddSteadyDancerEmbeds`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`WanVideoSamplerFromSettings`、`ImageConcatMulti`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`LoadImage`、`easy positive`、`VHS_VideoInfo`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSamplerSettings`、`ImpactInt`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`easy int`、`RHHiddenNodes`、`WanVideoDecode`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
