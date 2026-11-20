---
key: 平台全量/❹「写真V0」Z+K 写真分镜「9.19」_2023430928676163585.json
name: ❹「写真V0」Z+K 写真分镜「9.19」_2023430928676163585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/❹「写真V0」Z+K 写真分镜「9.19」_2023430928676163585.json
hash: 4e6296d770685797
coverage: 0.485714
learned_at: 2026-11-14 01:21:09
nodes: [ConditioningZeroOut, VAEDecode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetImageSize, SetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, CLIPTextEncode, GetNode, GetNode, SetNode, SetNode, easy int, ReferenceLatent, VAEEncode, GetNode, GetNode, SetNode, SetNode, VAEDecode, GetNode, GetNode, easy cleanGpuUsed, SaveImage, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, EmptySD3LatentImage, GetNode, GetNode, SetNode, TextInput_, llama_cpp_instruct_adv, ModelPassThrough, SetNode, RandomNoise, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, PrimitiveString, PrimitiveString, GetNode, StringConcatenate, easy cleanGpuUsed, ImageCASharpening+, PlaySound|pysssss, SetNode, SetNode, SeedVR2VideoUpscaler, KSamplerSelect, CFGGuider, CLIPLoader, llama_cpp_parameters, SomethingToString, GetNode, easy cleanGpuUsed, SetNode, SomethingToString, GetNode, ProcessString, easy cleanGpuUsed, SetNode, GetNode, GetNode, easy promptLine, SetNode, GetNode, easy int, easy int, ImageScaleBy, CLIPTextEncode, easy int, PlaySound|pysssss, GetNode, GetNode, Any Switch (rgthree), GetNode, Image Comparer (rgthree), EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, SamplerCustomAdvanced, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, GetNode, GetNode, UpscaleModelLoader, ImageUpscaleWithModel, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TextInput_, easy cleanGpuUsed, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, UNETLoader, VAELoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, ProcessString, easy showAnything, easy showAnything, SaveImage, SetNode, TextInput_, KSampler, TextInput_, Note, Note, GetNode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, CLIPLoader, VAELoader, llama_cpp_parameters, UNETLoader, llama_cpp_model_loader, llama_cpp_model_loader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1120033220973629, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/❹「写真V0」Z+K 写真分镜「9.19」_2023430928676163585.json

> 来源文件 `comfyui_library/workflows/平台全量/❹「写真V0」Z+K 写真分镜「9.19」_2023430928676163585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（140 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `EmptySD3LatentImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `TextInput_`
- `llama_cpp_instruct_adv`
- `ModelPassThrough`
- `SetNode`
- `RandomNoise`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `StringConcatenate`
- `easy cleanGpuUsed`
- `ImageCASharpening+`
- `PlaySound|pysssss`
- `SetNode`
- `SetNode`
- `SeedVR2VideoUpscaler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPLoader`
- `llama_cpp_parameters`
- `SomethingToString`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `SomethingToString`
- `GetNode`
- `ProcessString`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy promptLine`
- `SetNode`
- `GetNode`
- `easy int`
- `easy int`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy int`
- `PlaySound|pysssss`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TextInput_`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `ProcessString`
- `easy showAnything`
- `easy showAnything`
- `SaveImage`
- `SetNode`
- `TextInput_`
- `KSampler` ★核心
- `TextInput_`
- `Note`
- `Note`
- `GetNode`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `CLIPLoader`
- `VAELoader`
- `llama_cpp_parameters`
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1120033220973629`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **49%**（68/140）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`GetImageSize`、`CLIPTextEncode`、`easy int`、`ReferenceLatent`、`VAEEncode`、`easy cleanGpuUsed`、`SaveImage`、`EmptySD3LatentImage`、`TextInput_`、`llama_cpp_instruct_adv`、`ModelPassThrough`、`RandomNoise`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`StringConcatenate`、`ImageCASharpening+`、`PlaySound|pysssss`、`SeedVR2VideoUpscaler`、`KSamplerSelect`、`CFGGuider`、`CLIPLoader`、`llama_cpp_parameters`、`SomethingToString`、`ProcessString`、`easy promptLine`、`ImageScaleBy`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`KSampler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`llama_cpp_model_loader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
