---
name: text_to_image_controlnet_inpaint_lora_9
type: Text To Image
frequency: 2
level: weak
coverage: 0.611
common_nodes: [Anything Everywhere, CLIPTextEncode, CLIPVisionLoader, CM_FloatToInt, CM_SDXLResolution, CR Color Panel, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FloatSlider, FluxGuidance, GetNode, Image Blend by Mask, Image Comparer (rgthree), ImageCompositeMasked, ImageConcanate, ImageListToBatch+, ImageResizeKJ, Images to RGB, ImpactConditionalBranch, InvertMask, InvertMask (segment anything), KSampler, KSampler (Efficient), LayerColor: ColorAdapter, LayerMask: MaskStroke, LayerMask: SegmentAnythingUltra V2, LayerUtility: GetColorToneV2, LayerUtility: ImageBlendAdvance V2, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LaMa, LayerUtility: NumberCalculatorV2, LayerUtility: Seed, LoadImage, LoraLoader, LoraLoaderModelOnly, MaskComposite, MaskToImage, PreviewBridge, PreviewImage, PrimitiveInt, RH_Captioner, ReduxAdvanced, ReferenceLatent, SaveImage, SetNode, ShowText, StringFunction|pysssss, StyleModelLoader, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/产品换背景商用级细节完美保留＋sota级产品高清放大v1_1966038533418946562.json, 平台全量/产品换背景商用级细节完美保留＋sota级产品高清放大v2_1966428977495781377.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品换背景商用级细节完美保留＋sota级产品高清放大v1_1966038533418946562.json、平台全量/产品换背景商用级细节完美保留＋sota级产品高清放大v2_1966428977495781377.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CM_FloatToInt`
- `CM_SDXLResolution`
- `CR Color Panel`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FloatSlider`
- `FluxGuidance`
- `GetNode`
- `Image Blend by Mask`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageListToBatch+`
- `ImageResizeKJ`
- `Images to RGB`
- `ImpactConditionalBranch`
- `InvertMask`
- `InvertMask (segment anything)`
- `KSampler`
- `KSampler (Efficient)`
- `LayerColor: ColorAdapter`
- `LayerMask: MaskStroke`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: GetColorToneV2`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LaMa`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: Seed`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `MaskToImage`
- `PreviewBridge`
- `PreviewImage`
- `PrimitiveInt`
- `RH_Captioner`
- `ReduxAdvanced`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `ShowText`
- `StringFunction|pysssss`
- `StyleModelLoader`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `DetailTransfer` —— 1/2 个有
- `ICLightConditioning` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `LayerColor: AutoAdjustV2` —— 1/2 个有
- `LayerColor: Brightness & Contrast` —— 1/2 个有
- `LayerColor: Color of Shadow & Highlight` —— 1/2 个有
- `LayerFilter: GaussianBlur` —— 1/2 个有
- `LayerMask: Shadow & Highlight Mask` —— 1/2 个有
- `LayerMask: TransparentBackgroundUltra` —— 1/2 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadAndApplyICLightUnet` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy ipadapterApply` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 25% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.96 | - | 2 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.96，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
