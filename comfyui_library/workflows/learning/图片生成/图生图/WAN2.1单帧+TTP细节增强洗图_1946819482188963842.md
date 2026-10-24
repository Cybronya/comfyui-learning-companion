---
key: 图片生成/图生图/WAN2.1单帧+TTP细节增强洗图_1946819482188963842.json
name: WAN2.1单帧+TTP细节增强洗图_1946819482188963842
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.1单帧+TTP细节增强洗图_1946819482188963842.json
hash: 48b584d356775717
coverage: 0.854167
learned_at: 2026-10-23 11:27:25
nodes: [LoraLoader, LoraLoader, VAEDecode, LoraLoader, EsesImageEffectBloom, KSampler, ImageListToImageBatch, TTP_Tile_image_size, TTP_Image_Tile_Batch, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, TTP_Image_Assy, CLIPTextEncode, Text Multiline, easy showAnything, VAELoader, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecodeTiled, ImageScaleDownToSize, PreviewImage, SaveImage, CR Simple Image Compare, Note, Note, CLIPLoader, MarkdownNote, PreviewImage, ImageSharpen, Text Concatenate, CLIPTextEncode, UNETLoader, VAELoader, VAEEncode, MarkdownNote, PathchSageAttentionKJ, ImageScaleDownToSize, LayerFilter: FilmV2, VAEEncode, ImpactImageBatchToImageList, SaveImage, RH_Captioner, DualCLIPLoader, UNETLoader, SaveImage, LoadImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.9, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "exponential", "seed": 831147112870635, "steps": 20, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 图片生成/图生图/WAN2.1单帧+TTP细节增强洗图_1946819482188963842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.1单帧+TTP细节增强洗图_1946819482188963842.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `EsesImageEffectBloom`
- `KSampler` ★核心
- `ImageListToImageBatch`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `easy showAnything`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `ImageScaleDownToSize`
- `PreviewImage`
- `SaveImage`
- `CR Simple Image Compare`
- `Note`
- `Note`
- `CLIPLoader`
- `MarkdownNote`
- `PreviewImage`
- `ImageSharpen`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `ImageScaleDownToSize`
- `LayerFilter: FilmV2`
- `VAEEncode` ★核心
- `ImpactImageBatchToImageList`
- `SaveImage`
- `RH_Captioner`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `831147112870635`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `exponential`
- `denoise` = `0.9`

## 知识

覆盖率 **85%**（41/48）

**有卡**：`LoraLoader`、`VAEDecode`、`EsesImageEffectBloom`、`KSampler`、`ImageListToImageBatch`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`TTP_Image_Assy`、`CLIPTextEncode`、`Text Multiline`、`VAELoader`、`VAEDecodeTiled`、`ImageScaleDownToSize`、`SaveImage`、`CR Simple Image Compare`、`CLIPLoader`、`ImageSharpen`、`Text Concatenate`、`UNETLoader`、`VAEEncode`、`PathchSageAttentionKJ`、`LayerFilter: FilmV2`、`ImpactImageBatchToImageList`、`RH_Captioner`、`DualCLIPLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled
