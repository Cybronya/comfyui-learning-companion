---
key: 视频生成/图生视频/SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2087040327587815426.json
name: SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2087040327587815426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2087040327587815426.json
hash: 29c2921b8e2c928f
coverage: 0.794872
learned_at: 2026-10-16 21:07:28
nodes: [WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, PoseDetectionOneToAllAnimation, PreviewImage, PreviewImage, WanVideoClipVisionEncode, OnnxDetectionModelLoader, WanVideoSamplerFromSettings, WanVideoDecode, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoContextOptions, WanVideoScheduler, WanVideoSamplerSettings, Reroute, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, GetImageSizeAndCount, SetNode, SetNode, ImageResizeKJv2, WanVideoEncode, WanVideoClipVisionEncode, SetNode, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoImageToVideoEncode, ImageConcatMulti, VHS_LoadVideo, VHS_VideoCombine, GetImageRangeFromBatch, ImageConcatMulti, GetNode, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2087040327587815426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2087040327587815426.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoContextOptions`
- `WanVideoScheduler`
- `WanVideoSamplerSettings` ★核心
- `Reroute`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoEncode`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`

## 知识

覆盖率 **79%**（31/39）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`PoseDetectionOneToAllAnimation`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoSamplerFromSettings`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoContextOptions`、`WanVideoScheduler`、`WanVideoSamplerSettings`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoEncode`、`ImageConcatMulti`、`VHS_LoadVideo`、`GetImageRangeFromBatch`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
