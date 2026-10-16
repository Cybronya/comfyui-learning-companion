---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047160236468867073.json
name: 动作迁移 动作模仿  wan2.2_2047160236468867073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047160236468867073.json
hash: 02cbe0aa183d7dfe
coverage: 0.744186
learned_at: 2026-10-15 22:37:03
nodes: [WanVideoTextEncodeCached, WanVideoScheduler, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, CR Prompt Text, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, WanVideoSamplerFromSettings, Reroute, WanVideoSamplerSettings, GetImageSizeAndCount, PoseDetectionOneToAllAnimation, PreviewImage, PreviewImage, ImageResizeKJv2, SetNode, VHS_VideoCombine, GetNode, GetNode, ImageConcatMulti, SetNode, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, GetImageRangeFromBatch, WanVideoEncode, ImageConcatMulti, OnnxDetectionModelLoader, LoadImage, VHS_LoadVideo, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047160236468867073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047160236468867073.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `WanVideoTextEncodeCached`
- `WanVideoScheduler`
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
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `ImageConcatMulti`
- `OnnxDetectionModelLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoScheduler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CR Prompt Text`、`WanVideoContextOptions`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`GetImageSizeAndCount`、`PoseDetectionOneToAllAnimation`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoAddSteadyDancerEmbeds`、`GetImageRangeFromBatch`、`WanVideoEncode`、`OnnxDetectionModelLoader`、`LoadImage`、`VHS_LoadVideo`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
