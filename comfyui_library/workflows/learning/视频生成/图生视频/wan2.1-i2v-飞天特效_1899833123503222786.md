---
key: 视频生成/图生视频/wan2.1-i2v-飞天特效_1899833123503222786.json
name: wan2.1-i2v-飞天特效_1899833123503222786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1-i2v-飞天特效_1899833123503222786.json
hash: 4c312e86404e7f9d
coverage: 1
learned_at: 2026-10-15 22:29:22
nodes: [WanVideoEnhanceAVideo, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, Upscale Model Loader, ImageUpscaleWithModel, WanVideoSampler, WanVideoDecode, WanVideoTextEncode, WanVideoImageClipEncode, LoadImage, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTeaCache, LoadWanVideoClipTextEncoder, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1-i2v-飞天特效_1899833123503222786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899833123503222786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（18 个）：
- `WanVideoEnhanceAVideo`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `Upscale Model Loader`
- `ImageUpscaleWithModel`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoImageClipEncode`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `LoadWanVideoClipTextEncoder` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`WanVideoEnhanceAVideo`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`Upscale Model Loader`、`ImageUpscaleWithModel`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoImageClipEncode`、`LoadImage`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`LoadWanVideoClipTextEncoder`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
