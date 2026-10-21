---
name: unknown_workflow_video_lora_sampler_705
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.782333
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1951972629169295361.json, 视频生成/文生视频/1950555101742223362.json, 视频生成/文生视频/1950435690355015681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_705

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1951972629169295361.json、视频生成/文生视频/1950555101742223362.json、视频生成/文生视频/1950435690355015681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `Wan22PromptSelector` —— 2/3 个有
- `ImpactSwitch` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
