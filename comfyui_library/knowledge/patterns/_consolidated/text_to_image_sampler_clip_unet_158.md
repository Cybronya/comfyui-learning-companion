---
name: text_to_image_sampler_clip_unet_158
type: Text To Image
frequency: 4
level: moderate
coverage: 0.91075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/klein-9b kv版-极速版-_2032297078877065218.json, 图片生成/图生图/z-image-turbo_2034208282579050498.json, 图片生成/图生图/z-image-图生图_2057417058383646721.json, 图片生成/图生图/z-image-图生图_2060273356666134529.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/klein-9b kv版-极速版-_2032297078877065218.json、图片生成/图生图/z-image-turbo_2034208282579050498.json、图片生成/图生图/z-image-图生图_2057417058383646721.json、图片生成/图生图/z-image-图生图_2060273356666134529.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `CR Prompt List` —— 1/4 个有
- `FluxKVCache` —— 1/4 个有
- `ImageScaleToMaxDimension` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.7 | 0.65 - 1 | 4 | 81% |
| 宽度 | 1052 | 1024 - 1536 | 4 | 82% |
| 高度 | 1536 | 1024 - 1920 | 4 | 79% |
| LoRA 模型强度 | 1.11022e-16 | - | 2 | 0% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.65 - 1，4 个样本，取值集中（一致性 81%）
- 宽度 中位数 1052，观测区间 1024 - 1536，4 个样本，取值集中（一致性 82%）
- 高度 中位数 1536，观测区间 1024 - 1920，4 个样本
- LoRA 模型强度 中位数 1.11022e-16，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
