---
key: 图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json
name: Krea2角色四视图-文生图1.1_2094675007816425474
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json
hash: 865f8928d4c46760
coverage: 0.827586
learned_at: 2026-10-20 01:19:11
nodes: [llama_cpp_parameters, EmptyLatentImage, ConditioningZeroOut, CLIPLoader, VAELoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, ImageScaleToTotalPixels, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, INTConstant, SeedVR2VideoUpscaler, PreviewImage, VAEDecode, SaveImage, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, llama_cpp_model_loader, PrimitiveStringMultiline, PDRatioSelector, ratio_selector, Int, PreviewAny, llama_cpp_instruct_adv, PrimitiveStringMultiline]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "simple", "seed": 848824601139743, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `llama_cpp_parameters`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
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
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_model_loader`
- `PrimitiveStringMultiline`
- `PDRatioSelector`
- `ratio_selector`
- `Int`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `848824601139743`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`llama_cpp_parameters`、`EmptyLatentImage`、`ConditioningZeroOut`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`ModelSamplingAuraFlow`、`SaveImage`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`INTConstant`、`SeedVR2VideoUpscaler`、`VAEDecode`、`LoraLoaderModelOnly`、`UNETLoader`、`llama_cpp_model_loader`、`PDRatioSelector`、`ratio_selector`、`Int`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
