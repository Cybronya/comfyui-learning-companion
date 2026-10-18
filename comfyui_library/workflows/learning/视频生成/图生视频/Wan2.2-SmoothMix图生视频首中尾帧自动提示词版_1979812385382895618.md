---
key: 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json
name: Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json
hash: 6bce34e18d0caee3
coverage: 0.875
learned_at: 2026-10-15 22:32:26
nodes: [WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, PrimitiveInt, PrimitiveInt, easy cleanGpuUsed, ImageResizeKJv2, WanVideoEncodeLatentBatch, WanVideoDecode, GetImageSizeAndCount, easy cleanGpuUsed, ShowText|pysssss, WanVideoContextOptions, WanVideoSetLoRAs, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, PrimitiveInt, AILab_MiniCPM_4_V_Advanced, ImageResizeKJv2, WanVideoModelLoader, LoadImage, LoadImage, LoadImage, MarkdownNote, WanVideoModelLoader, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageBatchMultiple+, SimpleMath+, WanVideoSampler, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979812385382895618.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `WanVideoEncodeLatentBatch`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `WanVideoContextOptions`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `AILab_MiniCPM_4_V_Advanced`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImageBatchMultiple+`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoEncodeLatentBatch`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`WanVideoSetLoRAs`、`WanVideoSampler`、`VHS_VideoCombine`、`AILab_MiniCPM_4_V_Advanced`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageBatchMultiple+`、`SimpleMath+`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncodeLatentBatch
