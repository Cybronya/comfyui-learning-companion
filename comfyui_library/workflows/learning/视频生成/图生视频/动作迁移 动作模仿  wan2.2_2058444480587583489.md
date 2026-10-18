---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2058444480587583489.json
name: 动作迁移 动作模仿  wan2.2_2058444480587583489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿  wan2.2_2058444480587583489.json
hash: f6b579c331bc18b2
coverage: 0.744186
learned_at: 2026-10-15 22:38:23
nodes: [WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, GetNode, GetNode, ImageConcatMulti, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoAddSteadyDancerEmbeds, WanVideoSamplerSettings, WanVideoSamplerFromSettings, Reroute, PrimitiveNode, PrimitiveNode, VHS_LoadVideo, GetImageSizeAndCount, OnnxDetectionModelLoader, ImageResizeKJv2, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, WanVideoContextOptions, WanVideoTextEncodeCached, WanVideoScheduler, CR Prompt Text, ImageResizeKJv2, SetNode, VHS_VideoCombine, GetImageRangeFromBatch, WanVideoEncode, WanVideoClipVisionEncode, SetNode, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2058444480587583489.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058444480587583489.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoSamplerSettings` ★核心
- `WanVideoSamplerFromSettings` ★核心
- `Reroute`
- `PrimitiveNode`
- `PrimitiveNode`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `WanVideoContextOptions`
- `WanVideoTextEncodeCached`
- `WanVideoScheduler`
- `CR Prompt Text`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`WanVideoSamplerFromSettings`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`WanVideoScheduler`、`CR Prompt Text`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoDecode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
