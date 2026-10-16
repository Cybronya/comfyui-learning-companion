---
key: 视频生成/图生视频/通义万相wan2.1万物老化特效_1912458633853239298.json
name: 通义万相wan2.1万物老化特效_1912458633853239298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1912458633853239298.json
hash: 224d3a8ca310ed27
coverage: 1
learned_at: 2026-10-15 22:29:32
nodes: [LayerUtility: PurgeVRAM, VHS_VideoCombine, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoDecode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, UpscaleImageByUsingModel, UpscaleModelLoader, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTeaCache, WanVideoImageClipEncode, ImageResizeKJ, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.1万物老化特效_1912458633853239298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912458633853239298.json`

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
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **100%**（21/21）

**有卡**：`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`UpscaleImageByUsingModel`、`UpscaleModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoImageClipEncode`、`ImageResizeKJ`、`WanVideoTextEncode`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
