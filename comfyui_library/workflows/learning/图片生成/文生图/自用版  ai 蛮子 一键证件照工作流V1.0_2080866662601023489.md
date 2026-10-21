---
key: 图片生成/文生图/自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489.json
name: 自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489.json
hash: 9babaee98cf6fe8a
coverage: 0.48855
learned_at: 2026-10-20 00:40:41
nodes: [GetNode, GetNode, SingleImageLayoutNode, Any Switch (rgthree), GetNode, SetNode, GetNode, ModelSamplingAuraFlow, SetNode, SetNode, SetNode, SetNode, PrimitiveStringMultiline, SetNode, SetNode, SetNode, SetNode, IDPhotoClothingSelector_孤海, IDPhotoClothingSelector_孤海, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, 孤海-取色器, GetNode, GetNode, GetNode, SetNode, SetNode, easy seed, SetNode, SetNode, 布尔孤海, SetNode, SetNode, GetNode, GetNode, Image Comparer (rgthree), 忽略多组孤海, 布尔孤海, 孤海注释, 孤海注释, 孤海注释, 忽略多组孤海, 孤海注释, GetNode, GetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, easy ifElse, Text Concatenate, GuHai_IDPhotoCrop, RMBG, ImageComposite+, ColorConverterGuhai, ColorConverterGuhai, easy showAnything, KSampler, ConditioningZeroOut, VAEEncode, VAEDecode, VRAM_Debug, 孤海-自定义颜色, GetNode, GetNode, SetNode, Any Switch (rgthree), ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, ImageResize+, TTP_Image_Assy, ImageCASharpening+, GetImageSize+, VRAM_Debug, SaveImage, GuHai_IDPhotoCrop, PreviewImage, GoohaiUniversalSlider, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, LoadImage, TextEncodeQwenImageEditPlus, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, ImageBlur, Flux2KleinModelConfig_EditUtils, Flux2KleinConfigPreparer_EditUtils, CLIPTextEncode, VAEDecode, 图像缩放V2_孤海, KSampler, ReferenceLatent, easy imageColorMatch, easy ifElse, ColorCorrect, EditTextEncode_EditUtils, SeedVR2VideoUpscaler, VRAM_Debug, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, GetNode, SaveImage, SeedVR2LoadVAEModel, Image Comparer (rgthree), SetNode, LoraLoaderModelOnly, CLIPLoader, SetNode, VAELoader, PreviewImage, 孤海注释]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.8, "sampler_name": "euler", "scheduler": "simple", "seed": 1106919809378802, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
- `GetNode`
- `GetNode`
- `SingleImageLayoutNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `IDPhotoClothingSelector_孤海`
- `IDPhotoClothingSelector_孤海`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `孤海-取色器`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy seed`
- `SetNode`
- `SetNode`
- `布尔孤海`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `忽略多组孤海`
- `布尔孤海`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `忽略多组孤海`
- `孤海注释`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy ifElse`
- `Text Concatenate`
- `GuHai_IDPhotoCrop`
- `RMBG`
- `ImageComposite+`
- `ColorConverterGuhai`
- `ColorConverterGuhai`
- `easy showAnything`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `VRAM_Debug`
- `孤海-自定义颜色`
- `GetNode`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `GetImageSize+`
- `VRAM_Debug`
- `SaveImage`
- `GuHai_IDPhotoCrop`
- `PreviewImage`
- `GoohaiUniversalSlider`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageBlur`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `图像缩放V2_孤海`
- `KSampler` ★核心
- `ReferenceLatent`
- `easy imageColorMatch`
- `easy ifElse`
- `ColorCorrect`
- `EditTextEncode_EditUtils`
- `SeedVR2VideoUpscaler`
- `VRAM_Debug`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `GetNode`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `PreviewImage`
- `孤海注释`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1106919809378802`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8`

## 知识

覆盖率 **49%**（64/131）

**有卡**：`SingleImageLayoutNode`、`ModelSamplingAuraFlow`、`IDPhotoClothingSelector_孤海`、`孤海-取色器`、`easy seed`、`布尔孤海`、`忽略多组孤海`、`Text Concatenate`、`GuHai_IDPhotoCrop`、`RMBG`、`ImageComposite+`、`ColorConverterGuhai`、`KSampler`、`ConditioningZeroOut`、`VAEEncode`、`VAEDecode`、`VRAM_Debug`、`孤海-自定义颜色`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ImageResize+`、`TTP_Image_Assy`、`ImageCASharpening+`、`GetImageSize+`、`SaveImage`、`GoohaiUniversalSlider`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`ImageBlur`、`Flux2KleinModelConfig_EditUtils`、`Flux2KleinConfigPreparer_EditUtils`、`CLIPTextEncode`、`图像缩放V2_孤海`、`ReferenceLatent`、`easy imageColorMatch`、`ColorCorrect`、`EditTextEncode_EditUtils`、`SeedVR2LoadVAEModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
