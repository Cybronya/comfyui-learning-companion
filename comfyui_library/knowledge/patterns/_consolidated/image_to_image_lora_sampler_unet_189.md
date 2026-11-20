---
name: image_to_image_lora_sampler_unet_189
type: Image To Image
frequency: 3
level: moderate
coverage: 0.890667
common_nodes: [CLIPLoader, EmptySD3LatentImage, GetImageSize+, ImageScaleToTotalPixels, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2图像编辑单图_双图+klein图片编辑_2112734352307216385.json, 图片生成/图生图/krea2图像编辑（单图_双图）+klein图片编辑_2104374878999760898.json, 图片生成/图生图/最强单图编辑-krea2编辑_2099804375295283202.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_189

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/krea2图像编辑单图_双图+klein图片编辑_2112734352307216385.json、图片生成/图生图/krea2图像编辑（单图_双图）+klein图片编辑_2104374878999760898.json、图片生成/图生图/最强单图编辑-krea2编辑_2099804375295283202.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CLIPTextEncode` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
