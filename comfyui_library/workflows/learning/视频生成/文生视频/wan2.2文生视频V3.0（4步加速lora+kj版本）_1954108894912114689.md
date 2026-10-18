---
key: 视频生成/文生视频/wan2.2文生视频V3.0（4步加速lora+kj版本）_1954108894912114689.json
name: wan2.2文生视频V3.0（4步加速lora+kj版本）_1954108894912114689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频V3.0（4步加速lora+kj版本）_1954108894912114689.json
hash: 841f7f7f0e681b7e
coverage: 0.736842
learned_at: 2026-10-15 22:43:39
nodes: [WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, MathExpression|pysssss, GetNode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, SetNode, SetNode, WanVideoTextEncode, SetNode, WanVideoDecode, FloatToSigmas, StringToFloatList, Note, GetNode, GetNode, VHS_VideoCombine, RH_LLMAPI_NODE, ShowText|pysssss, GetNode, Primitive integer [Crystools], MathExpression|pysssss, CR Text, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2文生视频V3.0（4步加速lora+kj版本）_1954108894912114689.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1954108894912114689.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `WanVideoTextEncode`
- `SetNode`
- `WanVideoDecode`
- `FloatToSigmas`
- `StringToFloatList`
- `Note`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `GetNode`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoDecode`、`FloatToSigmas`、`StringToFloatList`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`Primitive integer [Crystools]`、`CR Text`、`JWInteger`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、RH_LLMAPI_NODE
