---
name: unknown_workflow_ipadapter_sampler_clip_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.718
common_nodes: [AlignYourStepsScheduler, Automatic CFG, CLIPTextEncode, CM_NumberBinaryOperation, CM_NumberToInt, CR Image Grid Panel, CR Text, CheckpointLoaderSimple, ColorMatch, ConcatText_Zho, DF_Image_scale_to_side, DF_Integer, DetailTransfer, EmptyLatentImage, GetImageSize+, GrowMask, ICLightApplyMaskGrey, ICLightConditioning, Image Blend by Mask, Image Blending Mode, Image Levels Adjustment, ImageCompositeAbsolute, ImageCompositeMasked, ImageGaussianBlur, ImageGenResolutionFromImage, ImageInvert, ImpactGaussianBlurMask, Int To Number (mtb), KSamplerSelect, LayerUtility: ExtendCanvas, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PreviewImage, SamplerCustom, SaveImage, Simple String, SplitImageWithAlpha, Text _O, Text to Number, VAEDecode, VAEEncodeArgMax, easy ipadapterApply]
problems: []
missing: []
members: [图片生成/图生图/一键拍立得｜一键生成系列_1908894397214109697.json, 平台全量/拍立得人像_1816298113677123585.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键拍立得｜一键生成系列_1908894397214109697.json、平台全量/拍立得人像_1816298113677123585.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `AlignYourStepsScheduler`
- `Automatic CFG`
- `CLIPTextEncode`
- `CM_NumberBinaryOperation`
- `CM_NumberToInt`
- `CR Image Grid Panel`
- `CR Text`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConcatText_Zho`
- `DF_Image_scale_to_side`
- `DF_Integer`
- `DetailTransfer`
- `EmptyLatentImage`
- `GetImageSize+`
- `GrowMask`
- `ICLightApplyMaskGrey`
- `ICLightConditioning`
- `Image Blend by Mask`
- `Image Blending Mode`
- `Image Levels Adjustment`
- `ImageCompositeAbsolute`
- `ImageCompositeMasked`
- `ImageGaussianBlur`
- `ImageGenResolutionFromImage`
- `ImageInvert`
- `ImpactGaussianBlurMask`
- `Int To Number (mtb)`
- `KSamplerSelect`
- `LayerUtility: ExtendCanvas`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `Simple String`
- `SplitImageWithAlpha`
- `Text _O`
- `Text to Number`
- `VAEDecode`
- `VAEEncodeArgMax`
- `easy ipadapterApply`

**可变部分**（部分 workflow 才有）：
- `BRIA_RMBG_ModelLoader_Zho` —— 1/2 个有
- `BRIA_RMBG_Zho` —— 1/2 个有
- `CR Color Panel` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `LayerUtility: TextImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `Text_Image_Multiline_Zho` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
