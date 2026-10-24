---
key: 图片生成/图生图/Krea+2+Identity+Edit+V1.2单图像编辑_2080592141822283777.json
name: Krea+2+Identity+Edit+V1.2单图像编辑_2080592141822283777
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea+2+Identity+Edit+V1.2单图像编辑_2080592141822283777.json
hash: 94b682ac72d4c31d
coverage: 0.894737
learned_at: 2026-10-23 11:07:37
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptySD3LatentImage, VAEEncode, ImageToMask, ImageBlur, MaskPreview+, KSampler, Image Comparer (rgthree), SaveImage, ImageCompositeMasked, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SaveImage, Krea2EditGroundedEncode, Krea2EditGroundedEncode, LoraLoaderModelOnly, Krea2EditModelPatch, TextInput_, Fast Groups Bypasser (rgthree), LoadImage, GrowMask, MaskToImage, DF_Integer, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SimpleMath+, GetImageSize, ImpactMinMax, TTP_Image_Tile_Batch, SeedVR2LoadDiTModel, DF_Integer, Image Comparer (rgthree), SaveImage, TTP_Image_Assy, ImageResize+, VAEDecode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 693628932593670, "steps": 10}
---

# 图片生成/图生图/Krea+2+Identity+Edit+V1.2单图像编辑_2080592141822283777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea+2+Identity+Edit+V1.2单图像编辑_2080592141822283777.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `ImageToMask`
- `ImageBlur`
- `MaskPreview+`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageCompositeMasked`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `LoraLoaderModelOnly` ★核心
- `Krea2EditModelPatch`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `GrowMask`
- `MaskToImage`
- `DF_Integer`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SimpleMath+`
- `GetImageSize`
- `ImpactMinMax`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadDiTModel`
- `DF_Integer`
- `Image Comparer (rgthree)`
- `SaveImage`
- `TTP_Image_Assy`
- `ImageResize+`
- `VAEDecode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `693628932593670`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptySD3LatentImage`、`VAEEncode`、`ImageToMask`、`ImageBlur`、`MaskPreview+`、`KSampler`、`SaveImage`、`ImageCompositeMasked`、`LayerUtility: ImageScaleByAspectRatio V2`、`Krea2EditGroundedEncode`、`LoraLoaderModelOnly`、`Krea2EditModelPatch`、`TextInput_`、`LoadImage`、`GrowMask`、`MaskToImage`、`DF_Integer`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SimpleMath+`、`GetImageSize`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`ImageResize+`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
