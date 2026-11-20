---
name: text_to_image_upscale_sampler_clip_41
type: Text To Image
frequency: 3
level: moderate
coverage: 0.789
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 宇宙超级无敌洗图_1995299863191597058.json, 图片生成/文生图/z-image-文生图_洗图_2008808216209133570.json, 平台全量/Z-Image Turbo 高质量洗图  高清放大 文生图 图生图自动反推提示词_2027269567059333121.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image 宇宙超级无敌洗图_1995299863191597058.json、图片生成/文生图/z-image-文生图_洗图_2008808216209133570.json、平台全量/Z-Image Turbo 高质量洗图  高清放大 文生图 图生图自动反推提示词_2027269567059333121.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Float` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowAnything|Mie` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.9 | 0.3 - 1 | 3 | 58% |
| 宽度 | 1280 | 1080 - 1920 | 3 | 75% |
| 高度 | 1920 | 1080 - 1920 | 3 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.3 - 1，3 个样本
- 宽度 中位数 1280，观测区间 1080 - 1920，3 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，3 个样本
