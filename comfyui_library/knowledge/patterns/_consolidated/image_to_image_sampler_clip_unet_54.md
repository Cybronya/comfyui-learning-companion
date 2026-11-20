---
name: image_to_image_sampler_clip_unet_54
type: Image To Image
frequency: 7
level: moderate
coverage: 0.936
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/CMF_2029777059152666625.json, 图片生成/图生图/FLUX 2 图生图_1993556092405874690.json, 图片生成/图生图/FLUX 2 多图编辑_1993562616243093506.json, 图片生成/图生图/FLUX-Klein 3图融合工作流_2014225545059373057.json, 图片生成/图生图/Flux2-klein-9b 人物换装_2015968151225245698.json, 图片生成/图生图/模特_2029780558808621057.json, 图片生成/文生图/2029774450773725185.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/CMF_2029777059152666625.json、图片生成/图生图/FLUX 2 图生图_1993556092405874690.json、图片生成/图生图/FLUX 2 多图编辑_1993562616243093506.json、图片生成/图生图/FLUX-Klein 3图融合工作流_2014225545059373057.json、图片生成/图生图/Flux2-klein-9b 人物换装_2015968151225245698.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `LayerUtility: ImageReel` —— 3/7 个有
- `LayerUtility: ImageReelComposit` —— 3/7 个有
- `RepeatLatentBatch` —— 3/7 个有
- `EmptyFlux2LatentImage` —— 2/7 个有
- `FluxGuidance` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `BiRefNetRMBG` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `PowerfulMaskCrop` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 20 | 7 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 20，7 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
