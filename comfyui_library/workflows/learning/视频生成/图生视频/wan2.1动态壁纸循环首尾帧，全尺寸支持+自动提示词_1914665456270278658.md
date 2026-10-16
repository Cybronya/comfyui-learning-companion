---
key: 视频生成/图生视频/wan2.1动态壁纸循环首尾帧，全尺寸支持+自动提示词_1914665456270278658.json
name: wan2.1动态壁纸循环首尾帧，全尺寸支持+自动提示词_1914665456270278658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1914665456270278658.json
hash: a56c4e1372cd1e4c
coverage: 1
learned_at: 2026-10-15 22:29:36
nodes: [WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSEDecode, WanVideoSESampler, WanVideoSEImageClipEncode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, UpscaleModelLoader, UpscaleImageWithModelIfNeed, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, DownloadAndLoadFlorence2Model, WanVideoTextEncode, StringFunction|pysssss, LoadWanVideoClipTextEncoder, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSEModelLoader, Florence2Run, WanVideoSLG, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1动态壁纸循环首尾帧，全尺寸支持+自动提示词_1914665456270278658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914665456270278658.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（24 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSEDecode`
- `WanVideoSESampler` ★核心
- `WanVideoSEImageClipEncode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `UpscaleModelLoader`
- `UpscaleImageWithModelIfNeed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `DownloadAndLoadFlorence2Model`
- `WanVideoTextEncode`
- `StringFunction|pysssss`
- `LoadWanVideoClipTextEncoder` ★核心
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSEModelLoader`
- `Florence2Run`
- `WanVideoSLG`
- `LoadImage`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSEDecode`、`WanVideoSESampler`、`WanVideoSEImageClipEncode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`UpscaleModelLoader`、`UpscaleImageWithModelIfNeed`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`DownloadAndLoadFlorence2Model`、`WanVideoTextEncode`、`StringFunction|pysssss`、`LoadWanVideoClipTextEncoder`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSEModelLoader`、`Florence2Run`、`WanVideoSLG`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSESampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoTextEncode、WanVideoVAELoader、WanVideoSEDecode、WanVideoSEImageClipEncode
