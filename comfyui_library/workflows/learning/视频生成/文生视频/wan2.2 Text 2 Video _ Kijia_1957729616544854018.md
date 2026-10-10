---
key: 视频生成/文生视频/wan2.2 Text 2 Video _ Kijia_1957729616544854018.json
name: wan2.2 Text 2 Video _ Kijia_1957729616544854018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 Text 2 Video _ Kijia_1957729616544854018.json
hash: 42f283f67d0befc9
coverage: 0.585366
learned_at: 2026-10-10 23:09:34
nodes: [PrimitiveBoolean, CR Text Replace, RH_LLMAPI_NODE, Text Multiline, easy showAnything, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, MathExpression|pysssss, INTConstant, WanVideoBlockSwap, WanVideoSampler, WanVideoSetLoRAs, PrimitiveNode, WanVideoSampler, WanVideoSetBlockSwap, easy int, easy int, VHS_VideoCombine, WanVideoDecode, Textbox, MarkdownNote, MarkdownNote, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, EmptyImage, SimpleMath+, WanVideoVAELoader, easy imageSize, MathExpression|pysssss, WanVideoEmptyEmbeds, easy ifElse, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, MarkdownNote]
patterns: []
missing: [CR Text Replace, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, Text Multiline, easy int, easy int, easy imageSize]
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2 Text 2 Video _ Kijia_1957729616544854018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 Text 2 Video _ Kijia_1957729616544854018.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `PrimitiveBoolean`
- `CR Text Replace`
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `easy showAnything`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `Textbox`
- `MarkdownNote`
- `MarkdownNote`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `EmptyImage`
- `SimpleMath+`
- `WanVideoVAELoader`
- `easy imageSize`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `easy ifElse`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MarkdownNote`

## 知识

覆盖率 **59%**（24/41）

**有卡**：`PrimitiveBoolean`、`RH_LLMAPI_NODE`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`VHS_VideoCombine`、`WanVideoDecode`、`Textbox`、`EmptyImage`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**缺卡**（11）：`CR Text Replace`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`Text Multiline`、`easy int`、`easy int`、`easy imageSize`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
