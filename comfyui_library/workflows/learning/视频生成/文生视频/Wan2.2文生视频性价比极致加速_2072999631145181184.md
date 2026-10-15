---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速_2072999631145181184.json
name: Wan2.2文生视频性价比极致加速_2072999631145181184
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速_2072999631145181184.json
hash: 7dcca5e04e05da3c
coverage: 0.75
learned_at: 2026-10-15 22:47:16
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, PrimitiveNode, PrimitiveNode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetRadialAttention, WanVideoSetRadialAttention, PrimitiveNode, PrimitiveNode, WanVideoContextOptions, easy seed, PrimitiveNode, StringToFloatList, FloatToSigmas, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, easy globalSeed, WanVideoEmptyEmbeds, String Literal]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频性价比极致加速_2072999631145181184.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速_2072999631145181184.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（36 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetRadialAttention`
- `WanVideoSetRadialAttention`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoContextOptions`
- `easy seed`
- `PrimitiveNode`
- `StringToFloatList`
- `FloatToSigmas`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `WanVideoEmptyEmbeds`
- `String Literal`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetRadialAttention`、`WanVideoContextOptions`、`easy seed`、`StringToFloatList`、`FloatToSigmas`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`WanVideoEmptyEmbeds`、`String Literal`

**用到的条目**：WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
