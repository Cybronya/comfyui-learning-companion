---
key: 图片生成/图生图/F.2Klein9B一键证件照侧脸转正换服装换背景高清排版_2065959891482800130.json
name: F.2Klein9B一键证件照侧脸转正换服装换背景高清排版_2065959891482800130
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein9B一键证件照侧脸转正换服装换背景高清排版_2065959891482800130.json
hash: 6e638014536a3305
coverage: 0.617647
learned_at: 2026-10-21 00:38:56
nodes: [GetNode, GetNode, ConditioningZeroOut, VAEEncode, CLIPTextEncode, ReferenceLatent, CLIPLoader, GetNode, GetNode, VAEDecode, GetNode, SetNode, TextInput_, GuHai_IDPhotoCrop, ImageComposite+, RMBG, SetNode, Text Concatenate, TextInput_, GetNode, ImageScaleBy, TTP_Image_Assy, SeedVR2LoadVAEModel, ImageResize+, GetImageSize+, TextEncodeQwenImageEditPlus, Flux2KleinConfigPreparer_EditUtils, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, GetNode, ImageCASharpening+, KSampler, GetNode, easy ifElse, CLIPLoader, LoraLoaderModelOnly, VAELoader, GetNode, SetNode, LoraLoaderModelOnly, GetNode, GetNode, ModelSamplingAuraFlow, UNETLoader, SetNode, VAEDecode, easy imageColorMatch, ImageBlur, UNETLoader, VAELoader, Flux2KleinModelConfig_EditUtils, GetNode, SetNode, GetNode, easy ifElse, 图像缩放V2_孤海, SetNode, ColorCorrect, SetNode, 布尔孤海, PreviewImage, TTP_Image_Tile_Batch, TTP_Tile_image_size, SetNode, SetNode, SetNode, SetNode, PreviewImage, LoadImage, SetNode, SaveImage, GetNode, GetNode, Any Switch (rgthree), LoadImage, GetNode, 孤海-图像添加水印, PreviewImage, LoraLoaderModelOnly, KSampler, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, ColorConverterGuhai, easy showAnything, 孤海-自定义颜色, ColorConverterGuhai, GetNode, Image Comparer (rgthree), 布尔孤海, EditTextEncode_EditUtils, LoraLoaderModelOnly, Image Comparer (rgthree), GoohaiUniversalSlider, LoadImage, easy seed, IDPhotoClothingSelector_孤海, IDPhotoClothingSelector_孤海, PreviewImage, 孤海-取色器, TextInput_]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.86, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 1106919809378802, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein9B一键证件照侧脸转正换服装换背景高清排版_2065959891482800130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein9B一键证件照侧脸转正换服装换背景高清排版_2065959891482800130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `TextInput_`
- `GuHai_IDPhotoCrop`
- `ImageComposite+`
- `RMBG`
- `SetNode`
- `Text Concatenate`
- `TextInput_`
- `GetNode`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `SeedVR2LoadVAEModel`
- `ImageResize+`
- `GetImageSize+`
- `TextEncodeQwenImageEditPlus`
- `Flux2KleinConfigPreparer_EditUtils`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `ImageCASharpening+`
- `KSampler` ★核心
- `GetNode`
- `easy ifElse`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `easy imageColorMatch`
- `ImageBlur`
- `UNETLoader` ★核心
- `VAELoader`
- `Flux2KleinModelConfig_EditUtils`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy ifElse`
- `图像缩放V2_孤海`
- `SetNode`
- `ColorCorrect`
- `SetNode`
- `布尔孤海`
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `SaveImage`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `LoadImage`
- `GetNode`
- `孤海-图像添加水印`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `ColorConverterGuhai`
- `easy showAnything`
- `孤海-自定义颜色`
- `ColorConverterGuhai`
- `GetNode`
- `Image Comparer (rgthree)`
- `布尔孤海`
- `EditTextEncode_EditUtils`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `GoohaiUniversalSlider`
- `LoadImage`
- `easy seed`
- `IDPhotoClothingSelector_孤海`
- `IDPhotoClothingSelector_孤海`
- `PreviewImage`
- `孤海-取色器`
- `TextInput_`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1106919809378802`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `0.86`

## 知识

覆盖率 **62%**（63/102）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`CLIPLoader`、`VAEDecode`、`TextInput_`、`GuHai_IDPhotoCrop`、`ImageComposite+`、`RMBG`、`Text Concatenate`、`ImageScaleBy`、`TTP_Image_Assy`、`SeedVR2LoadVAEModel`、`ImageResize+`、`GetImageSize+`、`TextEncodeQwenImageEditPlus`、`Flux2KleinConfigPreparer_EditUtils`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ImageCASharpening+`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`easy imageColorMatch`、`ImageBlur`、`Flux2KleinModelConfig_EditUtils`、`图像缩放V2_孤海`、`ColorCorrect`、`布尔孤海`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`LoadImage`、`SaveImage`、`孤海-图像添加水印`、`忽略多组孤海`、`ColorConverterGuhai`、`孤海-自定义颜色`、`EditTextEncode_EditUtils`、`GoohaiUniversalSlider`、`easy seed`、`IDPhotoClothingSelector_孤海`、`孤海-取色器`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
