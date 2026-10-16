---
key: 视频生成/图生视频/wan2.1 + ani全能视频S 动漫版图生视频工作流_1945723173868359681.json
name: wan2.1 + ani全能视频S 动漫版图生视频工作流_1945723173868359681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1945723173868359681.json
hash: e200503395e81221
coverage: 0.954545
learned_at: 2026-10-15 22:30:42
nodes: [WanVideoDecode, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoVAELoader, ImageResizeKJ, ImageScaleToMegapixels, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, UpscaleModelLoader, WanVideoEnhanceAVideo, PreviewImage, WanVideoModelLoader, WanVideoTextEncode, ImageSmartSharpen+, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoSampler, VHS_VideoCombine, WanVideoLoraSelect, LoadImage, RH_Translator]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 + ani全能视频S 动漫版图生视频工作流_1945723173868359681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1945723173868359681.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（22 个）：
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `ImageScaleToMegapixels`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoBlockSwap`
- `UpscaleModelLoader`
- `WanVideoEnhanceAVideo`
- `PreviewImage`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `ImageSmartSharpen+`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `LoadImage`
- `RH_Translator`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`WanVideoDecode`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImageResizeKJ`、`ImageScaleToMegapixels`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`UpscaleModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`WanVideoTextEncode`、`ImageSmartSharpen+`、`WanVideoImageToVideoEncode`、`WanVideoSLG`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`LoadImage`、`RH_Translator`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
