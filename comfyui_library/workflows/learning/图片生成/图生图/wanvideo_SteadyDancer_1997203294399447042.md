---
key: 图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json
name: wanvideo_SteadyDancer_1997203294399447042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json
hash: ef926488ffab457c
coverage: 0.58209
learned_at: 2026-10-23 11:46:15
nodes: [SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoBlockSwap, CLIPVisionLoader, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, ImageResizeKJv2, SetNode, GetImageRangeFromBatch, WanVideoEncode, WanVideoSamplerFromSettings, WanVideoSamplerSettings, PrimitiveNode, PrimitiveNode, WanVideoScheduler, WanVideoContextOptions, GetNode, ImageResizeKJv2, WanVideoLoraSelect, GetImageSizeAndCount, WanVideoTextEncodeCached, WanVideoAddSteadyDancerEmbeds, PreviewImage, WanVideoImageToVideoEncode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, ImageConcatMulti, ImageConcatMulti, WanVideoDecode, Reroute, Int, Int, easy mathInt, easy showAnything, VHS_LoadVideo, ImageConcatMulti, Int, VHS_VideoCombine, LoadImage, VHS_VideoCombine, WanVideoClipVisionEncode, VHS_VideoCombine, Int, Reroute, Int]
patterns: []
missing: []
---

# 图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（67 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `ImageResizeKJv2`
- `SetNode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoSamplerSettings` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoContextOptions`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeCached`
- `WanVideoAddSteadyDancerEmbeds`
- `PreviewImage`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoDecode`
- `Reroute`
- `Int`
- `Int`
- `easy mathInt`
- `easy showAnything`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `Int`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Int`
- `Reroute`
- `Int`

## 知识

覆盖率 **58%**（39/67）

**有卡**：`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageResizeKJv2`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoScheduler`、`WanVideoContextOptions`、`WanVideoLoraSelect`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`ImageConcatMulti`、`WanVideoDecode`、`Int`、`easy mathInt`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
