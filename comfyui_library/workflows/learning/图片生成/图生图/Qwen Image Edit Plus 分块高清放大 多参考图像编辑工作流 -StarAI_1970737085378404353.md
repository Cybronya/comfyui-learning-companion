---
key: 图片生成/图生图/Qwen Image Edit Plus 分块高清放大 多参考图像编辑工作流 -StarAI_1970737085378404353.json
name: Qwen Image Edit Plus 分块高清放大 多参考图像编辑工作流 -StarAI_1970737085378404353
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image Edit Plus 分块高清放大 多参考图像编辑工作流 -StarAI_1970737085378404353.json
hash: 41db0e06e29826d0
coverage: 0.904762
learned_at: 2026-10-23 11:13:16
nodes: [VAEDecodeTiled, CR Text, PrimitiveInt, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, TeaCache, VAEEncode, CR Text Concatenate, ReferenceLatent, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, UpscaleModelLoader, SeedVR2BlockSwap, SeedVR2, Images to RGB, Image Tiled, ImageUpscaleWithModel, ImageFromBatch, ImageConcanateOfUtils, ImageFromBatch, ImageFromBatch, ImageConcanateOfUtils, ImageFromBatch, ImageConcanateOfUtils, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Assy, TTP_Image_Tile_Batch, easy imageBatchToImageList, PreviewImage, ImageListToBatch+, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Int, Int, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, VAELoader, CLIPLoader, ModelSamplingAuraFlow, easy cleanGpuUsed, VAEDecode, EmptyLatentImage, TextEncodeQwenImageEditPlus, CLIPTextEncode, CFGNorm, SaveImage, Image Comparer (rgthree), KSampler, SaveImage, AIO_Preprocessor, CR Text, KSampler, LoadImage, MarkdownNote]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.15000000000000002, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 586071187784427, "steps": 25, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image Edit Plus 分块高清放大 多参考图像编辑工作流 -StarAI_1970737085378404353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image Edit Plus 分块高清放大 多参考图像编辑工作流 -StarAI_1970737085378404353.json`

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
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `AIO_Preprocessor`
- `CR Text`
- `KSampler` ★核心
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `586071187784427`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **90%**（57/63）

**有卡**：`VAEDecodeTiled`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`TeaCache`、`VAEEncode`、`CR Text Concatenate`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`UpscaleModelLoader`、`SeedVR2BlockSwap`、`SeedVR2`、`Images to RGB`、`Image Tiled`、`ImageUpscaleWithModel`、`ImageFromBatch`、`ImageConcanateOfUtils`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`ImageListToBatch+`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LoadImage`、`CLIPLoader`、`ModelSamplingAuraFlow`、`easy cleanGpuUsed`、`VAEDecode`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`SaveImage`、`KSampler`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
