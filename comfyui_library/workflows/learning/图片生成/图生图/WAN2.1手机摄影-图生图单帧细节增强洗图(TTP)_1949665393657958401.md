---
key: 图片生成/图生图/WAN2.1手机摄影-图生图单帧细节增强洗图(TTP)_1949665393657958401.json
name: WAN2.1手机摄影-图生图单帧细节增强洗图(TTP)_1949665393657958401
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.1手机摄影-图生图单帧细节增强洗图(TTP)_1949665393657958401.json
hash: 39e59451d7362172
coverage: 0.862745
learned_at: 2026-10-23 11:27:26
nodes: [UNETLoader, CLIPLoader, MarkdownNote, Note, Text Concatenate, easy showAnything, RH_Captioner, Note, VAEDecode, ImageSharpen, MarkdownNote, VAEEncode, BetterFilmGrain, CLIPTextEncode, VAELoader, CLIPTextEncode, EsesImageEffectBloom, VAEDecodeTiled, KSampler, VAEEncode, ImpactImageBatchToImageList, ImageListToImageBatch, TTP_Tile_image_size, TTP_Image_Tile_Batch, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, CLIPTextEncode, CLIPTextEncode, VAELoader, DualCLIPLoader, PreviewImage, UNETLoader, Fast Groups Bypasser (rgthree), CR Simple Image Compare, SaveImage, TTP_Image_Assy, ImageScaleDownToSize, CR Simple Image Compare, SaveImage, SaveImage, LayerFilter: FilmV2, PathchSageAttentionKJ, LoadImage, KSampler, SaveImage, Text Multiline, Text Multiline, LoraLoader, LoraLoader, LoraLoader]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 747899283532290, "steps": 10, "strength_clip": 1.0000000000000002, "strength_model": 0.6000000000000001}
---

# 图片生成/图生图/WAN2.1手机摄影-图生图单帧细节增强洗图(TTP)_1949665393657958401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.1手机摄影-图生图单帧细节增强洗图(TTP)_1949665393657958401.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `Note`
- `Text Concatenate`
- `easy showAnything`
- `RH_Captioner`
- `Note`
- `VAEDecode` ★核心
- `ImageSharpen`
- `MarkdownNote`
- `VAEEncode` ★核心
- `BetterFilmGrain`
- `CLIPTextEncode` ★核心
- `VAELoader`
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
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CR Simple Image Compare`
- `SaveImage`
- `TTP_Image_Assy`
- `ImageScaleDownToSize`
- `CR Simple Image Compare`
- `SaveImage`
- `SaveImage`
- `LayerFilter: FilmV2`
- `PathchSageAttentionKJ`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `Text Multiline`
- `Text Multiline`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `747899283532290`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `0.6000000000000001`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **86%**（44/51）

**有卡**：`UNETLoader`、`CLIPLoader`、`Text Concatenate`、`RH_Captioner`、`VAEDecode`、`ImageSharpen`、`VAEEncode`、`BetterFilmGrain`、`CLIPTextEncode`、`VAELoader`、`EsesImageEffectBloom`、`VAEDecodeTiled`、`KSampler`、`ImpactImageBatchToImageList`、`ImageListToImageBatch`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`DualCLIPLoader`、`CR Simple Image Compare`、`SaveImage`、`TTP_Image_Assy`、`ImageScaleDownToSize`、`LayerFilter: FilmV2`、`PathchSageAttentionKJ`、`LoadImage`、`Text Multiline`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled
