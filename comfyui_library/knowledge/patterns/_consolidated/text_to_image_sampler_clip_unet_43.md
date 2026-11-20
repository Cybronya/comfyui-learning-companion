---
name: text_to_image_sampler_clip_unet_43
type: Text To Image
frequency: 13
level: moderate
coverage: 0.840462
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageToMask, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RMBG, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy isMaskEmpty, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商主图-图片参考匹配_2037749676341993474.json, 图片生成/图生图/电商主图产品替换主图高清无损主图参考电商图生图优化_2074817965127725057.json, 图片生成/图生图/电商产品图自动匹配场景_2048288552840077314.json, 图片生成/图生图/电商产品场景图-替换产品-自动匹配背景_2090700807112056833.json, 图片生成/图生图/绝了，强烈推荐！为你的产品赋予生命、诗意和故事，电商产品主图-自动匹配场景。_2028644502524661762.json, 平台全量/【产品换背景】电商产品背景替换，保留材质细节_2072519782699716609.json, 平台全量/主图风格参考 电商产品主图迁移 图片参考风格匹配_2056239361561292802.json, 平台全量/产品换背景 重新打光融图 电商产品主图 自动匹配场景_2030825442340507650.json, 平台全量/人物模特+场景 电商场景主图 溶图合成打光 电商产品背景合成+融图打光_2027980376727101442.json, 平台全量/全品类-电商主图-自动生成_2050148813486206977.json, 平台全量/电商产品主图-自动匹配场景_2054467388019625986.json, 平台全量/电商产品主图匹配场景打光-自动模式_2031199651944206337.json, 平台全量/电商产品溶图-自动匹配场景_2049470083394707458.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/电商主图-图片参考匹配_2037749676341993474.json、图片生成/图生图/电商主图产品替换主图高清无损主图参考电商图生图优化_2074817965127725057.json、图片生成/图生图/电商产品图自动匹配场景_2048288552840077314.json、图片生成/图生图/电商产品场景图-替换产品-自动匹配背景_2090700807112056833.json、图片生成/图生图/绝了，强烈推荐！为你的产品赋予生命、诗意和故事，电商产品主图-自动匹配场景。_2028644502524661762.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
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
- `AILab_QwenVL` —— 9/13 个有
- `CR Text` —— 9/13 个有
- `FluxKontextImageScale` —— 9/13 个有
- `Image Comparer (rgthree)` —— 9/13 个有
- `ImageConcatMulti` —— 9/13 个有
- `LaMaInpainting` —— 9/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `PainterFluxImageEdit` —— 9/13 个有
- `PreviewAny` —— 9/13 个有
- `easy imageSize` —— 9/13 个有
- `ClipLoaderGGUF` —— 4/13 个有
- `EmptyFlux2LatentImage` —— 4/13 个有
- `LaMaInpaint` —— 4/13 个有
- `LayerUtility: CropByMask` —— 4/13 个有
- `LoadLaMaModel` —— 4/13 个有
- `Qwen3VL_Chat` —— 4/13 个有
- `easy showAnything` —— 4/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 13 | 65% |
| 高度 | 512 | 512 - 1024 | 13 | 65% |
| 采样步数 | 4 | 4 - 8 | 13 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 69% |
| 调度器 | simple | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，13 个样本
- 高度 中位数 512，观测区间 512 - 1024，13 个样本
- 采样步数 中位数 4，观测区间 4 - 8，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 69%
- 调度器 最常用 simple，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
