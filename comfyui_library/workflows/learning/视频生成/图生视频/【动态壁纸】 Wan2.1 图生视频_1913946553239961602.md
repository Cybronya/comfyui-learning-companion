---
key: 视频生成/图生视频/【动态壁纸】 Wan2.1 图生视频_1913946553239961602.json
name: 【动态壁纸】 Wan2.1 图生视频_1913946553239961602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1913946553239961602.json
hash: c735da700190d4f2
coverage: 0.727273
learned_at: 2026-10-15 22:29:35
nodes: [Anything Everywhere, Anything Everywhere, WanVideoVAELoader, WanVideoBlockSwap, WanVideoDecode, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoTeaCache, GetNode, VHS_VideoCombine, LoadWanVideoClipTextEncoder, WanVideoLoraSelect, SetNode, WanVideoSampler, Florence2Run, StringFunction|pysssss, LayerUtility: PurgeVRAM V2, SetNode, MathExpression|pysssss, GetNode, WanVideoTorchCompileSettings, Anything Everywhere, LoadWanVideoT5TextEncoder, WanVideoTextEncode, Anything Everywhere, WanVideoImageClipEncode, WanVideoModelLoader, DownloadAndLoadFlorence2Model, Anything Everywhere, Seed Everywhere, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【动态壁纸】 Wan2.1 图生视频_1913946553239961602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1913946553239961602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（33 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `GetNode`
- `VHS_VideoCombine`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoSampler` ★核心
- `Florence2Run`
- `StringFunction|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `Anything Everywhere`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `DownloadAndLoadFlorence2Model`
- `Anything Everywhere`
- `Seed Everywhere`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 知识

覆盖率 **73%**（24/33）

**有卡**：`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`VHS_VideoCombine`、`LoadWanVideoClipTextEncoder`、`WanVideoLoraSelect`、`WanVideoSampler`、`Florence2Run`、`StringFunction|pysssss`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoImageClipEncode`、`WanVideoModelLoader`、`DownloadAndLoadFlorence2Model`、`Seed Everywhere`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、Seed Everywhere、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode
