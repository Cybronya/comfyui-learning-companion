---
key: 平台全量/Qwen Image 2.1好玩的Lora_2106688379445399554.json
name: Qwen Image 2.1好玩的Lora_2106688379445399554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1好玩的Lora_2106688379445399554.json
hash: 8aac3c229716bc5d
coverage: 0.666667
learned_at: 2026-11-14 00:50:05
nodes: [SetNode, EmptyLatentImage, VAELoader, UNETLoader, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, Image Comparer (rgthree), AddLabel, QwenImage21Cache, PreviewImage, CLIPLoader, LoadImage, GetNode, GetNode, easy showAnything, 孤海注释, TTResolutionSelector, BatchImagesNode, ResolutionSelector, ImageConcatMulti, LoadImage, SetNode, TTResolutionSelector, ImageResizeKJv2, CR Prompt Text, CLIPLoader, KSampler, MuyeTextEditOutput, TextGenerate, ImageResizeKJv2, LoraLoaderModelOnly, SaveImage, SaveImageAdvanced, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 672414859686611, "steps": 40, "width": 1024}
---

# 平台全量/Qwen Image 2.1好玩的Lora_2106688379445399554.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1好玩的Lora_2106688379445399554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
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
- `孤海注释`
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `672414859686611`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（26/39）

**有卡**：`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`VAEDecode`、`TextEncodeQwenImage21`、`AddLabel`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`TTResolutionSelector`、`BatchImagesNode`、`ResolutionSelector`、`ImageConcatMulti`、`ImageResizeKJv2`、`CR Prompt Text`、`KSampler`、`MuyeTextEditOutput`、`TextGenerate`、`LoraLoaderModelOnly`、`SaveImage`、`SaveImageAdvanced`、`easy cleanGpuUsed`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
