---
key: Qwen2.1全能工作流带官方PE加强模型和节点，文生图图生图处理方案_2106501286328889345.json
name: Qwen2.1全能工作流带官方PE加强模型和节点，文生图图生图处理方案_2106501286328889345
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1全能工作流带官方PE加强模型和节点，文生图图生图处理方案_2106501286328889345.json
hash: 5ffa9c959051d16c
coverage: 0.626168
learned_at: 2026-10-10 20:59:06
nodes: [Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, VAEDecode, KSamplerAdvanced, QwenImage21Cache, KOOK_SaveJPGImage, UltimateSDUpscale, PreviewImage, SimpleMath+, GetImageSize, SimpleMath+, FloatConstant, UpscaleModelLoader, PreviewImage, AIO_Preprocessor, LoadImage, EmptyLatentImage, Image Comparer (rgthree), PreviewImage, Seed (rgthree), CLIPLoader, PreviewAny, CLIPLoader, PrimitiveFloat, PrimitiveFloat, JsonExtractString, JsonExtractString, PrimitiveStringMultiline, PrimitiveStringMultiline, PreviewAny, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, Seed (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ComfySwitchNode, TextGenerate, PreviewAny, CLIPLoader, VAELoader, PrimitiveBoolean, LoadImage, ComfySwitchNode, ImageConcatMulti, ResolutionSelector, UNETLoader, Anything Everywhere3, SaveImage, easy positive, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Seed (rgthree), LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, QwenMultiangleCameraNode, TextEncodeQwenImage21, Image Comparer (rgthree), SeedVR2LoadVAEModel, SaveImage, GetImageSize+, ImageResize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, ImageResize+, TTP_Image_Assy, KOOK_SaveJPGImage, ImageScaleBy, SeedVR2LoadDiTModel, GetImageSize+, RunningHub Deepcleaner, SeedVR2VideoUpscaler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RunningHub Deepcleaner, SimpleMath+, SimpleMath+, easy positive, GetImageSize+, GetImageSize+, ImageResize+, ImageResize+, Seed (rgthree), Seed (rgthree), Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen2.1全能工作流带官方PE加强模型和节点，文生图图生图处理方案_2106501286328889345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1全能工作流带官方PE加强模型和节点，文生图图生图处理方案_2106501286328889345.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `QwenImage21Cache`
- `KOOK_SaveJPGImage`
- `UltimateSDUpscale`
- `PreviewImage`
- `SimpleMath+`
- `GetImageSize`
- `SimpleMath+`
- `FloatConstant`
- `UpscaleModelLoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Seed (rgthree)`
- `CLIPLoader`
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `JsonExtractString`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `Seed (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ComfySwitchNode`
- `TextGenerate`
- `PreviewAny`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveBoolean`
- `LoadImage`
- `ComfySwitchNode`
- `ImageConcatMulti`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `Anything Everywhere3`
- `SaveImage`
- `easy positive`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Seed (rgthree)`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `QwenMultiangleCameraNode`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `ImageResize+`
- `TTP_Image_Assy`
- `KOOK_SaveJPGImage`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `GetImageSize+`
- `RunningHub Deepcleaner`
- `SeedVR2VideoUpscaler`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（67/107）

**有卡**：`LoadImage`、`VAEDecode`、`KSamplerAdvanced`、`QwenImage21Cache`、`KOOK_SaveJPGImage`、`UltimateSDUpscale`、`GetImageSize`、`FloatConstant`、`UpscaleModelLoader`、`AIO_Preprocessor`、`EmptyLatentImage`、`CLIPLoader`、`JsonExtractString`、`TextGenerate`、`VAELoader`、`PrimitiveBoolean`、`ImageConcatMulti`、`ResolutionSelector`、`UNETLoader`、`SaveImage`、`QwenMultiangleCameraNode`、`TextEncodeQwenImage21`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（17）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`RunningHub Deepcleaner`、`SimpleMath+`、`SimpleMath+`、`easy positive`、`GetImageSize+`、`GetImageSize+`、`ImageResize+`、`ImageResize+`、`Seed (rgthree)`、`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
