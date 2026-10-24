---
key: 图片生成/图生图/图生图重绘细节增强(WAN2.1)_1992501081584324609.json
name: 图生图重绘细节增强(WAN2.1)_1992501081584324609
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图重绘细节增强(WAN2.1)_1992501081584324609.json
hash: 75f241f4b3287737
coverage: 0.86
learned_at: 2026-10-23 12:44:00
nodes: [UNETLoader, CLIPLoader, MarkdownNote, Note, Text Concatenate, easy showAnything, Text Multiline, RH_Captioner, Note, LoraLoader, LoraLoader, VAEDecode, ImageSharpen, MarkdownNote, VAEEncode, BetterFilmGrain, Text Multiline, CLIPTextEncode, VAELoader, PathchSageAttentionKJ, CLIPTextEncode, EsesImageEffectBloom, VAEDecodeTiled, KSampler, VAEEncode, ImpactImageBatchToImageList, ImageListToImageBatch, TTP_Tile_image_size, TTP_Image_Tile_Batch, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, CLIPTextEncode, CLIPTextEncode, VAELoader, DualCLIPLoader, PreviewImage, CR Simple Image Compare, SaveImage, LayerFilter: FilmV2, ImageScaleDownToSize, PreviewImage, UNETLoader, SaveImage, SaveImage, ImageScaleDownToSize, TTP_Image_Assy, KSampler, LoraLoader, LoadImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 181505961835757, "steps": 10, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 图片生成/图生图/图生图重绘细节增强(WAN2.1)_1992501081584324609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图重绘细节增强(WAN2.1)_1992501081584324609.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `Note`
- `Text Concatenate`
- `easy showAnything`
- `Text Multiline`
- `RH_Captioner`
- `Note`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `ImageSharpen`
- `MarkdownNote`
- `VAEEncode` ★核心
- `BetterFilmGrain`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `EsesImageEffectBloom`
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
- `SaveImage`
- `LayerFilter: FilmV2`
- `ImageScaleDownToSize`
- `PreviewImage`
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `ImageScaleDownToSize`
- `TTP_Image_Assy`
- `KSampler` ★核心
- `LoraLoader` ★核心
- `LoadImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `181505961835757`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **86%**（43/50）

**有卡**：`UNETLoader`、`CLIPLoader`、`Text Concatenate`、`Text Multiline`、`RH_Captioner`、`LoraLoader`、`VAEDecode`、`ImageSharpen`、`VAEEncode`、`BetterFilmGrain`、`CLIPTextEncode`、`VAELoader`、`PathchSageAttentionKJ`、`EsesImageEffectBloom`、`VAEDecodeTiled`、`KSampler`、`ImpactImageBatchToImageList`、`ImageListToImageBatch`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`DualCLIPLoader`、`CR Simple Image Compare`、`SaveImage`、`LayerFilter: FilmV2`、`ImageScaleDownToSize`、`TTP_Image_Assy`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled
