---
name: text_to_image_sampler_clip_unet_187
type: Text To Image
frequency: 3
level: strong
coverage: 0.827333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, Latent Noise Injection, LatentColorMatchSimple, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2局部重绘_2071597181253013506.json, 图片生成/图生图/krea2真人文生图-绅士版_2070826251165724674.json, 图片生成/文生图/krea2文生图-双采版+单_多图_2116423812534333442.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/krea2局部重绘_2071597181253013506.json、图片生成/图生图/krea2真人文生图-绅士版_2070826251165724674.json、图片生成/文生图/krea2文生图-双采版+单_多图_2116423812534333442.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `Latent Noise Injection`
- `LatentColorMatchSimple`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ColorMatchV2` —— 1/3 个有
- `FastGroupsBypassSwitch` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `Int` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |
| 宽度 | 928 | 928 - 928 | 3 | 100% |
| 高度 | 1664 | 1664 - 1664 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- 宽度 中位数 928，观测区间 928 - 928，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1664，观测区间 1664 - 1664，3 个样本，取值集中（一致性 100%）
- 高发问题（8/3 个样本）：Steps较低可能导致细节不足
