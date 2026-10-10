---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_1978410048823169026.json
name: Wan2.2文生视频性价比极致加速V5_1978410048823169026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_1978410048823169026.json
hash: 942df6ee7060d746
coverage: 0.638298
learned_at: 2026-10-10 23:08:03
nodes: [SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoScheduler, PrimitiveNode, PrimitiveNode, easy seed, WanVideoScheduler, easy globalSeed, WanVideoVACEEncode, easy int, VHS_VideoCombine, Note, PrimitiveNode, easy float, easy float, easy float, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEEncode, String Literal, easy int, easy int, WanVideoModelLoader]
patterns: []
missing: [String Literal, easy float, easy float, easy float, easy int, easy int, easy int, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_1978410048823169026.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_1978410048823169026.json`

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

覆盖率 **64%**（30/47）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoScheduler`、`WanVideoVACEEncode`、`VHS_VideoCombine`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`

**缺卡**（9）：`String Literal`、`easy float`、`easy float`、`easy float`、`easy int`、`easy int`、`easy int`、`easy globalSeed`、`easy seed`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
