---
name: image_to_image_sampler_clip_unet_41
type: Image To Image
frequency: 9
level: strong
coverage: 0.982
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2029774450773725185.json, 图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2027362675549806594.json, 图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2038096758793838593.json, 图片生成/文生图/FLUX.2 Klein 超快速 文生图_图生图_多图编辑_2020865739288223746.json, 图片生成/文生图/FLUX2 Klein 文生图 和 图生图 工作流（AI小王子）_2015993179522207746.json, 图片生成/文生图/FLUX2+Klein+文生图+和+图生图+工作流_2059094392811642881.json, 图片生成/文生图/FLUX2+Klein+文生图+和+图生图+工作流_2064315210042789890.json, 图片生成/文生图/flux2 klein_2034072060485439490.json, 图片生成/文生图/亚秒级生成4k图！RTX+Flux2 klein图片编辑&文生图_2037896191970643970.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/2029774450773725185.json、图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2027362675549806594.json、图片生成/文生图/2倍加速！FLUX2 Klein 文生图 和 图生图 工作流（基于AI小王子加速优化）_2038096758793838593.json、图片生成/文生图/FLUX.2 Klein 超快速 文生图_图生图_多图编辑_2020865739288223746.json、图片生成/文生图/FLUX2 Klein 文生图 和 图生图 工作流（AI小王子）_2015993179522207746.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `LayerUtility: ImageReel` —— 5/9 个有
- `LayerUtility: ImageReelComposit` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `ZML_PreviewImage` —— 3/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `RTXVideoSuperResolution` —— 1/9 个有
- `RepeatLatentBatch` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有
- `easy imageSize` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 9 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，9 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（31/9 个样本）：Steps较低可能导致细节不足
