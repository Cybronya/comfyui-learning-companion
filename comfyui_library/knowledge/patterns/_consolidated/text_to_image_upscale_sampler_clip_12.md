---
name: text_to_image_upscale_sampler_clip_12
type: Text To Image
frequency: 8
level: weak
coverage: 0.903125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-IMAGE：图生图反推+高清放大_1996194694038167554.json, 图片生成/图生图/Z-Image 图生图 反推_1995485709760913410.json, 图片生成/图生图/Z-Image 图生图 反推_2005808646812565505.json, 图片生成/图生图/Z-Image+Qwen3VQA 反推图生图_1996873578433978370.json, 图片生成/图生图/Z-Image图生图反推｜人像写真提示词生成_2090906960488124417.json, 图片生成/图生图/Z-image  图生图 反推+高清放大_1997242707649183746.json, 图片生成/图生图/一键反推提示词｜Z-Image人像写真图生图_2091221735055126530.json, 图片生成/图生图/洗图反推提示词z-image最新模型｜反推提示词图生图二合一，洗图不出戏_2100498114716196865.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-IMAGE：图生图反推+高清放大_1996194694038167554.json、图片生成/图生图/Z-Image 图生图 反推_1995485709760913410.json、图片生成/图生图/Z-Image 图生图 反推_2005808646812565505.json、图片生成/图生图/Z-Image+Qwen3VQA 反推图生图_1996873578433978370.json、图片生成/图生图/Z-Image图生图反推｜人像写真提示词生成_2090906960488124417.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `Qwen3_VQA` —— 7/8 个有
- `ShowAnything|Mie` —— 7/8 个有
- `GetImageSize` —— 6/8 个有
- `JjkText` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `solarL_SaveImagesToZip` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `LayerUtility: ImageReel` —— 1/8 个有
- `LayerUtility: ImageReelComposit` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 9 | 8 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 8 | 27% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1052 | 80 - 1080 | 8 | 31% |
| 高度 | 1472 | 80 - 1920 | 8 | 24% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 9，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 80 - 1080，8 个样本，取值分散，一致性仅 31%
- 高度 中位数 1472，观测区间 80 - 1920，8 个样本，取值分散，一致性仅 24%
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
