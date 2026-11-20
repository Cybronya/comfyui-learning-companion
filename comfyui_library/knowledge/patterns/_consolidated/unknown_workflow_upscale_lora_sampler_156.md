---
name: unknown_workflow_upscale_lora_sampler_156
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.525
common_nodes: [APersonMaskGenerator, AdvancedLyingSigmaSampler, ApplyPulidFlux, ApplyTeaCachePatch, BasicGuider, BasicScheduler, BoolOperationNode, CFGGuider, CLIPTextEncode, CLIPVisionLoader, CR Overlay Text, CR Simple Image Compare, ConditioningZeroOut, DepthAnything_V2, DisplayAny, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, ETN_CropImage, FashionSegmentAccessories, FashionSegmentClothing, Float, FluxForwardOverrider, FluxGuidance, GetImageSize+, GetNode, GrowMaskWithBlur, INTConstant, Image Comparer (rgthree), ImageAndMaskPreview, ImageCompositeFromMaskBatch+, ImageCompositeMasked, ImageConcanate, ImageResize+, ImageSharpen, ImageToMask, ImpactCompare, ImpactExecutionOrderController, ImpactIsNotEmptySEGS, ImpactSimpleDetectorSEGS, InstructPixToPixConditioning, InvertMask, IsMaskEmpty, JWImageResizeByLongerSide, KSamplerSelect, LayerMask: BenUltra, LayerMask: LoadBenModel, LayerUtility: BooleanOperator, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V3, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageShift, LayerUtility: LaMa, List of any [Crystools], List of strings [Crystools], LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToImage, MaskToSEGS, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RandomNoise, ReActorFaceSwap, ReduxAdvanced, SAMLoader, SEGSDetailer, SEGSPaste, SEGSPreview, SamplerCustomAdvanced, SaveImage, SegsToCombinedMask, SetNode, ShowText|pysssss, SimpleMath+, StyleModelLoader, Text Input [Dream], ToBasicPipe, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UnetLoaderGGUF, UnloadAllModels, UpscaleModelLoader, VAEDecode, VAELoader, WidthHeightPicker, easy cleanGpuUsed, easy convertAnything, easy ifElse, easy imageToBase64, easy showAnything]
problems: []
missing: []
members: [平台全量/人物、姿态、背景、衣服，4合一_1889201955170934785.json, 平台全量/（new）人物、姿态、背景、衣服，4合一_1897357074311892994.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_156

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人物、姿态、背景、衣服，4合一_1889201955170934785.json、平台全量/（new）人物、姿态、背景、衣服，4合一_1897357074311892994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `APersonMaskGenerator`
- `AdvancedLyingSigmaSampler`
- `ApplyPulidFlux`
- `ApplyTeaCachePatch`
- `BasicGuider`
- `BasicScheduler`
- `BoolOperationNode`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Overlay Text`
- `CR Simple Image Compare`
- `ConditioningZeroOut`
- `DepthAnything_V2`
- `DisplayAny`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `ETN_CropImage`
- `FashionSegmentAccessories`
- `FashionSegmentClothing`
- `Float`
- `FluxForwardOverrider`
- `FluxGuidance`
- `GetImageSize+`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageCompositeFromMaskBatch+`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageResize+`
- `ImageSharpen`
- `ImageToMask`
- `ImpactCompare`
- `ImpactExecutionOrderController`
- `ImpactIsNotEmptySEGS`
- `ImpactSimpleDetectorSEGS`
- `InstructPixToPixConditioning`
- `InvertMask`
- `IsMaskEmpty`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LayerMask: BenUltra`
- `LayerMask: LoadBenModel`
- `LayerUtility: BooleanOperator`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageShift`
- `LayerUtility: LaMa`
- `List of any [Crystools]`
- `List of strings [Crystools]`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `MaskToSEGS`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `ReActorFaceSwap`
- `ReduxAdvanced`
- `SAMLoader`
- `SEGSDetailer`
- `SEGSPaste`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SegsToCombinedMask`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `StyleModelLoader`
- `Text Input [Dream]`
- `ToBasicPipe`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UnetLoaderGGUF`
- `UnloadAllModels`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `WidthHeightPicker`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy ifElse`
- `easy imageToBase64`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `ImageComposite+` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImpactDecomposeSEGS` —— 1/2 个有
- `ImpactFrom_SEG_ELT` —— 1/2 个有
- `ImpactFrom_SEG_ELT_crop_region` —— 1/2 个有
- `ImpactSEGSOrderedFilter` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LayerMask: CreateGradientMask` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/2 个有
- `LayerUtility: ImageScaleRestore` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `ToBinaryMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
