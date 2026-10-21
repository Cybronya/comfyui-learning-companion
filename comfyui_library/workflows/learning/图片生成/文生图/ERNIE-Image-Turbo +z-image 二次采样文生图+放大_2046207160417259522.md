---
key: 图片生成/文生图/ERNIE-Image-Turbo +z-image 二次采样文生图+放大_2046207160417259522.json
name: ERNIE-Image-Turbo +z-image 二次采样文生图+放大_2046207160417259522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ERNIE-Image-Turbo +z-image 二次采样文生图+放大_2046207160417259522.json
hash: bc0cc57dd985712e
coverage: 0.848485
learned_at: 2026-10-21 02:51:32
nodes: [TTP_Tile_image_size, TTP_Image_Tile_Batch, VAEDecodeTiled, ImageListToImageBatch, CLIPLoader, ImageScaleToTotalPixels, Note, VAEEncode, VAELoader, CLIPLoader, ConditioningZeroOut, ImageUpscaleWithModel, VAEDecode, UpscaleModelLoader, Note, SaveImage, ImpactImageBatchToImageList, TTP_Image_Assy, easy cleanGpuUsed, CLIPTextEncode, EmptyFlux2LatentImage, VAELoader, CLIPTextEncode, ConditioningZeroOut, KSampler, SaveImageJPG_GH, Image Comparer (rgthree), Note, Note, UNETLoader, LoraLoaderModelOnly, KSampler, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 271352022993627, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/ERNIE-Image-Turbo +z-image 二次采样文生图+放大_2046207160417259522.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ERNIE-Image-Turbo +z-image 二次采样文生图+放大_2046207160417259522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `Note`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `Note`
- `SaveImage`
- `ImpactImageBatchToImageList`
- `TTP_Image_Assy`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SaveImageJPG_GH`
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `271352022993627`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAEDecodeTiled`、`ImageListToImageBatch`、`CLIPLoader`、`ImageScaleToTotalPixels`、`VAEEncode`、`VAELoader`、`ConditioningZeroOut`、`ImageUpscaleWithModel`、`VAEDecode`、`UpscaleModelLoader`、`SaveImage`、`ImpactImageBatchToImageList`、`TTP_Image_Assy`、`easy cleanGpuUsed`、`CLIPTextEncode`、`EmptyFlux2LatentImage`、`KSampler`、`SaveImageJPG_GH`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
