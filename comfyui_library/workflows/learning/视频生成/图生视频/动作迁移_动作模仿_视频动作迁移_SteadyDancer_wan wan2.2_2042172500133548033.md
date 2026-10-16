---
key: 视频生成/图生视频/动作迁移_动作模仿_视频动作迁移_SteadyDancer_wan wan2.2_2042172500133548033.json
name: 动作迁移_动作模仿_视频动作迁移_SteadyDancer_wan wan2.2_2042172500133548033.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042172500133548033.json
hash: ce085925772098ed
coverage: 0.761905
learned_at: 2026-10-15 22:36:26
nodes: [WanVideoDecode, GetNode, GetNode, Reroute, LoadImage, VHS_VideoCombine, CR Prompt Text, WanVideoContextOptions, ImageResizeKJv2, ImageResizeKJv2, WanVideoSamplerSettings, WanVideoTextEncodeCached, WanVideoEncode, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, ImageConcatMulti, ImageConcatMulti, WanVideoImageToVideoEncode, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, WanVideoBlockSwap, OnnxDetectionModelLoader, GetImageSizeAndCount, PoseDetectionOneToAllAnimation, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, WanVideoScheduler, PrimitiveNode, PrimitiveNode, SetNode, WanVideoSamplerFromSettings, SetNode, GetImageRangeFromBatch, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移_动作模仿_视频动作迁移_SteadyDancer_wan wan2.2_2042172500133548033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042172500133548033.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `Reroute`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `WanVideoContextOptions`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoSamplerSettings` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `OnnxDetectionModelLoader`
- `GetImageSizeAndCount`
- `PoseDetectionOneToAllAnimation`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `WanVideoScheduler`
- `PrimitiveNode`
- `PrimitiveNode`
- `SetNode`
- `WanVideoSamplerFromSettings` ★核心
- `SetNode`
- `GetImageRangeFromBatch`
- `VHS_LoadVideo`

## 知识

覆盖率 **76%**（32/42）

**有卡**：`WanVideoDecode`、`LoadImage`、`VHS_VideoCombine`、`CR Prompt Text`、`WanVideoContextOptions`、`ImageResizeKJv2`、`WanVideoSamplerSettings`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoAddSteadyDancerEmbeds`、`ImageConcatMulti`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`PoseDetectionOneToAllAnimation`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoScheduler`、`WanVideoSamplerFromSettings`、`GetImageRangeFromBatch`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
