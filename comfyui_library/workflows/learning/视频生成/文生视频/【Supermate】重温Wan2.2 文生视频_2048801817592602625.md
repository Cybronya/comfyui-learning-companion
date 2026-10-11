---
key: 视频生成/文生视频/【Supermate】重温Wan2.2 文生视频_2048801817592602625.json
name: 【Supermate】重温Wan2.2 文生视频_2048801817592602625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【Supermate】重温Wan2.2 文生视频_2048801817592602625.json
hash: 52a22984cf2d38c0
coverage: 0.722222
learned_at: 2026-10-11 19:49:45
nodes: [Note, CreateCFGScheduleFloatList, easy int, PrimitiveNode, RH_Translator, VHS_VideoCombine, DF_Integer, JWInteger, JWInteger, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoDecode, WanVideoTextEncode, LoadWanVideoT5TextEncoder, MathExpression|pysssss, INTConstant, SimpleMath+, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Text Multiline, WanVideoVAELoader, WanVideoSampler, WanVideoSampler]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, Text Multiline, easy int]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/【Supermate】重温Wan2.2 文生视频_2048801817592602625.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【Supermate】重温Wan2.2 文生视频_2048801817592602625.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `Note`
- `CreateCFGScheduleFloatList`
- `easy int`
- `PrimitiveNode`
- `RH_Translator`
- `VHS_VideoCombine`
- `DF_Integer`
- `JWInteger`
- `JWInteger`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `INTConstant`
- `SimpleMath+`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Text Multiline`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心

## 知识

覆盖率 **72%**（26/36）

**有卡**：`CreateCFGScheduleFloatList`、`RH_Translator`、`VHS_VideoCombine`、`DF_Integer`、`JWInteger`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoDecode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoSampler`

**缺卡**（8）：`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`Text Multiline`、`easy int`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
