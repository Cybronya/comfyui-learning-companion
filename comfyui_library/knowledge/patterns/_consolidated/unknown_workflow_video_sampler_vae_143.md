---
name: unknown_workflow_video_sampler_vae_143
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6535
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImpactFloat, MathExpression|pysssss, PrimitiveFloat, SetNode, StringFunction|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEncodeCached, WanVideoVAELoader, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-KJ_1973048740976136194.json, 视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-smoothMix-KJ_1983039998909906946.json, 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json, 视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_143

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-KJ_1973048740976136194.json、视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-smoothMix-KJ_1983039998909906946.json、视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json、视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WanVideoLoraSelectMulti` —— 3/4 个有
- `EmptyImage` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `ImageLoader` —— 2/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `MemoryCleaner` —— 2/4 个有
- `MultiplePathsInput` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `QwenLoader` —— 2/4 个有
- `WanVideoEmptyEmbeds` —— 2/4 个有
- `WanVideoImageToVideoEncode` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoPromptExtender` —— 2/4 个有
- `WanVideoSetLoRAs` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
