---
key: 图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json
name: Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json
hash: 709b3bd075242aee
coverage: 0.792453
learned_at: 2026-10-19 22:15:22
nodes: [Reroute, LayerUtility: ImageReelComposit, ImpactInt, CLIPTextEncode, CLIPTextEncode, VAEDecode, LayerUtility: ImageReel, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, SaveImage, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, ImageScaleBy, Image Filter Adjustments, Image Comparer (rgthree), KSampler, VAEEncode, CLIPTextEncode, SomethingToString, Fast Groups Bypasser (rgthree), PlaySound|pysssss, VAEDecode, KSampler, EmptySD3LatentImage, VAELoader, UNETLoader, CR Text, INTConstant, INTConstant, ModelSamplingAuraFlow, SaveImage, CLIPLoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, SeedVR2VideoUpscaler, Image Filter Adjustments, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, Qwen3_VQA, ShowText|pysssss, Fast Groups Bypasser (rgthree), PreviewImage, PrimitiveFloat, Note, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 646853179883123, "steps": 25}
---

# 图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `Reroute`
- `LayerUtility: ImageReelComposit`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `Image Filter Adjustments`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SomethingToString`
- `Fast Groups Bypasser (rgthree)`
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAELoader`
- `UNETLoader` ★核心
- `CR Text`
- `INTConstant`
- `INTConstant`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SeedVR2VideoUpscaler`
- `Image Filter Adjustments`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `PrimitiveFloat`
- `Note`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `646853179883123`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（42/53）

**有卡**：`LayerUtility: ImageReelComposit`、`ImpactInt`、`CLIPTextEncode`、`VAEDecode`、`LayerUtility: ImageReel`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`Image Filter Adjustments`、`KSampler`、`VAEEncode`、`SomethingToString`、`PlaySound|pysssss`、`EmptySD3LatentImage`、`VAELoader`、`UNETLoader`、`CR Text`、`INTConstant`、`ModelSamplingAuraFlow`、`CLIPLoader`、`LoadImage`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SeedVR2LoadDiTModel
