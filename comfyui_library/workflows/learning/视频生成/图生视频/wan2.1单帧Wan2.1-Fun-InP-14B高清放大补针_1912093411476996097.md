---
key: 视频生成/图生视频/wan2.1单帧Wan2.1-Fun-InP-14B高清放大补针_1912093411476996097.json
name: wan2.1单帧Wan2.1-Fun-InP-14B高清放大补针_1912093411476996097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1912093411476996097.json
hash: 8e21b614a9272925
coverage: 1
learned_at: 2026-10-15 22:29:32
nodes: [WanVideoClipVisionEncode, WanVideoSampler, ImageResizeKJ, VHS_VideoCombine, WanVideoBlockSwap, WanVideoImageToVideoEncode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoDecode, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, UpscaleModelLoader, Get resolution [Crystools], VHS_VideoCombine, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoExperimentalArgs, WanVideoSLG, WanVideoTeaCache, WanVideoTextEncode, VHS_VideoCombine, ImageResizeKJ, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1单帧Wan2.1-Fun-InP-14B高清放大补针_1912093411476996097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912093411476996097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoDecode`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `UpscaleModelLoader`
- `Get resolution [Crystools]`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `LoadImage`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoSampler`、`ImageResizeKJ`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoDecode`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM`、`UpscaleModelLoader`、`Get resolution [Crystools]`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
