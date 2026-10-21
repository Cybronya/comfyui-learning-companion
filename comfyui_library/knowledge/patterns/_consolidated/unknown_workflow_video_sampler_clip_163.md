---
name: unknown_workflow_video_sampler_clip_163
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.611667
common_nodes: [CLIPTextEncode, CR Text, CheckpointLoaderSimple, ImageFromBatch+, ImageResizeKJ, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, RH_LLMAPI_NODE, Text Concatenate, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Text Concatenate]
members: [视频生成/图生视频/2005508507405348866.json, 视频生成/图生视频/1975577828731301889.json, 视频生成/文生视频/1975577828731301889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2005508507405348866.json、视频生成/图生视频/1975577828731301889.json、视频生成/文生视频/1975577828731301889.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `Mute / Bypass Relay (rgthree)` —— 2/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `Wan22PromptSelector` —— 2/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、ImageFromBatch+、LayerUtility: ImageScaleByAspectRatio V2、MathExpression|pysssss、Mute / Bypass Relay (rgthree)
