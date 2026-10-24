---
key: 图片生成/图生图/动漫转写实_动漫转真人_QwenEdit或者Flux2Klein+Zimage去除AI感_2031737816035627009.json
name: 动漫转写实_动漫转真人_QwenEdit或者Flux2Klein+Zimage去除AI感_2031737816035627009
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/动漫转写实_动漫转真人_QwenEdit或者Flux2Klein+Zimage去除AI感_2031737816035627009.json
hash: b8232ff146603a1c
coverage: 0.670213
learned_at: 2026-10-23 12:25:29
nodes: [ModelSamplingAuraFlow, Note, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Note, GetImageSizeAndCount, FluxKontextImageScale, ReferenceLatent, VAEEncode, ReferenceLatent, ConditioningZeroOut, ImageScaleToTotalPixels, LoraLoaderModelOnly, VAELoader, CLIPLoader, TextEncodeQwenImageEditPlus, VAEDecode, Note, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, KSamplerAdvanced, VAEEncode, CLIPTextEncode, CLIPTextEncode, Reroute, UpscaleModelLoader, CLIPLoader, VAELoader, UNETLoader, ImageScaleToMaxDimension, Image Comparer (rgthree), Reroute, Image Comparer (rgthree), SaveImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, ImageConcanate, ImageConcanate, SaveImage, SaveImage, CLIPTextEncode, UltimateSDUpscale, GetImageSizeAndCount, ImageScaleToTotalPixels, ReferenceLatent, ReferenceLatent, VAEEncode, Reroute, CLIPLoader, UNETLoader, VAELoader, VRAMReserver, Image Comparer (rgthree), Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, AILab_ImagePreview, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, VAEDecode, Reroute, Reroute, Image Comparer (rgthree), Reroute, Reroute, VAEDecode, Reroute, Reroute, TextEncodeQwenImageEditPlus, Reroute, CLIPTextEncode, Reroute, LoraLoaderModelOnly, UNETLoader, Reroute, CFGNorm, MarkdownNote, KSampler, easy ifElse, VRAMReserver, LoadImage, easy boolean, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 500790293162424, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/动漫转写实_动漫转真人_QwenEdit或者Flux2Klein+Zimage去除AI感_2031737816035627009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/动漫转写实_动漫转真人_QwenEdit或者Flux2Klein+Zimage去除AI感_2031737816035627009.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `ModelSamplingAuraFlow`
- `Note`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Note`
- `GetImageSizeAndCount`
- `FluxKontextImageScale`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
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
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `CFGNorm`
- `MarkdownNote`
- `KSampler` ★核心
- `easy ifElse`
- `VRAMReserver`
- `LoadImage`
- `easy boolean`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `500790293162424`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（63/94）

**有卡**：`ModelSamplingAuraFlow`、`FluxKontextMultiReferenceLatentMethod`、`GetImageSizeAndCount`、`FluxKontextImageScale`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`UNETLoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`UpscaleModelLoader`、`ImageScaleToMaxDimension`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`ImageConcanate`、`UltimateSDUpscale`、`VRAMReserver`、`AILab_ImagePreview`、`CFGNorm`、`KSampler`、`LoadImage`、`easy boolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
