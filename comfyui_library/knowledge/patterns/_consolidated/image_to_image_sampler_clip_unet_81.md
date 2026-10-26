---
name: image_to_image_sampler_clip_unet_81
type: Image To Image
frequency: 6
level: strong
coverage: 0.955167
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/饰品提取-Klein-9B_2025839437904613378.json, 图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2027362675549806594.json, 图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2038096758793838593.json, 图片生成/文生图/FLUX.2 Klein 超快速 文生图_图生图_多图编辑_2020865739288223746.json, 图片生成/文生图/flux Klein 工作流合集 文生图 图生图_2044235028636377090.json, 图片生成/文生图/亚秒级生成4k图！RTX+Flux2 klein图片编辑&文生图_2037896191970643970.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_81

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/饰品提取-Klein-9B_2025839437904613378.json、图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2027362675549806594.json、图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2038096758793838593.json、图片生成/文生图/FLUX.2 Klein 超快速 文生图_图生图_多图编辑_2020865739288223746.json、图片生成/文生图/flux Klein 工作流合集 文生图 图生图_2044235028636377090.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `ZML_PreviewImage` —— 3/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 6 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（20/6 个样本）：Steps较低可能导致细节不足
