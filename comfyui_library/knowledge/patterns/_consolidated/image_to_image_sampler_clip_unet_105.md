---
name: image_to_image_sampler_clip_unet_105
type: Image To Image
frequency: 5
level: strong
coverage: 0.5178
common_nodes: [Bookmark (rgthree), CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetNode, ImageScaleToTotalPixels, KSampler, Label (rgthree), LoadImage, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, SaveImage, SetNode, Switch any [Crystools], UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/当今最强！阿里生图模型Z-Image_1993863439988752385.json, 图片生成/文生图/阿里生图模型Z-Image-阿浩_1994001483769249794.json, 图片生成/文生图/阿里生图模型Z-Image-阿浩_2017794207607431170.json, 数字人/数字人/阿里生图模型Z-Image-阿浩_2013173069061300225.json, 数字人/数字人/阿里生图模型Z-Image-阿浩_2026864764109983745.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/当今最强！阿里生图模型Z-Image_1993863439988752385.json、图片生成/文生图/阿里生图模型Z-Image-阿浩_1994001483769249794.json、图片生成/文生图/阿里生图模型Z-Image-阿浩_2017794207607431170.json、数字人/数字人/阿里生图模型Z-Image-阿浩_2013173069061300225.json、数字人/数字人/阿里生图模型Z-Image-阿浩_2026864764109983745.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 5 个 workflow 都包含：
- `Bookmark (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `Switch any [Crystools]`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
