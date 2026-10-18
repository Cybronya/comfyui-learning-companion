---
key: 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2042065496551464962.json
name: 动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2042065496551464962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2042065496551464962.json
hash: 7d811e855f0d1cdd
coverage: 0.744186
learned_at: 2026-10-15 22:36:24
nodes: [WanVideoTextEncodeCached, WanVideoScheduler, OnnxDetectionModelLoader, VHS_LoadVideo, LoadImage, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, CR Prompt Text, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, WanVideoSamplerFromSettings, Reroute, WanVideoSamplerSettings, WanVideoDecode, GetImageSizeAndCount, PoseDetectionOneToAllAnimation, PreviewImage, PreviewImage, ImageResizeKJv2, SetNode, VHS_VideoCombine, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, SetNode, WanVideoEncode, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, GetImageRangeFromBatch, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2042065496551464962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042065496551464962.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `WanVideoTextEncodeCached`
- `WanVideoScheduler`
- `OnnxDetectionModelLoader`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `CR Prompt Text`
- `WanVideoContextOptions`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoSamplerFromSettings` ★核心
- `Reroute`
- `WanVideoSamplerSettings` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoScheduler`、`OnnxDetectionModelLoader`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CR Prompt Text`、`WanVideoContextOptions`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`PoseDetectionOneToAllAnimation`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoAddSteadyDancerEmbeds`、`GetImageRangeFromBatch`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
