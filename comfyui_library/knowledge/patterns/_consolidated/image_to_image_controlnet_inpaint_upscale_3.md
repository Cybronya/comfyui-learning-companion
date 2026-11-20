---
name: image_to_image_controlnet_inpaint_upscale_3
type: Image To Image
frequency: 5
level: strong
coverage: 0.855
common_nodes: [ApplyInstantID, ApplyPulid, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropFaces, DetailerForEach, DetectFaces, DifferentialDiffusion, FaceAnalysisModels, FaceBoundingBox, Florence2ModelLoader, Florence2Run, GrowMaskWithBlur, Image Comparer (rgthree), Image Crop Face, ImageCompositeMasked, ImageListToImageBatch, ImageResizeKJ, ImageScaleBy, ImageUpscaleWithModel, ImpactMakeImageList, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoader, MaskPreview+, MaskToSEGS, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PreviewImage, PulidFluxEvaClipLoader, PulidFluxFaceDetector, PulidFluxInsightFaceLoader, PulidFluxOptions, PulidInsightFaceLoader, PulidModelLoader, RHHiddenNodes, SaveImage, ShowText|pysssss, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, WarpFacesBack]
problems: []
missing: []
members: [平台全量/旅拍中国 1 张版本_1932314680440909825.json, 平台全量/旅拍中国_1930656665035845633.json, 平台全量/旅拍中国（无 nacha）_1939889769537310722.json, 数字人/数字人/旅拍中国0701（无问题 02）_1939947232085118977.json, 数字人/数字人/旅拍中国0701（无问题）_1939895180897984514.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/旅拍中国 1 张版本_1932314680440909825.json、平台全量/旅拍中国_1930656665035845633.json、平台全量/旅拍中国（无 nacha）_1939889769537310722.json、数字人/数字人/旅拍中国0701（无问题 02）_1939947232085118977.json、数字人/数字人/旅拍中国0701（无问题）_1939895180897984514.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
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
| 采样步数 | 11 | 11 - 11 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 0.55 | 0.55 - 0.55 | 5 | 100% |
| LoRA 模型强度 | 0.65 | 0.65 - 0.65 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 11，观测区间 11 - 11，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 0.55，观测区间 0.55 - 0.55，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.65，观测区间 0.65 - 0.65，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
