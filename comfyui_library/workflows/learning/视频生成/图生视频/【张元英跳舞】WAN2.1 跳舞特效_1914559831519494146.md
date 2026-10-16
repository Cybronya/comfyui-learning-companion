---
key: 视频生成/图生视频/【张元英跳舞】WAN2.1 跳舞特效_1914559831519494146.json
name: 【张元英跳舞】WAN2.1 跳舞特效_1914559831519494146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1914559831519494146.json
hash: d2131dcd1fbac93e
coverage: 1
learned_at: 2026-10-15 22:29:36
nodes: [Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, WanVideoTeaCache, WanVideoBlockSwap, WanVideoSampler, WanVideoVAELoader, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, LoadImage, TextBox, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoDecode, WanVideoImageClipEncode, WanVideoTextEncode, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/【张元英跳舞】WAN2.1 跳舞特效_1914559831519494146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914559831519494146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（19 个）：
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `TextBox`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`TextBox`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
