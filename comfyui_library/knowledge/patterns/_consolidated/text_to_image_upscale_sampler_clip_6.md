---
name: text_to_image_upscale_sampler_clip_6
type: Text To Image
frequency: 13
level: weak
coverage: 0.903692
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-IMAGE：图生图反推+高清放大_1996194694038167554.json, 图片生成/图生图/Z-Image 图生图 反推_1995485709760913410.json, 图片生成/图生图/Z-Image 图生图 反推_2005808646812565505.json, 图片生成/图生图/Z-Image+Qwen3VQA 反推图生图_1996873578433978370.json, 图片生成/图生图/Z-Image图生图反推｜人像写真提示词生成_2090906960488124417.json, 图片生成/图生图/Z-image  图生图 反推+高清放大_1997242707649183746.json, 图片生成/图生图/seedvr2图像高清放大｜图生图画质增强一键直出_2091296292063506433.json, 图片生成/图生图/seedvr2图像高清放大｜图生图画质增强直出_2091005891771461634.json, 图片生成/图生图/一键反推提示词｜Z-Image人像写真图生图_2091221735055126530.json, 图片生成/图生图/千问图像反推+Z-Image+SeedVR2 高清放大_1997203090476580866.json, 图片生成/图生图/反推提示词＋相似图片生成（图生图） 硕阳_2003404747770109954.json, 图片生成/文生图/Krea2 Turbo+RAW加速版双方案文生图处理工作流_2102150335660908546.json, 图片生成/文生图/Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Z-IMAGE：图生图反推+高清放大_1996194694038167554.json、图片生成/图生图/Z-Image 图生图 反推_1995485709760913410.json、图片生成/图生图/Z-Image 图生图 反推_2005808646812565505.json、图片生成/图生图/Z-Image+Qwen3VQA 反推图生图_1996873578433978370.json、图片生成/图生图/Z-Image图生图反推｜人像写真提示词生成_2090906960488124417.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/13 个有
- `ImageScaleBy` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `Qwen3_VQA` —— 9/13 个有
- `ShowAnything|Mie` —— 9/13 个有
- `VAEEncode` —— 8/13 个有
- `GetImageSize` —— 7/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `JjkText` —— 5/13 个有
- `solarL_SaveImagesToZip` —— 5/13 个有
- `孤海注释` —— 5/13 个有
- `Fast Groups Muter (rgthree)` —— 3/13 个有
- `CR Text Concatenate` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `Text` —— 2/13 个有
- `easy clearCacheAll` —— 2/13 个有
- `easy int` —— 2/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 9 | 13 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 13 | 27% |
| 采样算法 | euler | - | 13 | 46% |
| 调度器 | simple | - | 13 | 46% |
| 重绘幅度 | 1 | 0.9 - 1 | 13 | 97% |
| 宽度 | 1024 | 80 - 1080 | 13 | 30% |
| 高度 | 1680 | 80 - 1920 | 13 | 24% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 9，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，13 个样本，一致性 46%
- 调度器 最常用 simple，13 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，13 个样本，取值集中（一致性 97%）
- 宽度 中位数 1024，观测区间 80 - 1080，13 个样本，取值分散，一致性仅 30%
- 高度 中位数 1680，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 24%
- 高发问题（22/13 个样本）：Steps较低可能导致细节不足
