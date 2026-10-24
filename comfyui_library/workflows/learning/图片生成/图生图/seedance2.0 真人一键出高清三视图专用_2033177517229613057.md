---
key: 图片生成/图生图/seedance2.0 真人一键出高清三视图专用_2033177517229613057.json
name: seedance2.0 真人一键出高清三视图专用_2033177517229613057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/seedance2.0 真人一键出高清三视图专用_2033177517229613057.json
hash: c1a66c1cec186807
coverage: 0.82243
learned_at: 2026-10-23 11:45:12
nodes: [LoraLoaderModelOnly, VAELoader, ModelSamplingAuraFlow, CLIPLoader, CLIPTextEncode, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, VAEEncodeTiled, easy cleanGpuUsed, KSampler, easy cleanGpuUsed, PreviewImage, PreviewImage, CFGNorm, KSampler, ImageScaleToTotalPixels, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, INTConstant, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPTextEncode, UpscaleModelLoader, ImageUpscaleWithModel, VAEDecode, ImageScaleBy, VAEEncodeTiled, easy cleanGpuUsed, KSampler, easy cleanGpuUsed, PreviewImage, PreviewImage, FluxKontextImageScale, CFGNorm, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPLoader, CLIPTextEncode, UpscaleModelLoader, ImageUpscaleWithModel, VAEDecode, ImageScaleBy, VAEEncodeTiled, easy cleanGpuUsed, KSampler, easy cleanGpuUsed, PreviewImage, PreviewImage, FluxKontextImageScale, CFGNorm, KSampler, RH_Translator, RH_Translator, RH_Translator, Anything Everywhere, VAEDecode, VAEDecode, ImageScaleToTotalPixels, PreviewImage, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, INTConstant, VAEDecode, ImageScaleToTotalPixels, PreviewImage, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, INTConstant, VAEDecode, FluxKontextImageScale, SeedVR2VideoUpscaler, SeedVR2VideoUpscaler, SaveImage, SaveImage, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), Note, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, NunchakuQwenImageDiTLoader, TextEncodeQwenImageEditPlus, easy showAnything, Text, easy showAnything, TextEncodeQwenImageEditPlus, NunchakuQwenImageDiTLoader, Text, CLIPLoader, easy showAnything, TextEncodeQwenImageEditPlus, NunchakuQwenImageDiTLoader, Text, LoadImage, QwenImageLatentAspectRatio, easy imageConcat, easy imageConcat, easy imageConcat, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 77, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/seedance2.0 真人一键出高清三视图专用_2033177517229613057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/seedance2.0 真人一键出高清三视图专用_2033177517229613057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `VAEEncodeTiled` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `PreviewImage`
- `CFGNorm`
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncodeTiled` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `PreviewImage`
- `FluxKontextImageScale`
- `CFGNorm`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncodeTiled` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `PreviewImage`
- `FluxKontextImageScale`
- `CFGNorm`
- `KSampler` ★核心
- `RH_Translator`
- `RH_Translator`
- `RH_Translator`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `SeedVR2VideoUpscaler`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`
- `NunchakuQwenImageDiTLoader`
- `TextEncodeQwenImageEditPlus`
- `easy showAnything`
- `Text`
- `easy showAnything`
- `TextEncodeQwenImageEditPlus`
- `NunchakuQwenImageDiTLoader`
- `Text`
- `CLIPLoader`
- `easy showAnything`
- `TextEncodeQwenImageEditPlus`
- `NunchakuQwenImageDiTLoader`
- `Text`
- `LoadImage`
- `QwenImageLatentAspectRatio`
- `easy imageConcat`
- `easy imageConcat`
- `easy imageConcat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`

## 关键参数

- `seed` = `77`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（88/107）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`ModelSamplingAuraFlow`、`CLIPLoader`、`CLIPTextEncode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAEEncodeTiled`、`easy cleanGpuUsed`、`KSampler`、`CFGNorm`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`INTConstant`、`VAEDecode`、`FluxKontextImageScale`、`RH_Translator`、`SeedVR2VideoUpscaler`、`SaveImage`、`NunchakuQwenImageDiTLoader`、`TextEncodeQwenImageEditPlus`、`Text`、`LoadImage`、`QwenImageLatentAspectRatio`、`easy imageConcat`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 6 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
