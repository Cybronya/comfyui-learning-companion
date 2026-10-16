---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2058772271212359682.json
name: 动作迁移 动作模仿  wan2.2_2058772271212359682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058772271212359682.json
hash: 98649861b9e921a1
coverage: 0.744186
learned_at: 2026-10-15 22:38:28
nodes: [WanVideoClipVisionEncode, WanVideoBlockSwap, VHS_LoadVideo, LoadImage, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoContextOptions, PrimitiveNode, WanVideoModelLoader, WanVideoDecode, ImageConcatMulti, GetNode, WanVideoSamplerFromSettings, WanVideoSamplerSettings, PrimitiveNode, WanVideoTextEncodeCached, CR Prompt Text, WanVideoScheduler, ImageResizeKJv2, WanVideoEncode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, SetNode, CLIPVisionLoader, GetImageRangeFromBatch, WanVideoVAELoader, SetNode, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewImage, PreviewImage, ImageResizeKJv2, SetNode, SetNode, GetImageSizeAndCount, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, Reroute, WanVideoAddSteadyDancerEmbeds, GetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2058772271212359682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058772271212359682.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoContextOptions`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoSamplerSettings` ★核心
- `PrimitiveNode`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `WanVideoScheduler`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `WanVideoVAELoader`
- `SetNode`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoAddSteadyDancerEmbeds`
- `GetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoContextOptions`、`WanVideoModelLoader`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`WanVideoScheduler`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`GetImageRangeFromBatch`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseDetectionOneToAllAnimation`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoAddSteadyDancerEmbeds`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
