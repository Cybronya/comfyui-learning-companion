---
key: 图片生成/图生图/Qwen Image Edit Plus 多参考图像编辑工作流-test_2046780751697420289.json
name: Qwen Image Edit Plus 多参考图像编辑工作流-test_2046780751697420289
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image Edit Plus 多参考图像编辑工作流-test_2046780751697420289.json
hash: c4fe713bcac64b5b
coverage: 0.904762
learned_at: 2026-10-23 11:13:17
nodes: [VAEDecodeTiled, CR Text, PrimitiveInt, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, TeaCache, VAEEncode, CR Text Concatenate, ReferenceLatent, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, UpscaleModelLoader, SeedVR2BlockSwap, SeedVR2, Images to RGB, Image Tiled, ImageUpscaleWithModel, ImageFromBatch, ImageConcanateOfUtils, ImageFromBatch, ImageFromBatch, ImageConcanateOfUtils, ImageFromBatch, ImageConcanateOfUtils, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Assy, TTP_Image_Tile_Batch, easy imageBatchToImageList, PreviewImage, ImageListToBatch+, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Int, Int, LoraLoaderModelOnly, VAELoader, CLIPLoader, ModelSamplingAuraFlow, easy cleanGpuUsed, VAEDecode, EmptyLatentImage, CFGNorm, SaveImage, Image Comparer (rgthree), AIO_Preprocessor, KSampler, MarkdownNote, CLIPTextEncode, SaveImage, LoadImage, TextEncodeQwenImageEditPlus, UNETLoader, LoadImage, LoadImage, CR Text, KSampler]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1.1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 320919058706232, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image Edit Plus 多参考图像编辑工作流-test_2046780751697420289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image Edit Plus 多参考图像编辑工作流-test_2046780751697420289.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `VAEDecodeTiled` ★核心
- `CR Text`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `TeaCache`
- `VAEEncode` ★核心
- `CR Text Concatenate`
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `Images to RGB`
- `Image Tiled`
- `ImageUpscaleWithModel`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `PreviewImage`
- `ImageListToBatch+`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CFGNorm`
- `SaveImage`
- `Image Comparer (rgthree)`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `CR Text`
- `KSampler` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `320919058706232`
- `steps` = `8`
- `cfg` = `1.1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（57/63）

**有卡**：`VAEDecodeTiled`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`TeaCache`、`VAEEncode`、`CR Text Concatenate`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`UpscaleModelLoader`、`SeedVR2BlockSwap`、`SeedVR2`、`Images to RGB`、`Image Tiled`、`ImageUpscaleWithModel`、`ImageFromBatch`、`ImageConcanateOfUtils`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`ImageListToBatch+`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`CLIPLoader`、`ModelSamplingAuraFlow`、`easy cleanGpuUsed`、`VAEDecode`、`EmptyLatentImage`、`CFGNorm`、`SaveImage`、`AIO_Preprocessor`、`KSampler`、`LoadImage`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
