---
key: 图片生成/图生图/F.2Klein-zimage人像精修高清放大_2058053312079028225.json
name: F.2Klein-zimage人像精修高清放大_2058053312079028225
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein-zimage人像精修高清放大_2058053312079028225.json
hash: 3e6e18ab643a573e
coverage: 0.888889
learned_at: 2026-10-23 10:52:41
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, ModelSamplingAuraFlow, VAEDecode, easy cleanGpuUsed, KSamplerAdvanced, KSampler, VAEEncode, TextInput_, LoadImage, EditTextEncode_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinConfigPreparer_EditUtils, CLIPTextEncode, ReferenceLatent, 图像缩放V2_孤海, Image Comparer (rgthree), SeedVR2LoadVAEModel, ImageScaleBy, easy cleanGpuUsed, SeedVR2VideoUpscaler, ImageScaleBy, GetImageSize+, ImageResize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, TTP_Image_Assy, easy imageScaleToNormPixels, Image Comparer (rgthree), Get Image Size, 数学运算_孤海, easy showAnything, easy showAnything, easy imageColorMatch, easy ifElse, ColorCorrect, 孤海-浮点滑条, easy int, SaveImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, easy boolean, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, SeedVR2LoadDiTModel, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 1106919809378802, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein-zimage人像精修高清放大_2058053312079028225.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein-zimage人像精修高清放大_2058053312079028225.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `TextInput_`
- `LoadImage`
- `EditTextEncode_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `图像缩放V2_孤海`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `easy imageScaleToNormPixels`
- `Image Comparer (rgthree)`
- `Get Image Size`
- `数学运算_孤海`
- `easy showAnything`
- `easy showAnything`
- `easy imageColorMatch`
- `easy ifElse`
- `ColorCorrect`
- `孤海-浮点滑条`
- `easy int`
- `SaveImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `easy boolean`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadDiTModel`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1106919809378802`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（48/54）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingAuraFlow`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`KSampler`、`VAEEncode`、`TextInput_`、`LoadImage`、`EditTextEncode_EditUtils`、`Flux2KleinModelConfig_EditUtils`、`Flux2KleinConfigPreparer_EditUtils`、`ReferenceLatent`、`图像缩放V2_孤海`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`GetImageSize+`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`easy imageScaleToNormPixels`、`Get Image Size`、`数学运算_孤海`、`easy imageColorMatch`、`ColorCorrect`、`孤海-浮点滑条`、`easy int`、`SaveImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy boolean`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SeedVR2LoadDiTModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
