---
name: unknown_workflow_lora_sampler_clip_59
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.913111
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z - IMAGE - Distill loRa 速度对比工作流_2024672851546083330.json, 图片生成/文生图/Z-distill lora对比工作流_2082076301388767234.json, 图片生成/文生图/Z-image-Turbo 文生图_2046797778214461441.json, 图片生成/文生图/Zimage base 4步8步Lora对比_2021782849505992705.json, 图片生成/文生图/太强了！最高20倍提速！最新Z-distill lora对比工作流_2028648181180928001.json, 图片生成/文生图/批量文生图_2033573673789034498.json, 图片生成/文生图/最高20倍提速！Z-distill lora对比工作流_2021664209846673409.json, 图片生成/文生图/最高20倍提速！Z-distill lora对比工作流_2038453840286064642.json, 图片生成/文生图/超20倍提速！Z-distill-lora效果对比_2028642862866370561.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Z - IMAGE - Distill loRa 速度对比工作流_2024672851546083330.json、图片生成/文生图/Z-distill lora对比工作流_2082076301388767234.json、图片生成/文生图/Z-image-Turbo 文生图_2046797778214461441.json、图片生成/文生图/Zimage base 4步8步Lora对比_2021782849505992705.json、图片生成/文生图/太强了！最高20倍提速！最新Z-distill lora对比工作流_2028648181180928001.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy promptList` —— 8/9 个有
- `AddLabel` —— 7/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `ImageConcatMulti` —— 7/9 个有
- `easy globalSeed` —— 7/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 7 - 50 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 53% |
| 采样算法 | euler_ancestral | - | 9 | 67% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 7 - 50，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（16/9 个样本）：Steps较低可能导致细节不足
