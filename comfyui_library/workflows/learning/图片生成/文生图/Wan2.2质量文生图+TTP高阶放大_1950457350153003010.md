---
key: 图片生成/文生图/Wan2.2质量文生图+TTP高阶放大_1950457350153003010.json
name: Wan2.2质量文生图+TTP高阶放大_1950457350153003010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2质量文生图+TTP高阶放大_1950457350153003010.json
hash: 8b4515e029b7ecb2
coverage: 0.772727
learned_at: 2026-10-07 22:58:25
nodes: [CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, easy imageBatchToImageList, PreviewImage, UNETLoader, CLIPLoader, VAELoader, VAEEncode, SaveImage, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, TTP_Tile_image_size, UpscaleModelLoader, ImageScaleToTotalPixels, easy cleanGpuUsed, ImageListToImageBatch, easy cleanGpuUsed, TTP_Image_Assy, Reroute, KSampler, ImageUpscaleWithModel, PreviewImage, PreviewImage, TTP_Image_Tile_Batch, ModelSamplingSD3, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, CLIPTextEncode, Image Comparer (rgthree), SaveImage, SaveAnimatedWEBP]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy imageBatchToImageList]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 187457617380377, "steps": 10}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2质量文生图+TTP高阶放大_1950457350153003010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1950457350153003010.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `easy imageBatchToImageList`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `TTP_Image_Assy`
- `Reroute`
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveAnimatedWEBP`

## 关键参数

- `seed` = `187457617380377`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **77%**（34/44）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`VAEEncode`、`SaveImage`、`VAEDecode`、`ModelSamplingSD3`、`TTP_Tile_image_size`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`ImageListToImageBatch`、`TTP_Image_Assy`、`KSampler`、`ImageUpscaleWithModel`、`TTP_Image_Tile_Batch`、`EmptyHunyuanLatentVideo`、`SaveAnimatedWEBP`

**缺卡**（5）：`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageBatchToImageList`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
