---
name: text_to_image_sampler_clip_unet_127
type: Text To Image
frequency: 5
level: strong
coverage: 0.8676
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/klein-9b kv版-极速版-_2032297078877065218.json, 图片生成/图生图/z-image图生图工作流_2001988545583673345.json, 图片生成/图生图/z-image图生图工作流_2009950317806358530.json, 图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json, 图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_127

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/klein-9b kv版-极速版-_2032297078877065218.json、图片生成/图生图/z-image图生图工作流_2001988545583673345.json、图片生成/图生图/z-image图生图工作流_2009950317806358530.json、图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json、图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy promptList` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `FluxResolutionNode` —— 2/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `CR Prompt List` —— 1/5 个有
- `FluxKVCache` —— 1/5 个有
- `ImageScaleToMaxDimension` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.8 | 0.8 - 1 | 5 | 90% |
| 宽度 | 1024 | 1024 - 1536 | 5 | 82% |
| 高度 | 1536 | 1024 - 1536 | 5 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.8，观测区间 0.8 - 1，5 个样本，取值集中（一致性 90%）
- 宽度 中位数 1024，观测区间 1024 - 1536，5 个样本，取值集中（一致性 82%）
- 高度 中位数 1536，观测区间 1024 - 1536，5 个样本，取值集中（一致性 86%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
