---
key: 平台全量/FLUX一键换产品背景+优化V2.0_1948420176562782210.json
name: FLUX一键换产品背景+优化V2.0_1948420176562782210
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX一键换产品背景+优化V2.0_1948420176562782210.json
hash: f7c0a2fb796364b6
coverage: 0.846154
learned_at: 2026-11-14 00:25:48
nodes: [CLIPVisionEncode, VAELoader, Anything Everywhere, LayerUtility: ImageRemoveAlpha, Get Image Size, easy setNode, easy getNode, Image Blank, MaskToImage, ImageConcanate, ImageConcanate, ConditioningZeroOut, FluxGuidance, VAEDecode, PreviewBridge, InpaintModelConditioning, DifferentialDiffusion, KSampler, Image Comparer (rgthree), SetUnionControlNetType, AIO_Preprocessor, LoadImage, Joy_caption_two_load, DualCLIPLoader, UNETLoader, CLIPTextEncode, FluxGuidance, VAEEncode, KSampler, easy setNode, PreviewImage, VAEDecode, ConditioningZeroOut, DualCLIPLoader, VAELoader, CLIPVisionLoader, StyleModelLoader, LoraLoaderModelOnly, LoraLoader, VAEDecode, ImageToMask, PreviewImage, easy getNode, PreviewImage, PreviewImage, UNETLoader, Note, PreviewImage, LayerUtility: ExtendCanvas, LoraLoader, Crop (mtb), SaveImage, PreviewImage, CLIPTextEncode, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, RMBG, LayerMask: MaskGrow, LoraLoader, Joy_caption_two, ShowText|pysssss, easy getNode, easy showAnything, CLIPTextEncode, StyleModelApply, LoadImage, LoraLoader, FluxSamplerParams+, IPAdapterFluxLoader, ApplyIPAdapterFlux, ControlNetApplySD3, PreviewImage, CR Text, RH_Captioner, LayerUtility: TextJoin, FluxGuidance, ConditioningZeroOut, EmptyLatentImage]
patterns: [text_to_image, image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8, "denoise": 0.4, "height": 512, "lora_name": "AIGC电商写实超细腻感_v1.0.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 177288646744551, "steps": 8, "strength_clip": 1, "strength_model": 0.4000000000000001, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FLUX一键换产品背景+优化V2.0_1948420176562782210.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX一键换产品背景+优化V2.0_1948420176562782210.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `CLIPVisionEncode`
- `VAELoader`
- `Anything Everywhere`
- `LayerUtility: ImageRemoveAlpha`
- `Get Image Size`
- `easy setNode`
- `easy getNode`
- `Image Blank`
- `MaskToImage`
- `ImageConcanate`
- `ImageConcanate`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEDecode` ★核心
- `PreviewBridge`
- `InpaintModelConditioning`
- `DifferentialDiffusion`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `LoadImage`
- `Joy_caption_two_load`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `easy setNode`
- `PreviewImage`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `ImageToMask`
- `PreviewImage`
- `easy getNode`
- `PreviewImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `Note`
- `PreviewImage`
- `LayerUtility: ExtendCanvas`
- `LoraLoader` ★核心
- `Crop (mtb)`
- `SaveImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `LayerMask: MaskGrow`
- `LoraLoader` ★核心
- `Joy_caption_two`
- `ShowText|pysssss`
- `easy getNode`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `StyleModelApply`
- `LoadImage`
- `LoraLoader` ★核心
- `FluxSamplerParams+` ★核心
- `IPAdapterFluxLoader`
- `ApplyIPAdapterFlux`
- `ControlNetApplySD3` ★核心
- `PreviewImage`
- `CR Text`
- `RH_Captioner`
- `LayerUtility: TextJoin`
- `FluxGuidance`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `seed` = `177288646744551`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.4`
- `lora_name` = `AIGC电商写实超细腻感_v1.0.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `1`
- `controlnet_strength` = `0.8`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（66/78）

**有卡**：`CLIPVisionEncode`、`VAELoader`、`LayerUtility: ImageRemoveAlpha`、`Get Image Size`、`easy setNode`、`easy getNode`、`Image Blank`、`MaskToImage`、`ImageConcanate`、`ConditioningZeroOut`、`FluxGuidance`、`VAEDecode`、`PreviewBridge`、`InpaintModelConditioning`、`DifferentialDiffusion`、`KSampler`、`SetUnionControlNetType`、`AIO_Preprocessor`、`LoadImage`、`Joy_caption_two_load`、`DualCLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`VAEEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`LoraLoaderModelOnly`、`LoraLoader`、`ImageToMask`、`LayerUtility: ExtendCanvas`、`Crop (mtb)`、`SaveImage`、`ControlNetLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RMBG`、`LayerMask: MaskGrow`、`Joy_caption_two`、`StyleModelApply`、`FluxSamplerParams+`、`IPAdapterFluxLoader`、`ApplyIPAdapterFlux`、`ControlNetApplySD3`、`CR Text`、`RH_Captioner`、`LayerUtility: TextJoin`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
