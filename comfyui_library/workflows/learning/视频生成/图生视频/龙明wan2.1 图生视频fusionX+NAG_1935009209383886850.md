---
key: 视频生成/图生视频/龙明wan2.1 图生视频fusionX+NAG_1935009209383886850.json
name: 龙明wan2.1 图生视频fusionX+NAG_1935009209383886850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935009209383886850.json
hash: 7a207332cf300a05
coverage: 0.954545
learned_at: 2026-10-15 22:30:20
nodes: [DownloadAndLoadGIMMVFIModel, ImageSmartSharpen+, GIMMVFI_interpolate, UpscaleModelLoader, ImageScaleToMegapixels, WanVideoDecode, VHS_VideoCombine, ImageResizeKJ, WanVideoImageToVideoEncode, WanVideoTextEncodeSingle, WanVideoVAELoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoEnhanceAVideo, WanVideoSLG, PreviewImage, VHS_VideoCombine, LoadImage, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/龙明wan2.1 图生视频fusionX+NAG_1935009209383886850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935009209383886850.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（22 个）：
- `DownloadAndLoadGIMMVFIModel`
- `ImageSmartSharpen+`
- `GIMMVFI_interpolate`
- `UpscaleModelLoader`
- `ImageScaleToMegapixels`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `PreviewImage`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **95%**（21/22）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`ImageSmartSharpen+`、`GIMMVFI_interpolate`、`UpscaleModelLoader`、`ImageScaleToMegapixels`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`WanVideoTextEncodeSingle`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoApplyNAG`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`LoadImage`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、UpscaleModelLoader
