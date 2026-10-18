---
key: 视频生成/图生视频/通义万相wan2.1美女一字马_1909453938431504386.json
name: 通义万相wan2.1美女一字马_1909453938431504386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相wan2.1美女一字马_1909453938431504386.json
hash: df3eeac271f31e7b
coverage: 1
learned_at: 2026-10-15 22:29:29
nodes: [LayerUtility: PurgeVRAM, VHS_VideoCombine, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoDecode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, UpscaleImageByUsingModel, UpscaleModelLoader, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTeaCache, WanVideoImageClipEncode, ImageResizeKJ, LoadWanVideoClipTextEncoder, WanVideoTextEncode, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.1美女一字马_1909453938431504386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1909453938431504386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（21 个）：
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `UpscaleImageByUsingModel`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTeaCache`
- `WanVideoImageClipEncode`
- `ImageResizeKJ`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`UpscaleImageByUsingModel`、`UpscaleModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoImageClipEncode`、`ImageResizeKJ`、`LoadWanVideoClipTextEncoder`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
