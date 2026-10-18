---
key: 视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_2018170301388955650.json
name: 极速泼水变装特效可灵同款wan2.1+accvid_2018170301388955650.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_2018170301388955650.json
hash: bcb017b16788f687
coverage: 1
learned_at: 2026-10-15 22:34:53
nodes: [WanVideoTeaCache, WanVideoSLG, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoImageClipEncode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, ImageSizeAndBatchSize, MathExpression|pysssss, Int, Int, CR Text, WanVideoDecode, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_2018170301388955650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018170301388955650.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（24 个）：
- `WanVideoTeaCache`
- `WanVideoSLG`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageSizeAndBatchSize`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `CR Text`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `LoadImage`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`WanVideoTeaCache`、`WanVideoSLG`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoImageClipEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageSizeAndBatchSize`、`MathExpression|pysssss`、`Int`、`CR Text`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoSampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
