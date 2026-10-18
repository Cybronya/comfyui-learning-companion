---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047249835761344514.json
name: 动作迁移 动作模仿  wan2.2_2047249835761344514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047249835761344514.json
hash: a5e1e57abb3e4167
coverage: 0.744186
learned_at: 2026-10-15 22:37:04
nodes: [GetImageSizeAndCount, OnnxDetectionModelLoader, ImageResizeKJv2, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, CLIPVisionLoader, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, SetNode, Reroute, GetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, PrimitiveNode, WanVideoContextOptions, CR Prompt Text, SetNode, VHS_VideoCombine, GetImageRangeFromBatch, WanVideoEncode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, PrimitiveNode, GetNode, ImageConcatMulti, WanVideoScheduler, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, LoadImage, WanVideoSamplerSettings, WanVideoSamplerFromSettings, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047249835761344514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047249835761344514.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `Reroute`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `PrimitiveNode`
- `WanVideoContextOptions`
- `CR Prompt Text`
- `SetNode`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `PrimitiveNode`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoScheduler`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoSamplerSettings` ★核心
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`CLIPVisionLoader`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoContextOptions`、`CR Prompt Text`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoAddSteadyDancerEmbeds`、`ImageConcatMulti`、`WanVideoScheduler`、`VHS_LoadVideo`、`LoadImage`、`WanVideoSamplerSettings`、`WanVideoSamplerFromSettings`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
