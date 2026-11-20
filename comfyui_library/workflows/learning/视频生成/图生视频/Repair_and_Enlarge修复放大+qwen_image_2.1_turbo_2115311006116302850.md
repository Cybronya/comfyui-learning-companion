---
key: 视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115311006116302850.json
name: Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115311006116302850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115311006116302850.json
hash: 93c0833818739bb2
coverage: 0.717391
learned_at: 2026-10-30 17:58:37
nodes: [Int, GetNode, Int, SetNode, easy showAnything, ComfyMathExpression, ComfyMathExpression, easy showAnything, GetImageSize, ImageScaleToMaxDimension, GetNode, TTP_Image_Tile_Batch, SetNode, ImagePadForOutpaint, UNETLoader, SamplerCustom, easy imageBatchToImageList, easy imageListToImageBatch, TTP_Image_Assy, TextEncodeQwenImage21, PreviewImage, TTP_Tile_image_size, PreviewImage, PreviewImage, easy int, VAEDecode, easy imageInsetCrop, easy imageColorMatch, Image Remove Alpha JK, SetNode, GetNode, QwenImage21Cache, CLIPLoader, KSamplerSelect, ManualSigmas, VAELoader, Mute / Bypass Repeater (rgthree), UpscaleModelLoader, ImageUpscaleWithModel, Fast Bypasser (rgthree), LoraLoaderModelOnly, PreviewImage, SaveImage, easy imageColorMatch, LoadImage, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115311006116302850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115311006116302850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `Int`
- `GetNode`
- `Int`
- `SetNode`
- `easy showAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy showAnything`
- `GetImageSize`
- `ImageScaleToMaxDimension`
- `GetNode`
- `TTP_Image_Tile_Batch`
- `SetNode`
- `ImagePadForOutpaint`
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `TTP_Tile_image_size`
- `PreviewImage`
- `PreviewImage`
- `easy int`
- `VAEDecode` ★核心
- `easy imageInsetCrop`
- `easy imageColorMatch`
- `Image Remove Alpha JK`
- `SetNode`
- `GetNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAELoader`
- `Mute / Bypass Repeater (rgthree)`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Fast Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `SaveImage`
- `easy imageColorMatch`
- `LoadImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **72%**（33/46）

**有卡**：`Int`、`ComfyMathExpression`、`GetImageSize`、`ImageScaleToMaxDimension`、`TTP_Image_Tile_Batch`、`ImagePadForOutpaint`、`UNETLoader`、`SamplerCustom`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TextEncodeQwenImage21`、`TTP_Tile_image_size`、`easy int`、`VAEDecode`、`easy imageInsetCrop`、`easy imageColorMatch`、`Image Remove Alpha JK`、`QwenImage21Cache`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`Mute / Bypass Repeater (rgthree)`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`Fast Bypasser (rgthree)`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
