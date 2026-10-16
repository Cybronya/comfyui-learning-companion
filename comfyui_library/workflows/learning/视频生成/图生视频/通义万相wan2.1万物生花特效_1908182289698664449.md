---
key: 视频生成/图生视频/通义万相wan2.1万物生花特效_1908182289698664449.json
name: 通义万相wan2.1万物生花特效_1908182289698664449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1908182289698664449.json
hash: bd416d06554e81db
coverage: 1
learned_at: 2026-10-15 22:29:28
nodes: [VHS_VideoCombine, WanVideoBlockSwap, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoDecode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, UpscaleImageByUsingModel, UpscaleModelLoader, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTeaCache, ImageResizeKJ, WanVideoModelLoader, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoTextEncode, LoadWanVideoClipTextEncoder, LayerUtility: PurgeVRAM, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.1万物生花特效_1908182289698664449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1908182289698664449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（21 个）：
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
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
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `LayerUtility: PurgeVRAM`
- `LoadImage`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`UpscaleImageByUsingModel`、`UpscaleModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTeaCache`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoImageClipEncode`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`、`LayerUtility: PurgeVRAM`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
