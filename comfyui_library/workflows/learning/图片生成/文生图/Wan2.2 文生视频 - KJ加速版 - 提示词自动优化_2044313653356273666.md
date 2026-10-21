---
key: 图片生成/文生图/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_2044313653356273666.json
name: Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_2044313653356273666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_2044313653356273666.json
hash: 846afa5aa5df621d
coverage: 0.886364
learned_at: 2026-10-21 02:55:24
nodes: [PrimitiveBoolean, Note, DF_Integer, Note, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoVAELoader, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoTextEncode, MathExpression|pysssss, INTConstant, SimpleMath+, easy int, PrimitiveNode, WanVideoDecode, GetImageSizeAndCount, easy ifElse, CR Text Concatenate, RH_Prompter, ShowText|pysssss, RH_Translator, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, JWInteger, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CR Text, Text Multiline]
patterns: []
missing: []
---

# 图片生成/文生图/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_2044313653356273666.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_2044313653356273666.json`

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
- `CR Text`
- `Text Multiline`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`PrimitiveBoolean`、`DF_Integer`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`MathExpression|pysssss`、`INTConstant`、`SimpleMath+`、`easy int`、`WanVideoDecode`、`GetImageSizeAndCount`、`CR Text Concatenate`、`RH_Prompter`、`RH_Translator`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`JWInteger`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`CR Text`、`Text Multiline`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
