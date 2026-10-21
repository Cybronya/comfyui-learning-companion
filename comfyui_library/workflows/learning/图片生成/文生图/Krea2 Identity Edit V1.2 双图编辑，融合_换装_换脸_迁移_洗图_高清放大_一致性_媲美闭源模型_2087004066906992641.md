---
key: 图片生成/文生图/Krea2 Identity Edit V1.2 双图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087004066906992641.json
name: Krea2 Identity Edit V1.2 双图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087004066906992641
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Identity Edit V1.2 双图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087004066906992641.json
hash: 54a9bc8a601f922a
coverage: 0.911765
learned_at: 2026-10-20 00:58:54
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAEEncode, SaveImage, VAELoader, EmptySD3LatentImage, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, DF_Integer, SeedVR2LoadVAEModel, SimpleMath+, GetImageSize, ImpactMinMax, TTP_Image_Tile_Batch, SeedVR2LoadDiTModel, TTP_Image_Assy, DF_Integer, VAEDecode, ImageResize+, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), Krea2EditGroundedEncode, Krea2EditGroundedEncode, Krea2EditModelPatch, TextInput_, Label (rgthree), Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 100093144713201, "steps": 10}
---

# 图片生成/文生图/Krea2 Identity Edit V1.2 双图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087004066906992641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Identity Edit V1.2 双图编辑，融合_换装_换脸_迁移_洗图_高清放大_一致性_媲美闭源模型_2087004066906992641.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `SaveImage`
- `VAELoader`
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `DF_Integer`
- `SeedVR2LoadVAEModel`
- `SimpleMath+`
- `GetImageSize`
- `ImpactMinMax`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadDiTModel`
- `TTP_Image_Assy`
- `DF_Integer`
- `VAEDecode` ★核心
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `TextInput_`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `100093144713201`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEEncode`、`SaveImage`、`VAELoader`、`EmptySD3LatentImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`DF_Integer`、`SeedVR2LoadVAEModel`、`SimpleMath+`、`GetImageSize`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`VAEDecode`、`ImageResize+`、`SeedVR2VideoUpscaler`、`Krea2EditGroundedEncode`、`Krea2EditModelPatch`、`TextInput_`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
