---
key: 图片生成/图生图/qwen 2.1 高清修复放大 +TTP 高清无损放大 TTP分块放大 4k超清放大_2110176284570644482.json
name: qwen 2.1 高清修复放大 +TTP 高清无损放大 TTP分块放大 4k超清放大_2110176284570644482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen 2.1 高清修复放大 +TTP 高清无损放大 TTP分块放大 4k超清放大_2110176284570644482.json
hash: 6f65ba1f0c1f9c2b
coverage: 0.60177
learned_at: 2026-10-23 11:41:45
nodes: [ImageUpscaleWithModel, UpscaleModelLoader, GetNode, easy sam3ImageSegmentation, easy sam3ImageSegmentation, KuwaharaBlur, GetNode, AddMask, easy sam3ImageSegmentation, easy sam3ImageSegmentation, easy sam3ImageSegmentation, easy sam3ImageSegmentation, AddMask, AddMask, JjkText, GrowMaskWithBlur, LayerMask: BiRefNetUltraV2, LayerMask: BiRefNetUltraV2, GrowMaskWithBlur, LayerMask: LoadBiRefNetModelV2, Image Overlay, ImageNoiseAugmentation, ImageNoiseAugmentation, ImageNoiseAugmentation, JjkText, JjkText, JjkText, Image Overlay, Text Concatenate (JPS), GetNode, GetNode, SetNode, GetNode, GetNode, easy imageColorMatch, SetNode, GetNode, TTP_Image_Assy, easy sam3ModelLoader, GetNode, SetNode, Int, SetNode, GetNode, 孤海注释, 孤海注释, SetNode, GetNode, GoohaiUniversalSlider, SetNode, 忽略多组孤海, JjkText, SetNode, GrowMaskWithBlur, GrowMaskWithBlur, GrowMaskWithBlur, Text Concatenate (JPS), CR Text Replace, CR String To Number, easy showAnything, Mask Switch (JPS), JjkText, Image Overlay, SetNode, CR Text Replace, Text Concatenate (JPS), CR String To Number, SomethingToString, CR Text Replace, JjkText, CR String To Number, easy showAnything, CLIPLoader, KSamplerSelect, ManualSigmas, UNETLoader, QwenImage21Cache, SamplerCustom, VAEDecode, easy imageListToImageBatch, Text Concatenate (JPS), JjkText, VAELoader, Int, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, GetImageSize, ImageScale, easy int, TTP_Tile_image_size, SetNode, SetNode, TextEncodeQwenImage21, LoraLoaderModelOnly, PreviewImage, easy imageColorMatch, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Image Comparer (rgthree), GetNode, SaveImage, LoadImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, PreviewImage, CR Image Input Switch (4 way), 孤海注释, Note, 孤海注释]
patterns: []
missing: []
---

# 图片生成/图生图/qwen 2.1 高清修复放大 +TTP 高清无损放大 TTP分块放大 4k超清放大_2110176284570644482.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen 2.1 高清修复放大 +TTP 高清无损放大 TTP分块放大 4k超清放大_2110176284570644482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `GetNode`
- `easy sam3ImageSegmentation`
- `easy sam3ImageSegmentation`
- `KuwaharaBlur`
- `GetNode`
- `AddMask`
- `easy sam3ImageSegmentation`
- `easy sam3ImageSegmentation`
- `easy sam3ImageSegmentation`
- `easy sam3ImageSegmentation`
- `AddMask`
- `AddMask`
- `JjkText`
- `GrowMaskWithBlur`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: BiRefNetUltraV2`
- `GrowMaskWithBlur`
- `LayerMask: LoadBiRefNetModelV2`
- `Image Overlay`
- `ImageNoiseAugmentation`
- `ImageNoiseAugmentation`
- `ImageNoiseAugmentation`
- `JjkText`
- `JjkText`
- `JjkText`
- `Image Overlay`
- `Text Concatenate (JPS)`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy imageColorMatch`
- `SetNode`
- `GetNode`
- `TTP_Image_Assy`
- `easy sam3ModelLoader`
- `GetNode`
- `SetNode`
- `Int`
- `SetNode`
- `GetNode`
- `孤海注释`
- `孤海注释`
- `SetNode`
- `GetNode`
- `GoohaiUniversalSlider`
- `SetNode`
- `忽略多组孤海`
- `JjkText`
- `SetNode`
- `GrowMaskWithBlur`
- `GrowMaskWithBlur`
- `GrowMaskWithBlur`
- `Text Concatenate (JPS)`
- `CR Text Replace`
- `CR String To Number`
- `easy showAnything`
- `Mask Switch (JPS)`
- `JjkText`
- `Image Overlay`
- `SetNode`
- `CR Text Replace`
- `Text Concatenate (JPS)`
- `CR String To Number`
- `SomethingToString`
- `CR Text Replace`
- `JjkText`
- `CR String To Number`
- `easy showAnything`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `Text Concatenate (JPS)`
- `JjkText`
- `VAELoader`
- `Int`
- `TTP_Image_Tile_Batch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageBatchToImageList`
- `GetImageSize`
- `ImageScale`
- `easy int`
- `TTP_Tile_image_size`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `easy imageColorMatch`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `SaveImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `PreviewImage`
- `CR Image Input Switch (4 way)`
- `孤海注释`
- `Note`
- `孤海注释`

## 知识

覆盖率 **60%**（68/113）

**有卡**：`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy sam3ImageSegmentation`、`KuwaharaBlur`、`AddMask`、`GrowMaskWithBlur`、`LayerMask: BiRefNetUltraV2`、`LayerMask: LoadBiRefNetModelV2`、`Image Overlay`、`ImageNoiseAugmentation`、`Text Concatenate (JPS)`、`easy imageColorMatch`、`TTP_Image_Assy`、`easy sam3ModelLoader`、`Int`、`GoohaiUniversalSlider`、`忽略多组孤海`、`CR Text Replace`、`CR String To Number`、`Mask Switch (JPS)`、`SomethingToString`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`UNETLoader`、`QwenImage21Cache`、`SamplerCustom`、`VAEDecode`、`easy imageListToImageBatch`、`VAELoader`、`TTP_Image_Tile_Batch`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageBatchToImageList`、`GetImageSize`、`ImageScale`、`easy int`、`TTP_Tile_image_size`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`CR Image Input Switch (4 way)`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
