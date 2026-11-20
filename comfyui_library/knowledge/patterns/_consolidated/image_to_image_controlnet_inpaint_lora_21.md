---
name: image_to_image_controlnet_inpaint_lora_21
type: Image To Image
frequency: 2
level: weak
coverage: 0.764
common_nodes: [AIO_Preprocessor, AddMask, BasicGuider, BasicScheduler, Bjornulf_ShowJson, BlendInpaint, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CutForInpaint, DeepTranslatorTextNode, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptyImage, Fast Groups Bypasser (rgthree), FloatConstant, Florence2Run, FluxGuidance, Get Image Size, GetImageSize, GetImageSize+, GrowMask, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageComposite+, ImageConcanate, ImageConcatMulti, ImageCrop, ImageCrop+, ImageResize+, ImageScale, ImageToMask, ImageTransformPaddingRelative, ImitationHueNode, ImpactDecomposeSEGS, ImpactFrom_SEG_ELT, ImpactFrom_SEG_ELT_crop_region, ImpactSEGSOrderedFilter, InpaintModelConditioning, Int Literal, InvertMask, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LG_ImageSender, LayerColor: Brightness & Contrast, LayerMask: PersonMaskUltra V2, LayerMask: SegformerClothesPipelineLoader, LayerMask: SegformerUltraV2, LayerUtility: ColorImage, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore, LayerUtility: ImageScaleRestore V2, LoadImage, LoraLoader, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, MaskToImage, MaskToSEGS, Note Plus (mtb), PreviewBridge, PreviewImage, RHHiddenNodes, RH_Captioner, RH_ComfyFluxKontext, RandomNoise, RepeatLatentBatch, SEGSPreview, SamplerCustomAdvanced, SaveImage, SimpleMath+, StringConstant, StyleModelApply, StyleModelLoader, SubtractMask, Text Concatenate (JPS), ToBinaryMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy imageScaleDownToSize, easy int, easy mathInt, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/老照片修复最强工作流_1929096263181176833.json, 平台全量/商用级老照片修复进阶版_1915803330847637505.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/老照片修复最强工作流_1929096263181176833.json、平台全量/商用级老照片修复进阶版_1915803330847637505.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddMask`
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_ShowJson`
- `BlendInpaint`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CutForInpaint`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `FloatConstant`
- `Florence2Run`
- `FluxGuidance`
- `Get Image Size`
- `GetImageSize`
- `GetImageSize+`
- `GrowMask`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageComposite+`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageCrop`
- `ImageCrop+`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `ImageTransformPaddingRelative`
- `ImitationHueNode`
- `ImpactDecomposeSEGS`
- `ImpactFrom_SEG_ELT`
- `ImpactFrom_SEG_ELT_crop_region`
- `ImpactSEGSOrderedFilter`
- `InpaintModelConditioning`
- `Int Literal`
- `InvertMask`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `KSamplerSelect`
- `LG_ImageSender`
- `LayerColor: Brightness & Contrast`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegformerClothesPipelineLoader`
- `LayerMask: SegformerUltraV2`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `MaskToImage`
- `MaskToSEGS`
- `Note Plus (mtb)`
- `PreviewBridge`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_ComfyFluxKontext`
- `RandomNoise`
- `RepeatLatentBatch`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `StringConstant`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `Text Concatenate (JPS)`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageScaleDownToSize`
- `easy int`
- `easy mathInt`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
