---
key: 视频生成/图生视频/wan2.1-i2v-360度旋转_1899839551614115842.json
name: wan2.1-i2v-360度旋转_1899839551614115842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1899839551614115842.json
hash: dd23a4f9d669cd27
coverage: 1
learned_at: 2026-10-15 22:29:22
nodes: [WanVideoEnhanceAVideo, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, Upscale Model Loader, ImageUpscaleWithModel, WanVideoSampler, WanVideoDecode, LoadImage, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTeaCache, LoadWanVideoClipTextEncoder, WanVideoLoraSelect, WanVideoImageClipEncode, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1-i2v-360度旋转_1899839551614115842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899839551614115842.json`

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
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoLoraSelect`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`WanVideoEnhanceAVideo`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`Upscale Model Loader`、`ImageUpscaleWithModel`、`WanVideoSampler`、`WanVideoDecode`、`LoadImage`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`LoadWanVideoClipTextEncoder`、`WanVideoLoraSelect`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
