---
key: ❼「写真V2」Z双采+TTP-HD「9.20」_2039328218167123970.json
name: ❼「写真V2」Z双采+TTP-HD「9.20」_2039328218167123970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/❼「写真V2」Z双采+TTP-HD「9.20」_2039328218167123970.json
hash: 3c333ddf3fe3a5a8
coverage: 0.362069
learned_at: 2026-10-10 20:59:29
nodes: [SetNode, SetNode, GetNode, SetNode, EmptySD3LatentImage, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, StringConcatenate, GetNode, GetNode, GetNode, TTP_Image_Tile_Batch, GetNode, SetNode, easy imageSize, SetNode, GetNode, Any Switch (rgthree), GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, VAEDecode, SetNode, GetNode, GetNode, VAEDecode, SetNode, GetNode, easy cleanGpuUsed, SetNode, GetNode, SetNode, ModelPassThrough, PrimitiveString, Any Switch (rgthree), PlaySound|pysssss, KOOK_ImageCompression, GetNode, PrimitiveString, Any Switch (rgthree), GetNode, SetNode, KOOK_SaveJPGImage, CameraWatermarkNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy cleanGpuUsed, StringConcatenate, SetNode, GetNode, SomethingToString, GetNode, SetNode, ModelPassThrough, PreviewImage, TextInput_, TextInput_, easy int, easy imageSizeBySide, TextInput_, llama_cpp_instruct_adv, llama_cpp_instruct_adv, SetNode, MarkdownNote, easy int, easy int, TTP_Tile_image_size, MarkdownNote, TTP_Image_Assy, TextInput_, SeedVR2LoadVAEModel, MarkdownNote, Any Switch (rgthree), GetNode, PlaySound|pysssss, KOOK_ImageCompression, KOOK_ImageCompression, GetNode, ImageCASharpening+, GetNode, Any Switch (rgthree), SetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, SeedVR2VideoUpscaler, ConditioningZeroOut, SetNode, UNETLoader, GetNode, SetNode, GetNode, Image Comparer (rgthree), GetNode, KOOK_SaveJPGImage, GetNode, GetNode, PlaySound|pysssss, llama_cpp_parameters, llama_cpp_parameters, SaveImage, easy showAnything, TextInput_, TextInput_, TextInput_, CheckpointLoaderSimple, CLIPLoader, SetNode, VAELoader, Fast Groups Bypasser (rgthree), GetNode, CR Simple Text Watermark, CR Simple Text Watermark, CR Simple Text Watermark, CR Simple Text Watermark, TextInput_, MarkdownNote, MarkdownNote, TextInput_, TextInput_, UNETLoader, Fast Groups Bypasser (rgthree), GetNode, CLIPTextEncode, SetNode, LoraLoaderModelOnly, LazyCache, ModelSamplingAuraFlow, easy showAnything, CLIPTextEncode, MarkdownNote, KSamplerAdvanced, MarkdownNote, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, ImageScale, TextInput_, TextInput_, ModelSamplingAuraFlow, KSamplerAdvanced, TextInput_, LoraLoaderModelOnly, LazyCache, LoraLoaderModelOnly, KOOK_SaveJPGImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), GetNode, Any Switch (rgthree), LoadImage, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, llama_cpp_model_loader, easy int, ImageSharpen, ColorMatch, SeedVR2LoadDiTModel]
patterns: []
missing: [CR Simple Text Watermark, CR Simple Text Watermark, CR Simple Text Watermark, CR Simple Text Watermark, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, easy int, easy int, easy int, easy int, easy imageSize, easy imageSizeBySide]
parameters: {"cfg": 12, "checkpoint": "Z-Image-Base-8steps-White_Marble-AIO_v1.safetensors", "denoise": "simple", "sampler_name": 1, "scheduler": "dpmpp_sde", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识, 次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识, 次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识, 次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# ❼「写真V2」Z双采+TTP-HD「9.20」_2039328218167123970.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/❼「写真V2」Z双采+TTP-HD「9.20」_2039328218167123970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（174 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `EmptySD3LatentImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `TTP_Image_Tile_Batch`
- `GetNode`
- `SetNode`
- `easy imageSize`
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `SetNode`
- `ModelPassThrough`
- `PrimitiveString`
- `Any Switch (rgthree)`
- `PlaySound|pysssss`
- `KOOK_ImageCompression`
- `GetNode`
- `PrimitiveString`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `KOOK_SaveJPGImage`
- `CameraWatermarkNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `StringConcatenate`
- `SetNode`
- `GetNode`
- `SomethingToString`
- `GetNode`
- `SetNode`
- `ModelPassThrough`
- `PreviewImage`
- `TextInput_`
- `TextInput_`
- `easy int`
- `easy imageSizeBySide`
- `TextInput_`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `SetNode`
- `MarkdownNote`
- `easy int`
- `easy int`
- `TTP_Tile_image_size`
- `MarkdownNote`
- `TTP_Image_Assy`
- `TextInput_`
- `SeedVR2LoadVAEModel`
- `MarkdownNote`
- `Any Switch (rgthree)`
- `GetNode`
- `PlaySound|pysssss`
- `KOOK_ImageCompression`
- `KOOK_ImageCompression`
- `GetNode`
- `ImageCASharpening+`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `SeedVR2VideoUpscaler`
- `ConditioningZeroOut`
- `SetNode`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `KOOK_SaveJPGImage`
- `GetNode`
- `GetNode`
- `PlaySound|pysssss`
- `llama_cpp_parameters`
- `llama_cpp_parameters`
- `SaveImage`
- `easy showAnything`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `CR Simple Text Watermark`
- `CR Simple Text Watermark`
- `CR Simple Text Watermark`
- `CR Simple Text Watermark`
- `TextInput_`
- `MarkdownNote`
- `MarkdownNote`
- `TextInput_`
- `TextInput_`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LazyCache`
- `ModelSamplingAuraFlow`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScale`
- `TextInput_`
- `TextInput_`
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `TextInput_`
- `LoraLoaderModelOnly` ★核心
- `LazyCache`
- `LoraLoaderModelOnly` ★核心
- `KOOK_SaveJPGImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `LoadImage`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `llama_cpp_model_loader`
- `easy int`
- `ImageSharpen`
- `ColorMatch`
- `SeedVR2LoadDiTModel`

## 关键参数

- `checkpoint` = `Z-Image-Base-8steps-White_Marble-AIO_v1.safetensors`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_sde`
- `denoise` = `simple`

## 知识

覆盖率 **36%**（63/174）

**有卡**：`EmptySD3LatentImage`、`StringConcatenate`、`TTP_Image_Tile_Batch`、`VAEDecode`、`ModelPassThrough`、`KOOK_ImageCompression`、`KOOK_SaveJPGImage`、`CameraWatermarkNode`、`SomethingToString`、`TextInput_`、`llama_cpp_instruct_adv`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ConditioningZeroOut`、`UNETLoader`、`llama_cpp_parameters`、`SaveImage`、`CheckpointLoaderSimple`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LazyCache`、`ModelSamplingAuraFlow`、`KSamplerAdvanced`、`ImageScale`、`LoadImage`、`llama_cpp_model_loader`、`ImageSharpen`、`ColorMatch`、`SeedVR2LoadDiTModel`

**缺卡**（19）：`CR Simple Text Watermark`、`CR Simple Text Watermark`、`CR Simple Text Watermark`、`CR Simple Text Watermark`、`ImageCASharpening+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`PlaySound|pysssss`、`PlaySound|pysssss`、`PlaySound|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy int`、`easy int`、`easy int`、`easy int`、`easy imageSize`、`easy imageSizeBySide`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 学习发现

- 次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Simple Text Watermark` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明
