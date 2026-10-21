---
key: 图片生成/文生图/Anima+Aesthetic+1.1｜分块放大_2078701745957588993.json
name: Anima+Aesthetic+1.1｜分块放大_2078701745957588993
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜分块放大_2078701745957588993.json
hash: e5b04b459fc96f27
coverage: 0.844444
learned_at: 2026-10-20 00:18:46
nodes: [Reroute, UpscaleModelLoader, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, VAEDecodeTiled, SaveImage, ImageUpscaleWithModel, ImageScaleToTotalPixels, Seed (rgthree), ClownsharKSampler_Beta, LoadImage, WD14Tagger|pysssss, ShowText|pysssss, JWStringConcat, UNETLoader, LoraLoaderModelOnly, LoraLoader, VAEEncode, CLIPTextEncode, CLIPTextEncode, XB_UNetNameBroadcaster, CLIPLoader, VAELoader, Image Comparer (rgthree), KepStringLiteral, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, VAEDecodeTiled, SaveImage, WD14Tagger|pysssss, ShowText|pysssss, JWStringConcat, VAEEncode, CLIPTextEncode, CLIPTextEncode, Image Comparer (rgthree), KSampler]
patterns: [image_to_image, lora]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 8, "denoise": 1, "lora_name": "Gundam_RX78_Flux.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 20, "strength_clip": 0.85, "strength_model": 0.85}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/文生图/Anima+Aesthetic+1.1｜分块放大_2078701745957588993.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜分块放大_2078701745957588993.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `Reroute`
- `UpscaleModelLoader`
- `Reroute`
- `TTP_Image_Tile_Batch`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `Seed (rgthree)`
- `ClownsharKSampler_Beta` ★核心
- `LoadImage`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `JWStringConcat`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoader` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `XB_UNetNameBroadcaster`
- `CLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `KepStringLiteral`
- `Reroute`
- `TTP_Image_Tile_Batch`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `JWStringConcat`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `0`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`UpscaleModelLoader`、`TTP_Image_Tile_Batch`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`VAEDecodeTiled`、`SaveImage`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`Seed (rgthree)`、`ClownsharKSampler_Beta`、`LoadImage`、`WD14Tagger|pysssss`、`JWStringConcat`、`UNETLoader`、`LoraLoaderModelOnly`、`LoraLoader`、`VAEEncode`、`CLIPTextEncode`、`XB_UNetNameBroadcaster`、`CLIPLoader`、`VAELoader`、`KepStringLiteral`、`KSampler`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
