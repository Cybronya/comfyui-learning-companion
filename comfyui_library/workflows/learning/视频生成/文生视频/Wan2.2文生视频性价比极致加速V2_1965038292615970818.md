---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json
name: Wan2.2文生视频性价比极致加速V2_1965038292615970818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json
hash: aad9b73e411a8b15
coverage: 0.735294
learned_at: 2026-10-10 23:07:59
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoContextOptions, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, easy globalSeed, WanVideoEmptyEmbeds, String Literal, PrimitiveNode, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, VHS_VideoCombine, WanVideoScheduler, easy seed]
patterns: []
missing: [String Literal, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **74%**（25/34）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetRadialAttention`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoEmptyEmbeds`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`VHS_VideoCombine`

**缺卡**（3）：`String Literal`、`easy globalSeed`、`easy seed`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、VHS_VideoCombine

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
