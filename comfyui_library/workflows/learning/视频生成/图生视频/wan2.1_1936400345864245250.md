---
key: 视频生成/图生视频/wan2.1_1936400345864245250.json
name: wan2.1_1936400345864245250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1936400345864245250.json
hash: 01e3ee57e39a4295
coverage: 0.903226
learned_at: 2026-10-15 22:30:26
nodes: [WanVideoSampler, WanVideoExperimentalArgs, WanVideoTeaCache, ImageSmartSharpen+, ImageScaleToMegapixels, UpscaleModelLoader, GIMMVFI_interpolate, VHS_VideoCombine, easy cleanGpuUsed, WanVideoModelLoader, WanVideoDecode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoBlockSwap, DownloadAndLoadGIMMVFIModel, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, Note, WanVideoTextEncode, WanVideoLoraSelect, LoadImage, WanVideoImageClipEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1_1936400345864245250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936400345864245250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `ImageSmartSharpen+`
- `ImageScaleToMegapixels`
- `UpscaleModelLoader`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `Note`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoImageClipEncode`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`ImageSmartSharpen+`、`ImageScaleToMegapixels`、`UpscaleModelLoader`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTorchCompileSettings`、`WanVideoEnhanceAVideo`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoImageClipEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
