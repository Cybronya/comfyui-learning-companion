---
key: 图片生成/文生图/qwen image2.1 turbo二合一工作流 文生图图生图二合一_2109732642299142146.json
name: qwen image2.1 turbo二合一工作流 文生图图生图二合一_2109732642299142146
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image2.1 turbo二合一工作流 文生图图生图二合一_2109732642299142146.json
hash: 14b954560a39634c
coverage: 0.808824
learned_at: 2026-10-21 02:57:29
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveStringMultiline, PreviewAny, PrimitiveStringMultiline, TextGenerate, BatchImagesNode, ImageScaleToTotalPixels, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, PrimitiveStringMultiline, ImageResizeKJv2, GetImageSize, SamplerCustom, KSamplerSelect, ManualSigmas, QwenImage21Cache, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Any Switch (rgthree), TextEncodeQwenImage21, ResolutionSelector, VAEDecode, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen image2.1 turbo二合一工作流 文生图图生图二合一_2109732642299142146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image2.1 turbo二合一工作流 文生图图生图二合一_2109732642299142146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `ModelAttentionBackend`
- `CLIPLoader`
- `TextGenerate`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `GetImageSize`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **81%**（55/68）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`PrimitiveBoolean`、`TextGenerate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`ModelAttentionBackend`、`ImageResizeKJv2`、`GetImageSize`、`SamplerCustom`、`KSamplerSelect`、`ManualSigmas`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
