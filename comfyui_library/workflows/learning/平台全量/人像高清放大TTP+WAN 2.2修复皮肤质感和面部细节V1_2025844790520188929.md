---
key: 平台全量/人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节V1_2025844790520188929.json
name: 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节V1_2025844790520188929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节V1_2025844790520188929.json
hash: 687ad82b0c96cc9c
coverage: 0.777778
learned_at: 2026-11-14 01:36:39
nodes: [TTP_Image_Tile_Batch, ImageListToImageBatch, TTP_Image_Assy, CLIPTextEncode, CLIPTextEncode, easy imageSize, ImageUpscaleWithModel, ImageScaleToTotalPixels, ImpactImageBatchToImageList, VAEEncode, VAEDecode, Note, KSampler, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SaveImage, Note, TTP_Tile_image_size, Note, Note, LoadImage, UNETLoader, Note, UpscaleModelLoader, VAELoader, CLIPLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 757038673512136, "steps": 10}
---

# 平台全量/人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节V1_2025844790520188929.json

> 来源文件 `comfyui_library/workflows/平台全量/人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节V1_2025844790520188929.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `TTP_Image_Tile_Batch`
- `ImageListToImageBatch`
- `TTP_Image_Assy`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `ImpactImageBatchToImageList`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Note`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Note`
- `TTP_Tile_image_size`
- `Note`
- `Note`
- `LoadImage`
- `UNETLoader` ★核心
- `Note`
- `UpscaleModelLoader`
- `VAELoader`
- `CLIPLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `757038673512136`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **78%**（21/27）

**有卡**：`TTP_Image_Tile_Batch`、`ImageListToImageBatch`、`TTP_Image_Assy`、`CLIPTextEncode`、`easy imageSize`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`ImpactImageBatchToImageList`、`VAEEncode`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`TTP_Tile_image_size`、`LoadImage`、`UNETLoader`、`UpscaleModelLoader`、`VAELoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、VAEEncode
