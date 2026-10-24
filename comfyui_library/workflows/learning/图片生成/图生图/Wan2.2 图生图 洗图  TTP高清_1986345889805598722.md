---
key: 图片生成/图生图/Wan2.2 图生图 洗图  TTP高清_1986345889805598722.json
name: Wan2.2 图生图 洗图  TTP高清_1986345889805598722
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 图生图 洗图  TTP高清_1986345889805598722.json
hash: 0abee75d9614caea
coverage: 0.888889
learned_at: 2026-10-23 11:28:02
nodes: [DualCLIPLoader, UNETLoader, UpscaleModelLoader, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, KSampler, CR Simple Image Compare, SaveImage, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, UNETLoader, Text Multiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, VAEDecode, Text Concatenate, CLIPTextEncode, CLIPTextEncode, CR Simple Image Compare, VAELoader, easy showAnything, ImageScaleDownToSize, VAEEncode, PreviewImage, SaveImage, KSampler, Fast Groups Bypasser (rgthree), PrimitiveFloat, RH_Captioner, SaveImage, SaveImage, LoadImage, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 207214805589727, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2 图生图 洗图  TTP高清_1986345889805598722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 图生图 洗图  TTP高清_1986345889805598722.json`

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
- `UNETLoader` ★核心
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Simple Image Compare`
- `VAELoader`
- `easy showAnything`
- `ImageScaleDownToSize`
- `VAEEncode` ★核心
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveFloat`
- `RH_Captioner`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `207214805589727`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAELoader`、`CLIPTextEncode`、`ImpactImageBatchToImageList`、`VAEEncode`、`KSampler`、`CR Simple Image Compare`、`SaveImage`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`Text Multiline`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`ModelSamplingSD3`、`VAEDecode`、`Text Concatenate`、`ImageScaleDownToSize`、`RH_Captioner`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
