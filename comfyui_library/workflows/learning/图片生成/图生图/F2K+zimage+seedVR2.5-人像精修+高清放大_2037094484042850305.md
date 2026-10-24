---
key: 图片生成/图生图/F2K+zimage+seedVR2.5-人像精修+高清放大_2037094484042850305.json
name: F2K+zimage+seedVR2.5-人像精修+高清放大_2037094484042850305
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F2K+zimage+seedVR2.5-人像精修+高清放大_2037094484042850305.json
hash: 39e3a3056abeb39a
coverage: 0.826923
learned_at: 2026-10-23 10:53:04
nodes: [ImageScaleBy, TTP_Image_Tile_Batch, TTP_Tile_image_size, 数学运算_孤海, GetImageSize+, SeedVR2VideoUpscaler, easy cleanGpuUsed, SeedVR2LoadDiTModel, Flux2KleinModelConfig_EditUtils, Flux2KleinConfigPreparer_EditUtils, KSampler, EditTextEncode_EditUtils, VAEDecode, easy imageColorMatch, easy ifElse, ColorCorrect, CLIPTextEncode, ReferenceLatent, SetNode, KSamplerAdvanced, easy cleanGpuUsed, VAEEncode, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, VAEDecode, ImageScaleBy, easy imageScaleToNormPixels, easy showAnything, easy showAnything, SeedVR2LoadVAEModel, Get Image Size, easy boolean, MarkdownNote, MarkdownNote, LoadImage, TextInput_, MarkdownNote, PreviewImage, PreviewImage, FloatSlider, easy int, UNETLoader, CLIPLoader, VAELoader, Lora Loader Stack (rgthree), 图像缩放V2_孤海, CheckpointLoaderSimple, LoraLoaderModelOnly, ImageResize+, TTP_Image_Assy, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 8, "checkpoint": "z-image-turbo-bf16-aio.safetensors", "denoise": "beta57", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F2K+zimage+seedVR2.5-人像精修+高清放大_2037094484042850305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F2K+zimage+seedVR2.5-人像精修+高清放大_2037094484042850305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `ImageScaleBy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `数学运算_孤海`
- `GetImageSize+`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `SeedVR2LoadDiTModel`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `KSampler` ★核心
- `EditTextEncode_EditUtils`
- `VAEDecode` ★核心
- `easy imageColorMatch`
- `easy ifElse`
- `ColorCorrect`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `easy imageScaleToNormPixels`
- `easy showAnything`
- `easy showAnything`
- `SeedVR2LoadVAEModel`
- `Get Image Size`
- `easy boolean`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `TextInput_`
- `MarkdownNote`
- `PreviewImage`
- `PreviewImage`
- `FloatSlider`
- `easy int`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Lora Loader Stack (rgthree)`
- `图像缩放V2_孤海`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResize+`
- `TTP_Image_Assy`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta57`
- `checkpoint` = `z-image-turbo-bf16-aio.safetensors`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`ImageScaleBy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`数学运算_孤海`、`GetImageSize+`、`SeedVR2VideoUpscaler`、`easy cleanGpuUsed`、`SeedVR2LoadDiTModel`、`Flux2KleinModelConfig_EditUtils`、`Flux2KleinConfigPreparer_EditUtils`、`KSampler`、`EditTextEncode_EditUtils`、`VAEDecode`、`easy imageColorMatch`、`ColorCorrect`、`CLIPTextEncode`、`ReferenceLatent`、`KSamplerAdvanced`、`VAEEncode`、`ModelSamplingAuraFlow`、`easy imageScaleToNormPixels`、`SeedVR2LoadVAEModel`、`Get Image Size`、`easy boolean`、`LoadImage`、`TextInput_`、`FloatSlider`、`easy int`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Lora Loader Stack (rgthree)`、`图像缩放V2_孤海`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`ImageResize+`、`TTP_Image_Assy`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
