---
key: 图片生成/图生图/扩图专辑——Z-image+Flux-fill-OneReward+Flux-2-klein扩图流_2001819543137841154.json
name: 扩图专辑——Z-image+Flux-fill-OneReward+Flux-2-klein扩图流_2001819543137841154
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/扩图专辑——Z-image+Flux-fill-OneReward+Flux-2-klein扩图流_2001819543137841154.json
hash: 6664ee406636c7a6
coverage: 0.878788
learned_at: 2026-10-23 12:53:58
nodes: [GrowMaskWithBlur, CLIPLoader, VAEEncode, CLIPTextEncode, ReferenceLatent, CLIPTextEncode, InpaintModelConditioning, UNETLoader, DifferentialDiffusion, SetLatentNoiseMask, KSampler, SaveImage, INPAINT_InpaintWithModel, VAELoader, easy showAnything, INPAINT_LoadInpaintModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VAELoader, Note, KSampler, UNETLoader, DualCLIPLoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, DifferentialDiffusion, InpaintModelConditioning, PreviewImage, VAEDecode, LoadImage, SaveImage, Image Comparer (rgthree), ImagePadForOutpaint, Image Comparer (rgthree), VAEDecode, ImagePadForOutpaint, AILab_QwenVL, ReferenceLatent, ReferenceLatent, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, GetImageSize, ConditioningZeroOut, VAEEncode, DrawMaskOnImage, UNETLoader, RandomNoise, VAELoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, PreviewImage, SamplerCustomAdvanced, VAEDecode, ColorMatch, SaveImage, LoadImage, ImagePadForOutpaint, Image Comparer (rgthree), CLIPLoader, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 398924826166186, "steps": 10}
---

# 图片生成/图生图/扩图专辑——Z-image+Flux-fill-OneReward+Flux-2-klein扩图流_2001819543137841154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/扩图专辑——Z-image+Flux-fill-OneReward+Flux-2-klein扩图流_2001819543137841154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `GrowMaskWithBlur`
- `CLIPLoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `SetLatentNoiseMask`
- `KSampler` ★核心
- `SaveImage`
- `INPAINT_InpaintWithModel`
- `VAELoader`
- `easy showAnything`
- `INPAINT_LoadInpaintModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VAELoader`
- `Note`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `PreviewImage`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `ImagePadForOutpaint`
- `AILab_QwenVL`
- `ReferenceLatent`
- `ReferenceLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `DrawMaskOnImage`
- `UNETLoader` ★核心
- `RandomNoise`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ColorMatch`
- `SaveImage`
- `LoadImage`
- `ImagePadForOutpaint`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `398924826166186`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（58/66）

**有卡**：`GrowMaskWithBlur`、`CLIPLoader`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`InpaintModelConditioning`、`UNETLoader`、`DifferentialDiffusion`、`SetLatentNoiseMask`、`KSampler`、`SaveImage`、`INPAINT_InpaintWithModel`、`VAELoader`、`INPAINT_LoadInpaintModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`DualCLIPLoader`、`LoadImage`、`LoraLoaderModelOnly`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`ImagePadForOutpaint`、`AILab_QwenVL`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`GetImageSize`、`DrawMaskOnImage`、`RandomNoise`、`ImageScaleToTotalPixels`、`SamplerCustomAdvanced`、`ColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
