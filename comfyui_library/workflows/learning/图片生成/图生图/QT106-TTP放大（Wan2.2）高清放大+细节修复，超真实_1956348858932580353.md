---
key: 图片生成/图生图/QT106-TTP放大（Wan2.2）高清放大+细节修复，超真实_1956348858932580353.json
name: QT106-TTP放大（Wan2.2）高清放大+细节修复，超真实_1956348858932580353
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QT106-TTP放大（Wan2.2）高清放大+细节修复，超真实_1956348858932580353.json
hash: 6fa83e7d7fa956cd
coverage: 0.92
learned_at: 2026-10-23 11:11:02
nodes: [ModelSamplingSD3, ImageListToImageBatch, CLIPLoader, easy bookmark, Note, TTP_Image_Tile_Batch, CLIPTextEncode, VAELoader, UpscaleModelLoader, VAEEncode, TTP_Image_Assy, ImageUpscaleWithModel, VAEDecode, TTP_Tile_image_size, ImageScaleToTotalPixels, UNETLoader, easy imageBatchToImageList, CLIPTextEncode, LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), PlaySound|pysssss, LoadImage, LoraLoaderModelOnly, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 729443726548803, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QT106-TTP放大（Wan2.2）高清放大+细节修复，超真实_1956348858932580353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QT106-TTP放大（Wan2.2）高清放大+细节修复，超真实_1956348858932580353.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `ImageListToImageBatch`
- `CLIPLoader`
- `easy bookmark`
- `Note`
- `TTP_Image_Tile_Batch`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UpscaleModelLoader`
- `VAEEncode` ★核心
- `TTP_Image_Assy`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `PlaySound|pysssss`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `729443726548803`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`ModelSamplingSD3`、`ImageListToImageBatch`、`CLIPLoader`、`easy bookmark`、`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`VAELoader`、`UpscaleModelLoader`、`VAEEncode`、`TTP_Image_Assy`、`ImageUpscaleWithModel`、`VAEDecode`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`UNETLoader`、`easy imageBatchToImageList`、`LoraLoaderModelOnly`、`KSampler`、`PlaySound|pysssss`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
