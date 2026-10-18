---
key: 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2052755424847384578.json
name: 动作迁移 动作模仿  wan2.2_2052755424847384578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿  wan2.2_2052755424847384578.json
hash: 3a808db6dce8dff8
coverage: 0.744186
learned_at: 2026-10-15 22:37:32
nodes: [GetImageSizeAndCount, OnnxDetectionModelLoader, ImageResizeKJv2, PreviewImage, PreviewImage, PoseDetectionOneToAllAnimation, CR Prompt Text, WanVideoTextEncodeCached, WanVideoContextOptions, Reroute, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetImageRangeFromBatch, ImageResizeKJv2, WanVideoClipVisionEncode, SetNode, WanVideoEncode, PrimitiveNode, GetNode, GetNode, WanVideoScheduler, ImageConcatMulti, WanVideoImageToVideoEncode, WanVideoAddSteadyDancerEmbeds, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, PrimitiveNode, CLIPVisionLoader, WanVideoModelLoader, SetNode, SetNode, SetNode, WanVideoBlockSwap, VHS_VideoCombine, WanVideoLoraSelect, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan2.2_2052755424847384578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052755424847384578.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `CR Prompt Text`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `Reroute`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `SetNode`
- `WanVideoEncode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `WanVideoScheduler`
- `ImageConcatMulti`
- `WanVideoImageToVideoEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoSamplerSettings` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `PrimitiveNode`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`CR Prompt Text`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoScheduler`、`ImageConcatMulti`、`WanVideoImageToVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
