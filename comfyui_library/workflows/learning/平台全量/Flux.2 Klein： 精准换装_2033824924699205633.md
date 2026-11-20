---
key: 平台全量/Flux.2 Klein： 精准换装_2033824924699205633.json
name: Flux.2 Klein： 精准换装_2033824924699205633
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 Klein： 精准换装_2033824924699205633.json
hash: 7fe1ffa25ffc6c55
coverage: 0.853448
learned_at: 2026-11-14 00:28:53
nodes: [CLIPTextEncode, CLIPTextEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, VAEEncode, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, ReferenceLatent, KSampler, ReferenceLatent, FluxGuidance, ReferenceLatent, EmptyFlux2LatentImage, KSampler, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, ReferenceLatent, KSampler, ReferenceLatent, ReferenceLatent, FluxGuidance, CLIPTextEncode, CLIPTextEncode, VAEEncode, VAEEncode, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, ReferenceLatent, EmptyFlux2LatentImage, LayerUtility: PurgeVRAM, PreviewImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, easy promptReplace, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, PreviewImage, LayerUtility: PurgeVRAM, Note, VAEDecode, easy imageConcat, easy imageConcat, easy imageConcat, LayerUtility: PurgeVRAM, PreviewImage, SaveImage, easy imageConcat, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), VAEDecode, VAEDecode, SaveImage, ImageScaleBy, Reroute, easy positive, ShowText|pysssss, easy imageConcat, SeedVR2VideoUpscaler, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy promptReplace, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, ShowText|pysssss, llama_cpp_model_loader, llama_cpp_parameters, LayerUtility: PurgeVRAM, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM, ShowText|pysssss, ShowText|pysssss, LayerUtility: PurgeVRAM, ShowText|pysssss, ShowText|pysssss, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, easy positive, ShowText|pysssss, LoadImage, llama_cpp_instruct_adv, LoadImage, VAEDecode, PreviewImage, LoadImage, PreviewImage, RHHiddenNodes, UNETLoader, RHHiddenNodes, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1058623464663435, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2 Klein： 精准换装_2033824924699205633.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 Klein： 精准换装_2033824924699205633.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（116 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy promptReplace`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `Note`
- `VAEDecode` ★核心
- `easy imageConcat`
- `easy imageConcat`
- `easy imageConcat`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `SaveImage`
- `easy imageConcat`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageScaleBy`
- `Reroute`
- `easy positive`
- `ShowText|pysssss`
- `easy imageConcat`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy promptReplace`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `LayerUtility: PurgeVRAM`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy positive`
- `ShowText|pysssss`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `RHHiddenNodes`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1058623464663435`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（99/116）

**有卡**：`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`FluxGuidance`、`EmptyFlux2LatentImage`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy promptReplace`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VAEDecode`、`easy imageConcat`、`SaveImage`、`ImageScaleBy`、`easy positive`、`SeedVR2VideoUpscaler`、`LoadImage`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`RHHiddenNodes`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
