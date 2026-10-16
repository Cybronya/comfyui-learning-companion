---
key: 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2_2080951206196899842.json
name: 动作迁移 动作模仿  wan wan22 wan2.2_2080951206196899842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2080951206196899842.json
hash: b91389d24021ee20
coverage: 0.756098
learned_at: 2026-10-15 22:42:19
nodes: [WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, WanVideoSamplerFromSettings, WanVideoDecode, WanVideoAddSteadyDancerEmbeds, WanVideoContextOptions, WanVideoScheduler, WanVideoSamplerSettings, WanVideoBlockSwap, CLIPVisionLoader, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, ImageResizeKJv2, VHS_LoadVideo, GetNode, SetNode, GetImageSizeAndCount, SetNode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, OnnxDetectionModelLoader, PreviewImage, PreviewImage, ImageResizeKJv2, SetNode, WanVideoTextEncodeCached, WanVideoEncode, GetImageRangeFromBatch, WanVideoClipVisionEncode, GetNode, PoseDetectionOneToAllAnimation, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, GetNode, ImageConcatMulti, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿  wan wan22 wan2.2_2080951206196899842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080951206196899842.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoContextOptions`
- `WanVideoScheduler`
- `WanVideoSamplerSettings` ★核心
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoEncode`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `GetNode`
- `PoseDetectionOneToAllAnimation`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **76%**（31/41）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoSamplerFromSettings`、`WanVideoDecode`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoContextOptions`、`WanVideoScheduler`、`WanVideoSamplerSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`GetImageRangeFromBatch`、`PoseDetectionOneToAllAnimation`、`VHS_VideoCombine`、`ImageConcatMulti`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
