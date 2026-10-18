---
key: 视频生成/图生视频/🤖【Wan2.1视频】lightx2v 图生视频  超清加速版🤖_1935242546002198529.json
name: 🤖【Wan2.1视频】lightx2v 图生视频  超清加速版🤖_1935242546002198529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🤖【Wan2.1视频】lightx2v 图生视频  超清加速版🤖_1935242546002198529.json
hash: 01f7706e5dc9cd7f
coverage: 0.891892
learned_at: 2026-10-15 22:30:21
nodes: [GIMMVFI_interpolate, ImpactInt, WanVideoApplyNAG, WanVideoTextEncodeSingle, WanVideoClipVisionEncode, ImageResizeKJ, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, easy showAnything, UpscaleModelLoader, DownloadAndLoadGIMMVFIModel, ImageScaleToMegapixels, VHS_VideoCombine, PreviewImage, LoadImage, WanVideoVAELoader, WanVideoLoraSelect, CR Text, VHS_VideoCombine, Note, Seed (rgthree), LoadWanVideoT5TextEncoder, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoSampler, easy cleanGpuUsed, WanVideoDecode, SimpleMath+, WanVideoMagCache, WanVideoModelLoader, ImpactInt, ImpactInt, CLIPVisionLoader, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/🤖【Wan2.1视频】lightx2v 图生视频  超清加速版🤖_1935242546002198529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935242546002198529.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `GIMMVFI_interpolate`
- `ImpactInt`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `WanVideoClipVisionEncode`
- `ImageResizeKJ`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `easy showAnything`
- `UpscaleModelLoader`
- `DownloadAndLoadGIMMVFIModel`
- `ImageScaleToMegapixels`
- `VHS_VideoCombine`
- `PreviewImage`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `CR Text`
- `VHS_VideoCombine`
- `Note`
- `Seed (rgthree)`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `SimpleMath+`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `ImpactInt`
- `ImpactInt`
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`GIMMVFI_interpolate`、`ImpactInt`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`WanVideoClipVisionEncode`、`ImageResizeKJ`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoImageToVideoEncode`、`UpscaleModelLoader`、`DownloadAndLoadGIMMVFIModel`、`ImageScaleToMegapixels`、`VHS_VideoCombine`、`LoadImage`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`CR Text`、`Seed (rgthree)`、`LoadWanVideoT5TextEncoder`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`SimpleMath+`、`WanVideoMagCache`、`WanVideoModelLoader`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
