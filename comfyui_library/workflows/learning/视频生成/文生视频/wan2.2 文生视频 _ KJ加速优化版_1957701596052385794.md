---
key: 视频生成/文生视频/wan2.2 文生视频 _ KJ加速优化版_1957701596052385794.json
name: wan2.2 文生视频 _ KJ加速优化版_1957701596052385794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 文生视频 _ KJ加速优化版_1957701596052385794.json
hash: 802f613939bd5222
coverage: 0.853659
learned_at: 2026-10-15 22:47:34
nodes: [MarkdownNote, MarkdownNote, PrimitiveBoolean, CR Text Replace, RH_LLMAPI_NODE, Text Multiline, easy showAnything, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, SimpleMath+, WanVideoVAELoader, MathExpression|pysssss, INTConstant, WanVideoBlockSwap, WanVideoSampler, WanVideoSetLoRAs, PrimitiveNode, WanVideoSampler, WanVideoSetBlockSwap, easy int, easy int, VHS_VideoCombine, WanVideoDecode, Textbox, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy imageSize, EmptyImage, easy ifElse, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2 文生视频 _ KJ加速优化版_1957701596052385794.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 文生视频 _ KJ加速优化版_1957701596052385794.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `MarkdownNote`
- `MarkdownNote`
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
- `SimpleMath+`
- `WanVideoVAELoader`
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
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy imageSize`
- `EmptyImage`
- `easy ifElse`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MarkdownNote`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`PrimitiveBoolean`、`CR Text Replace`、`RH_LLMAPI_NODE`、`Text Multiline`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`WanVideoVAELoader`、`MathExpression|pysssss`、`INTConstant`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`easy int`、`VHS_VideoCombine`、`WanVideoDecode`、`Textbox`、`WanVideoEmptyEmbeds`、`easy imageSize`、`EmptyImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
