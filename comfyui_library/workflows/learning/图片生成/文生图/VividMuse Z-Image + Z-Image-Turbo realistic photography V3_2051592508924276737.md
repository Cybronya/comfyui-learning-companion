---
key: 图片生成/文生图/VividMuse Z-Image + Z-Image-Turbo realistic photography V3_2051592508924276737.json
name: VividMuse Z-Image + Z-Image-Turbo realistic photography V3_2051592508924276737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image + Z-Image-Turbo realistic photography V3_2051592508924276737.json
hash: 41250cd7080650bc
coverage: 0.837209
learned_at: 2026-10-21 02:55:17
nodes: [CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, GetImageSize+, ImageResize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, SeedVR2LoadVAEModel, ImageResize+, SeedVR2VideoUpscaler, PreviewImage, TTP_Image_Assy, SeedVR2LoadDiTModel, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, VAEDecode, PreviewImage, SaveImage, easy promptList, PreviewImage, PreviewImage, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, Seed (rgthree), EmptyLatentImage, VAEDecode, Image Comparer (rgthree), LayerColor: ColorAdapter, easy promptList, SaveImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "beta57", "height": 2048, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/VividMuse Z-Image + Z-Image-Turbo realistic photography V3_2051592508924276737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image + Z-Image-Turbo realistic photography V3_2051592508924276737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ImageScaleBy`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `GetImageSize+`
- `SeedVR2LoadVAEModel`
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `TTP_Image_Assy`
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `easy promptList`
- `PreviewImage`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LayerColor: ColorAdapter`
- `easy promptList`
- `SaveImage`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `beta57`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`CLIPTextEncode`、`ConditioningZeroOut`、`ImageScaleBy`、`GetImageSize+`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`easy promptList`、`KSamplerAdvanced`、`Seed (rgthree)`、`EmptyLatentImage`、`LayerColor: ColorAdapter`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
