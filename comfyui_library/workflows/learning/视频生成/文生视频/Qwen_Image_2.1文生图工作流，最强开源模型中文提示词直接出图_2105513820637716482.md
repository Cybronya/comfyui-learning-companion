---
key: 视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json
name: Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json
hash: ee3982b668ea9fc9
coverage: 0.886364
learned_at: 2026-10-10 00:07:22
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, UNETLoader, CLIPLoader, VAELoader, ResolutionSelector, KSampler, CLIPLoader, TextGenerateLTX2Prompt, SaveImageAdvanced, SaveImage, Text, easy showAnything, ImpactSwitch, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `SaveImageAdvanced`
- `SaveImage`
- `Text`
- `easy showAnything`
- `ImpactSwitch`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`KSampler`、`TextGenerateLTX2Prompt`、`SaveImageAdvanced`、`SaveImage`、`Text`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
