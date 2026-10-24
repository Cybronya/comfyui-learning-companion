---
key: 图片生成/图生图/FLUX （controlnet Union pro 2.0深度_线稿_姿势控制可选）洗图_1956969433690464258.json
name: FLUX （controlnet Union pro 2.0深度_线稿_姿势控制可选）洗图_1956969433690464258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX （controlnet Union pro 2.0深度_线稿_姿势控制可选）洗图_1956969433690464258.json
hash: cae1e866e4460006
coverage: 0.8125
learned_at: 2026-10-23 10:53:39
nodes: [PreviewImage, SetUnionControlNetType, PreviewImage, PreviewImage, SetUnionControlNetType, Note, Canny, AnyLineArtPreprocessor_aux, Image Comparer (rgthree), SetUnionControlNetType, SetUnionControlNetType, DWPreprocessor, PreviewImage, LayerUtility: JoyCaptionBeta1ExtraOptions, LoraLoader, CLIPTextEncode, ConditioningZeroOut, SaveImage, VAEDecode, CLIPTextEncode, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetApplyAdvanced, VAELoader, DepthAnythingV2Preprocessor, PreviewImage, workflow>放大, LayerUtility: LoadJoyCaptionBeta1Model, easy showAnything, DeepTranslatorTextNode, LayerUtility: JoyCaptionBeta1, FluxGuidance, VAEEncode, VAEDecode, ImageScaleToTotalPixels, workflow>获取latent, ControlNetApplyAdvanced, ControlNetApplyAdvanced, LoadImage, UNETLoader, DualCLIPLoader, Fast Groups Bypasser (rgthree), ControlNetApplyAdvanced, KSampler, ApplyFBCacheOnModel, LoraLoaderModelOnly]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 1, "lora_name": "FLUX\\加速模型\\FLUX.1-Turbo-Alpha.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 1028566748408667, "steps": 25, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/FLUX （controlnet Union pro 2.0深度_线稿_姿势控制可选）洗图_1956969433690464258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX （controlnet Union pro 2.0深度_线稿_姿势控制可选）洗图_1956969433690464258.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `PreviewImage`
- `SetUnionControlNetType`
- `PreviewImage`
- `PreviewImage`
- `SetUnionControlNetType`
- `Note`
- `Canny`
- `AnyLineArtPreprocessor_aux`
- `Image Comparer (rgthree)`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `DWPreprocessor`
- `PreviewImage`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `VAELoader`
- `DepthAnythingV2Preprocessor`
- `PreviewImage`
- `workflow>放大`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `easy showAnything`
- `DeepTranslatorTextNode`
- `LayerUtility: JoyCaptionBeta1`
- `FluxGuidance`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `workflow>获取latent`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `ApplyFBCacheOnModel`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `FLUX\加速模型\FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `controlnet_strength` = `0.8000000000000002`
- `seed` = `1028566748408667`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`SetUnionControlNetType`、`Canny`、`AnyLineArtPreprocessor_aux`、`DWPreprocessor`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LoraLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`VAELoader`、`DepthAnythingV2Preprocessor`、`workflow>放大`、`LayerUtility: LoadJoyCaptionBeta1Model`、`DeepTranslatorTextNode`、`LayerUtility: JoyCaptionBeta1`、`FluxGuidance`、`VAEEncode`、`ImageScaleToTotalPixels`、`workflow>获取latent`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`KSampler`、`ApplyFBCacheOnModel`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
