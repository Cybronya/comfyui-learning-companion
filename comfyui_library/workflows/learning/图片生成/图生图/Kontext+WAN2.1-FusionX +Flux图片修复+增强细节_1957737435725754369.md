---
key: 图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1957737435725754369.json
name: Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1957737435725754369
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1957737435725754369.json
hash: c40a36b1f698614d
coverage: 0.775862
learned_at: 2026-10-23 11:06:08
nodes: [PreviewImage, AIO_Preprocessor, PrimitiveNode, CR Latent Batch Size, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), VAEEncode, CLIPTextEncode, CLIPTextEncode, Note, Image Comparer (rgthree), ControlNetLoaderAdvanced, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Joy_caption_two_load, LayerUtility: ImageScaleByAspectRatio V2, FluxGuidance, ConditioningZeroOut, VAELoader, UNETLoader, CLIPLoader, ShowText|pysssss, VAELoader, Joy_caption_two, easy cleanGpuUsed, CLIPTextEncodeFlux, VAEEncode, CR Text Concatenate, Reroute, DualCLIPLoader, VAELoader, Image Comparer (rgthree), KSampler, Image Comparer (rgthree), ImageSharpen, ControlNetApplySD3, ReferenceLatent, VAEDecode, easy cleanGpuUsed, VAEEncode, DualCLIPLoader, CLIPTextEncode, SetUnionControlNetType, PrimitiveNode, RH_Translator, KSampler, VAEDecode, Reroute, Float, UNETLoader, UNETLoader, Image Comparer (rgthree), Text Multiline, PrimitiveNode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.7000000000000002, "denoise": 0.10000000000000002, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 279041723069172, "steps": 20}
---

# 图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1957737435725754369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext+WAN2.1-FusionX +Flux图片修复+增强细节_1957737435725754369.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `PreviewImage`
- `AIO_Preprocessor`
- `PrimitiveNode`
- `CR Latent Batch Size`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Image Comparer (rgthree)`
- `ControlNetLoaderAdvanced`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Joy_caption_two_load`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `VAELoader`
- `Joy_caption_two`
- `easy cleanGpuUsed`
- `CLIPTextEncodeFlux` ★核心
- `VAEEncode` ★核心
- `CR Text Concatenate`
- `Reroute`
- `DualCLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `ImageSharpen`
- `ControlNetApplySD3` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `SetUnionControlNetType`
- `PrimitiveNode`
- `RH_Translator`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Float`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `Text Multiline`
- `PrimitiveNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `279041723069172`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **78%**（45/58）

**有卡**：`AIO_Preprocessor`、`CR Latent Batch Size`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VAEDecode`、`SaveImage`、`VAEEncode`、`CLIPTextEncode`、`ControlNetLoaderAdvanced`、`LoadImage`、`Joy_caption_two_load`、`FluxGuidance`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`Joy_caption_two`、`easy cleanGpuUsed`、`CLIPTextEncodeFlux`、`CR Text Concatenate`、`DualCLIPLoader`、`ImageSharpen`、`ControlNetApplySD3`、`ReferenceLatent`、`SetUnionControlNetType`、`RH_Translator`、`Float`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
