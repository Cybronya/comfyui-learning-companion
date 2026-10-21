---
key: 图片生成/文生图/VividMuse Z-Image-Turbo-PurpleDreams_2046563756121006081.json
name: VividMuse Z-Image-Turbo-PurpleDreams_2046563756121006081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-PurpleDreams_2046563756121006081.json
hash: 03c61a5727701c2b
coverage: 0.83871
learned_at: 2026-10-21 02:55:19
nodes: [UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, SeedVR2VideoUpscaler, ImageResize+, SaveImage, Image Comparer (rgthree), VAEDecode, SeedVR2LoadVAEModel, ImageResize+, KSamplerAdvanced, SaveImage, LoraLoaderModelOnly, easy promptList, PreviewImage, TTP_Image_Assy, EmptyLatentImage, Seed (rgthree), PrimitiveStringMultiline, ImageScaleBy, SeedVR2LoadDiTModel, PreviewImage, Fast Groups Bypasser (rgthree), easy promptList]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "bong_tangent", "height": 2048, "sampler_name": 1, "scheduler": "exp_heun_2_x0_sde", "seed": "enable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/VividMuse Z-Image-Turbo-PurpleDreams_2046563756121006081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-PurpleDreams_2046563756121006081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `GetImageSize+`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `GetImageSize+`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SeedVR2LoadVAEModel`
- `ImageResize+`
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `easy promptList`
- `PreviewImage`
- `TTP_Image_Assy`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `PrimitiveStringMultiline`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `exp_heun_2_x0_sde`
- `denoise` = `bong_tangent`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`GetImageSize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`ImageResize+`、`SaveImage`、`VAEDecode`、`SeedVR2LoadVAEModel`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`easy promptList`、`TTP_Image_Assy`、`EmptyLatentImage`、`Seed (rgthree)`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
