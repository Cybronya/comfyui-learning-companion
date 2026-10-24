---
key: 图片生成/图生图/qwen-image-edit+TTP+SeedVR图片高清放大_2034445585201242114.json
name: qwen-image-edit+TTP+SeedVR图片高清放大_2034445585201242114
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-edit+TTP+SeedVR图片高清放大_2034445585201242114.json
hash: 0a044ab6368939ab
coverage: 0.8125
learned_at: 2026-10-23 11:42:48
nodes: [VAELoader, CLIPLoader, UNETLoader, KSampler, TextEncodeQwenImageEditPlus, CLIPTextEncode, EmptyLatentImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, easy showAnything, easy showAnything, TTP_Image_Assy, ImageResize+, PreviewImage, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Note, INTConstant, Setter, INTConstant, Setter, PrimitiveFloat, Setter, LayerUtility: ImageScaleByAspectRatio V2, Getter, Image Comparer (rgthree), Getter, Setter, VAEDecode, Setter, LoadImage, Getter, Getter, TTP_Image_Tile_Batch, TTP_Tile_image_size, Getter, Getter, ImageResize+, easy cleanGpuUsed, ImageScaleBy, GetImageSize+, easy showAnything, easy showAnything, GetImageSize+, ImageScaleBy]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-edit+TTP+SeedVR图片高清放大_2034445585201242114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-edit+TTP+SeedVR图片高清放大_2034445585201242114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `easy showAnything`
- `easy showAnything`
- `TTP_Image_Assy`
- `ImageResize+`
- `PreviewImage`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Note`
- `INTConstant`
- `Setter`
- `INTConstant`
- `Setter`
- `PrimitiveFloat`
- `Setter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Getter`
- `Image Comparer (rgthree)`
- `Getter`
- `Setter`
- `VAEDecode` ★核心
- `Setter`
- `LoadImage`
- `Getter`
- `Getter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Getter`
- `Getter`
- `ImageResize+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `GetImageSize+`
- `easy showAnything`
- `easy showAnything`
- `GetImageSize+`
- `ImageScaleBy`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`KSampler`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`TTP_Image_Assy`、`ImageResize+`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`INTConstant`、`Setter`、`LayerUtility: ImageScaleByAspectRatio V2`、`Getter`、`VAEDecode`、`LoadImage`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`ImageScaleBy`、`GetImageSize+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
