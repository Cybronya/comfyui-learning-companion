---
name: image_to_image_sampler_clip_unet_150
type: Image To Image
frequency: 3
level: moderate
coverage: 0.843333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, Latent Noise Injection, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像倍高清-krea2_2070830197829627905.json, 图片生成/图生图/图生图-krea2_2069933877975674882.json, 图片生成/图生图/洗图-krea2_2070082974246326274.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_150

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图像倍高清-krea2_2070830197829627905.json、图片生成/图生图/图生图-krea2_2069933877975674882.json、图片生成/图生图/洗图-krea2_2070082974246326274.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `Latent Noise Injection`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `ImageScaleToMaxDimension` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `ConditioningKrea2Rebalance` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LatentColorMatchSimple` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 3 - 8 | 3 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.3 | 0.2 - 0.5 | 3 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 3 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.2 - 0.5，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
