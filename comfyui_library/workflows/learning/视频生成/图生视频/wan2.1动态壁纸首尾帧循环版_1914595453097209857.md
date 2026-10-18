---
key: 视频生成/图生视频/wan2.1动态壁纸首尾帧循环版_1914595453097209857.json
name: wan2.1动态壁纸首尾帧循环版_1914595453097209857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1动态壁纸首尾帧循环版_1914595453097209857.json
hash: 06152c71ae67992d
coverage: 1
learned_at: 2026-10-15 22:29:36
nodes: [LoadWanVideoT5TextEncoder, WanVideoSEModelLoader, WanVideoTorchCompileSettings, LoadImage, WanVideoLoraSelect, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, LoadWanVideoClipTextEncoder, DownloadAndLoadGIMMVFIModel, WanVideoSEDecode, WanVideoBlockSwap, VHS_VideoCombine, GIMMVFI_interpolate, UpscaleImageWithModelIfNeed, VHS_VideoCombine, WanVideoTextEncode, UpscaleModelLoader, VHS_VideoCombine, WanVideoSESampler, WanVideoSEImageClipEncode, ImageResize+]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1动态壁纸首尾帧循环版_1914595453097209857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914595453097209857.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（23 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSEModelLoader`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `LoadWanVideoClipTextEncoder` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoSEDecode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `UpscaleImageWithModelIfNeed`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoSESampler` ★核心
- `WanVideoSEImageClipEncode`
- `ImageResize+`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSEModelLoader`、`WanVideoTorchCompileSettings`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`LoadWanVideoClipTextEncoder`、`DownloadAndLoadGIMMVFIModel`、`WanVideoSEDecode`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`UpscaleImageWithModelIfNeed`、`WanVideoTextEncode`、`UpscaleModelLoader`、`WanVideoSESampler`、`WanVideoSEImageClipEncode`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSESampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoTextEncode、WanVideoVAELoader、WanVideoSEDecode、WanVideoSEImageClipEncode
