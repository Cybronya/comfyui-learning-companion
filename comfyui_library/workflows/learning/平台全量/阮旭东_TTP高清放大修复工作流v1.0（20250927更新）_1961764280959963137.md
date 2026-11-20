---
key: 平台全量/阮旭东_TTP高清放大修复工作流v1.0（20250927更新）_1961764280959963137.json
name: 阮旭东_TTP高清放大修复工作流v1.0（20250927更新）_1961764280959963137
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/阮旭东_TTP高清放大修复工作流v1.0（20250927更新）_1961764280959963137.json
hash: 39cff4e85dafe0d2
coverage: 0.92
learned_at: 2026-11-14 02:49:37
nodes: [Image Comparer (rgthree), CLIPTextEncode, FluxGuidance, ConditioningZeroOut, VAEEncode, LoraLoaderModelOnly, KSampler, TTP_Image_Tile_Batch, easy imageBatchToImageList, ImageScaleToTotalPixels, TTP_Tile_image_size, ImageUpscaleWithModel, ImageResizeKJ, VAELoader, TTP_Image_Assy, ImageListToBatch+, VAEDecodeTiled, LoadImage, UpscaleModelLoader, DualCLIPLoader, UNETLoader, SaveImage, LoadImage, LoadImage, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.3, "sampler_name": "euler", "scheduler": "simple", "seed": 316430325547060, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/阮旭东_TTP高清放大修复工作流v1.0（20250927更新）_1961764280959963137.json

> 来源文件 `comfyui_library/workflows/平台全量/阮旭东_TTP高清放大修复工作流v1.0（20250927更新）_1961764280959963137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `ImageUpscaleWithModel`
- `ImageResizeKJ`
- `VAELoader`
- `TTP_Image_Assy`
- `ImageListToBatch+`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `UpscaleModelLoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `316430325547060`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`VAEEncode`、`LoraLoaderModelOnly`、`KSampler`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`ImageUpscaleWithModel`、`ImageResizeKJ`、`VAELoader`、`TTP_Image_Assy`、`ImageListToBatch+`、`VAEDecodeTiled`、`LoadImage`、`UpscaleModelLoader`、`DualCLIPLoader`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
