---
key: 视频生成/图生视频/wan22 wan2.2  动作迁移 SteadyDancer 角色替换_2042801321077641218.json
name: wan22 wan2.2  动作迁移 SteadyDancer 角色替换_2042801321077641218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042801321077641218.json
hash: bbdb51f14aedbdfd
coverage: 0.8
learned_at: 2026-10-15 22:36:29
nodes: [WanVideoTextEncodeCached, WanVideoScheduler, WanVideoDecode, WanVideoEncode, WanVideoSamplerSettings, WanVideoImageToVideoEncode, WanVideoContextOptions, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, CR Prompt Text, WanVideoClipVisionEncode, WanVideoSamplerFromSettings, ImageConcatMulti, ImageConcatMulti, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, PoseDetectionOneToAllAnimation, VHS_VideoCombine, PreviewImage, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, SetNode, SetNode, GetImageRangeFromBatch, WanVideoSetBlockSwap, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoBlockSwap, SetNode, SetNode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/wan22 wan2.2  动作迁移 SteadyDancer 角色替换_2042801321077641218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042801321077641218.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `WanVideoTextEncodeCached`
- `WanVideoScheduler`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoSamplerSettings` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoContextOptions`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `CR Prompt Text`
- `WanVideoClipVisionEncode`
- `WanVideoSamplerFromSettings` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `PoseDetectionOneToAllAnimation`
- `VHS_VideoCombine`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `WanVideoSetBlockSwap`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoScheduler`、`WanVideoDecode`、`WanVideoEncode`、`WanVideoSamplerSettings`、`WanVideoImageToVideoEncode`、`WanVideoContextOptions`、`WanVideoClipVisionEncode`、`WanVideoAddSteadyDancerEmbeds`、`CR Prompt Text`、`WanVideoSamplerFromSettings`、`ImageConcatMulti`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`PoseDetectionOneToAllAnimation`、`ImageResizeKJv2`、`GetImageRangeFromBatch`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
