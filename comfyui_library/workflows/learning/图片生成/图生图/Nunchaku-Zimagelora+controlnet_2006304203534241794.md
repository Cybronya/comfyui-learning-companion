---
key: 图片生成/图生图/Nunchaku-Zimagelora+controlnet_2006304203534241794.json
name: Nunchaku-Zimagelora+controlnet_2006304203534241794
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku-Zimagelora+controlnet_2006304203534241794.json
hash: aeeb5c3692d51aef
coverage: 0.754717
learned_at: 2026-10-23 11:10:02
nodes: [PreviewImage, PreviewImage, Note, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, LoadImage, LoadImage, QwenVisionNode, ShowText|pysssss, CLIPTextEncode, Image Comparer (rgthree), Any Switch (rgthree), VAEEncode, PreviewImage, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, QwenImageDiffsynthControlnet, ModelSamplingAuraFlow, PreviewImage, KSampler, KSampler, ImageUpscaleWithModel, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, TTP_Image_Tile_Batch, LayerUtility: PurgeVRAM V2, GetImageSize+, ImageResize+, PreviewImage, SeedVR2VideoUpscaler, TTP_Tile_image_size, Image Comparer (rgthree), UpscaleModelLoader, SeedVR2LoadDiTModel, Image Comparer (rgthree), TTP_Image_Assy, LayerUtility: PurgeVRAM V2, CLIPLoader, NunchakuZImageDiTLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), ModelPatchLoader, VAELoader, VAEDecode, PreviewImage, VAEDecode, SaveImage, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.5, "height": 512, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 620926546398131, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku-Zimagelora+controlnet_2006304203534241794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku-Zimagelora+controlnet_2006304203534241794.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `PreviewImage`
- `PreviewImage`
- `Note`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `QwenVisionNode`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `Any Switch (rgthree)`
- `VAEEncode` ★核心
- `PreviewImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `TTP_Image_Tile_Batch`
- `LayerUtility: PurgeVRAM V2`
- `GetImageSize+`
- `ImageResize+`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `TTP_Tile_image_size`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `NunchakuZImageDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ModelPatchLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `620926546398131`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.5`

## 知识

覆盖率 **75%**（40/53）

**有卡**：`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`LoadImage`、`QwenVisionNode`、`CLIPTextEncode`、`VAEEncode`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`ModelSamplingAuraFlow`、`KSampler`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM V2`、`TTP_Image_Tile_Batch`、`GetImageSize+`、`ImageResize+`、`SeedVR2VideoUpscaler`、`TTP_Tile_image_size`、`UpscaleModelLoader`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`CLIPLoader`、`NunchakuZImageDiTLoader`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`VAELoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
