---
key: 视频生成/文生视频/Wan2.1文生视频fusionX+NAG+视频放大_1942109815802118145.json
name: Wan2.1文生视频fusionX+NAG+视频放大_1942109815802118145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1942109815802118145.json
hash: ec8b0bf2adf21dd4
coverage: 1
learned_at: 2026-10-15 22:43:30
nodes: [DownloadAndLoadGIMMVFIModel, WanVideoApplyNAG, WanVideoSLG, WanVideoVAELoader, WanVideoTextEncodeSingle, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoEnhanceAVideo, WanVideoModelLoader, VHS_VideoCombine, WanVideoDecode, ImageUpscaleWithModel, UpscaleModelLoader, RIFE VFI, VHS_VideoCombine, WanVideoEmptyEmbeds, GIMMVFI_interpolate]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1文生视频fusionX+NAG+视频放大_1942109815802118145.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1942109815802118145.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoApplyNAG`
- `WanVideoSLG`
- `WanVideoVAELoader`
- `WanVideoTextEncodeSingle`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeSingle`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `GIMMVFI_interpolate`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`WanVideoApplyNAG`、`WanVideoSLG`、`WanVideoVAELoader`、`WanVideoTextEncodeSingle`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`RIFE VFI`、`WanVideoEmptyEmbeds`、`GIMMVFI_interpolate`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader
