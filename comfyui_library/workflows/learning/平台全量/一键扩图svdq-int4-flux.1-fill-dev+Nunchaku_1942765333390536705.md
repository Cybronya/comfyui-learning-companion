---
key: 平台全量/一键扩图svdq-int4-flux.1-fill-dev+Nunchaku_1942765333390536705.json
name: 一键扩图svdq-int4-flux.1-fill-dev+Nunchaku_1942765333390536705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键扩图svdq-int4-flux.1-fill-dev+Nunchaku_1942765333390536705.json
hash: d79717a458aba98a
coverage: 0.782609
learned_at: 2026-11-14 01:27:59
nodes: [MathExpression|pysssss, Reroute, RandomNoise, Reroute, easy imageSize, Reroute, easy imageSize, ShowText|pysssss, ShowText|pysssss, BasicScheduler, ImagePadForOutpaintMasked, INPAINT_LoadInpaintModel, UpscaleModelLoader, easy imageSize, Image Power Noise, INPAINT_InpaintWithModel, MaskToImage, Reroute, CLIPVisionEncode, KSamplerSelect, InpaintModelConditioning, Image Blend by Mask, RepeatImageBatch, NunchakuFluxDiTLoader, DeepTranslatorTextNode, VAELoader, NunchakuTextEncoderLoader, Reroute, CLIPTextEncodeFlux, CLIPTextEncodeFlux, Reroute, CLIPTextEncode, CLIPTextEncode, FluxGuidance, SamplerCustomAdvanced, RandomNoise, StyleModelApply, CFGGuider, CFGGuider, SamplerCustomAdvanced, RandomNoise, CLIPVisionEncode, RandomNoise, CLIPVisionEncode, SamplerCustomAdvanced, VAEEncode, KSamplerSelect, VAEEncode, SamplerCustomAdvanced, Reroute, CLIPVisionLoader, Reroute, Reroute, StyleModelLoader, Reroute, Reroute, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, DifferentialDiffusion, easy cleanGpuUsed, Int, Reroute, Reroute, VAEDecode, VAEDecode, VAEDecode, VAEDecode, LayerUtility: ImageMaskScaleAs, PreviewImage, ImageBatch, ImageBatch, PreviewImage, GrowMaskWithBlur, Reroute, LayerUtility: ImageMaskScaleAs, easy cleanGpuUsed, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageBlend, easy cleanGpuUsed, Reroute, Reroute, easy cleanGpuUsed, LayerUtility: ImageMaskScaleAs, GrowMaskWithBlur, JoinImageWithAlpha, JoinImageWithAlpha, LayerUtility: ImageBlend, easy cleanGpuUsed, PreviewImage, easy cleanGpuUsed, BasicScheduler, CFGGuider, StyleModelApply, FluxGuidance, LayerUtility: ImageBlend, SaveImage, Textbox, StyleModelApply, FluxGuidance, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, MathExpression|pysssss, easy imageSize, MathExpression|pysssss, RH_Captioner, ImageMaskSwitch, PrimitiveString, ImpactSwitch, ImagePadForOutpaintMasked, ImageScaleBy, PrimitiveFloat, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
---

# 平台全量/一键扩图svdq-int4-flux.1-fill-dev+Nunchaku_1942765333390536705.json

> 来源文件 `comfyui_library/workflows/平台全量/一键扩图svdq-int4-flux.1-fill-dev+Nunchaku_1942765333390536705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（115 个）：
- `MathExpression|pysssss`
- `Reroute`
- `RandomNoise`
- `Reroute`
- `easy imageSize`
- `Reroute`
- `easy imageSize`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `BasicScheduler`
- `ImagePadForOutpaintMasked`
- `INPAINT_LoadInpaintModel`
- `UpscaleModelLoader`
- `easy imageSize`
- `Image Power Noise`
- `INPAINT_InpaintWithModel`
- `MaskToImage`
- `Reroute`
- `CLIPVisionEncode`
- `KSamplerSelect` ★核心
- `InpaintModelConditioning`
- `Image Blend by Mask`
- `RepeatImageBatch`
- `NunchakuFluxDiTLoader`
- `DeepTranslatorTextNode`
- `VAELoader`
- `NunchakuTextEncoderLoader`
- `Reroute`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncodeFlux` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `StyleModelApply`
- `CFGGuider`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CLIPVisionEncode`
- `RandomNoise`
- `CLIPVisionEncode`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `CLIPVisionLoader`
- `Reroute`
- `Reroute`
- `StyleModelLoader`
- `Reroute`
- `Reroute`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `DifferentialDiffusion`
- `easy cleanGpuUsed`
- `Int`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageMaskScaleAs`
- `PreviewImage`
- `ImageBatch`
- `ImageBatch`
- `PreviewImage`
- `GrowMaskWithBlur`
- `Reroute`
- `LayerUtility: ImageMaskScaleAs`
- `easy cleanGpuUsed`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageBlend`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `LayerUtility: ImageMaskScaleAs`
- `GrowMaskWithBlur`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `LayerUtility: ImageBlend`
- `easy cleanGpuUsed`
- `PreviewImage`
- `easy cleanGpuUsed`
- `BasicScheduler`
- `CFGGuider`
- `StyleModelApply`
- `FluxGuidance`
- `LayerUtility: ImageBlend`
- `SaveImage`
- `Textbox`
- `StyleModelApply`
- `FluxGuidance`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `MathExpression|pysssss`
- `easy imageSize`
- `MathExpression|pysssss`
- `RH_Captioner`
- `ImageMaskSwitch`
- `PrimitiveString`
- `ImpactSwitch`
- `ImagePadForOutpaintMasked`
- `ImageScaleBy`
- `PrimitiveFloat`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 知识

覆盖率 **78%**（90/115）

**有卡**：`MathExpression|pysssss`、`RandomNoise`、`easy imageSize`、`BasicScheduler`、`ImagePadForOutpaintMasked`、`INPAINT_LoadInpaintModel`、`UpscaleModelLoader`、`Image Power Noise`、`INPAINT_InpaintWithModel`、`MaskToImage`、`CLIPVisionEncode`、`KSamplerSelect`、`InpaintModelConditioning`、`Image Blend by Mask`、`RepeatImageBatch`、`NunchakuFluxDiTLoader`、`DeepTranslatorTextNode`、`VAELoader`、`NunchakuTextEncoderLoader`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`FluxGuidance`、`SamplerCustomAdvanced`、`StyleModelApply`、`CFGGuider`、`VAEEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`NunchakuFluxLoraLoader`、`DifferentialDiffusion`、`easy cleanGpuUsed`、`Int`、`VAEDecode`、`LayerUtility: ImageMaskScaleAs`、`ImageBatch`、`GrowMaskWithBlur`、`LayerUtility: ImageBlend`、`JoinImageWithAlpha`、`SaveImage`、`Textbox`、`LayerUtility: ColorImage V2`、`RH_Captioner`、`ImageMaskSwitch`、`ImageScaleBy`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、CFGGuider、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
