---
name: text_to_image_sampler_clip_vae_35
type: Text To Image
frequency: 3
level: moderate
coverage: 0.857333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Muter (rgthree), Image Comparer (rgthree), KSampler, LoadImage, Qwen3_VQA, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE-AIO-4K洗高清图，文生图合集_2002740444461187074.json, 图片生成/文生图/Z-IMAGE-AIO-高清4K文生图洗稿图_2003355226528743425.json, 图片生成/文生图/Z-image 最强4K高清直出，文生图+图生图+反推生图 三大组合_2002720151814455298.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE-AIO-4K洗高清图，文生图合集_2002740444461187074.json、图片生成/文生图/Z-IMAGE-AIO-高清4K文生图洗稿图_2003355226528743425.json、图片生成/文生图/Z-image 最强4K高清直出，文生图+图生图+反推生图 三大组合_2002720151814455298.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `DyPE_FLUX` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `easy promptList` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 0.9 - 1 | 3 | 95% |
| 宽度 | 512 | 512 - 1280 | 3 | 53% |
| 高度 | 512 | 512 - 1920 | 3 | 32% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- 宽度 中位数 512，观测区间 512 - 1280，3 个样本
- 高度 中位数 512，观测区间 512 - 1920，3 个样本，取值分散，一致性仅 32%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
