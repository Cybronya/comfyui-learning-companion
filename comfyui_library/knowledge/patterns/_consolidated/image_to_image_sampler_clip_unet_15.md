---
name: image_to_image_sampler_clip_unet_15
type: Image To Image
frequency: 13
level: moderate
coverage: 0.833154
common_nodes: [CLIPTextEncodeFlux, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/FLUX图生图+提示词反推+latent放大_2106556743441534977.json, 图片生成/图生图/FLUX图生图工作流_2075049931479543809.json, 图片生成/图生图/FLUX洗图260815_2088646735945097218.json, 图片生成/图生图/Flux SRPO 细节增强洗图_1971579868788027394.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大(洗图神器）_1990339764551340034.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大(洗图神器）_2086801503968382978.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大_2092887306234589186.json, 图片生成/图生图/Flux图生图+提示词反推+Latent放大（RunningHub)_1916027994802946050.json, 图片生成/图生图/Flux洗图+PMRF放大工作流（更新）_1955444798025076737.json, 图片生成/图生图/Flux洗图工作流&JoyCaption&DeepSeek反推_1995408312558608385.json, 图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_1985316803440164865.json, 图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_2007715002215571458.json, 图片生成/图生图/Flux洗图（内含提示词反推）_2066788048234438657.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/FLUX图生图+提示词反推+latent放大_2106556743441534977.json、图片生成/图生图/FLUX图生图工作流_2075049931479543809.json、图片生成/图生图/FLUX洗图260815_2088646735945097218.json、图片生成/图生图/Flux SRPO 细节增强洗图_1971579868788027394.json、图片生成/图生图/Flux图生图+提示词反推+Latent放大(洗图神器）_1990339764551340034.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 12/13 个有
- `Image Comparer (rgthree)` —— 12/13 个有
- `JWImageResizeByLongerSide` —— 12/13 个有
- `Joy_caption_two` —— 12/13 个有
- `Joy_caption_two_load` —— 12/13 个有
- `PreviewImage` —— 11/13 个有
- `ShowText|pysssss` —— 11/13 个有
- `LatentUpscaleBy` —— 9/13 个有
- `JanusImageUnderstanding` —— 5/13 个有
- `JanusModelLoader` —— 5/13 个有
- `Save Text File` —— 4/13 个有
- `SaveText|pysssss` —— 4/13 个有
- `Translate` —— 4/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `DF_Text_Box` —— 1/13 个有
- `Float` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `PMRF` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 10 - 30 | 13 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 62% |
| 调度器 | normal | - | 13 | 46% |
| 重绘幅度 | 0.35 | 0.3 - 0.7 | 13 | 66% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 10 - 30，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 62%
- 调度器 最常用 normal，13 个样本，一致性 46%
- 重绘幅度 中位数 0.35，观测区间 0.3 - 0.7，13 个样本
