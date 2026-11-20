---
name: image_to_image_inpaint_upscale_lora_4
type: Image To Image
frequency: 5
level: strong
coverage: 0.5962
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetImageSize+, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageComposite+, ImageConcanate, ImageCrop, ImageResize+, ImageToMask, ImageUpscaleWithModel, ImpactDecomposeSEGS, ImpactFrom_SEG_ELT, ImpactFrom_SEG_ELT_crop_region, ImpactSEGSOrderedFilter, InpaintModelConditioning, JWImageResizeByLongerSide, KSampler, LayerMask: CreateGradientMask, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleRestore, LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToImage, MaskToSEGS, PreviewImage, SEGSPreview, SaveImage, SetNode, SimpleMath+, StyleModelLoader, ToBinaryMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换头_换脸_换发型 _ 绝对的一致性 自动蒙版_2011806668614541314.json, 平台全量/Redux + Fill ACE ++ 换发型、换头、手动自动蒙版_1889878083548196866.json, 平台全量/换发型_1968866197615857665.json, 平台全量/换装局部logo迁移修复_1956629428665286658.json, 平台全量/龙明Redux+Fill+ACE 换发型、换头、自动蒙版_1928668158121644033.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/换头_换脸_换发型 _ 绝对的一致性 自动蒙版_2011806668614541314.json、平台全量/Redux + Fill ACE ++ 换发型、换头、手动自动蒙版_1889878083548196866.json、平台全量/换发型_1968866197615857665.json、平台全量/换装局部logo迁移修复_1956629428665286658.json、平台全量/龙明Redux+Fill+ACE 换发型、换头、自动蒙版_1928668158121644033.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetImageSize+`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageComposite+`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactDecomposeSEGS`
- `ImpactFrom_SEG_ELT`
- `ImpactFrom_SEG_ELT_crop_region`
- `ImpactSEGSOrderedFilter`
- `InpaintModelConditioning`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerMask: CreateGradientMask`
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: ImageScaleRestore`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `MaskToSEGS`
- `PreviewImage`
- `SEGSPreview`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `StyleModelLoader`
- `ToBinaryMask`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 4/5 个有
- `CLIPVisionLoader` —— 4/5 个有
- `InvertMask` —— 4/5 个有
- `LayerMask: PersonMaskUltra V2` —— 4/5 个有
- `PulidFluxEvaClipLoader` —— 4/5 个有
- `PulidFluxInsightFaceLoader` —— 4/5 个有
- `PulidFluxModelLoader` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `ReduxAdvanced` —— 4/5 个有
- `SaveImageAndMetadata_` —— 4/5 个有
- `UnloadAllModels` —— 4/5 个有
- `AdvancedVisionLoader` —— 1/5 个有
- `CLIPVisionEncode` —— 1/5 个有
- `ICLightApplyMaskGrey` —— 1/5 个有
- `Image To Mask` —— 1/5 个有
- `InvertImageNode` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `MaskBlur+` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `StyleModelApply` —— 1/5 个有
- `easy isMaskEmpty` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.25 | 0.25 - 0.25 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 0.25，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
