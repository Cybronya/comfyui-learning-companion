---
key: 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json
name: qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json
hash: e6b66c6b0602b20e
coverage: 0.780488
learned_at: 2026-10-09 22:19:27
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, BasicScheduler, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, CLIPLoader, VAELoader, VAEDecode, UNETLoader, UNETLoader, VAEEncode, easy ifElse, LoadImage, ImageTile+, Image Comparer (rgthree), TextEncodeQwenImage21, ImageScaleToTotalPixelsX, EmptyLatentImage, ImageScaleToTotalPixelsX, ColorMatchV2, SaveImage, ImageUntile+, CLIPLoader, TextGenerateLTX2Prompt, ResolutionSelector, RandomNoise, KSampler, PreviewAny, VAEDecode, Seed (rgthree), PrimitiveStringMultiline, PreviewImage, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: [ImageTile+, ImageUntile+, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 977910913157194, "steps": 25, "width": 1024}
discoveries: [次要节点 `ImageTile+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageUntile+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2101840140003012609.json`

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

覆盖率 **78%**（32/41）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`BasicScheduler`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`LoadImage`、`TextEncodeQwenImage21`、`ImageScaleToTotalPixelsX`、`EmptyLatentImage`、`ColorMatchV2`、`SaveImage`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`RandomNoise`、`KSampler`

**缺卡**（3）：`ImageTile+`、`ImageUntile+`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `ImageTile+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageUntile+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
