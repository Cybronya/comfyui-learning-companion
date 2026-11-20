---
name: image_to_image_lora_sampler_unet_63
type: Image To Image
frequency: 9
level: strong
coverage: 0.411889
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/[Krea 2 系列 06] 从生成走向编辑 - 让生成模型拥有编辑能力_2081918392235286530.json, 图片生成/图生图/[Krea 2 系列 06] 从生成走向编辑_2089272764942348290.json, 图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_-_让生成模型拥有编辑能力_2084596690325172225.json, 图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_-_让生成模型拥有编辑能力_2084650753762877441.json, 图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_-_让生成模型拥有编辑能力_2085887149131522050.json, 图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_-_让生成模型拥有编辑能力_2087434927833960449.json, 图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_2092432755849261058.json, 图片生成/图生图/[Krea_2_系列图片编辑_2092595842329956353.json, 图片生成/文生图/道具-01-krea2-物品三视图_2089700978005200898.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/[Krea 2 系列 06] 从生成走向编辑 - 让生成模型拥有编辑能力_2081918392235286530.json、图片生成/图生图/[Krea 2 系列 06] 从生成走向编辑_2089272764942348290.json、图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_-_让生成模型拥有编辑能力_2084596690325172225.json、图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_-_让生成模型拥有编辑能力_2084650753762877441.json、图片生成/图生图/[Krea_2_系列_06]_从生成走向编辑_-_让生成模型拥有编辑能力_2085887149131522050.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：41%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `ImageStitch` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `easy promptLine` —— 8/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 720 | 9 | 88% |
| 高度 | 512 | 512 - 1280 | 9 | 60% |
| 采样步数 | 10 | 10 - 10 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 720，9 个样本，取值集中（一致性 88%）
- 高度 中位数 512，观测区间 512 - 1280，9 个样本
- 采样步数 中位数 10，观测区间 10 - 10，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
