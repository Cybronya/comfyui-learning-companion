---
key: 图片生成/文生图/Z加Qwen2.1写真分镜方案，文生图反推提示词出片_2110508368321409025.json
name: Z加Qwen2.1写真分镜方案，文生图反推提示词出片_2110508368321409025
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z加Qwen2.1写真分镜方案，文生图反推提示词出片_2110508368321409025.json
hash: 9537ea8f4e71c943
coverage: 0.539474
learned_at: 2026-10-21 02:56:38
nodes: [ConditioningZeroOut, VAEDecode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetImageSize, SetNode, SetNode, GetNode, SetNode, SetNode, easy int, GetNode, GetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, EmptySD3LatentImage, GetNode, GetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, PrimitiveString, PrimitiveString, GetNode, StringConcatenate, PlaySound|pysssss, CLIPLoader, llama_cpp_parameters, SomethingToString, GetNode, SetNode, SomethingToString, GetNode, SetNode, GetNode, GetNode, easy promptLine, SetNode, ImageScaleBy, CLIPTextEncode, easy int, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy cleanGpuUsed, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, UNETLoader, VAELoader, SetNode, SetNode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_model_loader, LayerUtility: TextBox, LayerUtility: TextBox, VAELoader, CLIPLoader, UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, QwenImage21Cache, LayerUtility: TextBox, ProcessString, easy cleanGpuUsed, ProcessString, easy cleanGpuUsed, easy showAnything, easy showAnything, SaveImage, SetNode, ImageScaleToTotalPixels, GetNode, SetNode, SeedVR2VideoUpscaler, UpscaleModelLoader, PlaySound|pysssss, GetNode, GetNode, GetNode, Any Switch (rgthree), Image Comparer (rgthree), GetNode, SaveImage, easy int, easy int, GetNode, TextEncodeQwenImage21, GetNode, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, ImageUpscaleWithModel, llama_cpp_instruct_adv, llama_cpp_instruct_adv, LayerUtility: TextBox, GetNode, SaveImage, KSampler, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z加Qwen2.1写真分镜方案，文生图反推提示词出片_2110508368321409025.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z加Qwen2.1写真分镜方案，文生图反推提示词出片_2110508368321409025.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（152 个）：
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
- `LayerUtility: TextBox`
- `GetNode`
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（82/152）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`GetImageSize`、`easy int`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`StringConcatenate`、`PlaySound|pysssss`、`CLIPLoader`、`llama_cpp_parameters`、`SomethingToString`、`easy promptLine`、`ImageScaleBy`、`CLIPTextEncode`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`llama_cpp_model_loader`、`LayerUtility: TextBox`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`QwenImage21Cache`、`ProcessString`、`SaveImage`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`UpscaleModelLoader`、`TextEncodeQwenImage21`、`ModelPreviewOverrideKJ`、`ImageUpscaleWithModel`、`llama_cpp_instruct_adv`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
