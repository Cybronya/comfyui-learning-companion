---
key: 视频生成/文生视频/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257.json
name: Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257.json
hash: c745a11d7a6b600f
coverage: 0.886364
learned_at: 2026-10-15 22:47:11
nodes: [PrimitiveBoolean, Note, DF_Integer, Note, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoVAELoader, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoTextEncode, MathExpression|pysssss, INTConstant, SimpleMath+, easy int, PrimitiveNode, WanVideoDecode, GetImageSizeAndCount, easy ifElse, CR Text, CR Text Concatenate, RH_Prompter, ShowText|pysssss, RH_Translator, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, JWInteger, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, Text Multiline]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `PrimitiveBoolean`
- `Note`
- `DF_Integer`
- `Note`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `MathExpression|pysssss`
- `INTConstant`
- `SimpleMath+`
- `easy int`
- `PrimitiveNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `easy ifElse`
- `CR Text`
- `CR Text Concatenate`
- `RH_Prompter`
- `ShowText|pysssss`
- `RH_Translator`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`PrimitiveBoolean`、`DF_Integer`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`MathExpression|pysssss`、`INTConstant`、`SimpleMath+`、`easy int`、`WanVideoDecode`、`GetImageSizeAndCount`、`CR Text`、`CR Text Concatenate`、`RH_Prompter`、`RH_Translator`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`JWInteger`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`Text Multiline`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
