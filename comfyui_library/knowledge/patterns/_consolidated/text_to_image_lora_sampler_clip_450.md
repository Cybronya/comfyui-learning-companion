---
name: text_to_image_lora_sampler_clip_450
type: Text To Image
frequency: 4
level: strong
coverage: 0.84075
common_nodes: [AddLabel, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, GetImageRangeFromBatch, GetImageSize+, ImageAndMaskPreview, ImageCompositeMasked, ImageConcanate, ImpactSwitch, KSampler, LayerUtility: ColorImage V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: ImageBlendAdvance V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MathExpression|pysssss, PreviewImage, ReferenceLatent, SaveImage, Text Concatenate (JPS), TextInput_, ToBinaryMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Kontext 全自动+手动自主切换换装_1939762212267593730.json, 图片生成/图生图/Kontext 指定区域双图融合_1942424711064391682.json, 平台全量/Kontext Dev基础功能大合集_1939190021960445954.json, 平台全量/Kontext 指定区域双图融合 -- 人像换背景_1943170463445245954.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_450

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext 全自动+手动自主切换换装_1939762212267593730.json、图片生成/图生图/Kontext 指定区域双图融合_1942424711064391682.json、平台全量/Kontext Dev基础功能大合集_1939190021960445954.json、平台全量/Kontext 指定区域双图融合 -- 人像换背景_1943170463445245954.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageRangeFromBatch`
- `GetImageSize+`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MathExpression|pysssss`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `Text Concatenate (JPS)`
- `TextInput_`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 3/4 个有
- `LayerMask: BenUltra` —— 3/4 个有
- `LayerMask: LoadBenModel` —— 3/4 个有
- `LayerUtility: JoyCaptionBeta1` —— 3/4 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 3/4 个有
- `Note Plus (mtb)` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ApplyPulidFlux` —— 2/4 个有
- `PulidFluxEvaClipLoader` —— 2/4 个有
- `PulidFluxInsightFaceLoader` —— 2/4 个有
- `PulidFluxModelLoader` —— 2/4 个有
- `BasicGuider` —— 1/4 个有
- `BasicScheduler` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `ClothesSegment` —— 1/4 个有
- `Convert Masks to Images` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GoogleTranslateTextNode` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Image To Mask` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `LayerMask: PersonMaskUltra V2` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `RandomNoise` —— 1/4 个有
- `SamplerCustomAdvanced` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1536 - 1536 | 4 | 100% |
| 高度 | 1152 | 1152 - 1152 | 4 | 100% |
| 采样步数 | 12 | 12 - 12 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 12，观测区间 12 - 12，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
