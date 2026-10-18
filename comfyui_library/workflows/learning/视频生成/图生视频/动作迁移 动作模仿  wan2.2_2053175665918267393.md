---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2053175665918267393.json
name: 动作迁移 动作模仿  wan2.2_2053175665918267393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿  wan2.2_2053175665918267393.json
hash: 2cef0eb06c790394
coverage: 0.744186
learned_at: 2026-10-15 22:37:37
nodes: [GetImageSizeAndCount, OnnxDetectionModelLoader, ImageResizeKJv2, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, SetNode, VHS_VideoCombine, CR Prompt Text, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, WanVideoVAELoader, SetNode, CLIPVisionLoader, SetNode, Reroute, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, VHS_VideoCombine, WanVideoLoraSelect, WanVideoBlockSwap, GetImageRangeFromBatch, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, SetNode, WanVideoEncode, WanVideoAddSteadyDancerEmbeds, WanVideoSamplerSettings, PrimitiveNode, GetNode, GetNode, WanVideoScheduler, ImageConcatMulti, ImageConcatMulti, WanVideoSamplerFromSettings, WanVideoDecode, WanVideoModelLoader, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2053175665918267393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053175665918267393.json`

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
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
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

## 知识

覆盖率 **74%**（32/43）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`VHS_VideoCombine`、`CR Prompt Text`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`GetImageRangeFromBatch`、`WanVideoImageToVideoEncode`、`WanVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`WanVideoScheduler`、`ImageConcatMulti`、`WanVideoSamplerFromSettings`、`WanVideoDecode`、`WanVideoModelLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
