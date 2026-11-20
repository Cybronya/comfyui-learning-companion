---
name: unknown_workflow_lora_sampler_clip_231
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.833
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptySD3LatentImage, ImagesConcanateToGrid, KSampler, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewImage, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy promptList, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/工作流基础系列4.1-Z-Image-Turbo文生图工作流-CFG值的影响-使用For循环_2044611513083760642.json, 图片生成/文生图/工作流基础系列4.2-Z-Image-Turbo文生图工作流-Step值的影响-使用For循环_2044635750297247746.json, 图片生成/文生图/工作流基础系列4.3-Z-Image-Turbo文生图工作流-Denoise值的影响-使用For循环_2044638092807639041.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_231

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/工作流基础系列4.1-Z-Image-Turbo文生图工作流-CFG值的影响-使用For循环_2044611513083760642.json、图片生成/文生图/工作流基础系列4.2-Z-Image-Turbo文生图工作流-Step值的影响-使用For循环_2044635750297247746.json、图片生成/文生图/工作流基础系列4.3-Z-Image-Turbo文生图工作流-Denoise值的影响-使用For循环_2044638092807639041.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `ImagesConcanateToGrid`
- `KSampler`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptList`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 2/3 个有
- `Int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
