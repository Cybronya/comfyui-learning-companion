---
name: unknown_workflow_sampler_clip_unet_24
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.863333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text, easy hiresFix, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, CR Text, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1953757506445213698.json, 图片生成/文生图/1953758140024147969.json, 图片生成/文生图/1953813624924110849.json, 图片生成/文生图/1953815517956112386.json, 图片生成/文生图/1954172979645181954.json, 图片生成/文生图/1954222888989683714.json, 图片生成/文生图/1954593530536718337.json, 图片生成/文生图/1954915934088544258.json, 图片生成/文生图/1955290519761928194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1953757506445213698.json、图片生成/文生图/1953758140024147969.json、图片生成/文生图/1953813624924110849.json、图片生成/文生图/1953815517956112386.json、图片生成/文生图/1954172979645181954.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 5/9 个有
- `PreviewImage` —— 4/9 个有
- `LayerUtility: ImageReel` —— 3/9 个有
- `LayerUtility: ImageReelComposit` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `Float` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `DF_Get_image_size` —— 1/9 个有
- `easy hiresFix` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 9 | 44% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，9 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、easy hiresFix、LayerUtility: ImageReel、LayerUtility: ImageReelComposit、CR Text
