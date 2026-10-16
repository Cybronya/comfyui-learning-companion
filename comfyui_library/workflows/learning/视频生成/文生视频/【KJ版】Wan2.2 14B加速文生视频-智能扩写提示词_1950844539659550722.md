---
key: 视频生成/文生视频/【KJ版】Wan2.2 14B加速文生视频-智能扩写提示词_1950844539659550722.json
name: 【KJ版】Wan2.2 14B加速文生视频-智能扩写提示词_1950844539659550722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950844539659550722.json
hash: c0398444e08d6b7c
coverage: 0.75
learned_at: 2026-10-15 22:43:37
nodes: [JWInteger, JWInteger, JWInteger, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, SetNode, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, GetNode, GetNode, CreateCFGScheduleFloatList, MathExpression|pysssss, GetNode, MathExpression|pysssss, Primitive integer [Crystools], GetNode, JWInteger, WanVideoTextEncode, WanVideoDecode, RH_LLMAPI_NODE, Text Concatenate, CR Text, Wan22PromptSelector, ImpactSwitch, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoVAELoader, SetNode, SetNode, easy showAnything, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/【KJ版】Wan2.2 14B加速文生视频-智能扩写提示词_1950844539659550722.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950844539659550722.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（40 个）：
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
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
- `CreateCFGScheduleFloatList`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `GetNode`
- `JWInteger`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `CR Text`
- `Wan22PromptSelector`
- `ImpactSwitch`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（30/40）

**有卡**：`JWInteger`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`WanVideoTextEncode`、`WanVideoDecode`、`RH_LLMAPI_NODE`、`Text Concatenate`、`CR Text`、`Wan22PromptSelector`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
