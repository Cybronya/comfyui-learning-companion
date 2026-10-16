---
key: 视频生成/图生视频/wan2.2图生视频加速优化_1959880278208622594.json
name: wan2.2图生视频加速优化_1959880278208622594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1959880278208622594.json
hash: bf634d5eaa00a70d
coverage: 0.809524
learned_at: 2026-10-15 22:31:25
nodes: [WanVideoSetBlockSwap, MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveBoolean, CR Text Replace, RH_LLMAPI_NODE, Text Multiline, easy showAnything, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, SimpleMath+, WanVideoVAELoader, WanVideoImageToVideoEncode, MathExpression|pysssss, INTConstant, WanVideoBlockSwap, WanVideoSampler, WanVideoSetLoRAs, PrimitiveNode, WanVideoSampler, WanVideoLoraSelect, WanVideoSetBlockSwap, easy int, easy int, VHS_VideoCombine, WanVideoDecode, MarkdownNote, easy ifElse, Textbox, RHHiddenNodes, easy ifElse, easy showAnything, LoadImage, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频加速优化_1959880278208622594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1959880278208622594.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoSetBlockSwap`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `CR Text Replace`
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `MathExpression|pysssss`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `MarkdownNote`
- `easy ifElse`
- `Textbox`
- `RHHiddenNodes`
- `easy ifElse`
- `easy showAnything`
- `LoadImage`
- `easy int`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`WanVideoSetBlockSwap`、`PrimitiveBoolean`、`CR Text Replace`、`RH_LLMAPI_NODE`、`Text Multiline`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`MathExpression|pysssss`、`INTConstant`、`WanVideoSampler`、`easy int`、`VHS_VideoCombine`、`WanVideoDecode`、`Textbox`、`RHHiddenNodes`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
