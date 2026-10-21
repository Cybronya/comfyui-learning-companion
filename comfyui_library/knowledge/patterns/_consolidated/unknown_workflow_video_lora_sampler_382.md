---
name: unknown_workflow_video_lora_sampler_382
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7465
common_nodes: [CR Text Replace, CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SimpleMath+, Text Multiline, Textbox, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy int, easy showAnything]
problems: []
missing: [CR Text Replace, MathExpression|pysssss, SimpleMath+, Text Multiline, easy int, easy imageSize]
members: [视频生成/图生视频/1956657065885143042.json, 视频生成/图生视频/1956615670723170306.json, 视频生成/图生视频/1959880278208622594.json, 视频生成/文生视频/1962918424819240961.json, 视频生成/文生视频/1957701596052385794.json, 视频生成/文生视频/1957729616544854018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_382

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1956657065885143042.json、视频生成/图生视频/1956615670723170306.json、视频生成/图生视频/1959880278208622594.json、视频生成/文生视频/1962918424819240961.json、视频生成/文生视频/1957701596052385794.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Text Replace`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `SimpleMath+`
- `Text Multiline`
- `Textbox`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `easy ifElse` —— 5/6 个有
- `EmptyImage` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `RHHiddenNodes` —— 3/6 个有
- `WanVideoEmptyEmbeds` —— 3/6 个有
- `WanVideoImageToVideoEncode` —— 3/6 个有
- `easy imageSize` —— 3/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Replace、MathExpression|pysssss、SimpleMath+、Text Multiline、easy int
