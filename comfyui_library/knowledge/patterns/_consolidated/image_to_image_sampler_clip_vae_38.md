---
name: image_to_image_sampler_clip_vae_38
type: Image To Image
frequency: 5
level: strong
coverage: 0.9582
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyQwenImageLayeredLatentImage, GetImageSize, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-Layered_2073769940812910594.json, 图片生成/图生图/Qwen-image-layered图层_2013528385682673666.json, 图片生成/图生图/Qwen_layered 图层分割_2019575774243721218.json, 图片生成/图生图/psd分层_2014860443415744513.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2008824799061090306.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_38

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Layered_2073769940812910594.json、图片生成/图生图/Qwen-image-layered图层_2013528385682673666.json、图片生成/图生图/Qwen_layered 图层分割_2019575774243721218.json、图片生成/图生图/psd分层_2014860443415744513.json、图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2008824799061090306.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyQwenImageLayeredLatentImage`
- `GetImageSize`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/5 个有
- `ImageScaleToMaxDimension` —— 3/5 个有
- `HAIGC_SavePSD` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `WD14Tagger|pysssss` —— 2/5 个有
- `HAIGC_CombineUnits` —— 1/5 个有
- `HAIGC_Layer` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 4 | 5 | 79% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
