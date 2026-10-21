---
key: 图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json
name: Krea2-文生图-v1.1_2094718098157948930
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json
hash: df9d3ec84a2f71d2
coverage: 0.864407
learned_at: 2026-10-20 01:18:57
nodes: [llama_cpp_model_loader, llama_cpp_parameters, EmptyLatentImage, ConditioningZeroOut, CLIPLoader, VAELoader, INTConstant, llama_cpp_model_loader, llama_cpp_parameters, EmptyLatentImage, ConditioningZeroOut, CLIPLoader, VAELoader, INTConstant, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, ImageScaleToTotalPixels, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, INTConstant, SeedVR2VideoUpscaler, PreviewImage, VAEDecode, ImageScaleToTotalPixels, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, INTConstant, SeedVR2VideoUpscaler, PreviewImage, VAEDecode, SaveImage, SaveImage, KSampler, ModelSamplingAuraFlow, SaveImage, LoraLoaderModelOnly, PreviewAny, llama_cpp_instruct_adv, UNETLoader, LoraLoaderModelOnly, CR Prompt Text, CR Prompt Text, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, llama_cpp_instruct_adv, PreviewAny, Int, PDRatioSelector, PrimitiveStringMultiline, ratio_selector, PrimitiveStringMultiline]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "simple", "seed": 40272947304437, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `Int`
- `PDRatioSelector`
- `PrimitiveStringMultiline`
- `ratio_selector`
- `PrimitiveStringMultiline`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `40272947304437`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（51/59）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_parameters`、`EmptyLatentImage`、`ConditioningZeroOut`、`CLIPLoader`、`VAELoader`、`INTConstant`、`CLIPTextEncode`、`KSampler`、`ModelSamplingAuraFlow`、`SaveImage`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VAEDecode`、`LoraLoaderModelOnly`、`llama_cpp_instruct_adv`、`UNETLoader`、`CR Prompt Text`、`Int`、`PDRatioSelector`、`ratio_selector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
