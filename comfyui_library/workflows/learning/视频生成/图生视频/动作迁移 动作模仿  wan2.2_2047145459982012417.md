---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047145459982012417.json
name: 动作迁移 动作模仿  wan2.2_2047145459982012417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047145459982012417.json
hash: 80b40a1044810ded
coverage: 0.744186
learned_at: 2026-10-15 22:37:03
nodes: [GetImageRangeFromBatch, VHS_LoadVideo, LoadImage, GetImageSizeAndCount, OnnxDetectionModelLoader, ImageResizeKJv2, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, ImageResizeKJv2, SetNode, VHS_VideoCombine, SetNode, WanVideoClipVisionEncode, CR Prompt Text, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, WanVideoVAELoader, SetNode, CLIPVisionLoader, SetNode, ImageConcatMulti, Reroute, WanVideoSamplerSettings, WanVideoSamplerFromSettings, WanVideoDecode, WanVideoScheduler, WanVideoAddSteadyDancerEmbeds, PrimitiveNode, WanVideoImageToVideoEncode, WanVideoEncode, WanVideoClipVisionEncode, ImageConcatMulti, GetNode, GetNode, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2047145459982012417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047145459982012417.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `GetImageRangeFromBatch`
- `VHS_LoadVideo`
- `LoadImage`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoClipVisionEncode`
- `CR Prompt Text`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `ImageConcatMulti`
- `Reroute`
- `WanVideoSamplerSettings` ★核心
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`
- `WanVideoScheduler`
- `WanVideoAddSteadyDancerEmbeds`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`GetImageRangeFromBatch`、`VHS_LoadVideo`、`LoadImage`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`CR Prompt Text`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ImageConcatMulti`、`WanVideoSamplerSettings`、`WanVideoSamplerFromSettings`、`WanVideoDecode`、`WanVideoScheduler`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoImageToVideoEncode`、`WanVideoEncode`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
