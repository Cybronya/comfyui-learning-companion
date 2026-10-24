---
key: 图片生成/图生图/FireRed-Image-edit1.1批量换装_2031180219440177154.json
name: FireRed-Image-edit1.1批量换装_2031180219440177154
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1批量换装_2031180219440177154.json
hash: 629f57aba4a62f07
coverage: 0.914634
learned_at: 2026-10-23 10:55:51
nodes: [BatchCount+, Display Int (rgthree), easy forLoopStart, ImageBatchMultiple+, ImageBatchMultiple+, ImageBatchMultiple+, ImageBatchMultiple+, UNETLoader, CLIPLoader, ModelSamplingAuraFlow, VAELoader, CFGNorm, LoraLoaderModelOnly, KSampler, VAEDecode, CLIPLoader, VAELoader, UltimateSDUpscaleCustomSample, Upscale Model Loader, UNETLoader, UpscaleModelLoader, AdvancedLyingSigmaSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, ImageUpscaleWithModel, easy cleanGpuUsed, CLIPTextEncode, ConditioningZeroOut, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, VAEEncode, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, easy forLoopEnd, easy batchAnything, SaveImage, PreviewImage, Image Comparer (rgthree), PreviewImage, FluxKontextImageScale, FluxKontextImageScale, PreviewImage, CR Prompt Text, Int, Note, Note, easy int, Note, Int, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 590451495747466, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1批量换装_2031180219440177154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1批量换装_2031180219440177154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `BatchCount+`
- `Display Int (rgthree)`
- `easy forLoopStart`
- `ImageBatchMultiple+`
- `ImageBatchMultiple+`
- `ImageBatchMultiple+`
- `ImageBatchMultiple+`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UltimateSDUpscaleCustomSample`
- `Upscale Model Loader`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `AdvancedLyingSigmaSampler` ★核心
- `KSamplerSelect` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `easy forLoopEnd`
- `easy batchAnything`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `PreviewImage`
- `CR Prompt Text`
- `Int`
- `Note`
- `Note`
- `easy int`
- `Note`
- `Int`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `590451495747466`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（75/82）

**有卡**：`BatchCount+`、`Display Int (rgthree)`、`easy forLoopStart`、`ImageBatchMultiple+`、`UNETLoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CFGNorm`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`UltimateSDUpscaleCustomSample`、`Upscale Model Loader`、`UpscaleModelLoader`、`AdvancedLyingSigmaSampler`、`KSamplerSelect`、`LayerUtility: PurgeVRAM V2`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`CLIPTextEncode`、`ConditioningZeroOut`、`ImageResize+`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch`、`easy forLoopEnd`、`easy batchAnything`、`SaveImage`、`FluxKontextImageScale`、`CR Prompt Text`、`Int`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
