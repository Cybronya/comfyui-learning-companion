---
key: 视频生成/图生视频/Wan2.2图生视频720P高清版自动提示词_1975197329210871809.json
name: Wan2.2图生视频720P高清版自动提示词_1975197329210871809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975197329210871809.json
hash: 70b7b5c01a200264
coverage: 0.888889
learned_at: 2026-10-15 22:32:07
nodes: [VHS_VideoCombine, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoSetBlockSwap, ImageResizeKJv2, CLIPVisionLoader, easy cleanGpuUsed, WanVideoSampler, GetImageSizeAndCount, VHS_VideoCombine, LoadImage, WanVideoLoraSelect, WanVideoTorchCompileSettings, LoadImage, WanVideoImageToVideoEncode, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSampler, WanVideoClipVisionEncode, WanVideoModelLoader, ShowText|pysssss, AILab_MiniCPM_4_V_Advanced, PrimitiveInt, PrimitiveInt, WanVideoModelLoader, WanVideoBlockSwap, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频720P高清版自动提示词_1975197329210871809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975197329210871809.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `ShowText|pysssss`
- `AILab_MiniCPM_4_V_Advanced`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `MarkdownNote`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoSampler`、`GetImageSizeAndCount`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`AILab_MiniCPM_4_V_Advanced`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
