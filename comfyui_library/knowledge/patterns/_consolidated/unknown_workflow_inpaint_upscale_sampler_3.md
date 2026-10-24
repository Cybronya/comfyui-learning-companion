---
name: unknown_workflow_inpaint_upscale_sampler_3
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.768833
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncodeFlux, CLIPVisionEncode, CLIPVisionLoader, DeepTranslatorTextNode, DifferentialDiffusion, FluxGuidance, GrowMaskWithBlur, INPAINT_InpaintWithModel, INPAINT_LoadInpaintModel, Image Blend by Mask, Image Comparer (rgthree), Image Power Noise, ImageMaskSwitch, ImagePadForOutpaintMasked, ImageScaleBy, InpaintModelConditioning, Int, KSamplerSelect, LoadImage, MaskToImage, MathExpression|pysssss, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StyleModelApply, StyleModelLoader, Textbox, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/flux扩图工作流 小白友好_1913607036645638146.json, 图片生成/图生图/扩图 _ 高级版（2张）_1915341673960767489.json, 图片生成/图生图/扩图_1923358810663284737.json, 图片生成/图生图/扩图_FLUX.filI_2042992092460359681.json, 图片生成/图生图/扩图_FLUX.fill_1896400597204008961.json, 图片生成/图生图/扩图·优化版 _ Nunchaku提速（2张）_1911225941106880514.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/flux扩图工作流 小白友好_1913607036645638146.json、图片生成/图生图/扩图 _ 高级版（2张）_1915341673960767489.json、图片生成/图生图/扩图_1923358810663284737.json、图片生成/图生图/扩图_FLUX.filI_2042992092460359681.json、图片生成/图生图/扩图_FLUX.fill_1896400597204008961.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncodeFlux`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadInpaintModel`
- `Image Blend by Mask`
- `Image Comparer (rgthree)`
- `Image Power Noise`
- `ImageMaskSwitch`
- `ImagePadForOutpaintMasked`
- `ImageScaleBy`
- `InpaintModelConditioning`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `Textbox`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `RepeatImageBatch` —— 5/6 个有
- `CLIPTextEncode` —— 3/6 个有
- `DualCLIPLoader` —— 3/6 个有
- `ImageBatch` —— 3/6 个有
- `JoinImageWithAlpha` —— 3/6 个有
- `LayerUtility: ColorImage V2` —— 3/6 个有
- `LayerUtility: ImageBlend` —— 3/6 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `NunchakuFluxDiTLoader` —— 3/6 个有
- `NunchakuFluxLoraLoader` —— 3/6 个有
- `NunchakuTextEncoderLoader` —— 3/6 个有
- `SamplerCustom` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `easy seed` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `ImpactSwitch` —— 1/6 个有
- `LayerUtility: BooleanOperator` —— 1/6 个有
- `Note _O` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `TextBox` —— 1/6 个有
- `easy ifElse` —— 1/6 个有
- `easy imageSizeBySide` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
