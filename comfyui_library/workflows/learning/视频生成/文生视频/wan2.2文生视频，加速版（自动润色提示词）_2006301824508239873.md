---
key: 视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json
name: wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json
hash: 092e209da07413a3
coverage: 0.666667
learned_at: 2026-10-11 03:07:13
nodes: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, PrimitiveBoolean, RH_Translator, WanVideoBlockSwap, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoDecode, easy ifElse, CR Text, CR Text Concatenate, RH_Prompter, ShowText|pysssss, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, SimpleMath+, MathExpression|pysssss, INTConstant, GetImageSizeAndCount, RIFE VFI, WanVideoSampler, WanVideoTorchCompileSettings, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, PrimitiveNode, DF_Integer, JWInteger, JWInteger, easy int, Note, Text Multiline, WanVideoSampler]
patterns: []
missing: [CR Text, CR Text Concatenate, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, RIFE VFI, SimpleMath+, Text Multiline, easy int]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PrimitiveBoolean`
- `RH_Translator`
- `WanVideoBlockSwap`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `easy ifElse`
- `CR Text`
- `CR Text Concatenate`
- `RH_Prompter`
- `ShowText|pysssss`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `MathExpression|pysssss`
- `INTConstant`
- `GetImageSizeAndCount`
- `RIFE VFI`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `PrimitiveNode`
- `DF_Integer`
- `JWInteger`
- `JWInteger`
- `easy int`
- `Note`
- `Text Multiline`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **67%**（30/45）

**有卡**：`PrimitiveBoolean`、`RH_Translator`、`WanVideoBlockSwap`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoDecode`、`RH_Prompter`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`DF_Integer`、`JWInteger`

**缺卡**（11）：`CR Text`、`CR Text Concatenate`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`RIFE VFI`、`SimpleMath+`、`Text Multiline`、`easy int`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
