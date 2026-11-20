---
name: text_to_image_sampler_clip_unet_163
type: Text To Image
frequency: 4
level: moderate
coverage: 0.7755
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu_Turbo 文生图_2070875528814481409.json, 图片生成/文生图/Z-Anime-基于ZIB底模的动漫风格模型_2064727085071032322.json, 图片生成/文生图/Z-image+t2i+i2i+文生图+图生图(6G显存可用)_2074048707573673985.json, 图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_163

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Boogu_Turbo 文生图_2070875528814481409.json、图片生成/文生图/Z-Anime-基于ZIB底模的动漫风格模型_2064727085071032322.json、图片生成/文生图/Z-image+t2i+i2i+文生图+图生图(6G显存可用)_2074048707573673985.json、图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `Float` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 3 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | euler | - | 4 | 25% |
| 重绘幅度 | 1 | 0.3 - 1 | 3 | 57% |
| 宽度 | 1024 | 928 - 1280 | 4 | 88% |
| 高度 | 1600 | 1536 - 1920 | 4 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 euler，4 个样本，一致性 25%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，3 个样本
- 宽度 中位数 1024，观测区间 928 - 1280，4 个样本，取值集中（一致性 88%）
- 高度 中位数 1600，观测区间 1536 - 1920，4 个样本，取值集中（一致性 91%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
