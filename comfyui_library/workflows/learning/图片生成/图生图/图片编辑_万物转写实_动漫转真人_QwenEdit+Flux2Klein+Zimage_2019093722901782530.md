---
key: 图片生成/图生图/图片编辑_万物转写实_动漫转真人_QwenEdit+Flux2Klein+Zimage_2019093722901782530.json
name: 图片编辑_万物转写实_动漫转真人_QwenEdit+Flux2Klein+Zimage_2019093722901782530
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑_万物转写实_动漫转真人_QwenEdit+Flux2Klein+Zimage_2019093722901782530.json
hash: 3d2bade0bde1fcfd
coverage: 0.670213
learned_at: 2026-10-23 12:41:28
nodes: [ModelSamplingAuraFlow, Note, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Note, CFGNorm, MarkdownNote, GetImageSizeAndCount, FluxKontextImageScale, Reroute, ReferenceLatent, VAEEncode, ReferenceLatent, ConditioningZeroOut, ImageScaleToTotalPixels, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, UNETLoader, TextEncodeQwenImageEditPlus, VAEDecode, Note, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, KSamplerAdvanced, VAEEncode, CLIPTextEncode, CLIPTextEncode, Reroute, UpscaleModelLoader, CLIPLoader, VAELoader, UNETLoader, ImageScaleToMaxDimension, Image Comparer (rgthree), Reroute, Image Comparer (rgthree), SaveImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, ImageConcanate, ImageConcanate, SaveImage, SaveImage, CLIPTextEncode, UltimateSDUpscale, GetImageSizeAndCount, ImageScaleToTotalPixels, ReferenceLatent, ReferenceLatent, VAEEncode, Reroute, CLIPLoader, UNETLoader, VAELoader, VRAMReserver, Image Comparer (rgthree), Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, AILab_ImagePreview, LoraLoaderModelOnly, VRAMReserver, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, VAEDecode, Reroute, Reroute, Image Comparer (rgthree), Reroute, Reroute, VAEDecode, KSampler, easy ifElse, Reroute, Reroute, Reroute, LoadImage, Note, TextEncodeQwenImageEditPlus, easy boolean, Reroute, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 8974322136815, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图片编辑_万物转写实_动漫转真人_QwenEdit+Flux2Klein+Zimage_2019093722901782530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑_万物转写实_动漫转真人_QwenEdit+Flux2Klein+Zimage_2019093722901782530.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `ModelSamplingAuraFlow`
- `Note`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Note`
- `CFGNorm`
- `MarkdownNote`
- `GetImageSizeAndCount`
- `FluxKontextImageScale`
- `Reroute`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `Note`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `UpscaleModelLoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ImageScaleToMaxDimension`
- `Image Comparer (rgthree)`
- `Reroute`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UltimateSDUpscale`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `Reroute`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VRAMReserver`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `AILab_ImagePreview`
- `LoraLoaderModelOnly` ★核心
- `VRAMReserver`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy ifElse`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoadImage`
- `Note`
- `TextEncodeQwenImageEditPlus`
- `easy boolean`
- `Reroute`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `8974322136815`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（63/94）

**有卡**：`ModelSamplingAuraFlow`、`FluxKontextMultiReferenceLatentMethod`、`CFGNorm`、`GetImageSizeAndCount`、`FluxKontextImageScale`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`KSamplerAdvanced`、`CLIPTextEncode`、`UpscaleModelLoader`、`ImageScaleToMaxDimension`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`ImageConcanate`、`UltimateSDUpscale`、`VRAMReserver`、`AILab_ImagePreview`、`KSampler`、`LoadImage`、`easy boolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
