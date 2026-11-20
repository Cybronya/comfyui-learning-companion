---
name: image_to_image_sampler_clip_unet_25
type: Image To Image
frequency: 13
level: moderate
coverage: 0.819923
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, DualCLIPLoader, Image Comparer (rgthree), JWImageResizeByLongerSide, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/FLUX图生图+提示词反推+latent放大_2106556743441534977.json, 图片生成/反推提示词/flux图生图提示词反推+模型放大工作流（可回到原尺寸）_1981605940547993601.json, 图片生成/图生图/FLUX洗图260815_2088646735945097218.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大(洗图神器）_1990339764551340034.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大(洗图神器）_2086801503968382978.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大_2092887306234589186.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大（RunningHub)_1916027994802946050.json, 图片生成/图生图/Flux洗图工作流&JoyCaption&DeepSeek反推_1995408312558608385.json, 图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_1985316803440164865.json, 图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_2007715002215571458.json, 图片生成/图生图/Flux洗图（内含提示词反推）_2066788048234438657.json, 图片生成/图生图/flux图生图提示词反推+模型放大工作流_1980444331452641282.json, 平台全量/Flux洗图工作流&JoyCaption&DeepSeek反推_1993579560226799617.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/FLUX图生图+提示词反推+latent放大_2106556743441534977.json、图片生成/反推提示词/flux图生图提示词反推+模型放大工作流（可回到原尺寸）_1981605940547993601.json、图片生成/图生图/FLUX洗图260815_2088646735945097218.json、图片生成/图生图/Flux图生图+提示词反推+Latent放大(洗图神器）_1990339764551340034.json、图片生成/图生图/Flux图生图+提示词反推+Latent放大(洗图神器）_2086801503968382978.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `JWImageResizeByLongerSide`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 12/13 个有
- `LatentUpscaleBy` —— 10/13 个有
- `JanusImageUnderstanding` —— 6/13 个有
- `JanusModelLoader` —— 6/13 个有
- `Save Text File` —— 5/13 个有
- `SaveText|pysssss` —— 5/13 个有
- `Translate` —— 5/13 个有
- `ImageScaleBy` —— 2/13 个有
- `ImageUpscaleWithModel` —— 2/13 个有
- `UpscaleModelLoader` —— 2/13 个有
- `easy imageSize` —— 2/13 个有
- `easy imageScaleDown` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 13 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | normal | - | 13 | 46% |
| 重绘幅度 | 0.35 | 0.15 - 0.7 | 13 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，13 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 normal，13 个样本，一致性 46%
- 重绘幅度 中位数 0.35，观测区间 0.15 - 0.7，13 个样本
