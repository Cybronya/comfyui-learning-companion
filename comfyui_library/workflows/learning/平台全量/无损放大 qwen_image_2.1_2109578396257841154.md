---
key: 平台全量/无损放大 qwen_image_2.1_2109578396257841154.json
name: 无损放大 qwen_image_2.1_2109578396257841154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/无损放大 qwen_image_2.1_2109578396257841154.json
hash: 4a5831e8b87ae15b
coverage: 0.693878
learned_at: 2026-11-14 02:12:52
nodes: [Int, Int, SetNode, easy showAnything, ComfyMathExpression, ComfyMathExpression, easy showAnything, GetImageSize, SetNode, Image Comparer (rgthree), easy imageColorMatch, SaveImage, SetNode, UpscaleModelLoader, ImageUpscaleWithModel, GetNode, Image Remove Alpha JK, PreviewImage, Bounded Image Crop, Inset Image Bounds, Image Bounds, UNETLoader, QwenImage21Cache, CLIPLoader, KSamplerSelect, ManualSigmas, ImagePadForOutpaint, VAEDecode, SamplerCustom, VAELoader, easy imageBatchToImageList, TTP_Image_Tile_Batch, TTP_Tile_image_size, GetNode, TTP_Image_Assy, GetNode, Reroute, easy imageColorMatch, easy imageListToImageBatch, ImageScaleToMaxDimension, Reroute, PreviewImage, PreviewImage, 忽略多组孤海, LoraLoaderModelOnly, TextEncodeQwenImage21, easy int, PreviewImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/无损放大 qwen_image_2.1_2109578396257841154.json

> 来源文件 `comfyui_library/workflows/平台全量/无损放大 qwen_image_2.1_2109578396257841154.json`

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
- `PreviewImage`
- `Bounded Image Crop`
- `Inset Image Bounds`
- `Image Bounds`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ImagePadForOutpaint`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `VAELoader`
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
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `easy int`
- `PreviewImage`
- `LoadImage`

## 知识

覆盖率 **69%**（34/49）

**有卡**：`Int`、`ComfyMathExpression`、`GetImageSize`、`easy imageColorMatch`、`SaveImage`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`Image Remove Alpha JK`、`Bounded Image Crop`、`Inset Image Bounds`、`Image Bounds`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`ImagePadForOutpaint`、`VAEDecode`、`SamplerCustom`、`VAELoader`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`easy imageListToImageBatch`、`ImageScaleToMaxDimension`、`忽略多组孤海`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`easy int`、`LoadImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
