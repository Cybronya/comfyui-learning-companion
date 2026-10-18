---
key: 视频生成/图生视频/【KJ加速版】Wan2.2 图生视频_1953401583553925122.json
name: 【KJ加速版】Wan2.2 图生视频_1953401583553925122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【KJ加速版】Wan2.2 图生视频_1953401583553925122.json
hash: 7525caffd151f9a9
coverage: 1
learned_at: 2026-10-15 22:31:05
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CR Text, WanVideoModelLoader, ImageResizeKJv2, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoDecode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoSampler, GetImageSizeAndCount, ImageFromBatch+, WanVideoSampler, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【KJ加速版】Wan2.2 图生视频_1953401583553925122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953401583553925122.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
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
- `easy cleanGpuUsed`
- `CR Text`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `WanVideoSampler` ★核心
- `LoadImage`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`CR Text`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`GetImageSizeAndCount`、`ImageFromBatch+`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
