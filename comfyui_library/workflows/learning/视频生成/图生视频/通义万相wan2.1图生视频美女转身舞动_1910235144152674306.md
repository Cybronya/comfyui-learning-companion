---
key: 视频生成/图生视频/通义万相wan2.1图生视频美女转身舞动_1910235144152674306.json
name: 通义万相wan2.1图生视频美女转身舞动_1910235144152674306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1910235144152674306.json
hash: 8ec4741f7180fbd7
coverage: 1
learned_at: 2026-10-15 22:29:29
nodes: [LayerUtility: PurgeVRAM, VHS_VideoCombine, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSampler, WanVideoEnhanceAVideo, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTeaCache, WanVideoImageClipEncode, ImageResizeKJ, WanVideoDecode, CR Upscale Image, WanVideoTextEncode, WanVideoLoraSelect, LoadImage, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.1图生视频美女转身舞动_1910235144152674306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1910235144152674306.json`

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
- `WanVideoLoraSelect`
- `LoadImage`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **100%**（20/20）

**有卡**：`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoImageClipEncode`、`ImageResizeKJ`、`WanVideoDecode`、`CR Upscale Image`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadImage`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
