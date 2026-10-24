---
name: image_to_image_controlnet_inpaint_lora_18
type: Image To Image
frequency: 2
level: weak
coverage: 0.849
common_nodes: [Anything Everywhere, ApplyPulidFlux, CLIPTextEncode, CLIPVisionLoader, CM_FloatToInt, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DualCLIPLoader, FluxGuidance, GetImageSize+, GrowMask, Image Resize Factor (mtb), ImageCompositeMasked, ImageConcanate, ImageCrop, ImageResize+, ImpactInt, InpaintModelConditioning, InvertMask, KSampler, LamaRemover, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: LoadSegmentAnythingModels, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerMask: SegmentAnythingUltra V2, LayerMask: SegmentAnythingUltra V3, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: CropByMask, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, PreviewImage, PulidEvaClipLoader, PulidFluxModelLoader, PulidInsightFaceLoader, ReduxAdvanced, SaveImage, SetUnionControlNetType, StyleModelLoader, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/人像动作迁移（还原背景）_1914728499343519746.json, 图片生成/图生图/人物动作迁移（还原背景）_1925759600254226433.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人像动作迁移（还原背景）_1914728499343519746.json、图片生成/图生图/人物动作迁移（还原背景）_1925759600254226433.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CM_FloatToInt`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `GrowMask`
- `Image Resize Factor (mtb)`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImpactInt`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `LamaRemover`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: CropByMask`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidInsightFaceLoader`
- `ReduxAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy makeImageForICLora`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.4 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
