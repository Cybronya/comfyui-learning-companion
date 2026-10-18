---
key: 视频生成/图生视频/通义万相wan2.1万物旋转360度特效_1901238900759609346.json
name: 通义万相wan2.1万物旋转360度特效_1901238900759609346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相wan2.1万物旋转360度特效_1901238900759609346.json
hash: dbd9d5ca35e43250
coverage: 1
learned_at: 2026-10-15 22:29:23
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoEnhanceAVideo, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, LoadImage, WanVideoLoraSelect, ImageResizeKJ, WanVideoVAELoader, WanVideoImageClipEncode, WanVideoTextEncode, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, CR Upscale Image, WanVideoDecode, LayerUtility: PurgeVRAM, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoTeaCache]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.1万物旋转360度特效_1901238900759609346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901238900759609346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（20 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `LoadImage`
- `WanVideoLoraSelect`
- `ImageResizeKJ`
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `CR Upscale Image`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`LoadImage`、`WanVideoLoraSelect`、`ImageResizeKJ`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`CR Upscale Image`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoTeaCache`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
