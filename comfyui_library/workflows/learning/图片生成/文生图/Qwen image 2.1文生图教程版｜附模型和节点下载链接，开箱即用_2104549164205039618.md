---
key: Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json
name: Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json
hash: 6e5a8b7c9768defd
coverage: 0.811594
learned_at: 2026-10-10 20:58:57
nodes: [TextGenerate, RegexExtract, Seed (rgthree), UNETLoader, CLIPLoader, VAELoader, SeedVR2LoadVAEModel, SaveImage, SeedVR2LoadDiTModel, ImageScaleToTotalPixels, PreviewImage, VAEDecode, SaveImage, PrimitiveStringMultiline, EmptyLatentImage, PreviewAny, ResolutionSelector, StringConcatenate, TextEncodeQwenImage21, Any Switch (rgthree), PrimitiveStringMultiline, PreviewImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), KSampler, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, SeedVR2VideoUpscaler]
patterns: [text_to_image]
missing: [Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `TextGenerate`
- `RegexExtract`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `ResolutionSelector`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `Any Switch (rgthree)`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
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
- `SeedVR2VideoUpscaler`

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

覆盖率 **81%**（56/69）

**有卡**：`TextGenerate`、`RegexExtract`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`StringConcatenate`、`TextEncodeQwenImage21`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`SeedVR2VideoUpscaler`

**缺卡**（1）：`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
