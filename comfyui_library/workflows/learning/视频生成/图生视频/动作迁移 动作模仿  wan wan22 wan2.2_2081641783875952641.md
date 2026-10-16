---
key: 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2_2081641783875952641.json
name: 动作迁移 动作模仿  wan wan22 wan2.2_2081641783875952641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2081641783875952641.json
hash: 371155e581f7f255
coverage: 0.794872
learned_at: 2026-10-15 22:42:23
nodes: [WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, PoseDetectionOneToAllAnimation, PreviewImage, PreviewImage, WanVideoClipVisionEncode, OnnxDetectionModelLoader, WanVideoSamplerFromSettings, WanVideoDecode, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoContextOptions, WanVideoScheduler, WanVideoSamplerSettings, Reroute, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, GetImageSizeAndCount, SetNode, SetNode, ImageResizeKJv2, WanVideoEncode, WanVideoClipVisionEncode, SetNode, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoImageToVideoEncode, ImageConcatMulti, VHS_VideoCombine, GetImageRangeFromBatch, ImageConcatMulti, GetNode, ImageResizeKJv2, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2_2081641783875952641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081641783875952641.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoContextOptions`
- `WanVideoScheduler`
- `WanVideoSamplerSettings` ★核心
- `Reroute`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoEncode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **79%**（31/39）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`PoseDetectionOneToAllAnimation`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoSamplerFromSettings`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoContextOptions`、`WanVideoScheduler`、`WanVideoSamplerSettings`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoEncode`、`ImageConcatMulti`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
