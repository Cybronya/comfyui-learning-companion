---
key: 视频生成/文生视频/火力 全开！冲锋枪射击特效--万相WAN2.1_1934071211976478722.json
name: 火力 全开！冲锋枪射击特效--万相WAN2.1_1934071211976478722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1934071211976478722.json
hash: 10a656d58c6c4545
coverage: 1
learned_at: 2026-10-15 22:43:27
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoBlockSwap, WanVideoModelLoader, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, UpscaleModelLoader, LoadImage, WanVideoTextEncode, WanVideoSampler, WanVideoTeaCache, WanVideoImageClipEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/火力 全开！冲锋枪射击特效--万相WAN2.1_1934071211976478722.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1934071211976478722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（17 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `ImageUpscaleWithModel`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `UpscaleModelLoader`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `WanVideoImageClipEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`ImageUpscaleWithModel`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`UpscaleModelLoader`、`LoadImage`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoImageClipEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
