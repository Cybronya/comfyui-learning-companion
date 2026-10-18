---
key: 视频生成/图生视频/Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json
name: Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json
hash: bdba9ad43a4624ec
coverage: 0.857143
learned_at: 2026-10-15 22:32:26
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetImageSizeAndCount, PrimitiveInt, VHS_VideoCombine, VHS_VideoCombine, ImageBatchMultiple+, ShowText|pysssss, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, PrimitiveInt, PrimitiveInt, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, SimpleMath+, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, MarkdownNote, LoadImage, WanVideoVAELoader, AILab_MiniCPM_4_V_Advanced]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979805991325831170.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBatchMultiple+`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `MarkdownNote`
- `LoadImage`
- `WanVideoVAELoader`
- `AILab_MiniCPM_4_V_Advanced`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`easy cleanGpuUsed`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`ImageBatchMultiple+`、`LoadImage`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`SimpleMath+`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`AILab_MiniCPM_4_V_Advanced`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoSetLoRAs
