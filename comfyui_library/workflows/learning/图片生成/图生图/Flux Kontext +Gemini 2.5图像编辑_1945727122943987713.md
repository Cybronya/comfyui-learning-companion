---
key: 图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑_1945727122943987713.json
name: Flux Kontext +Gemini 2.5图像编辑_1945727122943987713
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑_1945727122943987713.json
hash: 750377258972dafe
coverage: 0.833333
learned_at: 2026-10-23 10:56:21
nodes: [SaveImage, RH_ComfyFluxKontext, Image Comparer (rgthree), ReferenceLatent, FluxGuidance, VAEEncode, CLIPTextEncode, ConditioningZeroOut, KSampler, VAELoader, VAEEncode, ImageConcanate, PreviewImage, PreviewImage, DualCLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, VAEEncode, ConstrainImage|pysssss, Fast Groups Bypasser (rgthree), ImageConcanate, PreviewImage, UNETLoader, CLIPTextEncode, ConditioningZeroOut, VAEEncode, VAELoader, ReferenceLatent, FluxGuidance, KSampler, VAEDecode, SaveImage, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), ConstrainImage|pysssss, VAEDecode, ConstrainImage|pysssss, LoadImage, LoadImage, RH_Translator, UNETLoader, DualCLIPLoader, LoadImage, LoraLoader, RH_Translator, FluxKontextImageScale, RH_ComfyFluxKontext, LoadImage, LoadImage, RH_Translator, MarkdownNote, SaveImage, RH_Translator, LoadImage, Image Comparer (rgthree), LoadImage, SaveImage, Image Comparer (rgthree), RH_Nano_Banana_Image2Image]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "my_first_flux_kontext_lora_v1_000001000.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 149610246423554, "steps": 25, "strength_clip": 1, "strength_model": 0.8000000000000002}
---

# 图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑_1945727122943987713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑_1945727122943987713.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `SaveImage`
- `RH_ComfyFluxKontext`
- `Image Comparer (rgthree)`
- `ReferenceLatent`
- `FluxGuidance`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `ImageConcanate`
- `PreviewImage`
- `PreviewImage`
- `DualCLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ConstrainImage|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcanate`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `ReferenceLatent`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `ConstrainImage|pysssss`
- `VAEDecode` ★核心
- `ConstrainImage|pysssss`
- `LoadImage`
- `LoadImage`
- `RH_Translator`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `LoraLoader` ★核心
- `RH_Translator`
- `FluxKontextImageScale`
- `RH_ComfyFluxKontext`
- `LoadImage`
- `LoadImage`
- `RH_Translator`
- `MarkdownNote`
- `SaveImage`
- `RH_Translator`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `RH_Nano_Banana_Image2Image`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `149610246423554`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `my_first_flux_kontext_lora_v1_000001000.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `1`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`SaveImage`、`RH_ComfyFluxKontext`、`ReferenceLatent`、`FluxGuidance`、`VAEEncode`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`ImageConcanate`、`DualCLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxKontextImageScale`、`ConstrainImage|pysssss`、`UNETLoader`、`VAEDecode`、`LoadImage`、`RH_Translator`、`LoraLoader`、`RH_Nano_Banana_Image2Image`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
