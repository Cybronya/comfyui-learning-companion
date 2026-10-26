---
name: text_to_image_lora_sampler_clip_205
type: Text To Image
frequency: 9
level: strong
coverage: 0.914556
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize+, ImageStitch, KSampler, LayerMask: BenUltra, LayerMask: LoadBenModel, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReferenceLatent, SaveImage, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 换装秀【先脱后穿】_1954810397346848770.json, 图片生成/图生图/Kontext 精准换装_1955445547281760258.json, 图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json, 图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json, 图片生成/图生图/Kontext换装丨一致性换装丨一键换装！！_1981234234969022466.json, 图片生成/图生图/换装秀_1952195949659631617.json, 图片生成/图生图/模特一键换衣服+电商带货+产品展示（优化版-3.0）_2022618537390514178.json, 图片生成/图生图/模特一键换衣服+电商带货+产品展示（优化版-3.0）_2063497732433727490.json, 图片生成/图生图/电商版-最强模特换装流_1964547496225722369.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_205

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Kontext 换装秀【先脱后穿】_1954810397346848770.json、图片生成/图生图/Kontext 精准换装_1955445547281760258.json、图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json、图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json、图片生成/图生图/Kontext换装丨一致性换装丨一键换装！！_1981234234969022466.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `ImageStitch`
- `KSampler`
- `LayerMask: BenUltra`
- `LayerMask: LoadBenModel`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `ReferenceLatent`
- `SaveImage`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: JoyCaptionBeta1` —— 8/9 个有
- `LayerUtility: ImageReelComposit` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `LayerUtility: ImageReel` —— 5/9 个有
- `Anything Everywhere` —— 3/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `ImageScaleToTotalPixels` —— 3/9 个有
- `ImageUpscaleWithModel` —— 3/9 个有
- `Int` —— 3/9 个有
- `UpscaleModelLoader` —— 3/9 个有
- `easy hiresFix` —— 3/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1536 - 1536 | 9 | 100% |
| 高度 | 1152 | 1152 - 1152 | 9 | 100% |
| 采样步数 | 25 | 25 - 25 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1536 - 1536，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
