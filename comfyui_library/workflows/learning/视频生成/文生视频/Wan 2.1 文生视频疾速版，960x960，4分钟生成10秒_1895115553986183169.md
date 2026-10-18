---
key: 视频生成/文生视频/Wan 2.1 文生视频疾速版，960x960，4分钟生成10秒_1895115553986183169.json
name: Wan 2.1 文生视频疾速版，960x960，4分钟生成10秒_1895115553986183169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.1 文生视频疾速版，960x960，4分钟生成10秒_1895115553986183169.json
hash: 38ca4c7d639d2bef
coverage: 0.756757
learned_at: 2026-10-15 22:43:20
nodes: [SetNode, Int, SetNode, ConvertAny2Float, SetNode, WanVideoDecode, PlaySound|pysssss, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note Plus (mtb), VHS_VideoCombine, WanVideoTextEncode, WanVideoVAELoader, WanVideoContextOptions, ImageUpscaleWithModel, RIFE VFI, GetNode, easy cleanGpuUsed, VHS_VideoCombine, WanVideoModelLoader, Int, easy cleanGpuUsed, SeargePromptText, MathExpression|pysssss, SetNode, SetNode, Int, Int, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, GetNode, WanVideoEmptyEmbeds, WanVideoSampler, UpscaleModelLoader, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan 2.1 文生视频疾速版，960x960，4分钟生成10秒_1895115553986183169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1895115553986183169.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `SetNode`
- `Int`
- `SetNode`
- `ConvertAny2Float`
- `SetNode`
- `WanVideoDecode`
- `PlaySound|pysssss`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `GetNode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `Int`
- `easy cleanGpuUsed`
- `SeargePromptText`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `UpscaleModelLoader`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`Int`、`ConvertAny2Float`、`WanVideoDecode`、`PlaySound|pysssss`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Note Plus (mtb)`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoContextOptions`、`ImageUpscaleWithModel`、`RIFE VFI`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`SeargePromptText`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`UpscaleModelLoader`、`LoadWanVideoT5TextEncoder`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader
