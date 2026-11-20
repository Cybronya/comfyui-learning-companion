---
key: 平台全量/Wanvideo_SteadyDancer 动作迁移_1996402034372911106.json
name: Wanvideo_SteadyDancer 动作迁移_1996402034372911106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wanvideo_SteadyDancer 动作迁移_1996402034372911106.json
hash: 7ef22148a0402454
coverage: 0.596491
learned_at: 2026-11-14 01:07:13
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, ImageConcatMulti, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, GetImageRangeFromBatch, WanVideoEncode, GetNode, WanVideoSetLoRAs, PrimitiveNode, PrimitiveNode, ImageConcatMulti, CLIPVisionLoader, SetNode, GetNode, WanVideoClipVisionEncode, GetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, WanVideoAddSteadyDancerEmbeds, Note, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, ImageResizeKJv2, GetNode, PreviewImage, WanVideoDecode, WanVideoSamplerSettings, PoseAndFaceDetection, VHS_VideoCombine, WanVideoSamplerFromSettings, SetNode, SetNode, DrawViTPose, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoContextOptions, LoadImage, WanVideoImageToVideoEncode, OnnxDetectionModelLoader, WanVideoScheduler, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, VHS_VideoInfo]
patterns: []
missing: []
---

# 平台全量/Wanvideo_SteadyDancer 动作迁移_1996402034372911106.json

> 来源文件 `comfyui_library/workflows/平台全量/Wanvideo_SteadyDancer 动作迁移_1996402034372911106.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（57 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `GetNode`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `PrimitiveNode`
- `ImageConcatMulti`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoAddSteadyDancerEmbeds`
- `Note`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `GetNode`
- `PreviewImage`
- `WanVideoDecode`
- `WanVideoSamplerSettings` ★核心
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `WanVideoSamplerFromSettings` ★核心
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `OnnxDetectionModelLoader`
- `WanVideoScheduler`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

## 知识

覆盖率 **60%**（34/57）

**有卡**：`WanVideoClipVisionEncode`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSamplerSettings`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`WanVideoSamplerFromSettings`、`DrawViTPose`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`LoadImage`、`WanVideoImageToVideoEncode`、`OnnxDetectionModelLoader`、`WanVideoScheduler`、`VHS_LoadVideo`、`VHS_VideoInfo`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
