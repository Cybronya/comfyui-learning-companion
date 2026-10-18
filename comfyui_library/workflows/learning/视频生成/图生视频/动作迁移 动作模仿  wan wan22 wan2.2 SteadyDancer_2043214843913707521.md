---
key: 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2043214843913707521.json
name: 动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2043214843913707521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2043214843913707521.json
hash: acaf46019a78b243
coverage: 0.744186
learned_at: 2026-10-15 22:36:31
nodes: [WanVideoTextEncodeCached, WanVideoScheduler, OnnxDetectionModelLoader, VHS_LoadVideo, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, CR Prompt Text, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, WanVideoSamplerFromSettings, Reroute, WanVideoSamplerSettings, WanVideoDecode, GetImageSizeAndCount, ImageResizeKJv2, SetNode, VHS_VideoCombine, SetNode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, LoadImage, ImageConcatMulti, ImageConcatMulti, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, ImageResizeKJv2, GetImageRangeFromBatch]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2043214843913707521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043214843913707521.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `WanVideoTextEncodeCached`
- `WanVideoScheduler`
- `OnnxDetectionModelLoader`
- `VHS_LoadVideo`
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
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `LoadImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoScheduler`、`OnnxDetectionModelLoader`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CR Prompt Text`、`WanVideoContextOptions`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoAddSteadyDancerEmbeds`、`LoadImage`、`ImageConcatMulti`、`PoseDetectionOneToAllAnimation`、`GetImageRangeFromBatch`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
