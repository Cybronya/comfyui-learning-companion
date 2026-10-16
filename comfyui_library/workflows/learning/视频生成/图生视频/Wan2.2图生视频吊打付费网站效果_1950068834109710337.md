---
key: 视频生成/图生视频/Wan2.2图生视频吊打付费网站效果_1950068834109710337.json
name: Wan2.2图生视频吊打付费网站效果_1950068834109710337.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950068834109710337.json
hash: 5ae6b4e76f45b590
coverage: 1
learned_at: 2026-10-15 22:30:52
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageResizeKJv2, VHS_VideoCombine, CR Text, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频吊打付费网站效果_1950068834109710337.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950068834109710337.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `CR Text`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`easy cleanGpuUsed`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`ImageResizeKJv2`、`VHS_VideoCombine`、`CR Text`、`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
