---
name: image_to_image_controlnet_inpaint_upscale_7
type: Image To Image
frequency: 2
level: weak
coverage: 0.855
common_nodes: [ApplyInstantID, ApplyPulid, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropFaces, DetailerForEach, DetectFaces, DifferentialDiffusion, FaceAnalysisModels, FaceBoundingBox, Florence2ModelLoader, Florence2Run, GrowMaskWithBlur, Image Comparer (rgthree), Image Crop Face, ImageCompositeMasked, ImageListToImageBatch, ImageResizeKJ, ImageScaleBy, ImageUpscaleWithModel, ImpactMakeImageList, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoader, MaskPreview+, MaskToSEGS, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PreviewImage, PulidFluxEvaClipLoader, PulidFluxFaceDetector, PulidFluxInsightFaceLoader, PulidFluxOptions, PulidInsightFaceLoader, PulidModelLoader, RHHiddenNodes, SaveImage, ShowText|pysssss, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, WarpFacesBack]
problems: []
missing: []
members: [数字人/数字人/旅拍中国0701（无问题 02）_1939947232085118977.json, 数字人/数字人/旅拍中国0701（无问题）_1939895180897984514.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/旅拍中国0701（无问题 02）_1939947232085118977.json、数字人/数字人/旅拍中国0701（无问题）_1939895180897984514.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `ApplyPulid`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `CropFaces`
- `DetailerForEach`
- `DetectFaces`
- `DifferentialDiffusion`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `Florence2ModelLoader`
- `Florence2Run`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `Image Crop Face`
- `ImageCompositeMasked`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactMakeImageList`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `MaskToSEGS`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxFaceDetector`
- `PulidFluxInsightFaceLoader`
- `PulidFluxOptions`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `WarpFacesBack`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.55 | - | 2 | 100% |
| LoRA 模型强度 | 0.65 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.55，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
