---
key: 图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115617911112032258.json
name: SeedVR2.5_+_TTP_分块放大_2115617911112032258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115617911112032258.json
hash: 8babf32b176174d9
coverage: 0.71875
learned_at: 2026-10-30 17:51:22
nodes: [ImageResize+, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, Get Image Size, TTP_Image_Assy, Get Image Size, ImageScaleBy, ConstrainImage|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2LoadDiTModel, LoadImage, SaveImage, SeedVR2LoadVAEModel, Image Comparer (rgthree), SeedVR2, easy imageColorMatch, Int Literal, SaveImage, SetNode, GetNode, GetNode, PreviewImage, SetNode, easy boolean, PreviewImage, GetNode, SetNode, SetNode, easy boolean, PrimitiveInt, PrimitiveInt, SaveImage, Flux2KleinConfigPreparer_EditUtils, GetNode, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, Flux2KleinModelConfig_EditUtils, SetNode, 取色器_孤海, Image Comparer (rgthree), easy cleanGpuUsed, VAELoader, CLIPTextEncode, ModelSamplingAuraFlow, GetNode, SetNode, CLIPTextEncode, CLIPTextEncode, ReferenceLatent, EditTextEncode_EditUtils, CR Text Concatenate, GetNode, CR Text Concatenate, easy ifElse, KSampler, Image Comparer (rgthree), VAEDecode, TextInput_, LoraLoaderModelOnly, easy ifElse, UNETLoader, CLIPLoader, Image Comparer (rgthree), TTP_Image_Assy, TTP_Image_Tile_Batch, GetNode, ImageScaleBy, SeedVR2LoadDiTModel, VAEEncode, VAEDecode, SetNode, GetNode, SetNode, KSamplerAdvanced, SeedVR2VideoUpscaler, easy imageColorMatch, GetNode, 图像缩放V2_孤海, GetNode, StringConstant, ColorCorrect, ImageResize+, SetNode, SeedVR2LoadVAEModel, Get Image Size, ImageScaleBy, TTP_Tile_image_size, 数学运算_孤海, easy imageScaleToNormPixels, easy showAnything, easy showAnything, easy cleanGpuUsed, GetImageSize+, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, easy imageSize, TTP_Image_Tile_Batch, VAELoader_Any, UNETLoader_Any, LoraLoaderModelOnly, VAEEncode, ReferenceLatent, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, UpscaleModelLoader, RandomNoise, CLIPTextEncode, easy imageBatchToImageList, CLIPLoader_Any, VAEDecode, easy imageColorMatch, easy imageListToImageBatch, TTP_Image_Assy, ImageUpscaleWithModel, ImageScaleBy, SaveImageJPG_GH, Image Comparer (rgthree), easy imageColorMatch, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 8, "denoise": "beta57", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115617911112032258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115617911112032258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（128 个）：
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `Get Image Size`
- `TTP_Image_Assy`
- `Get Image Size`
- `ImageScaleBy`
- `ConstrainImage|pysssss`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `SeedVR2`
- `easy imageColorMatch`
- `Int Literal`
- `SaveImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `easy boolean`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy boolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `Flux2KleinModelConfig_EditUtils`
- `SetNode`
- `取色器_孤海`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `EditTextEncode_EditUtils`
- `CR Text Concatenate`
- `GetNode`
- `CR Text Concatenate`
- `easy ifElse`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `TextInput_`
- `LoraLoaderModelOnly` ★核心
- `easy ifElse`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `GetNode`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `SeedVR2VideoUpscaler`
- `easy imageColorMatch`
- `GetNode`
- `图像缩放V2_孤海`
- `GetNode`
- `StringConstant`
- `ColorCorrect`
- `ImageResize+`
- `SetNode`
- `SeedVR2LoadVAEModel`
- `Get Image Size`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `数学运算_孤海`
- `easy imageScaleToNormPixels`
- `easy showAnything`
- `easy showAnything`
- `easy cleanGpuUsed`
- `GetImageSize+`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `VAELoader_Any`
- `UNETLoader_Any` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `UpscaleModelLoader`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `easy imageBatchToImageList`
- `CLIPLoader_Any`
- `VAEDecode` ★核心
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `SaveImageJPG_GH`
- `Image Comparer (rgthree)`
- `easy imageColorMatch`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta57`

## 知识

覆盖率 **72%**（92/128）

**有卡**：`ImageResize+`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`Get Image Size`、`TTP_Image_Assy`、`ConstrainImage|pysssss`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`LoadImage`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2`、`easy imageColorMatch`、`Int Literal`、`easy boolean`、`Flux2KleinConfigPreparer_EditUtils`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`Flux2KleinModelConfig_EditUtils`、`取色器_孤海`、`easy cleanGpuUsed`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`ReferenceLatent`、`EditTextEncode_EditUtils`、`CR Text Concatenate`、`KSampler`、`VAEDecode`、`TextInput_`、`VAEEncode`、`KSamplerAdvanced`、`图像缩放V2_孤海`、`StringConstant`、`ColorCorrect`、`数学运算_孤海`、`easy imageScaleToNormPixels`、`GetImageSize+`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixelsX`、`easy imageSize`、`VAELoader_Any`、`UNETLoader_Any`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`UpscaleModelLoader`、`RandomNoise`、`easy imageBatchToImageList`、`CLIPLoader_Any`、`easy imageListToImageBatch`、`ImageUpscaleWithModel`、`SaveImageJPG_GH`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
