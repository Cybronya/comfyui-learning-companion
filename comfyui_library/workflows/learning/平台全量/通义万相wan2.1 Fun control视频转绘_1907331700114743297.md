---
key: 平台全量/通义万相wan2.1 Fun control视频转绘_1907331700114743297.json
name: 通义万相wan2.1 Fun control视频转绘_1907331700114743297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/通义万相wan2.1 Fun control视频转绘_1907331700114743297.json
hash: 86498aaa29f8db4d
coverage: 0.965517
learned_at: 2026-11-14 02:48:31
nodes: [CLIPVisionLoader, LoadImage, GetImageSizeAndCount, WanVideoImageToVideoEncode, ImageResizeKJ, DepthAnything_V2, WanVideoClipVisionEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoTeaCache, WanVideoExperimentalArgs, Reroute, WanVideoControlEmbeds, WanVideoEncode, VHS_VideoCombine, ImageResizeKJ, WanVideoTextEncode, WanVideoVRAMManagement, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, WanVideoSampler, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, DownloadAndLoadDepthAnythingV2Model, WanVideoVAELoader, WanVideoModelLoader, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/通义万相wan2.1 Fun control视频转绘_1907331700114743297.json

> 来源文件 `comfyui_library/workflows/平台全量/通义万相wan2.1 Fun control视频转绘_1907331700114743297.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `CLIPVisionLoader`
- `LoadImage`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJ`
- `DepthAnything_V2`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `Reroute`
- `WanVideoControlEmbeds`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `WanVideoVRAMManagement`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `DownloadAndLoadDepthAnythingV2Model`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `VHS_LoadVideo`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`CLIPVisionLoader`、`LoadImage`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`ImageResizeKJ`、`DepthAnything_V2`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoControlEmbeds`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoVRAMManagement`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`easy cleanGpuUsed`、`DownloadAndLoadDepthAnythingV2Model`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_LoadVideo`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
