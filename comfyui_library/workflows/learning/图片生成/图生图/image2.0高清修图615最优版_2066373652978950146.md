---
key: 图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json
name: image2.0高清修图615最优版_2066373652978950146
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json
hash: a0fd2ef4f2eb1e3b
coverage: 0.878788
learned_at: 2026-10-23 11:37:45
nodes: [CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Image Comparer (rgthree), LoadImage, ImageResizeKJv2, ConditioningZeroOut, ReferenceLatent, CLIPTextEncode, VAEEncode, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, VAEEncode, KSampler, VAEDecodeTiled, easy imageListToImageBatch, SaveImage, TTP_Image_Assy, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageBatchToImageList, easy showAnything, easy showAnything, ImageScaleToTotalPixels, UNETLoader, Image Comparer (rgthree), VAEDecode, easy imageColorMatch]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "beta", "seed": 814522379408685, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `ImageResizeKJv2`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `easy imageListToImageBatch`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `easy showAnything`
- `easy showAnything`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `easy imageColorMatch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `814522379408685`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`ImageResizeKJv2`、`ConditioningZeroOut`、`ReferenceLatent`、`CLIPTextEncode`、`VAEEncode`、`KSamplerAdvanced`、`KSampler`、`VAEDecodeTiled`、`easy imageListToImageBatch`、`SaveImage`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`ImageScaleToTotalPixels`、`VAEDecode`、`easy imageColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
