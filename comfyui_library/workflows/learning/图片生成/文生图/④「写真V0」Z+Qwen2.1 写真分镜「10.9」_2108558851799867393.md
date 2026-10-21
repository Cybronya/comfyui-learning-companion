---
key: 图片生成/文生图/④「写真V0」Z+Qwen2.1 写真分镜「10.9」_2108558851799867393.json
name: ④「写真V0」Z+Qwen2.1 写真分镜「10.9」_2108558851799867393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/④「写真V0」Z+Qwen2.1 写真分镜「10.9」_2108558851799867393.json
hash: 6c1fe3048d5181d7
coverage: 0.456
learned_at: 2026-10-21 02:57:54
nodes: [ConditioningZeroOut, VAEDecode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetImageSize, SetNode, SetNode, GetNode, SetNode, SetNode, easy int, GetNode, GetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, EmptySD3LatentImage, GetNode, GetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, PrimitiveString, PrimitiveString, GetNode, StringConcatenate, PlaySound|pysssss, CLIPLoader, llama_cpp_parameters, SomethingToString, GetNode, SetNode, SomethingToString, GetNode, SetNode, GetNode, GetNode, easy promptLine, SetNode, ImageScaleBy, CLIPTextEncode, easy int, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy cleanGpuUsed, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, UNETLoader, VAELoader, SetNode, SetNode, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_model_loader, LayerUtility: TextBox, LayerUtility: TextBox, VAELoader, CLIPLoader, UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, QwenImage21Cache, LayerUtility: TextBox, ProcessString, easy cleanGpuUsed, ProcessString, easy cleanGpuUsed, easy showAnything, easy showAnything, SaveImage, SetNode, ImageScaleToTotalPixels, GetNode, SetNode, SeedVR2VideoUpscaler, UpscaleModelLoader, PlaySound|pysssss, GetNode, GetNode, GetNode, Any Switch (rgthree), Image Comparer (rgthree), GetNode, SaveImage, easy int, easy int, GetNode, TextEncodeQwenImage21, GetNode, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, ImageUpscaleWithModel, llama_cpp_instruct_adv, llama_cpp_instruct_adv, Note, LayerUtility: TextBox, GetNode, SaveImage, KSampler, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1120033220973629, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/④「写真V0」Z+Qwen2.1 写真分镜「10.9」_2108558851799867393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/④「写真V0」Z+Qwen2.1 写真分镜「10.9」_2108558851799867393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（125 个）：
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
- `GetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
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
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `StringConcatenate`
- `PlaySound|pysssss`
- `CLIPLoader`
- `llama_cpp_parameters`
- `SomethingToString`
- `GetNode`
- `SetNode`
- `SomethingToString`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy promptLine`
- `SetNode`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy int`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `QwenImage21Cache`
- `LayerUtility: TextBox`
- `ProcessString`
- `easy cleanGpuUsed`
- `ProcessString`
- `easy cleanGpuUsed`
- `easy showAnything`
- `easy showAnything`
- `SaveImage`
- `SetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `SetNode`
- `SeedVR2VideoUpscaler`
- `UpscaleModelLoader`
- `PlaySound|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `GetNode`
- `SaveImage`
- `easy int`
- `easy int`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `ImageUpscaleWithModel`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `Note`
- `LayerUtility: TextBox`
- `GetNode`
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `1120033220973629`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **46%**（57/125）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`GetImageSize`、`easy int`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`StringConcatenate`、`PlaySound|pysssss`、`CLIPLoader`、`llama_cpp_parameters`、`SomethingToString`、`easy promptLine`、`ImageScaleBy`、`CLIPTextEncode`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`llama_cpp_model_loader`、`LayerUtility: TextBox`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`QwenImage21Cache`、`ProcessString`、`SaveImage`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`UpscaleModelLoader`、`TextEncodeQwenImage21`、`ModelPreviewOverrideKJ`、`ImageUpscaleWithModel`、`llama_cpp_instruct_adv`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
