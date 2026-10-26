---
name: image_to_image_sampler_clip_unet_90
type: Image To Image
frequency: 5
level: strong
coverage: 0.9194
common_nodes: [CLIPLoader, CLIPTextEncode, Image Blank, ImageCompositeMasked, JoinImageWithAlpha, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein-扩图_2058461347406503937.json, 图片生成/图生图/Flux2-Klein-扩图_2087947080038969345.json, 图片生成/图生图/Flux2-klein-无限扩图(颜色校正版)_2012322171997134849.json, 图片生成/图生图/Flux2-klein-无限扩图_2012182107996557314.json, 图片生成/图生图/Flux2-klein-物品移除（适用于小物品移除）_2012184119664447489.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-扩图_2058461347406503937.json、图片生成/图生图/Flux2-Klein-扩图_2087947080038969345.json、图片生成/图生图/Flux2-klein-无限扩图(颜色校正版)_2012322171997134849.json、图片生成/图生图/Flux2-klein-无限扩图_2012182107996557314.json、图片生成/图生图/Flux2-klein-物品移除（适用于小物品移除）_2012184119664447489.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Blank`
- `ImageCompositeMasked`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImagePadForOutpaint` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `Get Image Size` —— 3/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `Mask Fill Holes` —— 1/5 个有
- `YC Color Match` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 5 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，5 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
