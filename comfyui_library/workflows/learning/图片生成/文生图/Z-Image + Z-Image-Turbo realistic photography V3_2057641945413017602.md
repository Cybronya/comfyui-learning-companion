---
key: 图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json
name: Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json
hash: e92c6d5cec858fec
coverage: 0.853659
learned_at: 2026-10-19 22:45:46
nodes: [CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, GetImageSize+, ImageResize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, SeedVR2LoadVAEModel, ImageResize+, SeedVR2VideoUpscaler, PreviewImage, TTP_Image_Assy, SeedVR2LoadDiTModel, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, VAEDecode, PreviewImage, SaveImage, PreviewImage, PreviewImage, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, Seed (rgthree), EmptyLatentImage, VAEDecode, Image Comparer (rgthree), LayerColor: ColorAdapter, SaveImage, Fast Groups Bypasser (rgthree), easy promptList]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "beta57", "height": 2048, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
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
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`

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

覆盖率 **85%**（35/41）

**有卡**：`CLIPTextEncode`、`ConditioningZeroOut`、`ImageScaleBy`、`GetImageSize+`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`KSamplerAdvanced`、`Seed (rgthree)`、`EmptyLatentImage`、`LayerColor: ColorAdapter`、`easy promptList`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
