---
name: image_to_image_sampler_clip_unet_118
type: Image To Image
frequency: 4
level: strong
coverage: 0.8445
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SeedVR2+Flux kelin  高清放大工作流_2018183597924028418.json, 图片生成/图生图/flux-2-klein-多图编辑工作流_2015764934323343361.json, 图片生成/图生图/flux-2klein单图_多图编辑_2038533995062890497.json, 图片生成/图生图/饰品提取-Klein-9B_2025839437904613378.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_118

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SeedVR2+Flux kelin  高清放大工作流_2018183597924028418.json、图片生成/图生图/flux-2-klein-多图编辑工作流_2015764934323343361.json、图片生成/图生图/flux-2klein单图_多图编辑_2038533995062890497.json、图片生成/图生图/饰品提取-Klein-9B_2025839437904613378.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `SeedVR2ExtraArgs` —— 1/4 个有
- `easy imageColorMatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6.5 | 3 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.95 - 1 | 4 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6.5，观测区间 3 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.95 - 1，4 个样本，取值集中（一致性 98%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
