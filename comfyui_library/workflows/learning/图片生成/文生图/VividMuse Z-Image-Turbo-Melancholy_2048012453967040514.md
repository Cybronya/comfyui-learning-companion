---
key: 图片生成/文生图/VividMuse Z-Image-Turbo-Melancholy_2048012453967040514.json
name: VividMuse Z-Image-Turbo-Melancholy_2048012453967040514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-Melancholy_2048012453967040514.json
hash: a023e9b771d86674
coverage: 0.83871
learned_at: 2026-10-21 02:55:19
nodes: [UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, SeedVR2VideoUpscaler, ImageResize+, Image Comparer (rgthree), VAEDecode, SeedVR2LoadVAEModel, ImageResize+, TTP_Image_Assy, ImageScaleBy, SeedVR2LoadDiTModel, PreviewImage, easy promptList, KSamplerAdvanced, LoraLoaderModelOnly, PrimitiveStringMultiline, EmptyLatentImage, Seed (rgthree), easy promptList, Fast Groups Bypasser (rgthree), SaveImage, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "bong_tangent", "height": 2048, "sampler_name": 1, "scheduler": "exp_heun_2_x0_sde", "seed": "enable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/VividMuse Z-Image-Turbo-Melancholy_2048012453967040514.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-Melancholy_2048012453967040514.json`

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
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SeedVR2LoadVAEModel`
- `ImageResize+`
- `TTP_Image_Assy`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `easy promptList`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `easy promptList`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `PreviewImage`
- `SaveImage`

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

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`GetImageSize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`ImageResize+`、`VAEDecode`、`SeedVR2LoadVAEModel`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`easy promptList`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`Seed (rgthree)`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
