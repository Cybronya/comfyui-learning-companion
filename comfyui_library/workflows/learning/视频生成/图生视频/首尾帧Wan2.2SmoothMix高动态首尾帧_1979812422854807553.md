---
key: 视频生成/图生视频/首尾帧Wan2.2SmoothMix高动态首尾帧_1979812422854807553.json
name: 首尾帧Wan2.2SmoothMix高动态首尾帧_1979812422854807553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧Wan2.2SmoothMix高动态首尾帧_1979812422854807553.json
hash: 318c0ee54df18f6d
coverage: 0.848485
learned_at: 2026-10-15 22:32:26
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, LoadWanVideoT5TextEncoder, PrimitiveInt, PrimitiveInt, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, LoadImage, LoadImage, Int, WanVideoBlockSwap, PrimitiveInt, SimpleMath+, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, easy cleanGpuUsed, ImageResizeKJv2, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, GetImageSizeAndCount, ImageResizeKJv2, PrimitiveStringMultiline, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧Wan2.2SmoothMix高动态首尾帧_1979812422854807553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979812422854807553.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LoadImage`
- `LoadImage`
- `Int`
- `WanVideoBlockSwap`
- `PrimitiveInt`
- `SimpleMath+`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`easy cleanGpuUsed`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadImage`、`Int`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
