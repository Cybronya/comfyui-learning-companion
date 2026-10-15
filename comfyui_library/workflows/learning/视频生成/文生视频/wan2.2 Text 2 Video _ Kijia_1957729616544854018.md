---
key: 视频生成/文生视频/wan2.2 Text 2 Video _ Kijia_1957729616544854018.json
name: wan2.2 Text 2 Video _ Kijia_1957729616544854018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 Text 2 Video _ Kijia_1957729616544854018.json
hash: 42f283f67d0befc9
coverage: 0.853659
learned_at: 2026-10-15 22:47:34
nodes: [PrimitiveBoolean, CR Text Replace, RH_LLMAPI_NODE, Text Multiline, easy showAnything, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, MathExpression|pysssss, INTConstant, WanVideoBlockSwap, WanVideoSampler, WanVideoSetLoRAs, PrimitiveNode, WanVideoSampler, WanVideoSetBlockSwap, easy int, easy int, VHS_VideoCombine, WanVideoDecode, Textbox, MarkdownNote, MarkdownNote, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, EmptyImage, SimpleMath+, WanVideoVAELoader, easy imageSize, MathExpression|pysssss, WanVideoEmptyEmbeds, easy ifElse, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, MarkdownNote]
patterns: []
missing: []
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

覆盖率 **85%**（35/41）

**有卡**：`PrimitiveBoolean`、`CR Text Replace`、`RH_LLMAPI_NODE`、`Text Multiline`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`INTConstant`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`easy int`、`VHS_VideoCombine`、`WanVideoDecode`、`Textbox`、`EmptyImage`、`SimpleMath+`、`WanVideoVAELoader`、`easy imageSize`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
