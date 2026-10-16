---
key: 视频生成/图生视频/WAN2.1动态壁纸循环首尾帧_1918858509570473986.json
name: WAN2.1动态壁纸循环首尾帧_1918858509570473986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1918858509570473986.json
hash: bdd6243e9e8caee9
coverage: 1
learned_at: 2026-10-15 22:29:41
nodes: [WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSEDecode, WanVideoSESampler, WanVideoSEImageClipEncode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, UpscaleModelLoader, UpscaleImageWithModelIfNeed, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, DownloadAndLoadFlorence2Model, WanVideoTextEncode, StringFunction|pysssss, LoadWanVideoClipTextEncoder, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSEModelLoader, Florence2Run, WanVideoSLG, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1动态壁纸循环首尾帧_1918858509570473986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1918858509570473986.json`

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
