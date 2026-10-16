---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2053496869547982849.json
name: 动作迁移 动作模仿  wan2.2_2053496869547982849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2053496869547982849.json
hash: ad93baa1a26fd8e3
coverage: 0.744186
learned_at: 2026-10-15 22:37:39
nodes: [GetImageSizeAndCount, OnnxDetectionModelLoader, ImageResizeKJv2, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, SetNode, VHS_VideoCombine, CR Prompt Text, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, WanVideoVAELoader, SetNode, CLIPVisionLoader, SetNode, Reroute, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageRangeFromBatch, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, SetNode, WanVideoEncode, WanVideoAddSteadyDancerEmbeds, WanVideoSamplerSettings, PrimitiveNode, GetNode, GetNode, WanVideoScheduler, ImageConcatMulti, ImageConcatMulti, WanVideoSamplerFromSettings, WanVideoDecode, WanVideoModelLoader, VHS_VideoCombine, VHS_LoadVideo, LoadImage, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetBlockSwap, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2053496869547982849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053496869547982849.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `SetNode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `Reroute`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `WanVideoEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoSamplerSettings` ★核心
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `WanVideoScheduler`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`VHS_VideoCombine`、`CR Prompt Text`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageRangeFromBatch`、`WanVideoImageToVideoEncode`、`WanVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`WanVideoScheduler`、`ImageConcatMulti`、`WanVideoSamplerFromSettings`、`WanVideoDecode`、`WanVideoModelLoader`、`VHS_LoadVideo`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
