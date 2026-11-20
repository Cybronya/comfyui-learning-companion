---
name: image_to_image_sampler_clip_unet_136
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9256
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶WAN2.2单底噪图生图洗图流_1956293805874008065.json, 平台全量/F.2Kiein箱包全类目产品精修真实感全类目_2118218988625944578.json, 平台全量/Flux-Klein-9B-水印移除_2012780990472658945.json, 平台全量/Flux.2 klein-9B 换头换脸  更好一致性 高清修复细节_2035187664386793473.json, 平台全量/Flux.2-Klein-去马赛克-去水印-去遮挡-高清放大_2071758138289778689.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/▶WAN2.2单底噪图生图洗图流_1956293805874008065.json、平台全量/F.2Kiein箱包全类目产品精修真实感全类目_2118218988625944578.json、平台全量/Flux-Klein-9B-水印移除_2012780990472658945.json、平台全量/Flux.2 klein-9B 换头换脸  更好一致性 高清修复细节_2035187664386793473.json、平台全量/Flux.2-Klein-去马赛克-去水印-去遮挡-高清放大_2071758138289778689.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 2/5 个有
- `ColorMatch` —— 1/5 个有
- `LayerMask: LoadFlorence2Model` —— 1/5 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/5 个有
- `ModelSamplingSD3` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `YC Color Match` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 5 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
