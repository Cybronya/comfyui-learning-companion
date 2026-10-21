---
name: unknown_workflow_video_sampler_vae_111
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6198
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImpactFloat, MathExpression|pysssss, PrimitiveFloat, SetNode, StringFunction|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEncodeCached, WanVideoVAELoader, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: [MathExpression|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy positive, easy imageSize, easy seed]
members: [视频生成/图生视频/1973048740976136194.json, 视频生成/图生视频/1983039998909906946.json, 视频生成/文生视频/1972719438250332161.json, 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json, 视频生成/文生视频/2066055962227961856.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_111

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1973048740976136194.json、视频生成/图生视频/1983039998909906946.json、视频生成/文生视频/1972719438250332161.json、视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json、视频生成/文生视频/2066055962227961856.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImpactFloat`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `SetNode`
- `StringFunction|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSigmaToStep`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelectMulti` —— 4/5 个有
- `EmptyImage` —— 3/5 个有
- `QwenLoader` —— 3/5 个有
- `WanVideoEmptyEmbeds` —— 3/5 个有
- `WanVideoLoraSelect` —— 3/5 个有
- `WanVideoPromptExtender` —— 3/5 个有
- `ImageFromBatch` —— 2/5 个有
- `ImageLoader` —— 2/5 个有
- `ImageResizeKJ` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `MemoryCleaner` —— 2/5 个有
- `MultiplePathsInput` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `WanVideoImageToVideoEncode` —— 2/5 个有
- `WanVideoSetLoRAs` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、StringFunction|pysssss、easy anythingIndexSwitch、easy int、easy positive
