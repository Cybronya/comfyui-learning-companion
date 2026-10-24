---
key: 图片生成/图生图/2026Kontext-室内室外模型写实渲染V2.0_2043604660027658241.json
name: 2026Kontext-室内室外模型写实渲染V2.0_2043604660027658241
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/2026Kontext-室内室外模型写实渲染V2.0_2043604660027658241.json
hash: baab97dc18443bd8
coverage: 0.916667
learned_at: 2026-10-23 10:48:12
nodes: [ConditioningZeroOut, EmptyLatentImage, UNETLoader, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), Note, VAELoader, DualCLIPLoader, CLIPTextEncode, FluxGuidance, LoraLoader, CR Prompt Text, Text Concatenate, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LoadImage, DeepTranslatorTextNode]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 2, "cfg": 1, "denoise": 1, "height": 768, "lora_name": "室内模型图到效果图V6.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 55184624892313, "steps": 20, "strength_clip": 1, "strength_model": 1, "width": 512}
---

# 图片生成/图生图/2026Kontext-室内室外模型写实渲染V2.0_2043604660027658241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2026Kontext-室内室外模型写实渲染V2.0_2043604660027658241.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Note`
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `LoraLoader` ★核心
- `CR Prompt Text`
- `Text Concatenate`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `DeepTranslatorTextNode`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `width` = `512`
- `height` = `768`
- `batch_size` = `2`
- `seed` = `55184624892313`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `室内模型图到效果图V6.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`ConditioningZeroOut`、`EmptyLatentImage`、`UNETLoader`、`ReferenceLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`LoraLoader`、`CR Prompt Text`、`Text Concatenate`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoadImage`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
