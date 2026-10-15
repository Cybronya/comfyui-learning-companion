---
key: 图片生成/文生图/WAN2.1图生图单帧细节增强洗图(TTP)_1944310191020232705.json
name: WAN2.1图生图单帧细节增强洗图(TTP)_1944310191020232705
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.1图生图单帧细节增强洗图(TTP)_1944310191020232705.json
hash: b2d1825f0e707dd1
coverage: 0.76
learned_at: 2026-10-10 20:59:13
nodes: [UNETLoader, CLIPLoader, MarkdownNote, Note, Text Concatenate, easy showAnything, Text Multiline, RH_Captioner, Note, LoraLoader, LoraLoader, VAEDecode, ImageSharpen, MarkdownNote, VAEEncode, BetterFilmGrain, Text Multiline, CLIPTextEncode, VAELoader, PathchSageAttentionKJ, CLIPTextEncode, EsesImageEffectBloom, VAEDecodeTiled, KSampler, VAEEncode, ImpactImageBatchToImageList, ImageListToImageBatch, TTP_Tile_image_size, TTP_Image_Tile_Batch, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, CLIPTextEncode, CLIPTextEncode, VAELoader, DualCLIPLoader, PreviewImage, CR Simple Image Compare, SaveImage, LoadImage, LayerFilter: FilmV2, ImageScaleDownToSize, PreviewImage, UNETLoader, SaveImage, SaveImage, ImageScaleDownToSize, TTP_Image_Assy, KSampler, LoraLoader]
patterns: [image_to_image, lora]
missing: [CR Simple Image Compare, LayerFilter: FilmV2, Text Concatenate, Text Multiline, Text Multiline]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 866511102268658, "steps": 10, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识, 次要节点 `LayerFilter: FilmV2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/WAN2.1图生图单帧细节增强洗图(TTP)_1944310191020232705.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.1图生图单帧细节增强洗图(TTP)_1944310191020232705.json`

## 结构

**节点**（50 个）：
- `UNETLoader`
- `CLIPLoader`
- `MarkdownNote`
- `Note`
- `Text Concatenate`
- `easy showAnything`
- `Text Multiline`
- `RH_Captioner`
- `Note`
- `LoraLoader`
- `LoraLoader`
- `VAEDecode`
- `ImageSharpen`
- `MarkdownNote`
- `VAEEncode`
- `BetterFilmGrain`
- `Text Multiline`
- `CLIPTextEncode`
- `VAELoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode`
- `EsesImageEffectBloom`
- `VAEDecodeTiled`
- `KSampler`
- `VAEEncode`
- `ImpactImageBatchToImageList`
- `ImageListToImageBatch`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAELoader`
- `DualCLIPLoader`
- `PreviewImage`
- `CR Simple Image Compare`
- `SaveImage`
- `LoadImage`
- `LayerFilter: FilmV2`
- `ImageScaleDownToSize`
- `PreviewImage`
- `UNETLoader`
- `SaveImage`
- `SaveImage`
- `ImageScaleDownToSize`
- `TTP_Image_Assy`
- `KSampler`
- `LoraLoader`

**识别到的模式**：image_to_image、lora

## 关键参数

- `cfg` = `1`
- `denoise` = `0.20000000000000004`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `seed` = `866511102268658`
- `steps` = `10`
- `strength_clip` = `1.0000000000000002`
- `strength_model` = `1.0000000000000002`

## 知识

覆盖率 **76%**（38/50）

**有卡**：`UNETLoader`、`CLIPLoader`、`MarkdownNote`、`Note`、`Text Concatenate`、`easy showAnything`、`Text Multiline`、`RH_Captioner`、`LoraLoader`、`VAEDecode`、`ImageSharpen`、`VAEEncode`、`BetterFilmGrain`、`CLIPTextEncode`、`VAELoader`、`PathchSageAttentionKJ`、`EsesImageEffectBloom`、`VAEDecodeTiled`、`KSampler`、`ImpactImageBatchToImageList`、`ImageListToImageBatch`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`DualCLIPLoader`、`PreviewImage`、`CR Simple Image Compare`

**缺卡**（5）：`CR Simple Image Compare`、`LayerFilter: FilmV2`、`Text Concatenate`、`Text Multiline`、`Text Multiline`

## 学习发现

- 次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerFilter: FilmV2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
