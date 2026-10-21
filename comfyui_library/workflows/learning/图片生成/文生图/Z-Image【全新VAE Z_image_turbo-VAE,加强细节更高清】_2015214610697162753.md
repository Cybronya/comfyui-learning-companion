---
key: 图片生成/文生图/Z-Image【全新VAE Z_image_turbo-VAE,加强细节更高清】_2015214610697162753.json
name: Z-Image【全新VAE Z_image_turbo-VAE,加强细节更高清】_2015214610697162753
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image【全新VAE Z_image_turbo-VAE,加强细节更高清】_2015214610697162753.json
hash: 2aa09a4c3fd03a03
coverage: 0.833333
learned_at: 2026-10-19 22:15:27
nodes: [CLIPTextEncode, ImageResize+, ImageScaleBy, ImageResize+, SeedVR2VideoUpscaler, TTP_Tile_image_size, TTP_Image_Tile_Batch, GetImageSize+, TTP_Image_Assy, GetImageSize+, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, VAEDecode, Note, UNETLoader, CLIPLoader, PrimitiveFloat, EmptyLatentImage, CLIPTextEncode, LoraLoaderModelOnly, ModelSamplingAuraFlow, Text Multiline, PreviewImage, VAELoader, Note, KSampler, Note, VAELoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 1045502413679055, "steps": 9, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image【全新VAE Z_image_turbo-VAE,加强细节更高清】_2015214610697162753.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image【全新VAE Z_image_turbo-VAE,加强细节更高清】_2015214610697162753.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `ImageScaleBy`
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `GetImageSize+`
- `TTP_Image_Assy`
- `GetImageSize+`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `VAEDecode` ★核心
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveFloat`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `Text Multiline`
- `PreviewImage`
- `VAELoader`
- `Note`
- `KSampler` ★核心
- `Note`
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1045502413679055`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`CLIPTextEncode`、`ImageResize+`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`GetImageSize+`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`Text Multiline`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
