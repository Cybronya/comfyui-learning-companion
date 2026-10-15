---
key: 图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json
name: Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json
hash: ec7b82afd9b158f7
coverage: 0.835052
learned_at: 2026-10-15 22:27:37
nodes: [PrimitiveInt, Seed_, JjkText, JWInteger, JWInteger, ImageScaleToTotalPixels, easy cleanGpuUsed, easy compare, easy int, easy int, easy ifElse, easy ifElse, easy showAnything, easy showAnything, easy showAnything, GetImageSize, CLIPLoader, VAEDecodeTiled, UNETLoader, CLIPTextEncode, VAEEncodeTiled, easy forLoopEnd, CLIPTextEncode, LoraLoaderModelOnly, SimpleMath+, SimpleMath+, ImageResize+, Get Image Size, Image Comparer (rgthree), SeedVR2BlockSwap, RH_Captioner, VAELoader, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, KSamplerAdvanced, VAEDecode, PreviewImage, JoinStrings, easy showAnything, ConstrainImage|pysssss, PreviewImage, LoraLoaderModelOnly, Note, Note, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageSize, VAEDecode, ImageSharpen, easy imageColorMatch, SetNode, ConstrainImage|pysssss, ImageResize+, UNETLoader, VAEDecode, ImageSharpen, easy batchAnything, easy forLoopStart, easy imageCount, ImageFromBatch, easy showAnything, KSampler, ImpactMinMax, ImageCASharpening+, SeedVR2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, easy imageBatchToImageList, easy imageListToImageBatch, ImageUpscaleWithModel, JjkText, UpscaleModelLoader, KSamplerAdvanced, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, KSampler, ModelSamplingSD3, SaveImage, SaveImage, LoadImage, TTP_Image_Assy, VAELoader, VAELoader, VAEEncode, SaveLatent]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.10000000000000002, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 983381153161005, "steps": 3, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `PrimitiveInt`
- `Seed_`
- `JjkText`
- `JWInteger`
- `JWInteger`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `easy compare`
- `easy int`
- `easy int`
- `easy ifElse`
- `easy ifElse`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `GetImageSize`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncodeTiled` ★核心
- `easy forLoopEnd`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `ImageResize+`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `SeedVR2BlockSwap`
- `RH_Captioner`
- `VAELoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `JoinStrings`
- `easy showAnything`
- `ConstrainImage|pysssss`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageSize`
- `VAEDecode` ★核心
- `ImageSharpen`
- `easy imageColorMatch`
- `SetNode`
- `ConstrainImage|pysssss`
- `ImageResize+`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ImageSharpen`
- `easy batchAnything`
- `easy forLoopStart`
- `easy imageCount`
- `ImageFromBatch`
- `easy showAnything`
- `KSampler` ★核心
- `ImpactMinMax`
- `ImageCASharpening+`
- `SeedVR2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `ImageUpscaleWithModel`
- `JjkText`
- `UpscaleModelLoader`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `TTP_Image_Assy`
- `VAELoader`
- `VAELoader`
- `VAEEncode` ★核心
- `SaveLatent`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `983381153161005`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（81/97）

**有卡**：`Seed_`、`JWInteger`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`easy compare`、`easy int`、`GetImageSize`、`CLIPLoader`、`VAEDecodeTiled`、`UNETLoader`、`CLIPTextEncode`、`VAEEncodeTiled`、`easy forLoopEnd`、`LoraLoaderModelOnly`、`SimpleMath+`、`ImageResize+`、`Get Image Size`、`SeedVR2BlockSwap`、`RH_Captioner`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSampler`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`VAEDecode`、`JoinStrings`、`ConstrainImage|pysssss`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageSize`、`ImageSharpen`、`easy imageColorMatch`、`easy batchAnything`、`easy forLoopStart`、`easy imageCount`、`ImageFromBatch`、`ImpactMinMax`、`ImageCASharpening+`、`SeedVR2`、`EmptyLatentImage`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`SaveImage`、`LoadImage`、`TTP_Image_Assy`、`VAEEncode`、`SaveLatent`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
