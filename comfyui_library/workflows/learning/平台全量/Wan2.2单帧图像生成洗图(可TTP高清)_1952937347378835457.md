---
key: 平台全量/Wan2.2单帧图像生成洗图(可TTP高清)_1952937347378835457.json
name: Wan2.2单帧图像生成洗图(可TTP高清)_1952937347378835457
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2单帧图像生成洗图(可TTP高清)_1952937347378835457.json
hash: 3562730d78df2a62
coverage: 0.964912
learned_at: 2026-11-14 01:06:20
nodes: [ModelSamplingSD3, CLIPLoader, CLIPTextEncode, Text Concatenate, CLIPTextEncode, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, Text Multiline, DualCLIPLoader, UNETLoader, UpscaleModelLoader, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, KSampler, CR Simple Image Compare, SaveImage, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, VAEDecode, SaveImage, KSamplerAdvanced, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], GetImageSizeAndCount, ImageScaleDownToSize, EmptyHunyuanLatentVideo, VAELoader, VAEEncode, easy anythingIndexSwitch, LoraLoaderModelOnly, PathchSageAttentionKJ, easy showAnything, RH_Captioner, LoraLoaderModelOnly, UNETLoader, easy anythingIndexSwitch, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, PathchSageAttentionKJ, VAEDecode, PreviewImage, SaveImage, SaveImage, CR Simple Image Compare, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "fixed"}
---

# 平台全量/Wan2.2单帧图像生成洗图(可TTP高清)_1952937347378835457.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2单帧图像生成洗图(可TTP高清)_1952937347378835457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactImageBatchToImageList`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `CR Simple Image Compare`
- `SaveImage`
- `TTP_Image_Assy`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `GetImageSizeAndCount`
- `ImageScaleDownToSize`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `VAEEncode` ★核心
- `easy anythingIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `easy showAnything`
- `RH_Captioner`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy anythingIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `CR Simple Image Compare`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **96%**（55/57）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`Text Concatenate`、`UNETLoader`、`LoraLoaderModelOnly`、`Text Multiline`、`DualCLIPLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAELoader`、`ImpactImageBatchToImageList`、`VAEEncode`、`KSampler`、`CR Simple Image Compare`、`SaveImage`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`VAEDecode`、`KSamplerAdvanced`、`Primitive integer [Crystools]`、`GetImageSizeAndCount`、`ImageScaleDownToSize`、`EmptyHunyuanLatentVideo`、`easy anythingIndexSwitch`、`PathchSageAttentionKJ`、`RH_Captioner`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
