---
key: 视频生成/图生视频/wan2.1 720p图生视频fusionX+NAG，上传图片点击运行工作流即可！_2046787167770382338.json
name: wan2.1 720p图生视频fusionX+NAG，上传图片点击运行工作流即可！_2046787167770382338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046787167770382338.json
hash: 3e15f4d962d4205e
coverage: 0.954545
learned_at: 2026-10-15 22:37:00
nodes: [DownloadAndLoadGIMMVFIModel, ImageSmartSharpen+, GIMMVFI_interpolate, UpscaleModelLoader, ImageScaleToMegapixels, WanVideoDecode, VHS_VideoCombine, ImageResizeKJ, WanVideoImageToVideoEncode, WanVideoTextEncodeSingle, WanVideoVAELoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoEnhanceAVideo, WanVideoSLG, PreviewImage, VHS_VideoCombine, WanVideoSampler, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 720p图生视频fusionX+NAG，上传图片点击运行工作流即可！_2046787167770382338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046787167770382338.json`

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
- `WanVideoSampler` ★核心
- `LoadImage`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`ImageSmartSharpen+`、`GIMMVFI_interpolate`、`UpscaleModelLoader`、`ImageScaleToMegapixels`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`WanVideoTextEncodeSingle`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoApplyNAG`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoSampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、UpscaleModelLoader
