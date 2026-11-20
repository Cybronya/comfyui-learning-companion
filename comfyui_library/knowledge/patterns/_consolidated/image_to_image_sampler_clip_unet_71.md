---
name: image_to_image_sampler_clip_unet_71
type: Image To Image
frequency: 8
level: moderate
coverage: 0.99225
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json, 图片生成/图生图/赛博玄幻·湘灵 女主｜图生图_2093230068645584897.json, 图片生成/图生图/赛博玄幻修仙者｜墨渊·图生图_2093285943129231361.json, 图片生成/图生图/赛博玄幻修仙者｜燕青·图生图_2093374930367901697.json, 平台全量/赛博玄幻修仙者｜分镜图集器_2093584749993484290.json, 平台全量/赛博玄幻修仙者｜分镜生成器_2093545878811398145.json, 平台全量/赛博玄幻修仙者｜图生图_2092999468789620738.json, 平台全量/赛博玄幻修仙者｜角色设计器_2093577134592843777.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_71

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json、图片生成/图生图/赛博玄幻·湘灵 女主｜图生图_2093230068645584897.json、图片生成/图生图/赛博玄幻修仙者｜墨渊·图生图_2093285943129231361.json、图片生成/图生图/赛博玄幻修仙者｜燕青·图生图_2093374930367901697.json、平台全量/赛博玄幻修仙者｜分镜图集器_2093584749993484290.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `CR Text` —— 1/8 个有
- `ConditioningCombine` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ModelPatchLoader` —— 1/8 个有
- `ZImageFunControlnet` —— 1/8 个有
- `图像缩放V2_孤海` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | 10 - 22 | 8 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 8 | 84% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | normal | - | 8 | 88% |
| 重绘幅度 | 0.75 | 0.75 - 1 | 8 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22，观测区间 10 - 22，8 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，8 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 normal，8 个样本，一致性 88%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 1，8 个样本，取值集中（一致性 89%）
