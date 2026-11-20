---
name: text_to_image_sampler_clip_vae_30
type: Text To Image
frequency: 4
level: moderate
coverage: 0.85
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Muter (rgthree), Image Comparer (rgthree), KSampler, LoadImage, Qwen3_VQA, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE-AIO-4K洗高清图，文生图合集_2002740444461187074.json, 图片生成/文生图/Z-IMAGE-AIO-高清4K文生图洗稿图_2003355226528743425.json, 图片生成/文生图/Z-image 最强4K高清直出，文生图+图生图+反推生图 三大组合_2002720151814455298.json, 平台全量/Z-IMAGE-AIO-4K高清洗图 图片反推 自动洗图 图片去除Ai感 文生图合集 真实人物细节多_2008797736388268033.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_30

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE-AIO-4K洗高清图，文生图合集_2002740444461187074.json、图片生成/文生图/Z-IMAGE-AIO-高清4K文生图洗稿图_2003355226528743425.json、图片生成/文生图/Z-image 最强4K高清直出，文生图+图生图+反推生图 三大组合_2002720151814455298.json、平台全量/Z-IMAGE-AIO-4K高清洗图 图片反推 自动洗图 图片去除Ai感 文生图合集 真实人物细节多_2008797736388268033.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CheckpointLoaderSimple` —— 3/4 个有
- `DyPE_FLUX` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `ImpactInt` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `easy promptList` —— 2/4 个有
- `CLIPLoader` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `VAELoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 4 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.95 | 0.9 - 1 | 4 | 95% |
| 宽度 | 512 | 512 - 1280 | 4 | 53% |
| 高度 | 512 | 512 - 1920 | 4 | 29% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，4 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.95，观测区间 0.9 - 1，4 个样本，取值集中（一致性 95%）
- 宽度 中位数 512，观测区间 512 - 1280，4 个样本
- 高度 中位数 512，观测区间 512 - 1920，4 个样本，取值分散，一致性仅 29%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
