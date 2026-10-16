---
key: 视频生成/图生视频/动作迁移 动作模仿  wan22  wan2.2_2047889744532606978.json
name: 动作迁移 动作模仿  wan22  wan2.2_2047889744532606978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047889744532606978.json
hash: 7039ea03979f07f6
coverage: 0.744186
learned_at: 2026-10-15 22:37:07
nodes: [WanVideoTextEncodeCached, WanVideoScheduler, OnnxDetectionModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, CR Prompt Text, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, WanVideoSamplerFromSettings, Reroute, WanVideoSamplerSettings, WanVideoDecode, GetImageSizeAndCount, PoseDetectionOneToAllAnimation, PreviewImage, PreviewImage, ImageResizeKJv2, SetNode, VHS_VideoCombine, GetNode, ImageConcatMulti, SetNode, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoAddSteadyDancerEmbeds, GetImageRangeFromBatch, ImageConcatMulti, VHS_LoadVideo, LoadImage, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanVideoClipVisionEncode, WanVideoEncode, WanVideoClipVisionEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan22  wan2.2_2047889744532606978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047889744532606978.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `WanVideoTextEncodeCached`
- `WanVideoScheduler`
- `OnnxDetectionModelLoader`
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
- `ImageConcatMulti`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoScheduler`、`OnnxDetectionModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CR Prompt Text`、`WanVideoContextOptions`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`PoseDetectionOneToAllAnimation`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoImageToVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`LoadImage`、`WanVideoClipVisionEncode`、`WanVideoEncode`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
