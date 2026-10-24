---
key: 图片生成/图生图/wan2.2+TTP高清放大 V2_1990104620653572098.json
name: wan2.2+TTP高清放大 V2_1990104620653572098
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2+TTP高清放大 V2_1990104620653572098.json
hash: 33f6d0b693112abe
coverage: 0.857143
learned_at: 2026-10-23 11:45:56
nodes: [UpscaleModelLoader, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, VAEDecode, ImageUpscaleWithModel, TTP_CoordinateSplitter, CLIPTextEncode, easy showAnything, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageInsetCrop, TTP_Image_Assy, Constant Number, easy imageBatchToImageList, easy imageListToImageBatch, JJC_JoyCaption, ConditioningAverage, TTP_condsetarea_merge, TTP_condtobatch, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, Image Comparer (rgthree), LoadImage, SaveImage, PreviewImage, KSampler, ImageScaleToTotalPixels, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "beta", "seed": 172615424112288, "steps": 10}
---

# 图片生成/图生图/wan2.2+TTP高清放大 V2_1990104620653572098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2+TTP高清放大 V2_1990104620653572098.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UpscaleModelLoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `TTP_CoordinateSplitter`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageInsetCrop`
- `TTP_Image_Assy`
- `Constant Number`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `JJC_JoyCaption`
- `ConditioningAverage`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `172615424112288`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`UpscaleModelLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`ImageUpscaleWithModel`、`TTP_CoordinateSplitter`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy imageInsetCrop`、`TTP_Image_Assy`、`Constant Number`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`JJC_JoyCaption`、`ConditioningAverage`、`TTP_condsetarea_merge`、`TTP_condtobatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`SaveImage`、`KSampler`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
