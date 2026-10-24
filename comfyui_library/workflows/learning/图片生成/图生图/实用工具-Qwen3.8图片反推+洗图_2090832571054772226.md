---
key: 图片生成/图生图/实用工具-Qwen3.8图片反推+洗图_2090832571054772226.json
name: 实用工具-Qwen3.8图片反推+洗图_2090832571054772226
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/实用工具-Qwen3.8图片反推+洗图_2090832571054772226.json
hash: d1d83d5bb094a169
coverage: 0.710526
learned_at: 2026-10-23 12:48:02
nodes: [CLIPLoader, SetNode, VAELoader, SetNode, UNETLoader, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, GetNode, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SetNode, GetNode, GetNode, WujiCleaner, ConditioningZeroOut, GetNode, EmptyLatentImage, KSampler, VAEDecode, SetNode, GetNode, INTConstant, SaveImage, Text, llama_cpp_model_loader, llama_cpp_instruct_adv, ImageResizeKJv2, llama_cpp_parameters, Label (rgthree), LoadImage, CLIPTextEncode, PreviewAny, easy saveText, TTResolutionSelector, Label (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 155398055834981, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/实用工具-Qwen3.8图片反推+洗图_2090832571054772226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/实用工具-Qwen3.8图片反推+洗图_2090832571054772226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SetNode`
- `GetNode`
- `GetNode`
- `WujiCleaner`
- `ConditioningZeroOut`
- `GetNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `INTConstant`
- `SaveImage`
- `Text`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `ImageResizeKJv2`
- `llama_cpp_parameters`
- `Label (rgthree)`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `easy saveText`
- `TTResolutionSelector`
- `Label (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `155398055834981`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **71%**（27/38）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`WujiCleaner`、`ConditioningZeroOut`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`INTConstant`、`SaveImage`、`Text`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ImageResizeKJv2`、`llama_cpp_parameters`、`Label (rgthree)`、`LoadImage`、`CLIPTextEncode`、`easy saveText`、`TTResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
