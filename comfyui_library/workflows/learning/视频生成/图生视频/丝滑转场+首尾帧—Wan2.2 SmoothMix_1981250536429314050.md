---
key: 视频生成/图生视频/丝滑转场+首尾帧—Wan2.2 SmoothMix_1981250536429314050.json
name: 丝滑转场+首尾帧—Wan2.2 SmoothMix_1981250536429314050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/丝滑转场+首尾帧—Wan2.2 SmoothMix_1981250536429314050.json
hash: 484cc4d8bc95d565
coverage: 0.909091
learned_at: 2026-10-15 22:32:36
nodes: [easy cleanGpuUsed, PreviewImage, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoDecode, LoadWanVideoT5TextEncoder, TextBox, GetImageSizeAndCount, WanVideoTextEncode, LoadImage, LoadImage, RH_LLMAPI_NODE, ImageBatchMultiple+, easy showAnything, PrimitiveInt, SimpleMath+, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSetLoRAs, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, CR SDXL Aspect Ratio, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/丝滑转场+首尾帧—Wan2.2 SmoothMix_1981250536429314050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981250536429314050.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `easy cleanGpuUsed`
- `PreviewImage`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `TextBox`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `ImageBatchMultiple+`
- `easy showAnything`
- `PrimitiveInt`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CR SDXL Aspect Ratio`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`easy cleanGpuUsed`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`TextBox`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`LoadImage`、`RH_LLMAPI_NODE`、`ImageBatchMultiple+`、`SimpleMath+`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`CR SDXL Aspect Ratio`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoSetLoRAs
