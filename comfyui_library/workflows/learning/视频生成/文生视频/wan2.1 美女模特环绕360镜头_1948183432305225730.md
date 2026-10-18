---
key: 视频生成/文生视频/wan2.1 美女模特环绕360镜头_1948183432305225730.json
name: wan2.1 美女模特环绕360镜头_1948183432305225730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1 美女模特环绕360镜头_1948183432305225730.json
hash: 50e8bee09420a1bb
coverage: 0.967742
learned_at: 2026-10-15 22:43:32
nodes: [WanVideoExperimentalArgs, WanVideoTeaCache, ImageSmartSharpen+, ImageScaleToMegapixels, UpscaleModelLoader, GIMMVFI_interpolate, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, LayerUtility: PurgeVRAM, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoVAELoader, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, WanVideoEnhanceAVideo, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoSampler, LayerUtility: PurgeVRAM, LoadImage, Fast Groups Bypasser (rgthree), WanVideoImageClipEncode, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1 美女模特环绕360镜头_1948183432305225730.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1948183432305225730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `ImageSmartSharpen+`
- `ImageScaleToMegapixels`
- `UpscaleModelLoader`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoEnhanceAVideo`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`ImageSmartSharpen+`、`ImageScaleToMegapixels`、`UpscaleModelLoader`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`WanVideoEnhanceAVideo`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoSampler`、`LoadImage`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
