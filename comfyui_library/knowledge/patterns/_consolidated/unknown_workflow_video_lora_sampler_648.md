---
name: unknown_workflow_video_lora_sampler_648
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.857
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, ImageFromBatch+, JWInteger, JWStringConcat, LayerColor: Brightness & Contrast, LoadWanVideoT5TextEncoder, MathExpression|pysssss, ShowText|pysssss, TextConcat, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1953073108568764418.json, 视频生成/文生视频/1955159900055900162.json, 视频生成/文生视频/1958344875328618498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_648

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1953073108568764418.json、视频生成/文生视频/1955159900055900162.json、视频生成/文生视频/1958344875328618498.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `ImageFromBatch+`
- `JWInteger`
- `JWStringConcat`
- `LayerColor: Brightness & Contrast`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `ShowText|pysssss`
- `TextConcat`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `JjkShowText` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RunningHub ThinkSound` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `String` —— 1/3 个有
- `easy mathInt` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
