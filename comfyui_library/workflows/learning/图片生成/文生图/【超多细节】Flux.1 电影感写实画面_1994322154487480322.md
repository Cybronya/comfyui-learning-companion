---
key: 图片生成/文生图/【超多细节】Flux.1 电影感写实画面_1994322154487480322.json
name: 【超多细节】Flux.1 电影感写实画面_1994322154487480322
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【超多细节】Flux.1 电影感写实画面_1994322154487480322.json
hash: 866ccd1deca55795
coverage: 0.86
learned_at: 2026-10-19 21:33:20
nodes: [DualCLIPLoader, CLIPTextEncode, ConditioningZeroOut, LayerUtility: LoadJoyCaptionBeta1Model, UNETLoader, UNETLoader, EmptyLatentImage, LayerUtility: JoyCaptionBeta1, easy ifElse, PrimitiveBoolean, VAELoader, Anything Everywhere, easy imageBatchToImageList, LoraLoaderModelOnly, VAEEncode, TTP_Tile_image_size, UpscaleModelLoader, ImageScaleBy, ImageUpscaleWithModel, TTP_Image_Tile_Batch, LayerUtility: JoyCaptionBeta1, DualCLIPLoader, VAEDecode, easy imageListToImageBatch, TTP_Image_Assy, SaveImage, Image Comparer (rgthree), LayerUtility: LoadJoyCaptionBeta1Model, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, KSampler, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text Concatenate, CR Text Concatenate, Text Multiline, LoraLoaderModelOnly, KSampler, LoadImage, easy ifElse, easy ifElse, Text Multiline, easy showAnything, MaraScottIsEmptyOrNone_v1, RH_Translator, Text Multiline, VAEDecode, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 904, "sampler_name": "euler", "scheduler": "beta", "seed": 713637336246651, "steps": 8, "width": 1600}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【超多细节】Flux.1 电影感写实画面_1994322154487480322.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【超多细节】Flux.1 电影感写实画面_1994322154487480322.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: JoyCaptionBeta1`
- `easy ifElse`
- `PrimitiveBoolean`
- `VAELoader`
- `Anything Everywhere`
- `easy imageBatchToImageList`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `TTP_Image_Tile_Batch`
- `LayerUtility: JoyCaptionBeta1`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `easy ifElse`
- `easy ifElse`
- `Text Multiline`
- `easy showAnything`
- `MaraScottIsEmptyOrNone_v1`
- `RH_Translator`
- `Text Multiline`
- `VAEDecode` ★核心
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1600`
- `height` = `904`
- `batch_size` = `1`
- `seed` = `713637336246651`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（43/50）

**有卡**：`DualCLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LayerUtility: LoadJoyCaptionBeta1Model`、`UNETLoader`、`EmptyLatentImage`、`LayerUtility: JoyCaptionBeta1`、`PrimitiveBoolean`、`VAELoader`、`easy imageBatchToImageList`、`LoraLoaderModelOnly`、`VAEEncode`、`TTP_Tile_image_size`、`UpscaleModelLoader`、`ImageScaleBy`、`ImageUpscaleWithModel`、`TTP_Image_Tile_Batch`、`VAEDecode`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`SaveImage`、`KSampler`、`CR Text Concatenate`、`Text Multiline`、`LoadImage`、`MaraScottIsEmptyOrNone_v1`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
