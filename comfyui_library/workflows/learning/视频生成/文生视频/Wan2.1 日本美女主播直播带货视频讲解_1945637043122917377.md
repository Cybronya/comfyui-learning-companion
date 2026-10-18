---
key: 视频生成/文生视频/Wan2.1 日本美女主播直播带货视频讲解_1945637043122917377.json
name: Wan2.1 日本美女主播直播带货视频讲解_1945637043122917377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 日本美女主播直播带货视频讲解_1945637043122917377.json
hash: d3e1699e1dbcfd2c
coverage: 1
learned_at: 2026-10-15 22:43:31
nodes: [WanVideoSLG, LoadWanVideoT5TextEncoder, DownloadAndLoadGIMMVFIModel, WanVideoDecode, GIMMVFI_interpolate, WanVideoBlockSwap, ImageScaleToMegapixels, VHS_VideoCombine, UpscaleModelLoader, WanVideoEnhanceAVideo, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoVAELoader, WanVideoModelLoader, WanVideoTextEncodeSingle, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 日本美女主播直播带货视频讲解_1945637043122917377.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1945637043122917377.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoSLG`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `WanVideoBlockSwap`
- `ImageScaleToMegapixels`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeSingle`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`WanVideoSLG`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadGIMMVFIModel`、`WanVideoDecode`、`GIMMVFI_interpolate`、`WanVideoBlockSwap`、`ImageScaleToMegapixels`、`VHS_VideoCombine`、`UpscaleModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoLoraSelect、UpscaleModelLoader、UpscaleModelLoader
