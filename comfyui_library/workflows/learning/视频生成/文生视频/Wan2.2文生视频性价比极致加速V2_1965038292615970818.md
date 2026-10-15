---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json
name: Wan2.2文生视频性价比极致加速V2_1965038292615970818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json
hash: aad9b73e411a8b15
coverage: 0.823529
learned_at: 2026-10-15 22:47:15
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoContextOptions, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, easy globalSeed, WanVideoEmptyEmbeds, String Literal, PrimitiveNode, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, VHS_VideoCombine, WanVideoScheduler, easy seed]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（34 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
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
- `WanVideoContextOptions`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `WanVideoEmptyEmbeds`
- `String Literal`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `VHS_VideoCombine`
- `WanVideoScheduler`
- `easy seed`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetRadialAttention`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`WanVideoEmptyEmbeds`、`String Literal`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`VHS_VideoCombine`、`easy seed`

**用到的条目**：WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
