---
name: image_to_image_ipadapter_inpaint_upscale
type: Image To Image
frequency: 2
level: weak
coverage: 0.897
common_nodes: [AddMask, BasicGuider, BasicScheduler, BrushNet, BrushNetLoader, CLIPTextEncode, CR Simple Image Compare, CR Text Concatenate, CR Upscale Image, CheckpointLoaderSimple, ConditioningZeroOut, DSINE-NormalMapPreprocessor, DeepTranslatorTextNode, DetailTransfer, DifferentialDiffusion, DisableNoise, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageResizeKJ, InjectLatentNoise+, InpaintModelConditioning, InvertMask, JoinImageWithAlpha, KSampler, KSamplerSelect, LG_Relight_Basic, Label (rgthree), LayerColor: Brightness & Contrast, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: LoadFlorence2Model, LayerMask: MaskEdgeShrink, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ExtendCanvas, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageBlend, LayerUtility: ImageScaleRestore V2, LayerUtility: LaMa, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskPreview+, PreviewBridge, PreviewImage, RandomNoise, RepeatLatentBatch, ResizeMask, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SplitSigmasDenoise, SubtractMask, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imagePixelPerfect]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/【电商】🐳🐧产品换背景【顶级万能版】_1892037512263798785.json, 平台全量/【电商】🐳🐧服装换人换背景【顶级版工作流】_1893198505786421249.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【电商】🐳🐧产品换背景【顶级万能版】_1892037512263798785.json、平台全量/【电商】🐳🐧服装换人换背景【顶级版工作流】_1893198505786421249.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `BasicGuider`
- `BasicScheduler`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `CR Text Concatenate`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DSINE-NormalMapPreprocessor`
- `DeepTranslatorTextNode`
- `DetailTransfer`
- `DifferentialDiffusion`
- `DisableNoise`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `InjectLatentNoise+`
- `InpaintModelConditioning`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSampler`
- `KSamplerSelect`
- `LG_Relight_Basic`
- `Label (rgthree)`
- `LayerColor: Brightness & Contrast`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskEdgeShrink`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: LaMa`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewBridge`
- `PreviewImage`
- `RandomNoise`
- `RepeatLatentBatch`
- `ResizeMask`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `SubtractMask`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imagePixelPerfect`

**可变部分**（部分 workflow 才有）：
- `ACN_AdvancedControlNetApply_v2` —— 1/2 个有
- `AnyLineArtPreprocessor_aux` —— 1/2 个有
- `Color (hexadecimal)` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `DetailDaemonSamplerNode` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageComposite+` —— 1/2 个有
- `ImageCrop+` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 1/2 个有
- `LayerMask: SegformerUltraV2` —— 1/2 个有
- `LayerStyle: ColorOverlay V2` —— 1/2 个有
- `LayerUtility: CropBoxResolve` —— 1/2 个有
- `LayerUtility: CropByMask` —— 1/2 个有
- `PowerPaint` —— 1/2 个有
- `PowerPaintCLIPLoader` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TeaCache` —— 1/2 个有
- `Text Find and Replace` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.95 | - | 1 | 100% |
| 采样步数 | 8.5 | - | 2 | 94% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 67% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
