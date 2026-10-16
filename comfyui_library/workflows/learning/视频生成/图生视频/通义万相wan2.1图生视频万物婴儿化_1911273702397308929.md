---
key: 视频生成/图生视频/通义万相wan2.1图生视频万物婴儿化_1911273702397308929.json
name: 通义万相wan2.1图生视频万物婴儿化_1911273702397308929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1911273702397308929.json
hash: b4056aa98b6823d8
coverage: 1
learned_at: 2026-10-15 22:29:30
nodes: [LayerUtility: PurgeVRAM, VHS_VideoCombine, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSampler, WanVideoEnhanceAVideo, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTeaCache, WanVideoImageClipEncode, ImageResizeKJ, WanVideoDecode, CR Upscale Image, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.1图生视频万物婴儿化_1911273702397308929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911273702397308929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（20 个）：
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTeaCache`
- `WanVideoImageClipEncode`
- `ImageResizeKJ`
- `WanVideoDecode`
- `CR Upscale Image`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **100%**（20/20）

**有卡**：`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoImageClipEncode`、`ImageResizeKJ`、`WanVideoDecode`、`CR Upscale Image`、`WanVideoTextEncode`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
