---
key: 图片生成/文生图/Krea2 Identity Edit V1.2 单图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087023965511438337.json
name: Krea2 Identity Edit V1.2 单图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087023965511438337
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Identity Edit V1.2 单图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087023965511438337.json
hash: ac058482e8f63ee0
coverage: 0.897436
learned_at: 2026-10-20 00:58:53
nodes: [UNETLoader, CLIPLoader, VAELoader, ImageToMask, ImageBlur, KSampler, Image Comparer (rgthree), Krea2EditGroundedEncode, Krea2EditGroundedEncode, LoraLoaderModelOnly, Krea2EditModelPatch, MaskToImage, DF_Integer, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SimpleMath+, GetImageSize, ImpactMinMax, TTP_Image_Tile_Batch, SeedVR2LoadDiTModel, DF_Integer, Image Comparer (rgthree), SaveImage, TTP_Image_Assy, ImageResize+, VAEDecode, Label (rgthree), LoadImage, EmptySD3LatentImage, ImageCompositeMasked, SaveImage, MaskPreview+, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, GrowMask, VAEEncode, Fast Groups Bypasser (rgthree), TextInput_, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 408611498234253, "steps": 10}
---

# 图片生成/文生图/Krea2 Identity Edit V1.2 单图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087023965511438337.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Identity Edit V1.2 单图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087023965511438337.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageToMask`
- `ImageBlur`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `LoraLoaderModelOnly` ★核心
- `Krea2EditModelPatch`
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
- `Label (rgthree)`
- `LoadImage`
- `EmptySD3LatentImage`
- `ImageCompositeMasked`
- `SaveImage`
- `MaskPreview+`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMask`
- `VAEEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `TextInput_`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `408611498234253`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageToMask`、`ImageBlur`、`KSampler`、`Krea2EditGroundedEncode`、`LoraLoaderModelOnly`、`Krea2EditModelPatch`、`MaskToImage`、`DF_Integer`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SimpleMath+`、`GetImageSize`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`SaveImage`、`TTP_Image_Assy`、`ImageResize+`、`VAEDecode`、`Label (rgthree)`、`LoadImage`、`EmptySD3LatentImage`、`ImageCompositeMasked`、`MaskPreview+`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMask`、`VAEEncode`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
