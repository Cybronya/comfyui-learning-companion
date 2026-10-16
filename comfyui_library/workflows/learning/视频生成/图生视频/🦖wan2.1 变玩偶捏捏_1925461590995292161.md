---
key: 视频生成/图生视频/🦖wan2.1 变玩偶捏捏_1925461590995292161.json
name: 🦖wan2.1 变玩偶捏捏_1925461590995292161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1925461590995292161.json
hash: 7095b4fe28534864
coverage: 1
learned_at: 2026-10-15 22:29:52
nodes: [LayerUtility: PurgeVRAM, WanVideoTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoTextEncode, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoImageClipEncode, LoadWanVideoClipTextEncoder, GetImageRangeFromBatch, WanVideoImageClipEncode, WanVideoSampler, WanVideoDecode, WanVideoDecode, Image Batch, VHS_VideoCombine, WanVideoVAELoader, WanVideoSampler, LoadImage, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/图生视频/🦖wan2.1 变玩偶捏捏_1925461590995292161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1925461590995292161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（29 个）：
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoImageClipEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `GetImageRangeFromBatch`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoDecode`
- `Image Batch`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoImageClipEncode`、`LoadWanVideoClipTextEncoder`、`GetImageRangeFromBatch`、`WanVideoSampler`、`WanVideoDecode`、`Image Batch`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
