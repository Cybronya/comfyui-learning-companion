---
key: 图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_1986368993206431746.json
name: Wan2.2单帧图像生成洗图(可TTP高清)_1986368993206431746
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_1986368993206431746.json
hash: dbc9994c99836552
coverage: 0.964912
learned_at: 2026-10-23 11:28:17
nodes: [ModelSamplingSD3, CLIPLoader, RH_Captioner, CLIPTextEncode, Text Concatenate, easy showAnything, CLIPTextEncode, ModelSamplingSD3, VAEDecode, PreviewImage, GetImageSizeAndCount, UNETLoader, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Text Multiline, DualCLIPLoader, UNETLoader, UpscaleModelLoader, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, KSampler, CR Simple Image Compare, SaveImage, ImageScaleDownToSize, SaveImage, CR Simple Image Compare, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, VAEDecode, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, SaveImage, VAELoader, VAEEncode, easy anythingIndexSwitch, easy anythingIndexSwitch, Primitive integer [Crystools], KSamplerAdvanced, KSamplerAdvanced, Primitive integer [Crystools], Primitive integer [Crystools], LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_1986368993206431746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_1986368993206431746.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetImageSizeAndCount`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `ImageScaleDownToSize`
- `SaveImage`
- `CR Simple Image Compare`
- `TTP_Image_Assy`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAELoader`
- `VAEEncode` ★核心
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `Primitive integer [Crystools]`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **96%**（55/57）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`RH_Captioner`、`CLIPTextEncode`、`Text Concatenate`、`VAEDecode`、`GetImageSizeAndCount`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`Text Multiline`、`DualCLIPLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAELoader`、`ImpactImageBatchToImageList`、`VAEEncode`、`KSampler`、`CR Simple Image Compare`、`SaveImage`、`ImageScaleDownToSize`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`easy anythingIndexSwitch`、`Primitive integer [Crystools]`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
