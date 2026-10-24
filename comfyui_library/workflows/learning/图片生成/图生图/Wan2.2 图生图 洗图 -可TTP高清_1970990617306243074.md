---
key: 图片生成/图生图/Wan2.2 图生图 洗图 -可TTP高清_1970990617306243074.json
name: Wan2.2 图生图 洗图 -可TTP高清_1970990617306243074
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 图生图 洗图 -可TTP高清_1970990617306243074.json
hash: 08aebe98121e5cf2
coverage: 0.888889
learned_at: 2026-10-23 11:28:02
nodes: [DualCLIPLoader, UNETLoader, UpscaleModelLoader, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, KSampler, CR Simple Image Compare, SaveImage, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, SaveImage, UNETLoader, Text Multiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, VAEDecode, SaveImage, Text Concatenate, CLIPTextEncode, CLIPTextEncode, CR Simple Image Compare, VAELoader, RH_Captioner, easy showAnything, LoadImage, ImageScaleDownToSize, VAEEncode, PreviewImage, SaveImage, KSampler, Fast Groups Bypasser (rgthree), PrimitiveFloat, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 568681196656404, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2 图生图 洗图 -可TTP高清_1970990617306243074.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 图生图 洗图 -可TTP高清_1970990617306243074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
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
- `SaveImage`
- `UNETLoader` ★核心
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Simple Image Compare`
- `VAELoader`
- `RH_Captioner`
- `easy showAnything`
- `LoadImage`
- `ImageScaleDownToSize`
- `VAEEncode` ★核心
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveFloat`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `568681196656404`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAELoader`、`CLIPTextEncode`、`ImpactImageBatchToImageList`、`VAEEncode`、`KSampler`、`CR Simple Image Compare`、`SaveImage`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`Text Multiline`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`ModelSamplingSD3`、`VAEDecode`、`Text Concatenate`、`RH_Captioner`、`LoadImage`、`ImageScaleDownToSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
