---
key: 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2043550053435969538.json
name: 动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2043550053435969538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043550053435969538.json
hash: 2e96fd81d0d13584
coverage: 0.744186
learned_at: 2026-10-15 22:36:32
nodes: [WanVideoTextEncodeCached, WanVideoScheduler, OnnxDetectionModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, CR Prompt Text, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, WanVideoSamplerFromSettings, Reroute, WanVideoSamplerSettings, WanVideoDecode, GetImageSizeAndCount, ImageResizeKJv2, SetNode, VHS_VideoCombine, SetNode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, ImageConcatMulti, ImageConcatMulti, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, ImageResizeKJv2, GetImageRangeFromBatch, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2 SteadyDancer_2043550053435969538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043550053435969538.json`

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
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
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
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoScheduler`、`OnnxDetectionModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CR Prompt Text`、`WanVideoContextOptions`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoAddSteadyDancerEmbeds`、`ImageConcatMulti`、`PoseDetectionOneToAllAnimation`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
