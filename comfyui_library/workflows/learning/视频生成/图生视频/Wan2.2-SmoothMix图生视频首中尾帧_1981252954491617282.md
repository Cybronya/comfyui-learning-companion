---
key: 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json
name: Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json
hash: a75a1767485b9b0d
coverage: 0.891892
learned_at: 2026-10-15 22:32:36
nodes: [WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, PrimitiveInt, PrimitiveInt, ImageResizeKJv2, WanVideoEncodeLatentBatch, WanVideoDecode, GetImageSizeAndCount, easy cleanGpuUsed, WanVideoContextOptions, WanVideoSetLoRAs, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, PrimitiveInt, WanVideoModelLoader, LoadImage, LoadImage, MarkdownNote, WanVideoModelLoader, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, CR Text, LoadImage, ImageResizeKJv2, SimpleMath+]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981252954491617282.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
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
- `ImageResizeKJv2`
- `WanVideoEncodeLatentBatch`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `WanVideoContextOptions`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `WanVideoModelLoader`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `CR Text`
- `LoadImage`
- `ImageResizeKJv2`
- `SimpleMath+`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoEncodeLatentBatch`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`WanVideoSetLoRAs`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`CR Text`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncodeLatentBatch
