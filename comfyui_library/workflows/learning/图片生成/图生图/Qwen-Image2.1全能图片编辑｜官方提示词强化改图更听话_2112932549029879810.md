---
key: 图片生成/图生图/Qwen-Image2.1全能图片编辑｜官方提示词强化改图更听话_2112932549029879810.json
name: Qwen-Image2.1全能图片编辑｜官方提示词强化改图更听话_2112932549029879810
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1全能图片编辑｜官方提示词强化改图更听话_2112932549029879810.json
hash: 99f11ce85fe8ee03
coverage: 0.839506
learned_at: 2026-10-26 22:03:24
nodes: [ResolutionSelector, PrimitiveBoolean, PrimitiveStringMultiline, StringFormat, KSampler, VAEDecode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), ComfySwitchNode, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, TextGenerate, BatchImagesNode, CLIPLoader, PrimitiveStringMultiline, RegexExtract, ShowAnything|Mie, ShowAnything|Mie, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, QwenImage21Cache, SaveImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image2.1全能图片编辑｜官方提示词强化改图更听话_2112932549029879810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1全能图片编辑｜官方提示词强化改图更听话_2112932549029879810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `StringFormat`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
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

覆盖率 **84%**（68/81）

**有卡**：`ResolutionSelector`、`PrimitiveBoolean`、`StringFormat`、`KSampler`、`VAEDecode`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LoadImage`、`TextGenerate`、`BatchImagesNode`、`CLIPLoader`、`RegexExtract`、`ShowAnything|Mie`、`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImage`、`SeedVR2VideoUpscaler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
