---
key: 图片生成/图生图/Krea+2+Identity+Edit+V1.2双图像编辑_2080593657756999681.json
name: Krea+2+Identity+Edit+V1.2双图像编辑_2080593657756999681
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea+2+Identity+Edit+V1.2双图像编辑_2080593657756999681.json
hash: 3f6c2f212906ad1e
coverage: 0.9375
learned_at: 2026-10-23 11:07:37
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAEEncode, Krea2EditGroundedEncode, Image Comparer (rgthree), SaveImage, VAELoader, EmptySD3LatentImage, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Krea2EditGroundedEncode, TextInput_, Krea2EditModelPatch, LoadImage, LoadImage, DF_Integer, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SimpleMath+, GetImageSize, ImpactMinMax, TTP_Image_Tile_Batch, ImageResize+, SeedVR2LoadDiTModel, Image Comparer (rgthree), TTP_Image_Assy, DF_Integer, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 321729911260624, "steps": 10}
---

# 图片生成/图生图/Krea+2+Identity+Edit+V1.2双图像编辑_2080593657756999681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea+2+Identity+Edit+V1.2双图像编辑_2080593657756999681.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `Krea2EditGroundedEncode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAELoader`
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Krea2EditGroundedEncode`
- `TextInput_`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoadImage`
- `DF_Integer`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SimpleMath+`
- `GetImageSize`
- `ImpactMinMax`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `DF_Integer`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `321729911260624`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEEncode`、`Krea2EditGroundedEncode`、`SaveImage`、`VAELoader`、`EmptySD3LatentImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextInput_`、`Krea2EditModelPatch`、`LoadImage`、`DF_Integer`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SimpleMath+`、`GetImageSize`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`ImageResize+`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
