---
key: 图片生成/图生图/参考填充_FLUX.fill（效果不错！！！）_1895042782594007041.json
name: 参考填充_FLUX.fill（效果不错！！！）_1895042782594007041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/参考填充_FLUX.fill（效果不错！！！）_1895042782594007041.json
hash: 73794b4f9135c6b4
coverage: 0.722892
learned_at: 2026-10-23 12:34:45
nodes: [DualCLIPLoader, VAELoader, UNETLoader, Reroute, Reroute, DifferentialDiffusion, Reroute, Reroute, Reroute, CFGGuider, CLIPTextEncodeFlux, KSamplerSelect, VAEEncode, CLIPTextEncodeFlux, SamplerCustomAdvanced, Reroute, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncodeFlux, CLIPTextEncodeFlux, GrowMaskWithBlur, InpaintModelConditioning, ImageToMask, MaskToImage, RH_Captioner, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, easy imageSize, easy imageSize, easy imageConcat, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ColorImage V2, easy imageConcat, PreviewImage, CLIPVisionLoader, StyleModelLoader, CLIPVisionEncode, StyleModelApply, FluxGuidance, KSamplerSelect, BasicScheduler, CFGGuider, SamplerCustomAdvanced, PreviewImage, VAEDecode, RandomNoise, Reroute, BasicScheduler, Any Switch (rgthree), Reroute, RH_Captioner, Textbox, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, DeepTranslatorTextNode, DeepTranslatorTextNode, UNETLoader, Mute / Bypass Relay (rgthree), Reroute, PreviewImage, ImageCrop, SaveImage, LoadImage, Image Comparer (rgthree), Label (rgthree), LoraLoaderModelOnly, PreviewImage, Label (rgthree), Label (rgthree), easy float, Mute / Bypass Repeater (rgthree), easy imageSize, LoadImage, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PreviewImage, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/参考填充_FLUX.fill（效果不错！！！）_1895042782594007041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/参考填充_FLUX.fill（效果不错！！！）_1895042782594007041.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Reroute`
- `Reroute`
- `DifferentialDiffusion`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `CLIPTextEncodeFlux` ★核心
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncodeFlux` ★核心
- `GrowMaskWithBlur`
- `InpaintModelConditioning`
- `ImageToMask`
- `MaskToImage`
- `RH_Captioner`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `easy imageSize`
- `easy imageSize`
- `easy imageConcat`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ColorImage V2`
- `easy imageConcat`
- `PreviewImage`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `RandomNoise`
- `Reroute`
- `BasicScheduler`
- `Any Switch (rgthree)`
- `Reroute`
- `RH_Captioner`
- `Textbox`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `UNETLoader` ★核心
- `Mute / Bypass Relay (rgthree)`
- `Reroute`
- `PreviewImage`
- `ImageCrop`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `easy float`
- `Mute / Bypass Repeater (rgthree)`
- `easy imageSize`
- `LoadImage`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `PreviewImage`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **72%**（60/83）

**有卡**：`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`DifferentialDiffusion`、`CFGGuider`、`CLIPTextEncodeFlux`、`KSamplerSelect`、`VAEEncode`、`SamplerCustomAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`InpaintModelConditioning`、`ImageToMask`、`MaskToImage`、`RH_Captioner`、`easy imageSize`、`easy imageConcat`、`LayerUtility: ColorImage V2`、`CLIPVisionLoader`、`StyleModelLoader`、`CLIPVisionEncode`、`StyleModelApply`、`FluxGuidance`、`BasicScheduler`、`VAEDecode`、`RandomNoise`、`Textbox`、`DeepTranslatorTextNode`、`Mute / Bypass Relay (rgthree)`、`ImageCrop`、`SaveImage`、`LoadImage`、`Label (rgthree)`、`LoraLoaderModelOnly`、`easy float`、`Mute / Bypass Repeater (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、LoadImage、CFGGuider、FluxGuidance、KSamplerSelect
