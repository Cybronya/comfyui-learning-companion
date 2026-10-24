---
key: 图片生成/图生图/扩图_FLUX.filI_2042992092460359681.json
name: 扩图_FLUX.filI_2042992092460359681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/扩图_FLUX.filI_2042992092460359681.json
hash: 5369cf6b3964c98f
coverage: 0.74359
learned_at: 2026-10-23 12:53:55
nodes: [VAELoader, MathExpression|pysssss, MathExpression|pysssss, DeepTranslatorTextNode, Reroute, Reroute, RandomNoise, easy imageSize, Label (rgthree), Label (rgthree), DualCLIPLoader, Reroute, ImageScaleBy, Image Comparer (rgthree), PreviewImage, CFGGuider, DifferentialDiffusion, easy imageSize, UNETLoader, easy imageSize, MathExpression|pysssss, ImagePadForOutpaintMasked, ImageMaskSwitch, LoadImage, ShowText|pysssss, Reroute, ShowText|pysssss, PreviewImage, BasicScheduler, Textbox, CLIPTextEncodeFlux, ImagePadForOutpaintMasked, easy seed, StyleModelApply, StyleModelLoader, Reroute, LoraLoaderModelOnly, VAEDecode, Image Comparer (rgthree), UNETLoader, SamplerCustom, KSamplerSelect, FluxGuidance, INPAINT_LoadInpaintModel, UpscaleModelLoader, easy imageSize, Image Power Noise, INPAINT_InpaintWithModel, PreviewImage, MaskToImage, PreviewImage, PreviewImage, Reroute, GrowMaskWithBlur, Reroute, Reroute, SaveImage, VAEDecode, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, SamplerCustomAdvanced, KSamplerSelect, VAEEncode, CLIPVisionLoader, InpaintModelConditioning, Image Blend by Mask, Reroute, RepeatImageBatch, Int, RH_Captioner, Textbox, CLIPTextEncodeFlux, Reroute, Reroute, BasicScheduler, StyleModelApply, FluxGuidance]
patterns: []
missing: []
---

# 图片生成/图生图/扩图_FLUX.filI_2042992092460359681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/扩图_FLUX.filI_2042992092460359681.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `VAELoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `DeepTranslatorTextNode`
- `Reroute`
- `Reroute`
- `RandomNoise`
- `easy imageSize`
- `Label (rgthree)`
- `Label (rgthree)`
- `DualCLIPLoader`
- `Reroute`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `CFGGuider`
- `DifferentialDiffusion`
- `easy imageSize`
- `UNETLoader` ★核心
- `easy imageSize`
- `MathExpression|pysssss`
- `ImagePadForOutpaintMasked`
- `ImageMaskSwitch`
- `LoadImage`
- `ShowText|pysssss`
- `Reroute`
- `ShowText|pysssss`
- `PreviewImage`
- `BasicScheduler`
- `Textbox`
- `CLIPTextEncodeFlux` ★核心
- `ImagePadForOutpaintMasked`
- `easy seed`
- `StyleModelApply`
- `StyleModelLoader`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `INPAINT_LoadInpaintModel`
- `UpscaleModelLoader`
- `easy imageSize`
- `Image Power Noise`
- `INPAINT_InpaintWithModel`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `GrowMaskWithBlur`
- `Reroute`
- `Reroute`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `CLIPVisionLoader`
- `InpaintModelConditioning`
- `Image Blend by Mask`
- `Reroute`
- `RepeatImageBatch`
- `Int`
- `RH_Captioner`
- `Textbox`
- `CLIPTextEncodeFlux` ★核心
- `Reroute`
- `Reroute`
- `BasicScheduler`
- `StyleModelApply`
- `FluxGuidance`

## 知识

覆盖率 **74%**（58/78）

**有卡**：`VAELoader`、`MathExpression|pysssss`、`DeepTranslatorTextNode`、`RandomNoise`、`easy imageSize`、`Label (rgthree)`、`DualCLIPLoader`、`ImageScaleBy`、`CFGGuider`、`DifferentialDiffusion`、`UNETLoader`、`ImagePadForOutpaintMasked`、`ImageMaskSwitch`、`LoadImage`、`BasicScheduler`、`Textbox`、`CLIPTextEncodeFlux`、`easy seed`、`StyleModelApply`、`StyleModelLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SamplerCustom`、`KSamplerSelect`、`FluxGuidance`、`INPAINT_LoadInpaintModel`、`UpscaleModelLoader`、`Image Power Noise`、`INPAINT_InpaintWithModel`、`MaskToImage`、`GrowMaskWithBlur`、`SaveImage`、`CLIPVisionEncode`、`CLIPVisionLoader`、`SamplerCustomAdvanced`、`VAEEncode`、`InpaintModelConditioning`、`Image Blend by Mask`、`RepeatImageBatch`、`Int`、`RH_Captioner`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、LoadImage、CFGGuider、FluxGuidance、KSamplerSelect
