---
key: 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json
name: qwen-image-2.1-服装模特图姿势裂变_2101840140003012609
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json
hash: e6b66c6b0602b20e
coverage: 0.853659
learned_at: 2026-10-15 22:25:36
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, BasicScheduler, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, CLIPLoader, VAELoader, VAEDecode, UNETLoader, UNETLoader, VAEEncode, easy ifElse, LoadImage, ImageTile+, Image Comparer (rgthree), TextEncodeQwenImage21, ImageScaleToTotalPixelsX, EmptyLatentImage, ImageScaleToTotalPixelsX, ColorMatchV2, SaveImage, ImageUntile+, CLIPLoader, TextGenerateLTX2Prompt, ResolutionSelector, RandomNoise, KSampler, PreviewAny, VAEDecode, Seed (rgthree), PrimitiveStringMultiline, PreviewImage, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 977910913157194, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
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

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `977910913157194`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`BasicScheduler`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`LoadImage`、`ImageTile+`、`TextEncodeQwenImage21`、`ImageScaleToTotalPixelsX`、`EmptyLatentImage`、`ColorMatchV2`、`SaveImage`、`ImageUntile+`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`RandomNoise`、`KSampler`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector
