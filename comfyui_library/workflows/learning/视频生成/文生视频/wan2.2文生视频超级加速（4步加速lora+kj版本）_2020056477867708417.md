---
key: 视频生成/文生视频/wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417.json
name: wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频超级加速（4步加速lora+kj版本）_2020056477867708417.json
hash: ef5d2ec6c3fe3cab
coverage: 0.756757
learned_at: 2026-10-15 22:47:36
nodes: [GetNode, GetNode, WanVideoDecode, FloatToSigmas, WanVideoTextEncode, WanVideoSampler, MathExpression|pysssss, WanVideoSetBlockSwap, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoTorchCompileSettings, GetNode, GetNode, Primitive integer [Crystools], WanVideoContextOptions, WanVideoSampler, JWInteger, JWInteger, JWInteger, MathExpression|pysssss, WanVideoEmptyEmbeds, Note, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, CR Text, StringToFloatList, WanVideoBlockSwap]
patterns: []
missing: []
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

覆盖率 **76%**（28/37）

**有卡**：`WanVideoDecode`、`FloatToSigmas`、`WanVideoTextEncode`、`WanVideoSampler`、`MathExpression|pysssss`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`Primitive integer [Crystools]`、`WanVideoContextOptions`、`JWInteger`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`CR Text`、`StringToFloatList`、`WanVideoBlockSwap`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、VHS_VideoCombine
