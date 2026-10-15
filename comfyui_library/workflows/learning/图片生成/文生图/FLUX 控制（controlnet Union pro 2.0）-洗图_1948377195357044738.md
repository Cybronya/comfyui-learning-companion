---
key: 图片生成/文生图/FLUX 控制（controlnet Union pro 2.0）-洗图_1948377195357044738.json
name: FLUX 控制（controlnet Union pro 2.0）-洗图_1948377195357044738
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX 控制（controlnet Union pro 2.0）-洗图_1948377195357044738.json
hash: ece055b88fe36471
coverage: 0.8125
learned_at: 2026-10-15 22:26:17
nodes: [PreviewImage, SetUnionControlNetType, PreviewImage, ControlNetApplyAdvanced, PreviewImage, SetUnionControlNetType, Note, Canny, LoraLoaderModelOnly, ControlNetApplyAdvanced, AnyLineArtPreprocessor_aux, Image Comparer (rgthree), ControlNetApplyAdvanced, SetUnionControlNetType, VAEEncode, SetUnionControlNetType, DWPreprocessor, PreviewImage, LayerUtility: JoyCaptionBeta1ExtraOptions, LoraLoader, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, SaveImage, VAEDecode, CLIPTextEncode, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetApplyAdvanced, VAELoader, Fast Groups Bypasser (rgthree), KSampler, VAEDecode, DepthAnythingV2Preprocessor, workflow>获取latent, DualCLIPLoader, LoadImage, ImageScaleToTotalPixels, PreviewImage, workflow>放大, LayerUtility: LoadJoyCaptionBeta1Model, ApplyFBCacheOnModel, UNETLoader, LayerUtility: JoyCaptionBeta1, DeepTranslatorTextNode, easy showAnything]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "lora_name": "FLUX\\加速模型\\FLUX.1-Turbo-Alpha.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 123466, "steps": 25, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/文生图/FLUX 控制（controlnet Union pro 2.0）-洗图_1948377195357044738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX 控制（controlnet Union pro 2.0）-洗图_1948377195357044738.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `PreviewImage`
- `SetUnionControlNetType`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `SetUnionControlNetType`
- `Note`
- `Canny`
- `LoraLoaderModelOnly` ★核心
- `ControlNetApplyAdvanced` ★核心
- `AnyLineArtPreprocessor_aux`
- `Image Comparer (rgthree)`
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `VAEEncode` ★核心
- `SetUnionControlNetType`
- `DWPreprocessor`
- `PreviewImage`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `DepthAnythingV2Preprocessor`
- `workflow>获取latent`
- `DualCLIPLoader`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `workflow>放大`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `ApplyFBCacheOnModel`
- `UNETLoader` ★核心
- `LayerUtility: JoyCaptionBeta1`
- `DeepTranslatorTextNode`
- `easy showAnything`

**识别到的模式**：image_to_image、lora

## 关键参数

- `controlnet_strength` = `0.7000000000000001`
- `lora_name` = `FLUX\加速模型\FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `123466`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`SetUnionControlNetType`、`ControlNetApplyAdvanced`、`Canny`、`LoraLoaderModelOnly`、`AnyLineArtPreprocessor_aux`、`VAEEncode`、`DWPreprocessor`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LoraLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxGuidance`、`SaveImage`、`VAEDecode`、`ControlNetLoader`、`VAELoader`、`KSampler`、`DepthAnythingV2Preprocessor`、`workflow>获取latent`、`DualCLIPLoader`、`LoadImage`、`ImageScaleToTotalPixels`、`workflow>放大`、`LayerUtility: LoadJoyCaptionBeta1Model`、`ApplyFBCacheOnModel`、`UNETLoader`、`LayerUtility: JoyCaptionBeta1`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
