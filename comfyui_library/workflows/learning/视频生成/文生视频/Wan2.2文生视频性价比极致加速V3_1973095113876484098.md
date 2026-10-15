---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速V3_1973095113876484098.json
name: Wan2.2文生视频性价比极致加速V3_1973095113876484098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V3_1973095113876484098.json
hash: c527e9319ff1c8cd
coverage: 0.818182
learned_at: 2026-10-15 22:47:15
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoScheduler, PrimitiveNode, PrimitiveNode, easy seed, WanVideoScheduler, easy globalSeed, WanVideoVACEEncode, easy int, easy int, easy int, easy float, easy float, String Literal, VHS_VideoCombine, easy float, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Note, PrimitiveNode, WanVideoSigmaToStep]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频性价比极致加速V3_1973095113876484098.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V3_1973095113876484098.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（44 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetRadialAttention`
- `WanVideoSetRadialAttention`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoScheduler`
- `PrimitiveNode`
- `PrimitiveNode`
- `easy seed`
- `WanVideoScheduler`
- `easy globalSeed`
- `WanVideoVACEEncode`
- `easy int`
- `easy int`
- `easy int`
- `easy float`
- `easy float`
- `String Literal`
- `VHS_VideoCombine`
- `easy float`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Note`
- `PrimitiveNode`
- `WanVideoSigmaToStep`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoScheduler`、`easy seed`、`easy globalSeed`、`WanVideoVACEEncode`、`easy int`、`easy float`、`String Literal`、`VHS_VideoCombine`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSigmaToStep`

**用到的条目**：WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
