---
name: text_to_image_sampler_clip_checkpoint_12
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7096
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [PortraitMaster_中文版, easy seed]
members: [图片生成/文生图/1906519526463442946.json, 图片生成/文生图/1928323196418670594.json, 图片生成/文生图/Z-Image文生图支持LORA以及细节增强_2016028625149104130.json, 图片生成/文生图/z-image-turbo-aio-课程对应工作流____1998300993865547778.json, 图片生成/文生图/z-image-文生图_2013815667270619137.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1906519526463442946.json、图片生成/文生图/1928323196418670594.json、图片生成/文生图/Z-Image文生图支持LORA以及细节增强_2016028625149104130.json、图片生成/文生图/z-image-turbo-aio-课程对应工作流____1998300993865547778.json、图片生成/文生图/z-image-文生图_2013815667270619137.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LatentUpscaleBy` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LoraLoader` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `PortraitMaster_中文版` —— 2/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | 768 - 1152 | 5 | 86% |
| 高度 | 1736 | 1280 - 1736 | 5 | 89% |
| 采样步数 | 9 | 3 - 25 | 5 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 11% |
| 采样算法 | res_multistep | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.55 - 1 | 5 | 73% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1152，观测区间 768 - 1152，5 个样本，取值集中（一致性 86%）
- 高度 中位数 1736，观测区间 1280 - 1736，5 个样本，取值集中（一致性 89%）
- 采样步数 中位数 9，观测区间 3 - 25，5 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 res_multistep，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.55 - 1，5 个样本
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：PortraitMaster_中文版、easy seed
