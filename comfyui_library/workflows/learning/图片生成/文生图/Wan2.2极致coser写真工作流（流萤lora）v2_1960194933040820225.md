---
key: 图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json
name: Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json
hash: ec7b82afd9b158f7
coverage: 0.618557
learned_at: 2026-10-10 20:59:14
nodes: [PrimitiveInt, Seed_, JjkText, JWInteger, JWInteger, ImageScaleToTotalPixels, easy cleanGpuUsed, easy compare, easy int, easy int, easy ifElse, easy ifElse, easy showAnything, easy showAnything, easy showAnything, GetImageSize, CLIPLoader, VAEDecodeTiled, UNETLoader, CLIPTextEncode, VAEEncodeTiled, easy forLoopEnd, CLIPTextEncode, LoraLoaderModelOnly, SimpleMath+, SimpleMath+, ImageResize+, Get Image Size, Image Comparer (rgthree), SeedVR2BlockSwap, RH_Captioner, VAELoader, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, KSamplerAdvanced, VAEDecode, PreviewImage, JoinStrings, easy showAnything, ConstrainImage|pysssss, PreviewImage, LoraLoaderModelOnly, Note, Note, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageSize, VAEDecode, ImageSharpen, easy imageColorMatch, SetNode, ConstrainImage|pysssss, ImageResize+, UNETLoader, VAEDecode, ImageSharpen, easy batchAnything, easy forLoopStart, easy imageCount, ImageFromBatch, easy showAnything, KSampler, ImpactMinMax, ImageCASharpening+, SeedVR2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, easy imageBatchToImageList, easy imageListToImageBatch, ImageUpscaleWithModel, JjkText, UpscaleModelLoader, KSamplerAdvanced, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, KSampler, ModelSamplingSD3, SaveImage, SaveImage, LoadImage, TTP_Image_Assy, VAELoader, VAELoader, VAEEncode, SaveLatent]
patterns: [text_to_image, image_to_image]
missing: [ConstrainImage|pysssss, ConstrainImage|pysssss, ImageCASharpening+, LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, easy batchAnything, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, easy imageBatchToImageList, easy imageColorMatch, easy imageCount, easy imageListToImageBatch, easy int, easy int, Get Image Size, ImageResize+, ImageResize+, easy imageSize]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.10000000000000002, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 983381153161005, "steps": 3, "width": 512}
discoveries: [次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy compare` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `Get Image Size` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json`

## 结构

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
- `VAEDecodeTiled`
- `UNETLoader`
- `CLIPTextEncode`
- `VAEEncodeTiled`
- `easy forLoopEnd`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResize+`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `SeedVR2BlockSwap`
- `RH_Captioner`
- `VAELoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode`
- `CLIPLoader`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSampler`
- `LoraLoaderModelOnly`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced`
- `VAEDecode`
- `PreviewImage`
- `JoinStrings`
- `easy showAnything`
- `ConstrainImage|pysssss`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `Note`
- `Note`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageSize`
- `VAEDecode`
- `ImageSharpen`
- `easy imageColorMatch`
- `SetNode`
- `ConstrainImage|pysssss`
- `ImageResize+`
- `UNETLoader`
- `VAEDecode`
- `ImageSharpen`
- `easy batchAnything`
- `easy forLoopStart`
- `easy imageCount`
- `ImageFromBatch`
- `easy showAnything`
- `KSampler`
- `ImpactMinMax`
- `ImageCASharpening+`
- `SeedVR2`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `EmptyLatentImage`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `ImageUpscaleWithModel`
- `JjkText`
- `UpscaleModelLoader`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `KSampler`
- `ModelSamplingSD3`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `TTP_Image_Assy`
- `VAELoader`
- `VAELoader`
- `VAEEncode`
- `SaveLatent`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `0.10000000000000002`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `983381153161005`
- `steps` = `3`
- `width` = `512`

## 知识

覆盖率 **62%**（60/97）

**有卡**：`PrimitiveInt`、`Seed_`、`JjkText`、`JWInteger`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`easy compare`、`easy int`、`easy ifElse`、`easy showAnything`、`GetImageSize`、`CLIPLoader`、`VAEDecodeTiled`、`UNETLoader`、`CLIPTextEncode`、`VAEEncodeTiled`、`easy forLoopEnd`、`LoraLoaderModelOnly`、`SimpleMath+`、`ImageResize+`、`Get Image Size`、`Image Comparer (rgthree)`、`SeedVR2BlockSwap`、`RH_Captioner`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSampler`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`VAEDecode`、`PreviewImage`、`JoinStrings`、`ConstrainImage|pysssss`、`Note`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageSize`、`ImageSharpen`、`easy imageColorMatch`、`SetNode`

**缺卡**（21）：`ConstrainImage|pysssss`、`ConstrainImage|pysssss`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`SimpleMath+`、`easy batchAnything`、`easy cleanGpuUsed`、`easy compare`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageBatchToImageList`、`easy imageColorMatch`、`easy imageCount`、`easy imageListToImageBatch`、`easy int`、`easy int`、`Get Image Size`、`ImageResize+`、`ImageResize+`、`easy imageSize`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy compare` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `Get Image Size` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
