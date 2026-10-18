---
key: 视频生成/图生视频/Wan2.2提取视频首尾帧生成视频_1974460906073665538.json
name: Wan2.2提取视频首尾帧生成视频_1974460906073665538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2提取视频首尾帧生成视频_1974460906073665538.json
hash: 13b4ef0adfeb7cd4
coverage: 0.880952
learned_at: 2026-10-15 22:32:05
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoModelLoader, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoSampler, WanVideoClipVisionEncode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, PrimitiveInt, PrimitiveInt, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, PreviewImage, VHS_VideoCombine, SimpleMath+, ImageFromBatch+, ImageFromBatch+, CR Text, VHS_VideoInfo, VHS_LoadVideo, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2提取视频首尾帧生成视频_1974460906073665538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974460906073665538.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `SimpleMath+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `CR Text`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `MarkdownNote`

## 知识

覆盖率 **88%**（37/42）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`SimpleMath+`、`ImageFromBatch+`、`CR Text`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
