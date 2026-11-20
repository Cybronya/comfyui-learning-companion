---
name: text_to_image_lora_sampler_clip_66
type: Text To Image
frequency: 17
level: strong
coverage: 0.897529
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetImageSize+, ImageStitch, KSampler, LayerMask: BenUltra, LayerMask: LoadBenModel, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReferenceLatent, SaveImage, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 换装秀【先脱后穿】_1954810397346848770.json, 图片生成/图生图/Kontext 精准换装_1955445547281760258.json, 图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json, 图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json, 图片生成/图生图/Kontext换装丨一致性换装丨一键换装！！_1981234234969022466.json, 图片生成/图生图/换装秀_1952195949659631617.json, 图片生成/图生图/模特一键换衣服+电商带货+产品展示（优化版-3.0）_2022618537390514178.json, 图片生成/图生图/模特一键换衣服+电商带货+产品展示（优化版-3.0）_2063497732433727490.json, 图片生成/图生图/电商版-最强模特换装流_1964547496225722369.json, 平台全量/004.换装_2004398379738300418.json, 平台全量/Kontext 换装秀2.0_1952931440989302785.json, 平台全量/Kontext 换装秀2.0_1952932357901905922.json, 平台全量/Kontext 换装秀3.0 --之单独换裤子_1943971398694080513.json, 平台全量/Kontext 换装秀3.0- 之单独换上衣_1943968169235189761.json, 平台全量/Kontext 换装秀3.0--之换全套_1943964273808670721.json, 平台全量/Kontext 换装秀4.0_1944965304159232001.json, 平台全量/空白工作流_1955077560399007745.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Kontext 换装秀【先脱后穿】_1954810397346848770.json、图片生成/图生图/Kontext 精准换装_1955445547281760258.json、图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json、图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json、图片生成/图生图/Kontext换装丨一致性换装丨一键换装！！_1981234234969022466.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetImageSize+`
- `ImageStitch`
- `KSampler`
- `LayerMask: BenUltra`
- `LayerMask: LoadBenModel`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `FluxKontextImageScale` —— 16/17 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 16/17 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 16/17 个有
- `LayerUtility: JoyCaptionBeta1` —— 15/17 个有
- `LayerUtility: ImageReelComposit` —— 13/17 个有
- `PreviewImage` —— 13/17 个有
- `LayerUtility: ImageReel` —— 12/17 个有
- `easy showAnything` —— 11/17 个有
- `AddMask` —— 4/17 个有
- `ClothesSegment` —— 4/17 个有
- `Image Comparer (rgthree)` —— 4/17 个有
- `ImageAndMaskPreview` —— 4/17 个有
- `LayerMask: PersonMaskUltra V2` —— 4/17 个有
- `Anything Everywhere` —— 3/17 个有
- `ImageScaleToTotalPixels` —— 3/17 个有
- `ImageUpscaleWithModel` —— 3/17 个有
- `Int` —— 3/17 个有
- `UpscaleModelLoader` —— 3/17 个有
- `easy hiresFix` —— 3/17 个有
- `Note Plus (mtb)` —— 2/17 个有
- `CropByMask` —— 1/17 个有
- `Qwen3_VQA` —— 1/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `RH_Translator` —— 1/17 个有
- `ShowAnything|Mie` —— 1/17 个有
- `SubtractMask` —— 1/17 个有
- `easy anythingIndexSwitch` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1536 - 1536 | 17 | 100% |
| 高度 | 1152 | 1152 - 1152 | 17 | 100% |
| 采样步数 | 25 | 12 - 25 | 17 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1536 - 1536，17 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 12 - 25，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
