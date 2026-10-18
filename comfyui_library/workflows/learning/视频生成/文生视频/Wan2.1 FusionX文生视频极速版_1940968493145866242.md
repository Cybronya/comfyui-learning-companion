---
key: 视频生成/文生视频/Wan2.1 FusionX文生视频极速版_1940968493145866242.json
name: Wan2.1 FusionX文生视频极速版_1940968493145866242.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 FusionX文生视频极速版_1940968493145866242.json
hash: 966d3276b17e565f
coverage: 0.944444
learned_at: 2026-10-15 22:43:30
nodes: [WanVideoSLG, LoadWanVideoT5TextEncoder, DownloadAndLoadGIMMVFIModel, WanVideoDecode, GIMMVFI_interpolate, WanVideoBlockSwap, ImageScaleToMegapixels, Fast Groups Bypasser (rgthree), VHS_VideoCombine, UpscaleModelLoader, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoVAELoader, WanVideoModelLoader, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoEmptyEmbeds, WanVideoTextEncodeSingle]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 FusionX文生视频极速版_1940968493145866242.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1940968493145866242.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（18 个）：
- `WanVideoSLG`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `WanVideoBlockSwap`
- `ImageScaleToMegapixels`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncodeSingle`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`WanVideoSLG`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadGIMMVFIModel`、`WanVideoDecode`、`GIMMVFI_interpolate`、`WanVideoBlockSwap`、`ImageScaleToMegapixels`、`VHS_VideoCombine`、`UpscaleModelLoader`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、UpscaleModelLoader、UpscaleModelLoader、VHS_VideoCombine
