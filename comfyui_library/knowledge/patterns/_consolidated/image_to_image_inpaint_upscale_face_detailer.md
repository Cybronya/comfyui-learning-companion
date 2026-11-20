---
name: image_to_image_inpaint_upscale_face_detailer
type: Image To Image
frequency: 3
level: strong
coverage: 0.854
common_nodes: [Any Switch (rgthree), Bounded Image Blend with Mask, Bounded Image Crop with Mask, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FaceDetailer, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageCompositeMasked, ImageListToImageBatch, ImageResize+, ImageScale, ImageToMask, ImpactImageBatchToImageList, InpaintCrop, InpaintModelConditioning, InpaintStitch, JWImageResizeByLongerSide, JWMaskResize, KSampler, LayerMask: MaskGrow, LayerMask: SegformerB2ClothesUltra, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore V2, LayerUtility: PurgeVRAM, LoadImage, MaskPreview+, MaskToImage, MathExpression|pysssss, PreviewImage, RepeatLatentBatch, SAMLoader, SaveImage, SetLatentNoiseMask, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy float, easy ifElse, easy imageConcat, easy imageCropFromMask, easy imageSize, easy imageSizeBySide, easy int, easy isMaskEmpty, easy positive, easy seed]
problems: []
missing: []
members: [图片生成/图生图/【RICK团队】万物迁移V2_1906537202107748353.json, 平台全量/RH万物迁移V2_1928284820558725121.json, 平台全量/万物迁移2.0_1954922658841313282.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【RICK团队】万物迁移V2_1906537202107748353.json、平台全量/RH万物迁移V2_1928284820558725121.json、平台全量/万物迁移2.0_1954922658841313282.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bounded Image Blend with Mask`
- `Bounded Image Crop with Mask`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FaceDetailer`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `ImpactImageBatchToImageList`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
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
- `MaskPreview+`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RepeatLatentBatch`
- `SAMLoader`
- `SaveImage`
- `SetLatentNoiseMask`
- `StyleModelApply`
- `StyleModelLoader`
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
- `easy ifElse`
- `easy imageConcat`
- `easy imageCropFromMask`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy int`
- `easy isMaskEmpty`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `JWImageResize` —— 2/3 个有
- `Preview Chooser` —— 2/3 个有
- `easy imageChooser` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.25 | 0.25 - 0.25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 0.25，3 个样本，取值集中（一致性 100%）
