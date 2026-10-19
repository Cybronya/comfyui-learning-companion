---
name: unknown_workflow_sampler_clip_unet_56
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8694
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text]
members: [图片生成/文生图/1957313561636827138.json, 图片生成/文生图/1960181642029641729.json, 图片生成/文生图/1962501732217536513.json, 图片生成/文生图/1973970749973204993.json, 图片生成/文生图/小腰精_胸部_2103720016867848193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1957313561636827138.json、图片生成/文生图/1960181642029641729.json、图片生成/文生图/1962501732217536513.json、图片生成/文生图/1973970749973204993.json、图片生成/文生图/小腰精_胸部_2103720016867848193.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoraLoader` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `TextConcatenator` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 5 | 48% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 7 | 5 | 26% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1.5 | 4 | 76% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，5 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 7，5 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1.5，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
