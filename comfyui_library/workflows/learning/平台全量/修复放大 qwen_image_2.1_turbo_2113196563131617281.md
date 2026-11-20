---
key: 平台全量/修复放大 qwen_image_2.1_turbo_2113196563131617281.json
name: 修复放大 qwen_image_2.1_turbo_2113196563131617281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/修复放大 qwen_image_2.1_turbo_2113196563131617281.json
hash: e41606b0ce0ccefd
coverage: 0.693878
learned_at: 2026-11-14 01:39:09
nodes: [Int, Int, SetNode, easy showAnything, ComfyMathExpression, ComfyMathExpression, easy showAnything, GetImageSize, SetNode, Image Comparer (rgthree), easy imageColorMatch, SaveImage, SetNode, UpscaleModelLoader, ImageUpscaleWithModel, GetNode, Image Remove Alpha JK, easy int, PreviewImage, Bounded Image Crop, Inset Image Bounds, Image Bounds, UNETLoader, TextEncodeQwenImage21, QwenImage21Cache, CLIPLoader, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, ImagePadForOutpaint, VAEDecode, SamplerCustom, VAELoader, PreviewImage, easy imageBatchToImageList, TTP_Image_Tile_Batch, TTP_Tile_image_size, GetNode, TTP_Image_Assy, GetNode, Reroute, easy imageColorMatch, easy imageListToImageBatch, ImageScaleToMaxDimension, Reroute, PreviewImage, PreviewImage, 忽略多组孤海, LoadImage]
patterns: []
missing: []
---

# 平台全量/修复放大 qwen_image_2.1_turbo_2113196563131617281.json

> 来源文件 `comfyui_library/workflows/平台全量/修复放大 qwen_image_2.1_turbo_2113196563131617281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `Int`
- `Int`
- `SetNode`
- `easy showAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy showAnything`
- `GetImageSize`
- `SetNode`
- `Image Comparer (rgthree)`
- `easy imageColorMatch`
- `SaveImage`
- `SetNode`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `GetNode`
- `Image Remove Alpha JK`
- `easy int`
- `PreviewImage`
- `Bounded Image Crop`
- `Inset Image Bounds`
- `Image Bounds`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `ImagePadForOutpaint`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `VAELoader`
- `PreviewImage`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `GetNode`
- `TTP_Image_Assy`
- `GetNode`
- `Reroute`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `ImageScaleToMaxDimension`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `忽略多组孤海`
- `LoadImage`

## 知识

覆盖率 **69%**（34/49）

**有卡**：`Int`、`ComfyMathExpression`、`GetImageSize`、`easy imageColorMatch`、`SaveImage`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`Image Remove Alpha JK`、`easy int`、`Bounded Image Crop`、`Inset Image Bounds`、`Image Bounds`、`UNETLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`ImagePadForOutpaint`、`VAEDecode`、`SamplerCustom`、`VAELoader`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`easy imageListToImageBatch`、`ImageScaleToMaxDimension`、`忽略多组孤海`、`LoadImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
