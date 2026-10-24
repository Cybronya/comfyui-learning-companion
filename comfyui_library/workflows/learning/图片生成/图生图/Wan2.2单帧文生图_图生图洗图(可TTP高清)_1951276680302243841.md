---
key: 图片生成/图生图/Wan2.2单帧文生图_图生图洗图(可TTP高清)_1951276680302243841.json
name: Wan2.2单帧文生图_图生图洗图(可TTP高清)_1951276680302243841
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2单帧文生图_图生图洗图(可TTP高清)_1951276680302243841.json
hash: 3cff57a7099d1715
coverage: 0.932203
learned_at: 2026-10-23 11:28:20
nodes: [CLIPTextEncode, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, UNETLoader, UpscaleModelLoader, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, KSampler, CR Simple Image Compare, SaveImage, SaveImage, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, VAEDecode, SaveImage, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, easy anythingIndexSwitch, easy anythingIndexSwitch, Primitive integer [Crystools], Primitive integer [Crystools], easy showAnything, Text Concatenate, Text Multiline, CLIPLoader, RH_Captioner, LoraLoaderModelOnly, VAEDecode, KSamplerAdvanced, PreviewImage, LoraLoaderModelOnly, ModelSamplingSD3, CR Simple Image Compare, SaveImage, VAELoader, VAEEncode, EmptyHunyuanLatentVideo, GetImageSizeAndCount, ImageScaleDownToSize, LoadImage, Note, Note, Primitive integer [Crystools]]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/Wan2.2单帧文生图_图生图洗图(可TTP高清)_1951276680302243841.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2单帧文生图_图生图洗图(可TTP高清)_1951276680302243841.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `SaveImage`
- `TTP_Image_Assy`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `easy showAnything`
- `Text Concatenate`
- `Text Multiline`
- `CLIPLoader`
- `RH_Captioner`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CR Simple Image Compare`
- `SaveImage`
- `VAELoader`
- `VAEEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `GetImageSizeAndCount`
- `ImageScaleDownToSize`
- `LoadImage`
- `Note`
- `Note`
- `Primitive integer [Crystools]`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **93%**（55/59）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAELoader`、`ImpactImageBatchToImageList`、`VAEEncode`、`KSampler`、`CR Simple Image Compare`、`SaveImage`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`VAEDecode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`easy anythingIndexSwitch`、`Primitive integer [Crystools]`、`Text Concatenate`、`Text Multiline`、`CLIPLoader`、`RH_Captioner`、`EmptyHunyuanLatentVideo`、`GetImageSizeAndCount`、`ImageScaleDownToSize`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
