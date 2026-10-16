---
key: 视频生成/图生视频/Wan2.1文生视频fusionX+NAG_1936289706663399425.json
name: Wan2.1文生视频fusionX+NAG_1936289706663399425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1936289706663399425.json
hash: 772447b067fa329b
coverage: 0.95
learned_at: 2026-10-15 22:30:25
nodes: [WanVideoDecode, WanVideoSampler, VHS_VideoCombine, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoSLG, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, UpscaleModelLoader, ImageUpscaleWithModel, easy clearCacheAll, easy cleanGpuUsed, MarkdownNote, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoApplyNAG, WanVideoEmptyEmbeds, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1文生视频fusionX+NAG_1936289706663399425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936289706663399425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（20 个）：
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTextEncodeSingle`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`easy clearCacheAll`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader
