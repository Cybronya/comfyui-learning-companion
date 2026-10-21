---
key: 图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105063037303611394.json
name: qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105063037303611394
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105063037303611394.json
hash: 01bf4d1176d1df56
coverage: 0.857143
learned_at: 2026-10-21 00:46:02
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, BasicScheduler, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, CLIPLoader, VAELoader, VAEDecode, UNETLoader, UNETLoader, VAEEncode, easy ifElse, LoadImage, ImageTile+, Image Comparer (rgthree), TextEncodeQwenImage21, ImageScaleToTotalPixelsX, EmptyLatentImage, ImageScaleToTotalPixelsX, ColorMatchV2, SaveImage, ImageUntile+, CLIPLoader, TextGenerateLTX2Prompt, ResolutionSelector, RandomNoise, KSampler, PreviewAny, VAEDecode, Seed (rgthree), PrimitiveStringMultiline, PreviewImage, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105063037303611394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105063037303611394.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `ReferenceLatent`
- `BasicScheduler`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `easy ifElse`
- `LoadImage`
- `ImageTile+`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `ImageScaleToTotalPixelsX`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixelsX`
- `ColorMatchV2`
- `SaveImage`
- `ImageUntile+`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `RandomNoise`
- `KSampler` ★核心
- `PreviewAny`
- `VAEDecode` ★核心
- `Seed (rgthree)`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `PreviewImage`
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

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **86%**（60/70）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`BasicScheduler`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`LoadImage`、`ImageTile+`、`TextEncodeQwenImage21`、`ImageScaleToTotalPixelsX`、`EmptyLatentImage`、`ColorMatchV2`、`SaveImage`、`ImageUntile+`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`RandomNoise`、`KSampler`、`Seed (rgthree)`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
