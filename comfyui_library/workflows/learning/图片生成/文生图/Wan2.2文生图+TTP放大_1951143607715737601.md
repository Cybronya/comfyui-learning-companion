---
key: 图片生成/文生图/Wan2.2文生图+TTP放大_1951143607715737601.json
name: Wan2.2文生图+TTP放大_1951143607715737601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图+TTP放大_1951143607715737601.json
hash: d44de5fd276fe5f6
coverage: 0.772727
learned_at: 2026-10-07 22:59:01
nodes: [LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, VAELoader, easy imageBatchToImageList, PreviewImage, ModelSamplingSD3, VAELoader, VAEEncode, easy cleanGpuUsed, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, TTP_Tile_image_size, ImageListToImageBatch, easy cleanGpuUsed, Reroute, PreviewImage, PreviewImage, TTP_Image_Tile_Batch, TTP_Image_Assy, CLIPLoader, easy cleanGpuUsed, KSamplerAdvanced, KSamplerAdvanced, SaveAnimatedWEBP, SaveImage, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleToTotalPixels, easy cleanGpuUsed, KSampler, LoraLoaderModelOnly, UNETLoader, CLIPLoader, SaveImage, Image Comparer (rgthree), EmptyHunyuanLatentVideo, VAEDecode]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 527188287153237, "steps": 8}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2文生图+TTP放大_1951143607715737601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1951143607715737601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `easy imageBatchToImageList`
- `PreviewImage`
- `ModelSamplingSD3`
- `VAELoader`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `TTP_Tile_image_size`
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveAnimatedWEBP`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `527188287153237`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **77%**（34/44）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`ModelSamplingSD3`、`VAEEncode`、`VAEDecode`、`TTP_Tile_image_size`、`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`CLIPLoader`、`KSamplerAdvanced`、`SaveAnimatedWEBP`、`SaveImage`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`KSampler`、`EmptyHunyuanLatentVideo`

**缺卡**（5）：`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageBatchToImageList`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
