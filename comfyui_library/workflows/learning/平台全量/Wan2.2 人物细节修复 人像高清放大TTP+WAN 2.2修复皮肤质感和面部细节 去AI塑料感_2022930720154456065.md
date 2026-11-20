---
key: 平台全量/Wan2.2 人物细节修复 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节 去AI塑料感_2022930720154456065.json
name: Wan2.2 人物细节修复 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节 去AI塑料感_2022930720154456065
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 人物细节修复 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节 去AI塑料感_2022930720154456065.json
hash: 296137e19903775e
coverage: 0.807692
learned_at: 2026-11-14 01:05:39
nodes: [TTP_Image_Tile_Batch, ImageListToImageBatch, TTP_Image_Assy, CLIPTextEncode, CLIPTextEncode, easy imageSize, ImageUpscaleWithModel, ImageScaleToTotalPixels, ImpactImageBatchToImageList, VAEEncode, Note, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SaveImage, Note, TTP_Tile_image_size, Note, Note, LoadImage, UNETLoader, UpscaleModelLoader, CLIPLoader, VAELoader, KSampler, VAEDecode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 1113502951708940, "steps": 10}
---

# 平台全量/Wan2.2 人物细节修复 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节 去AI塑料感_2022930720154456065.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 人物细节修复 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节 去AI塑料感_2022930720154456065.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
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
- `Note`
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
- `UpscaleModelLoader`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1113502951708940`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`TTP_Image_Tile_Batch`、`ImageListToImageBatch`、`TTP_Image_Assy`、`CLIPTextEncode`、`easy imageSize`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`ImpactImageBatchToImageList`、`VAEEncode`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`TTP_Tile_image_size`、`LoadImage`、`UNETLoader`、`UpscaleModelLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、VAEEncode
