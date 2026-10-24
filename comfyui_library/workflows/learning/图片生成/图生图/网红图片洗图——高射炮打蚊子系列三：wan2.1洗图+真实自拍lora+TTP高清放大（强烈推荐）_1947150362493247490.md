---
key: 图片生成/图生图/网红图片洗图——高射炮打蚊子系列三：wan2.1洗图+真实自拍lora+TTP高清放大（强烈推荐）_1947150362493247490.json
name: 网红图片洗图——高射炮打蚊子系列三：wan2.1洗图+真实自拍lora+TTP高清放大（强烈推荐）_1947150362493247490
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/网红图片洗图——高射炮打蚊子系列三：wan2.1洗图+真实自拍lora+TTP高清放大（强烈推荐）_1947150362493247490.json
hash: 72fedb71c10e1e2c
coverage: 0.86
learned_at: 2026-10-23 13:21:54
nodes: [MarkdownNote, Note, easy showAnything, Text Multiline, LoraLoader, LoraLoader, VAEDecode, ImageSharpen, LoraLoader, BetterFilmGrain, CLIPTextEncode, PathchSageAttentionKJ, CLIPTextEncode, EsesImageEffectBloom, KSampler, VAEDecodeTiled, KSampler, VAEEncode, ImpactImageBatchToImageList, ImageListToImageBatch, TTP_Tile_image_size, TTP_Image_Tile_Batch, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, CLIPTextEncode, CLIPTextEncode, VAELoader, DualCLIPLoader, PreviewImage, CR Simple Image Compare, LayerFilter: FilmV2, PreviewImage, UNETLoader, SaveImage, ImageScaleDownToSize, TTP_Image_Assy, RH_Captioner, ImageScaleDownToSize, Note, Text Multiline, Text Concatenate, VAEEncode, MarkdownNote, LoadImage, SaveImage, UNETLoader, CLIPLoader, VAELoader, SaveImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.9, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "exponential", "seed": 977711050108397, "steps": 20, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 图片生成/图生图/网红图片洗图——高射炮打蚊子系列三：wan2.1洗图+真实自拍lora+TTP高清放大（强烈推荐）_1947150362493247490.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/网红图片洗图——高射炮打蚊子系列三：wan2.1洗图+真实自拍lora+TTP高清放大（强烈推荐）_1947150362493247490.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `MarkdownNote`
- `Note`
- `easy showAnything`
- `Text Multiline`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `ImageSharpen`
- `LoraLoader` ★核心
- `BetterFilmGrain`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `EsesImageEffectBloom`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ImpactImageBatchToImageList`
- `ImageListToImageBatch`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `PreviewImage`
- `CR Simple Image Compare`
- `LayerFilter: FilmV2`
- `PreviewImage`
- `UNETLoader` ★核心
- `SaveImage`
- `ImageScaleDownToSize`
- `TTP_Image_Assy`
- `RH_Captioner`
- `ImageScaleDownToSize`
- `Note`
- `Text Multiline`
- `Text Concatenate`
- `VAEEncode` ★核心
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `977711050108397`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `exponential`
- `denoise` = `0.9`

## 知识

覆盖率 **86%**（43/50）

**有卡**：`Text Multiline`、`LoraLoader`、`VAEDecode`、`ImageSharpen`、`BetterFilmGrain`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`EsesImageEffectBloom`、`KSampler`、`VAEDecodeTiled`、`VAEEncode`、`ImpactImageBatchToImageList`、`ImageListToImageBatch`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAELoader`、`DualCLIPLoader`、`CR Simple Image Compare`、`LayerFilter: FilmV2`、`UNETLoader`、`SaveImage`、`ImageScaleDownToSize`、`TTP_Image_Assy`、`RH_Captioner`、`Text Concatenate`、`LoadImage`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled
