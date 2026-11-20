---
name: unknown_workflow_controlnet_ipadapter_inpaint_10
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7915
common_nodes: [BboxToInt, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPTextEncodeFlux, CR Image Input Switch, CR Integer To String, CR Set Value On Boolean, CR Text Blacklist, CR Text Concatenate, CheckpointLoaderSimple, ConditioningZeroOut, Constant Number, ControlNetApplyAdvanced, ControlNetLoader, Convert Masks to Images, DeepTranslatorTextNode, DifferentialDiffusion, Display Any (rgthree), DownloadAndLoadFlorence2Model, DualCLIPLoader, Fast Groups Bypasser (rgthree), Float, Florence2Run, Florence2toCoordinates, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, GrowMaskWithBlur, INPAINT_ApplyFooocusInpaint, INPAINT_LoadFooocusInpaint, INPAINT_MaskedBlur, INPAINT_MaskedFill, INPAINT_VAEEncodeInpaintConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Blending Mode, Image Comparer (rgthree), ImageComposite+, ImageGenResolutionFromImage, ImagePadForOutpaint, ImageScaleBy, ImpactCompare, ImpactSwitch, Int, Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: ColorImage, LayerUtility: CropByMask, LayerUtility: ImageBlend, LayerUtility: ImageCombineAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LaMa, LineArtPreprocessor, LoadImage, LoraLoader|pysssss, MaskComposite, MiDaS-DepthMapPreprocessor, Number Input Condition, PowerPaint, PowerPaintCLIPLoader, PreviewImage, SAMModelLoader (segment anything), SaveImage, ShowText|pysssss, SimpleMath+, SimpleMathDual+, Text Multiline, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/万能商用-参考风格产品换背景_1920348919128064002.json, 平台全量/新手友好-参考风格产品换背景-测试版_1923848361927954434.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_inpaint_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/万能商用-参考风格产品换背景_1920348919128064002.json、平台全量/新手友好-参考风格产品换背景-测试版_1923848361927954434.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BboxToInt`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Image Input Switch`
- `CR Integer To String`
- `CR Set Value On Boolean`
- `CR Text Blacklist`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Constant Number`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Convert Masks to Images`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `Display Any (rgthree)`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `Florence2Run`
- `Florence2toCoordinates`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `GrowMaskWithBlur`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_MaskedBlur`
- `INPAINT_MaskedFill`
- `INPAINT_VAEEncodeInpaintConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Blending Mode`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImageGenResolutionFromImage`
- `ImagePadForOutpaint`
- `ImageScaleBy`
- `ImpactCompare`
- `ImpactSwitch`
- `Int`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerUtility: ColorImage`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageCombineAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LaMa`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader|pysssss`
- `MaskComposite`
- `MiDaS-DepthMapPreprocessor`
- `Number Input Condition`
- `PowerPaint`
- `PowerPaintCLIPLoader`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SaveImage`
- `ShowText|pysssss`
- `SimpleMath+`
- `SimpleMathDual+`
- `Text Multiline`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
