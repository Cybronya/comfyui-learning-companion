---
key: 视频生成/文生视频/wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417.json
name: wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417.json
hash: ef5d2ec6c3fe3cab
coverage: 0.648649
learned_at: 2026-10-11 03:16:51
nodes: [GetNode, GetNode, WanVideoDecode, FloatToSigmas, WanVideoTextEncode, WanVideoSampler, MathExpression|pysssss, WanVideoSetBlockSwap, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoTorchCompileSettings, GetNode, GetNode, Primitive integer [Crystools], WanVideoContextOptions, WanVideoSampler, JWInteger, JWInteger, JWInteger, MathExpression|pysssss, WanVideoEmptyEmbeds, Note, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, CR Text, StringToFloatList, WanVideoBlockSwap]
patterns: []
missing: [CR Text, MathExpression|pysssss, MathExpression|pysssss, Primitive integer [Crystools]]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（37 个）：
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `FloatToSigmas`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `WanVideoSetBlockSwap`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `Primitive integer [Crystools]`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `Note`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `CR Text`
- `StringToFloatList`
- `WanVideoBlockSwap`

## 知识

覆盖率 **65%**（24/37）

**有卡**：`WanVideoDecode`、`FloatToSigmas`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`JWInteger`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`StringToFloatList`、`WanVideoBlockSwap`

**缺卡**（4）：`CR Text`、`MathExpression|pysssss`、`MathExpression|pysssss`、`Primitive integer [Crystools]`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、VHS_VideoCombine

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
