---
key: 图片生成/图生图/Wan2.2全面升级：智能图像增幅器，细节与风格双重升级！细节增加_洗图洗稿_TTP高清放大_仿图_1950479284634832898.json
name: Wan2.2全面升级：智能图像增幅器，细节与风格双重升级！细节增加_洗图洗稿_TTP高清放大_仿图_1950479284634832898
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2全面升级：智能图像增幅器，细节与风格双重升级！细节增加_洗图洗稿_TTP高清放大_仿图_1950479284634832898.json
hash: 30e0e5a013603a22
coverage: 0.944444
learned_at: 2026-10-23 11:28:12
nodes: [ImageScaleBy, ImageListToImageBatch, TTP_Image_Assy, DualCLIPLoader, CLIPTextEncode, VAEDecodeTiled, SaveImage, Note, Image Comparer (rgthree), ImageUpscaleWithModel, LayerUtility: ImageScaleRestore V2, VAEEncode, CLIPLoader, VAELoader, CLIPTextEncode, TTP_Image_Tile_Batch, ImpactImageBatchToImageList, VAEEncode, KSampler, TTP_Tile_image_size, ImageUpscaleWithModel, Upscale Model Loader, UNETLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, UpscaleModelLoader, LoraLoaderModelOnly, LoadImage, RH_Captioner, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, FastFilmGrain, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 333424206430249, "steps": 10}
---

# 图片生成/图生图/Wan2.2全面升级：智能图像增幅器，细节与风格双重升级！细节增加_洗图洗稿_TTP高清放大_仿图_1950479284634832898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2全面升级：智能图像增幅器，细节与风格双重升级！细节增加_洗图洗稿_TTP高清放大_仿图_1950479284634832898.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `ImageScaleBy`
- `ImageListToImageBatch`
- `TTP_Image_Assy`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `Note`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleRestore V2`
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `TTP_Image_Tile_Batch`
- `ImpactImageBatchToImageList`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `TTP_Tile_image_size`
- `ImageUpscaleWithModel`
- `Upscale Model Loader`
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FastFilmGrain`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `333424206430249`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`ImageScaleBy`、`ImageListToImageBatch`、`TTP_Image_Assy`、`DualCLIPLoader`、`CLIPTextEncode`、`VAEDecodeTiled`、`SaveImage`、`ImageUpscaleWithModel`、`LayerUtility: ImageScaleRestore V2`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`TTP_Image_Tile_Batch`、`ImpactImageBatchToImageList`、`KSampler`、`TTP_Tile_image_size`、`Upscale Model Loader`、`UNETLoader`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`LoadImage`、`RH_Captioner`、`VAEDecode`、`FastFilmGrain`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
