---
key: 图片生成/图生图/Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330.json
name: Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330.json
hash: 25d8db4449cdca5d
coverage: 0.764706
learned_at: 2026-10-10 20:48:06
nodes: [VAELoader, EmptyLatentImage, QwenImage21Cache, UNETLoader, CLIPLoader, KSampler, Image Comparer (rgthree), SeedVR2LoadDiTModel, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, PrimitiveStringMultiline, PrimitiveStringMultiline, StringFormat, TextEncodeQwenImage21, SaveImage, CLIPLoader, PrimitiveStringMultiline, BatchImagesNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), TextGenerate, Fast Groups Bypasser (rgthree), ShowAnything|Mie, ResolutionSelector, PrimitiveBoolean, ShowAnything|Mie, LoadImage, ComfySwitchNode, RegexExtract, PrimitiveStringMultiline, ComfySwitchNode, VAEDecode, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [ShowAnything|Mie, ShowAnything|Mie]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `StringFormat`
- `TextEncodeQwenImage21`
- `SaveImage`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `TextGenerate`
- `Fast Groups Bypasser (rgthree)`
- `ShowAnything|Mie`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `ShowAnything|Mie`
- `LoadImage`
- `ComfySwitchNode`
- `RegexExtract`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
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

覆盖率 **76%**（52/68）

**有卡**：`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`KSampler`、`SeedVR2LoadDiTModel`、`SaveImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`StringFormat`、`TextEncodeQwenImage21`、`BatchImagesNode`、`LoadImage`、`TextGenerate`、`ResolutionSelector`、`PrimitiveBoolean`、`RegexExtract`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`ShowAnything|Mie`、`ShowAnything|Mie`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
