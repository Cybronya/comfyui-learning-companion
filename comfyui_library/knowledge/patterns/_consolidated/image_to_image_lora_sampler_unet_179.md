---
name: image_to_image_lora_sampler_unet_179
type: Image To Image
frequency: 4
level: moderate
coverage: 0.90425
common_nodes: [CLIPLoader, EmptySD3LatentImage, GetImageSize+, ImageScaleToTotalPixels, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2图像编辑单图_双图+klein图片编辑_2112734352307216385.json, 图片生成/图生图/krea2图像编辑单图_双图+klein图片编辑_2114997161833357313.json, 图片生成/图生图/krea2图像编辑（单图_双图）+klein图片编辑_2104374878999760898.json, 图片生成/图生图/最强单图编辑-krea2编辑_2099804375295283202.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_179

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/krea2图像编辑单图_双图+klein图片编辑_2112734352307216385.json、图片生成/图生图/krea2图像编辑单图_双图+klein图片编辑_2114997161833357313.json、图片生成/图生图/krea2图像编辑（单图_双图）+klein图片编辑_2104374878999760898.json、图片生成/图生图/最强单图编辑-krea2编辑_2099804375295283202.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetImageSize+`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
