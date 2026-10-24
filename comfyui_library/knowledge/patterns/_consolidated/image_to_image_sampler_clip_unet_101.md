---
name: image_to_image_sampler_clip_unet_101
type: Image To Image
frequency: 5
level: strong
coverage: 0.9618
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片一键去水印工具_1994723497270185986.json, 图片生成/图生图/图片去水印 一键消除水印_1991030181810872322.json, 图片生成/图生图/增加自然光影（无光影家具空间生成真实自然光影效果kontext_全能溶图打光_）_1986703454842384386.json, 图片生成/图生图/模特手持产品生成V4_1957790299702788098.json, 图片生成/图生图/精修-金属类-kontxet_1959152559569186818.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_101

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图片一键去水印工具_1994723497270185986.json、图片生成/图生图/图片去水印 一键消除水印_1991030181810872322.json、图片生成/图生图/增加自然光影（无光影家具空间生成真实自然光影效果kontext_全能溶图打光_）_1986703454842384386.json、图片生成/图生图/模特手持产品生成V4_1957790299702788098.json、图片生成/图生图/精修-金属类-kontxet_1959152559569186818.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `ImpactImageBatchToImageList` —— 1/5 个有
- `Int` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `workflow>HyperSpeed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
