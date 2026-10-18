---
key: 视频生成/图生视频/LR3.0_2029096092029165570.json
name: LR3.0_2029096092029165570.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LR3.0_2029096092029165570.json
hash: 196f0f572653488a
coverage: 0.742857
learned_at: 2026-10-15 22:35:21
nodes: [GetNode, SetNode, SetNode, CLIPLoader, SetNode, SetNode, UNETLoader, LoraLoaderModelOnly, GetNode, VAEEncode, TextEncodeQwenImageEditPlus, KSampler, GetNode, GetNode, TextEncodeQwenImageEdit, VAEDecode, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, UNETLoader, LayerUtility: PurgeVRAM V2, Qwen3_VQA, JoinStrings, ShowText|pysssss, easy showAnything, CLIPTextEncode, VAEEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, KSampler, Reroute, ConditioningZeroOut, easy clearCacheAll, easy cleanGpuUsed, ImageScaleBy, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, VAEDecode, KSampler, VAELoader, ImageScaleToTotalPixels, SaveImage, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, easy promptList, easy showAnything, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, ModelSamplingAuraFlow, CFGNorm, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, KSampler, VAEDecode, VAEEncode, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Image Comparer (rgthree), RH_Nano_Banana2_Gemini31Flash, SaveImage, JjkText, JjkText, easy showAnything, JjkText, TextCombinerTwo, TextCombinerTwo, RH_Prompter, JjkText, RH_Prompter, FluxResolutionNode, easy showAnything, JjkText, ImpactSwitch, SaveImage, SaveImage, ImageScaleBy, RH_Jimeng_Image2Image, LoadImage, LoadImage, LoadImage, LoadImage, SaveVideo, ImageResize+, ImageResize+, RH_Jimeng_Image2Video_V2, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LR3.0_2029096092029165570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029096092029165570.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEdit`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `Qwen3_VQA`
- `JoinStrings`
- `ShowText|pysssss`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSampler` ★核心
- `Reroute`
- `ConditioningZeroOut`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `easy promptList`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `RH_Prompter`
- `JjkText`
- `RH_Prompter`
- `FluxResolutionNode`
- `easy showAnything`
- `JjkText`
- `ImpactSwitch`
- `SaveImage`
- `SaveImage`
- `ImageScaleBy`
- `RH_Jimeng_Image2Image`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveVideo`
- `ImageResize+`
- `ImageResize+`
- `RH_Jimeng_Image2Video_V2`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1002`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（78/105）

**有卡**：`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`KSampler`、`TextEncodeQwenImageEdit`、`VAEDecode`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`Qwen3_VQA`、`JoinStrings`、`CLIPTextEncode`、`ConditioningZeroOut`、`easy clearCacheAll`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SaveImage`、`QwenMultiangleCameraNode`、`easy promptList`、`ModelSamplingAuraFlow`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`RH_Nano_Banana2_Gemini31Flash`、`TextCombinerTwo`、`RH_Prompter`、`FluxResolutionNode`、`RH_Jimeng_Image2Image`、`LoadImage`、`SaveVideo`、`ImageResize+`、`RH_Jimeng_Image2Video_V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
