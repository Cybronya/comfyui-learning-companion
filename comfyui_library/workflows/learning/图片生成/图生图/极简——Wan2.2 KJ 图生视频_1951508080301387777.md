---
key: 图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json
name: 极简——Wan2.2 KJ 图生视频_1951508080301387777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json
hash: 208d7677b3f897ad
coverage: 1
learned_at: 2026-10-23 13:09:09
nodes: [INTConstant, GetImageSizeAndCount, WanVideoDecode, INTConstant, SimpleMath+, CreateCFGScheduleFloatList, VHS_VideoCombine, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, INTConstant, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler]
patterns: []
missing: []
---

# 图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `INTConstant`
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（25/25）

**有卡**：`INTConstant`、`GetImageSizeAndCount`、`WanVideoDecode`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
