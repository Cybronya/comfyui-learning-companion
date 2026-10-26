---
name: text_to_image_sampler_clip_unet_135
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8464
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageToMask, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RMBG, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy isMaskEmpty, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商主图-图片参考匹配_2037749676341993474.json, 图片生成/图生图/电商主图产品替换主图高清无损主图参考电商图生图优化_2074817965127725057.json, 图片生成/图生图/电商产品图自动匹配场景_2048288552840077314.json, 图片生成/图生图/电商产品场景图-替换产品-自动匹配背景_2090700807112056833.json, 图片生成/图生图/绝了，强烈推荐！为你的产品赋予生命、诗意和故事，电商产品主图-自动匹配场景。_2028644502524661762.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/电商主图-图片参考匹配_2037749676341993474.json、图片生成/图生图/电商主图产品替换主图高清无损主图参考电商图生图优化_2074817965127725057.json、图片生成/图生图/电商产品图自动匹配场景_2048288552840077314.json、图片生成/图生图/电商产品场景图-替换产品-自动匹配背景_2090700807112056833.json、图片生成/图生图/绝了，强烈推荐！为你的产品赋予生命、诗意和故事，电商产品主图-自动匹配场景。_2028644502524661762.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageToMask`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RMBG`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy isMaskEmpty`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `CR Text` —— 3/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `LaMaInpainting` —— 3/5 个有
- `PainterFluxImageEdit` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `easy imageSize` —— 3/5 个有
- `ClipLoaderGGUF` —— 2/5 个有
- `EmptyFlux2LatentImage` —— 2/5 个有
- `LaMaInpaint` —— 2/5 个有
- `LayerUtility: CropByMask` —— 2/5 个有
- `LoadLaMaModel` —— 2/5 个有
- `Qwen3VL_Chat` —— 2/5 个有
- `easy showAnything` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 5 | 65% |
| 高度 | 512 | 512 - 1024 | 5 | 65% |
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，5 个样本
- 高度 中位数 512，观测区间 512 - 1024，5 个样本
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
