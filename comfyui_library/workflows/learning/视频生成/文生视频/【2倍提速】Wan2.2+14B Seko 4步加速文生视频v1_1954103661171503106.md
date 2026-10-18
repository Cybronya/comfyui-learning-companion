---
key: 视频生成/文生视频/【2倍提速】Wan2.2+14B Seko 4步加速文生视频v1_1954103661171503106.json
name: 【2倍提速】Wan2.2+14B Seko 4步加速文生视频v1_1954103661171503106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【2倍提速】Wan2.2+14B Seko 4步加速文生视频v1_1954103661171503106.json
hash: 8b77d40e4ccceb4b
coverage: 0.75
learned_at: 2026-10-15 22:43:39
nodes: [JWInteger, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, MathExpression|pysssss, MathExpression|pysssss, WanVideoTextEncode, RH_LLMAPI_NODE, Text Concatenate, Wan22PromptSelector, ImpactSwitch, WanVideoEmptyEmbeds, FloatToSigmas, Note, StringToFloatList, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, SetNode, SetNode, WanVideoSampler, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, JWInteger, GetNode, WanVideoSampler, easy showAnything, WanVideoDecode, CreateVideo, CR Text, GetNode, GetNode, Primitive integer [Crystools], GetNode, JWInteger, JWInteger, PreViewVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/【2倍提速】Wan2.2+14B Seko 4步加速文生视频v1_1954103661171503106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1954103661171503106.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（44 个）：
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoTextEncode`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `Wan22PromptSelector`
- `ImpactSwitch`
- `WanVideoEmptyEmbeds`
- `FloatToSigmas`
- `Note`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `SetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `JWInteger`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `WanVideoDecode`
- `CreateVideo`
- `CR Text`
- `GetNode`
- `GetNode`
- `Primitive integer [Crystools]`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `PreViewVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（33/44）

**有卡**：`JWInteger`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`WanVideoTextEncode`、`RH_LLMAPI_NODE`、`Text Concatenate`、`Wan22PromptSelector`、`WanVideoEmptyEmbeds`、`FloatToSigmas`、`StringToFloatList`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`CreateVideo`、`CR Text`、`Primitive integer [Crystools]`、`PreViewVideo`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、Wan22PromptSelector
