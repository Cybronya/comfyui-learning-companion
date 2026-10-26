---
name: text_to_image_inpaint_lora_sampler_3
type: Text To Image
frequency: 3
level: strong
coverage: 0.852667
common_nodes: [BasicGuider, BlockifyMask, Bool, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), ImageScale, ImpactMakeAnyList, ImpactNeg, InpaintCropImproved, Int, JjkText, KSampler, KSamplerSelect, LayerColor: BrightnessContrastV2, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SmartColorMatch, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy compare, easy ifElse, easy imageSize, easy imageSizeBySide, easy int, easy isMaskEmpty, solarL_SaveImagesToZip, 取色器_孤海, 图像接缝, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein商品替换_2107419139630526466.json, 图片生成/图生图/Flux2-klein小批量万物迁移零偏移｜图生图商品替换电商产品_2090092327686729729.json, 图片生成/图生图/万物迁移零偏移｜Flux2-klein小批量商品替换图生图_2089803072192208898.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2-klein商品替换_2107419139630526466.json、图片生成/图生图/Flux2-klein小批量万物迁移零偏移｜图生图商品替换电商产品_2090092327686729729.json、图片生成/图生图/万物迁移零偏移｜Flux2-klein小批量商品替换图生图_2089803072192208898.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BlockifyMask`
- `Bool`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImpactMakeAnyList`
- `ImpactNeg`
- `InpaintCropImproved`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: BrightnessContrastV2`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SmartColorMatch`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy compare`
- `easy ifElse`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy int`
- `easy isMaskEmpty`
- `solarL_SaveImagesToZip`
- `取色器_孤海`
- `图像接缝`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
