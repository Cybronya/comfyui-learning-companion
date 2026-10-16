---
key: 视频生成/图生视频/Wan2.2取视频首尾帧生成视频自动提示词版_1974477475709366273.json
name: Wan2.2取视频首尾帧生成视频自动提示词版_1974477475709366273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1974477475709366273.json
hash: d81a0010efaabe1d
coverage: 0.847826
learned_at: 2026-10-15 22:32:05
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, PreviewImage, VHS_VideoCombine, VHS_VideoInfo, ImageFromBatch+, ImageFromBatch+, ImageBatchMultiple+, VHS_LoadVideo, SimpleMath+, MarkdownNote, ShowText|pysssss, GetImageSizeAndCount, AILab_MiniCPM_4_V_Advanced, PrimitiveInt, PrimitiveInt, PrimitiveInt, SimpleMath+, WanVideoModelLoader, WanVideoSampler, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2取视频首尾帧生成视频自动提示词版_1974477475709366273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974477475709366273.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageBatchMultiple+`
- `VHS_LoadVideo`
- `SimpleMath+`
- `MarkdownNote`
- `ShowText|pysssss`
- `GetImageSizeAndCount`
- `AILab_MiniCPM_4_V_Advanced`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`ImageResizeKJv2`、`VHS_VideoInfo`、`ImageFromBatch+`、`ImageBatchMultiple+`、`VHS_LoadVideo`、`SimpleMath+`、`GetImageSizeAndCount`、`AILab_MiniCPM_4_V_Advanced`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
