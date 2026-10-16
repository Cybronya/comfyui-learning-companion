---
key: 视频生成/文生视频/【KJ版】Wan2.2+14B 4步加速文生视频-智能扩写版_1953642911277744130.json
name: 【KJ版】Wan2.2+14B 4步加速文生视频-智能扩写版_1953642911277744130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1953642911277744130.json
hash: ef93d8e6d3cee9e4
coverage: 0.738095
learned_at: 2026-10-15 22:43:39
nodes: [JWInteger, JWInteger, JWInteger, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, SetNode, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, GetNode, GetNode, MathExpression|pysssss, GetNode, MathExpression|pysssss, GetNode, WanVideoTextEncode, RH_LLMAPI_NODE, Text Concatenate, Wan22PromptSelector, ImpactSwitch, WanVideoEmptyEmbeds, WanVideoVAELoader, SetNode, SetNode, easy showAnything, WanVideoLoraSelect, Primitive integer [Crystools], WanVideoDecode, FloatToSigmas, Note, VHS_VideoCombine, StringToFloatList, WanVideoLoraSelect, CR Text, WanVideoSampler, WanVideoSampler, JWInteger]
patterns: []
missing: []
---

# 视频生成/文生视频/【KJ版】Wan2.2+14B 4步加速文生视频-智能扩写版_1953642911277744130.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1953642911277744130.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（42 个）：
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `WanVideoTextEncode`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `Wan22PromptSelector`
- `ImpactSwitch`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `WanVideoLoraSelect`
- `Primitive integer [Crystools]`
- `WanVideoDecode`
- `FloatToSigmas`
- `Note`
- `VHS_VideoCombine`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `CR Text`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `JWInteger`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`JWInteger`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`WanVideoTextEncode`、`RH_LLMAPI_NODE`、`Text Concatenate`、`Wan22PromptSelector`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`Primitive integer [Crystools]`、`WanVideoDecode`、`FloatToSigmas`、`VHS_VideoCombine`、`StringToFloatList`、`CR Text`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、Wan22PromptSelector
