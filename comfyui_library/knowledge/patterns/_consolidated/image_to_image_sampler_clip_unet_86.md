---
name: image_to_image_sampler_clip_unet_86
type: Image To Image
frequency: 5
level: strong
coverage: 0.8022
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F2Klein-9b产品融图-电商产品光影融合_2064683050432294914.json, 图片生成/图生图/Flux2 Klein-修服装类 原尺寸_2027624962948866049.json, 图片生成/图生图/产品场景光影融合超级透视溶图打光、产品替换，套图、统一打光、_2089872123803291650.json, 图片生成/图生图/全能溶图 溶图打光 图像无缝融合 光影无缝溶图_2087145452339810305.json, 图片生成/图生图/电商产品精修-产品图洗图-高清修复（Flux-2-klein-9B）_2027640206618267650.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_86

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/F2Klein-9b产品融图-电商产品光影融合_2064683050432294914.json、图片生成/图生图/Flux2 Klein-修服装类 原尺寸_2027624962948866049.json、图片生成/图生图/产品场景光影融合超级透视溶图打光、产品替换，套图、统一打光、_2089872123803291650.json、图片生成/图生图/全能溶图 溶图打光 图像无缝融合 光影无缝溶图_2087145452339810305.json、图片生成/图生图/电商产品精修-产品图洗图-高清修复（Flux-2-klein-9B）_2027640206618267650.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `InspyrenetRembg` —— 2/5 个有
- `MaskToImage` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `HYPIRImageRestoration` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 5 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，5 个样本，取值集中（一致性 96%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
