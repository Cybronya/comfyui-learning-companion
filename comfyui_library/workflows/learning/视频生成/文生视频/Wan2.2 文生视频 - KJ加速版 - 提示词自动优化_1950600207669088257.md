---
key: 视频生成/文生视频/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257.json
name: Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257.json
hash: c745a11d7a6b600f
coverage: 0.659091
learned_at: 2026-10-10 23:07:02
nodes: [PrimitiveBoolean, Note, DF_Integer, Note, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoVAELoader, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoTextEncode, MathExpression|pysssss, INTConstant, SimpleMath+, easy int, PrimitiveNode, WanVideoDecode, GetImageSizeAndCount, easy ifElse, CR Text, CR Text Concatenate, RH_Prompter, ShowText|pysssss, RH_Translator, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, JWInteger, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, Text Multiline]
patterns: []
missing: [CR Text, CR Text Concatenate, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, Text Multiline, easy int]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
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

覆盖率 **66%**（29/44）

**有卡**：`PrimitiveBoolean`、`DF_Integer`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`INTConstant`、`WanVideoDecode`、`GetImageSizeAndCount`、`RH_Prompter`、`RH_Translator`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`JWInteger`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`

**缺卡**（10）：`CR Text`、`CR Text Concatenate`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`Text Multiline`、`easy int`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
