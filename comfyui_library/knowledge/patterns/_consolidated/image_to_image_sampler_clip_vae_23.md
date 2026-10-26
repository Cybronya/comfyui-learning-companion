---
name: image_to_image_sampler_clip_vae_23
type: Image To Image
frequency: 9
level: strong
coverage: 0.867556
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux_kontext_官方工作流 多图_1938482540896256001.json, 图片生成/图生图/kontext_手绘情侣头像星蝶少女头像一键真人转手绘_2029009784497770498.json, 图片生成/图生图/kontext灰度图工作流_1963233328004575234.json, 图片生成/图生图/产品_人像精修_2071792524552921090.json, 图片生成/图生图/人像精修+上妆-kontxet_1959201923981324289.json, 图片生成/图生图/动漫线稿上色｜多彩活力插画_1942398408399204354.json, 图片生成/图生图/图片胸部变大神器 Flux Kontext一键变大胸_2015768410298261506.json, 图片生成/图生图/图片胸部增强神器 一键变丰胸放大，优化美女身材_2051213394669252609.json, 图片生成/图生图/最强素颜化妆上妆flux_kontext_dev_1963264724798517250.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_23

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/flux_kontext_官方工作流 多图_1938482540896256001.json、图片生成/图生图/kontext_手绘情侣头像星蝶少女头像一键真人转手绘_2029009784497770498.json、图片生成/图生图/kontext灰度图工作流_1963233328004575234.json、图片生成/图生图/产品_人像精修_2071792524552921090.json、图片生成/图生图/人像精修+上妆-kontxet_1959201923981324289.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `ReferenceLatent` —— 8/9 个有
- `FluxKontextImageScale` —— 7/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `UNETLoader` —— 7/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `ImageConcanate` —— 4/9 个有
- `ImageStitch` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `EmptySD3LatentImage` —— 2/9 个有
- `TeaCache` —— 2/9 个有
- `UnetLoaderGGUF` —— 2/9 个有
- `DetailTransfer` —— 1/9 个有
- `GoogleTranslateTextNode` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `Preview from image [Crystools]` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 9 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
