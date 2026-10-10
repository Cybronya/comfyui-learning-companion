---
key: wan2.2 文生图+放大合集_1975596827603021826.json
name: wan2.2 文生图+放大合集_1975596827603021826
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2 文生图+放大合集_1975596827603021826.json
hash: 6e563860f3c6a5b7
coverage: 0.8
learned_at: 2026-10-10 20:59:27
nodes: [ModelSamplingSD3, VAELoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, VAEDecode, KSamplerAdvanced, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, LoaderGGUF, CLIPLoader, SeedVR2BlockSwap, Image Comparer (rgthree), VAEDecode, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, SaveImage, SaveImage, easy imageBatchToImageList, ImageUpscaleWithModel, easy cleanGpuUsed, ImageScaleToTotalPixels, easy cleanGpuUsed, ImageListToImageBatch, VAELoader, LayerUtility: PurgeVRAM, VAEEncode, ModelSamplingSD3, KSampler, VAEDecode, SaveImage, LoadImage, TTP_Image_Assy, TTP_Tile_image_size, TTP_Image_Tile_Batch, UpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, Image Comparer (rgthree), easy cleanGpuUsed, UnetLoaderGGUF, LoraLoaderModelOnly, CLIPLoader, VAELoader, Fast Groups Muter (rgthree), easy cleanGpuUsed, SeedVR2GGUF, LoraLoaderModelOnly, Text, UnetLoaderGGUF, easy cleanGpuUsed, Note]
patterns: [image_to_image]
missing: [LayerUtility: PurgeVRAM, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy imageBatchToImageList]
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 359343628422723, "steps": 10}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识]
---

# wan2.2 文生图+放大合集_1975596827603021826.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2 文生图+放大合集_1975596827603021826.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `LoaderGGUF`
- `CLIPLoader`
- `SeedVR2BlockSwap`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `SaveImage`
- `SaveImage`
- `easy imageBatchToImageList`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `ImageListToImageBatch`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Muter (rgthree)`
- `easy cleanGpuUsed`
- `SeedVR2GGUF`
- `LoraLoaderModelOnly` ★核心
- `Text`
- `UnetLoaderGGUF` ★核心
- `easy cleanGpuUsed`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `359343628422723`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`ModelSamplingSD3`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`LoaderGGUF`、`SeedVR2BlockSwap`、`SaveImage`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`ImageListToImageBatch`、`VAEEncode`、`KSampler`、`LoadImage`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`UpscaleModelLoader`、`UnetLoaderGGUF`、`SeedVR2GGUF`、`Text`

**缺卡**（7）：`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageBatchToImageList`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
