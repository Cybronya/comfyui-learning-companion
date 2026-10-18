---
key: 视频生成/图生视频/wanvideo_SteadyDancer_1995382364060758018.json
name: wanvideo_SteadyDancer_1995382364060758018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wanvideo_SteadyDancer_1995382364060758018.json
hash: a10fdad8cada5227
coverage: 0.571429
learned_at: 2026-10-15 22:33:22
nodes: [WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, GetNode, GetNode, GetNode, SetNode, GetImageSizeAndCount, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoEncode, GetNode, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, VHS_LoadVideo, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, ImageResizeKJv2, SetNode, GetImageRangeFromBatch, WanVideoEncode, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, WanVideoTextEncodeCached, WanVideoSamplerFromSettings, WanVideoSamplerSettings, PrimitiveNode, PrimitiveNode, WanVideoScheduler, WanVideoContextOptions]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo_SteadyDancer_1995382364060758018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995382364060758018.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `VHS_LoadVideo`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `ImageResizeKJv2`
- `SetNode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoTextEncodeCached`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoSamplerSettings` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoContextOptions`

## 知识

覆盖率 **57%**（32/56）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoTextEncodeCached`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoScheduler`、`WanVideoContextOptions`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
