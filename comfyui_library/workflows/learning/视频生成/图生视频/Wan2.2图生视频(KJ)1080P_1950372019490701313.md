---
key: 视频生成/图生视频/Wan2.2图生视频(KJ)1080P_1950372019490701313.json
name: Wan2.2图生视频(KJ)1080P_1950372019490701313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950372019490701313.json
hash: f07c42b19ee42e30
coverage: 0.935484
learned_at: 2026-10-15 22:30:54
nodes: [LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoModelLoader, easy cleanGpuUsed, WanVideoLoraSelect, WanVideoModelLoader, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, WanVideoApplyNAG, easy cleanGpuUsed, WanVideoImageToVideoEncode, LoadImage, PrimitiveInt, WanVideoSampler, WanVideoSampler, WanVideoBlockSwap, WanVideoTextEncodeSingle, ImageResizeKJv2, SeedVR2BlockSwap, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, easy cleanGpuUsed, GetImageSizeAndCount, SeedVR2, CR Text, WanVideoDecode, SimpleMath+, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频(KJ)1080P_1950372019490701313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950372019490701313.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `WanVideoApplyNAG`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `PrimitiveInt`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoTextEncodeSingle`
- `ImageResizeKJv2`
- `SeedVR2BlockSwap`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `SeedVR2`
- `CR Text`
- `WanVideoDecode`
- `SimpleMath+`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`WanVideoLoraSelect`、`WanVideoApplyNAG`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoSampler`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`SeedVR2BlockSwap`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`GetImageSizeAndCount`、`SeedVR2`、`CR Text`、`WanVideoDecode`、`SimpleMath+`、`VHS_VideoCombine`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
