---
name: unknown_workflow_sampler_clip_unet_24
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.921429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text, easy promptConcat, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1953747187043848193.json, 图片生成/文生图/1953757506445213698.json, 图片生成/文生图/1953758140024147969.json, 图片生成/文生图/1953813624924110849.json, 图片生成/文生图/1953815517956112386.json, 图片生成/文生图/1954027659858890754.json, 图片生成/文生图/1954190525895196674.json, 图片生成/文生图/1954435913382281217.json, 图片生成/文生图/1954444879856332802.json, 图片生成/文生图/1954589330377469954.json, 图片生成/文生图/1954593530536718337.json, 图片生成/文生图/1954598236717760514.json, 图片生成/文生图/1955172373663137794.json, 图片生成/文生图/1971073668736552962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/1953747187043848193.json、图片生成/文生图/1953757506445213698.json、图片生成/文生图/1953758140024147969.json、图片生成/文生图/1953813624924110849.json、图片生成/文生图/1953815517956112386.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/14 个有
- `CR Prompt Text` —— 5/14 个有
- `ConditioningZeroOut` —— 4/14 个有
- `Float` —— 4/14 个有
- `CFGZeroStar` —— 3/14 个有
- `RH_LLMAPI_NODE` —— 3/14 个有
- `easy promptConcat` —— 3/14 个有
- `easy showAnything` —— 3/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `LoadImage` —— 1/14 个有
- `RH_Captioner` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 14 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 14 | 30% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，14 个样本，取值分散，一致性仅 30%
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、easy promptConcat、LayerUtility: ImageScaleByAspectRatio V2
