---
key: 图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json
name: Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json
hash: 06a3021943392fae
coverage: 0.803279
learned_at: 2026-10-21 00:42:07
nodes: [UNETLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, PrimitiveStringMultiline, StringConcatenate, BatchImagesNode, ImageScaleToTotalPixels, SaveImage, SaveImageAdvanced, KSampler, VAEDecode, RegexExtract, CLIPLoader, TextGenerate, LoadImage, ComfySwitchNode, PreviewAny, Image Comparer (rgthree), PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveBoolean, ComfySwitchNode, EmptyLatentImage, LoadImage, LoadImage, ResolutionSelector, LoadImage, PrimitiveBoolean, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RegexExtract`
- `CLIPLoader`
- `TextGenerate`
- `LoadImage`
- `ComfySwitchNode`
- `PreviewAny`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **80%**（49/61）

**有卡**：`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LoadImage`、`StringConcatenate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`SaveImage`、`SaveImageAdvanced`、`KSampler`、`VAEDecode`、`RegexExtract`、`CLIPLoader`、`TextGenerate`、`PrimitiveBoolean`、`EmptyLatentImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
