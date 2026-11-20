---
name: text_to_image_inpaint_upscale_face_detailer
type: Text To Image
frequency: 2
level: weak
coverage: 0.857
common_nodes: [Any Switch (rgthree), Bounded Image Blend with Mask, Bounded Image Crop with Mask, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, FaceDetailer, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageCompositeMasked, ImageCrop, ImageFromBatch+, ImageListToImageBatch, ImageResize+, ImageScale, ImageToMask, ImageUpscaleWithModel, ImpactMakeImageBatch, InpaintCrop, InpaintModelConditioning, InpaintStitch, JWImageResize, JWImageResizeByLongerSide, JWMaskResize, KSampler, LayerMask: MaskGrow, LayerMask: SegformerB2ClothesUltra, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToImage, MathExpression|pysssss, PreviewImage, SAMLoader, SaveImage, SetLatentNoiseMask, ShowText|pysssss, StyleModelApply, StyleModelLoader, TTP_text_mix, Text Concatenate, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy float, easy forLoopEnd, easy forLoopStart, easy imageBatchToImageList, easy imageConcat, easy imageCropFromMask, easy imageSize, easy imageSizeBySide, easy int, easy positive, easy seed]
problems: []
missing: []
members: [平台全量/【RICK团队】万物主图V2_1906540571689947137.json, 平台全量/电商模特主图一致性换服装_1900484590195351554.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【RICK团队】万物主图V2_1906540571689947137.json、平台全量/电商模特主图一致性换服装_1900484590195351554.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bounded Image Blend with Mask`
- `Bounded Image Crop with Mask`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageCrop`
- `ImageFromBatch+`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactMakeImageBatch`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `JWImageResize`
- `JWImageResizeByLongerSide`
- `JWMaskResize`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `TTP_text_mix`
- `Text Concatenate`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageBatchToImageList`
- `easy imageConcat`
- `easy imageCropFromMask`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy int`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Preview Chooser` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.2 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
