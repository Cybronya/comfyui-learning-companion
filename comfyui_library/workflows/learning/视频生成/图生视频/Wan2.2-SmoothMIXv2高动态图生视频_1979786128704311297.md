---
key: 视频生成/图生视频/Wan2.2-SmoothMIXv2高动态图生视频_1979786128704311297.json
name: Wan2.2-SmoothMIXv2高动态图生视频_1979786128704311297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979786128704311297.json
hash: 1a6a635cea96f2ac
coverage: 0.862069
learned_at: 2026-10-15 22:32:26
nodes: [WanVideoSetBlockSwap, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, easy cleanGpuUsed, VHS_VideoCombine, PrimitiveInt, SimpleMath+, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoDecode, WanVideoModelLoader, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, ImageResizeKJv2, MarkdownNote, LoadImage, PrimitiveInt, PrimitiveInt, CR Text, WanVideoSampler, WanVideoSampler, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-SmoothMIXv2高动态图生视频_1979786128704311297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979786128704311297.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `SimpleMath+`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `CR Text`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`SimpleMath+`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`LoadImage`、`CR Text`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、GetImageSizeAndCount
