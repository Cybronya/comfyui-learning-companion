---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_2072999498567426048.json
name: Wan2.2文生视频性价比极致加速V5_2072999498567426048
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_2072999498567426048.json
hash: 897de0ec0960e5c4
coverage: 0.829787
learned_at: 2026-10-15 22:47:16
nodes: [SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoScheduler, PrimitiveNode, PrimitiveNode, easy seed, WanVideoScheduler, easy globalSeed, WanVideoVACEEncode, easy int, VHS_VideoCombine, Note, PrimitiveNode, easy float, easy float, easy float, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEEncode, String Literal, easy int, easy int, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_2072999498567426048.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_2072999498567426048.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（47 个）：
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
- `VHS_VideoCombine`
- `Note`
- `PrimitiveNode`
- `easy float`
- `easy float`
- `easy float`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `String Literal`
- `easy int`
- `easy int`
- `WanVideoModelLoader`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoScheduler`、`easy seed`、`easy globalSeed`、`WanVideoVACEEncode`、`easy int`、`VHS_VideoCombine`、`easy float`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`String Literal`

**用到的条目**：WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
