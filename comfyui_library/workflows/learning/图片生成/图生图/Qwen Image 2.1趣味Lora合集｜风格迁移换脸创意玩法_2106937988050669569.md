---
key: 图片生成/图生图/Qwen Image 2.1趣味Lora合集｜风格迁移换脸创意玩法_2106937988050669569.json
name: Qwen Image 2.1趣味Lora合集｜风格迁移换脸创意玩法_2106937988050669569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1趣味Lora合集｜风格迁移换脸创意玩法_2106937988050669569.json
hash: 3939f2d0299ec48c
coverage: 0.802469
learned_at: 2026-10-21 00:42:47
nodes: [SetNode, EmptyLatentImage, VAELoader, UNETLoader, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, Image Comparer (rgthree), AddLabel, QwenImage21Cache, PreviewImage, CLIPLoader, LoadImage, GetNode, GetNode, easy showAnything, TTResolutionSelector, BatchImagesNode, ResolutionSelector, ImageConcatMulti, LoadImage, SetNode, TTResolutionSelector, ImageResizeKJv2, CR Prompt Text, CLIPLoader, KSampler, MuyeTextEditOutput, TextGenerate, ImageResizeKJv2, LoraLoaderModelOnly, SaveImage, SaveImageAdvanced, easy cleanGpuUsed, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1趣味Lora合集｜风格迁移换脸创意玩法_2106937988050669569.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1趣味Lora合集｜风格迁移换脸创意玩法_2106937988050669569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `SetNode`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `AddLabel`
- `QwenImage21Cache`
- `PreviewImage`
- `CLIPLoader`
- `LoadImage`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `TTResolutionSelector`
- `BatchImagesNode`
- `ResolutionSelector`
- `ImageConcatMulti`
- `LoadImage`
- `SetNode`
- `TTResolutionSelector`
- `ImageResizeKJv2`
- `CR Prompt Text`
- `CLIPLoader`
- `KSampler` ★核心
- `MuyeTextEditOutput`
- `TextGenerate`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `easy cleanGpuUsed`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

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

覆盖率 **80%**（65/81）

**有卡**：`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`VAEDecode`、`TextEncodeQwenImage21`、`AddLabel`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`TTResolutionSelector`、`BatchImagesNode`、`ResolutionSelector`、`ImageConcatMulti`、`ImageResizeKJv2`、`CR Prompt Text`、`KSampler`、`MuyeTextEditOutput`、`TextGenerate`、`LoraLoaderModelOnly`、`SaveImage`、`SaveImageAdvanced`、`easy cleanGpuUsed`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
