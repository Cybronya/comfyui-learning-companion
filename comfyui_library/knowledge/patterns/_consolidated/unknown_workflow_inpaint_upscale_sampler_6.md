---
name: unknown_workflow_inpaint_upscale_sampler_6
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8464
common_nodes: [Bounded Image Blend with Mask, Bounded Image Crop with Mask, CLIPTextEncode, CLIPVisionLoader, CR Color Panel, CR Upscale Image, DifferentialDiffusion, DualCLIPLoader, GetImageSize+, Image Comparer (rgthree), ImageCompositeMasked, ImageConcanate, ImageToMask, ImpactImageBatchToImageList, InpaintCrop, InpaintModelConditioning, InpaintStitch, JWImageResize, JWImageResizeByLongerSide, KSampler, LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore V2, LoadImage, MaskPreview+, MaskToImage, MathExpression|pysssss, PreviewImage, RepeatLatentBatch, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy ifElse, easy imageConcat, easy imageCropFromMask, easy imageSize, easy imageSizeBySide, easy int, easy isMaskEmpty]
problems: []
missing: []
members: [图片生成/图生图/Flux.1-万物重绘_万物迁移_1982490386239242241.json, 图片生成/图生图/万物迁移换装_1942410924168785921.json, 图片生成/图生图/模特自动换衣 一键换装_换产品_1976462041307324417.json, 平台全量/【大炮VIP】模特自动换衣 一键换装_换产品_1910522308606525442.json, 平台全量/一键自动换装_1908746808808644609.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux.1-万物重绘_万物迁移_1982490386239242241.json、图片生成/图生图/万物迁移换装_1942410924168785921.json、图片生成/图生图/模特自动换衣 一键换装_换产品_1976462041307324417.json、平台全量/【大炮VIP】模特自动换衣 一键换装_换产品_1910522308606525442.json、平台全量/一键自动换装_1908746808808644609.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `Bounded Image Blend with Mask`
- `Bounded Image Crop with Mask`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Color Panel`
- `CR Upscale Image`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageToMask`
- `ImpactImageBatchToImageList`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `JWImageResize`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageConcat`
- `easy imageCropFromMask`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy int`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/5 个有
- `CLIPVisionEncode` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `ImageResize+` —— 3/5 个有
- `JWMaskResize` —— 3/5 个有
- `LayerMask: SegformerB2ClothesUltra` —— 3/5 个有
- `PreviewBridge` —— 3/5 个有
- `StyleModelApply` —— 3/5 个有
- `easy positive` —— 3/5 个有
- `InspyrenetRembg` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `ReduxAdvanced` —— 2/5 个有
- `Note Plus (mtb)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
