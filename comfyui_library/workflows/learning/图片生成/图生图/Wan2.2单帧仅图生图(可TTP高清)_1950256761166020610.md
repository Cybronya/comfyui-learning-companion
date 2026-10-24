---
key: 图片生成/图生图/Wan2.2单帧仅图生图(可TTP高清)_1950256761166020610.json
name: Wan2.2单帧仅图生图(可TTP高清)_1950256761166020610
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2单帧仅图生图(可TTP高清)_1950256761166020610.json
hash: 4786be53969a6ca8
coverage: 0.952381
learned_at: 2026-10-23 11:28:15
nodes: [ModelSamplingSD3, CLIPLoader, RH_Captioner, CLIPTextEncode, Text Concatenate, easy showAnything, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, Text Multiline, DualCLIPLoader, UNETLoader, UpscaleModelLoader, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, KSampler, CR Simple Image Compare, SaveImage, SaveImage, CR Simple Image Compare, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, VAEDecode, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleDownToSize, VAEEncode, VAELoader, Note, SaveImage, LoadImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1107898887063502, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2单帧仅图生图(可TTP高清)_1950256761166020610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2单帧仅图生图(可TTP高清)_1950256761166020610.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
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
- `SaveImage`
- `CR Simple Image Compare`
- `TTP_Image_Assy`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleDownToSize`
- `VAEEncode` ★核心
- `VAELoader`
- `Note`
- `SaveImage`
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1107898887063502`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **95%**（40/42）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`RH_Captioner`、`CLIPTextEncode`、`Text Concatenate`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`Text Multiline`、`DualCLIPLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAELoader`、`ImpactImageBatchToImageList`、`VAEEncode`、`KSampler`、`CR Simple Image Compare`、`SaveImage`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`VAEDecode`、`ImageScaleDownToSize`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
