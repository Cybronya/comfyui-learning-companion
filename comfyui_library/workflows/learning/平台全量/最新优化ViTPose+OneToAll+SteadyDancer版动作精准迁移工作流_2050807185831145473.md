---
key: 平台全量/最新优化ViTPose+OneToAll+SteadyDancer版动作精准迁移工作流_2050807185831145473.json
name: 最新优化ViTPose+OneToAll+SteadyDancer版动作精准迁移工作流_2050807185831145473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最新优化ViTPose+OneToAll+SteadyDancer版动作精准迁移工作流_2050807185831145473.json
hash: 115d75f2e409d853
coverage: 0.611111
learned_at: 2026-11-14 02:15:55
nodes: [LoadImage, VHS_LoadVideo, WanVideoLoraSelect, CLIPVisionLoader, SetNode, WanVideoVAELoader, VHS_VideoCombine, TextInput_, Int, Int, WanVideoModelLoader, WanVideoSetLoRAs, PreviewImage, PreviewImage, VHS_VideoInfoLoaded, easy showAnything, SetNode, SetNode, SetNode, ImageResizeKJv2, WanVideoClipVisionEncode, GetImageSizeAndCount, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddSteadyDancerEmbeds, GetNode, WanVideoEncode, PreviewImage, PreviewImage, GetNode, WanVideoClipVisionEncode, GetNode, WanVideoImageToVideoEncode, WanVideoScheduler, WanVideoSamplerSettings, WanVideoTextEncodeCached, WanVideoContextOptions, WanVideoSamplerFromSettings, SetNode, GetNode, ImageConcatMulti, WanVideoDecode, easy cleanGpuUsed, GetNode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, GetImageRangeFromBatch, PreviewImage, PoseDetectionOneToAllAnimation, OnnxDetectionModelLoader]
patterns: []
missing: []
---

# 平台全量/最新优化ViTPose+OneToAll+SteadyDancer版动作精准迁移工作流_2050807185831145473.json

> 来源文件 `comfyui_library/workflows/平台全量/最新优化ViTPose+OneToAll+SteadyDancer版动作精准迁移工作流_2050807185831145473.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（54 个）：
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `TextInput_`
- `Int`
- `Int`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddSteadyDancerEmbeds`
- `GetNode`
- `WanVideoEncode`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoScheduler`
- `WanVideoSamplerSettings` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `WanVideoSamplerFromSettings` ★核心
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `OnnxDetectionModelLoader`

## 知识

覆盖率 **61%**（33/54）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`WanVideoLoraSelect`、`CLIPVisionLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`TextInput_`、`Int`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoScheduler`、`WanVideoSamplerSettings`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoSamplerFromSettings`、`ImageConcatMulti`、`WanVideoDecode`、`easy cleanGpuUsed`、`GetImageRangeFromBatch`、`PoseDetectionOneToAllAnimation`、`OnnxDetectionModelLoader`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
