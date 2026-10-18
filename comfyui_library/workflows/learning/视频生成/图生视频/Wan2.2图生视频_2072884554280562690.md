---
key: 视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json
name: Wan2.2图生视频_2072884554280562690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json
hash: a96a98a3f842e20b
coverage: 0.885714
learned_at: 2026-10-15 22:40:58
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageResizeKJv2, VHS_VideoCombine, WanVideoBlockSwap, CLIPVisionLoader, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, CR Text, PrimitiveInt, PrimitiveInt, WanVideoClipVisionEncode, GetImageSizeAndCount, PrimitiveInt, SimpleMath+, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072884554280562690.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CR Text`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `PrimitiveInt`
- `SimpleMath+`
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSampler`、`CR Text`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`SimpleMath+`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
