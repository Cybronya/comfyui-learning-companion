---
key: 图片生成/文生图/极速泼水变装特效可灵同款wan2.1+accvid_1930983914234687490.json
name: 极速泼水变装特效可灵同款wan2.1+accvid_1930983914234687490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/极速泼水变装特效可灵同款wan2.1+accvid_1930983914234687490.json
hash: 12934aebd5042cf8
coverage: 1
learned_at: 2026-10-15 22:28:54
nodes: [CR Text, LoadImage, WanVideoModelLoader, WanVideoTextEncode, Int, WanVideoVAELoader, easy cleanGpuUsed, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTorchCompileSettings, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, ImageSizeAndBatchSize, LoadWanVideoClipTextEncoder, WanVideoImageClipEncode, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSampler, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/文生图/极速泼水变装特效可灵同款wan2.1+accvid_1930983914234687490.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/极速泼水变装特效可灵同款wan2.1+accvid_1930983914234687490.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（22 个）：
- `CR Text`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `Int`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `ImageSizeAndBatchSize`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoImageClipEncode`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CR Text`、`LoadImage`、`WanVideoModelLoader`、`WanVideoTextEncode`、`Int`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`ImageSizeAndBatchSize`、`LoadWanVideoClipTextEncoder`、`WanVideoImageClipEncode`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
