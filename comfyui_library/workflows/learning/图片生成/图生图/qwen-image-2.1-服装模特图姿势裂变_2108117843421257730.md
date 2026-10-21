---
key: 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2108117843421257730.json
name: qwen-image-2.1-服装模特图姿势裂变_2108117843421257730
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2108117843421257730.json
hash: 49a6d8f75d3baf6e
coverage: 0.853659
learned_at: 2026-10-21 00:46:06
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, BasicScheduler, RandomNoise, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, CLIPLoader, VAELoader, VAEDecode, KSampler, UNETLoader, UNETLoader, VAEEncode, easy ifElse, VAEDecode, LoadImage, ImageTile+, Image Comparer (rgthree), TextEncodeQwenImage21, ImageScaleToTotalPixelsX, PrimitiveStringMultiline, EmptyLatentImage, ImageScaleToTotalPixelsX, PreviewImage, ColorMatchV2, SaveImage, ImageUntile+, PreviewImage, CLIPLoader, TextGenerateLTX2Prompt, PreviewAny, Seed (rgthree), ResolutionSelector]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 871605622548972, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2108117843421257730.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2108117843421257730.json`

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
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `easy ifElse`
- `VAEDecode` ★核心
- `LoadImage`
- `ImageTile+`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `ImageScaleToTotalPixelsX`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixelsX`
- `PreviewImage`
- `ColorMatchV2`
- `SaveImage`
- `ImageUntile+`
- `PreviewImage`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `Seed (rgthree)`
- `ResolutionSelector`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `871605622548972`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`BasicScheduler`、`RandomNoise`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`VAEEncode`、`LoadImage`、`ImageTile+`、`TextEncodeQwenImage21`、`ImageScaleToTotalPixelsX`、`EmptyLatentImage`、`ColorMatchV2`、`SaveImage`、`ImageUntile+`、`TextGenerateLTX2Prompt`、`Seed (rgthree)`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector
