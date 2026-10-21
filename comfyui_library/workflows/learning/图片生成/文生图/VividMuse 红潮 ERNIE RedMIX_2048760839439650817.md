---
key: 图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json
name: VividMuse 红潮 ERNIE RedMIX_2048760839439650817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json
hash: 635a4b88d454e99a
coverage: 0.83871
learned_at: 2026-10-21 02:55:20
nodes: [UNETLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, GetImageSize+, ImageResize+, TTP_Tile_image_size, GetImageSize+, ImageScaleBy, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageResize+, SeedVR2VideoUpscaler, TTP_Image_Assy, PreviewImage, Image Comparer (rgthree), easy promptList, PrimitiveStringMultiline, Seed (rgthree), EmptyLatentImage, PreviewImage, CheckpointLoaderSimple, SaveImage, VAELoader, VAEDecode, CLIPLoader, easy promptList, KSampler, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraft_ernieRedmix.safetensors", "denoise": 1, "height": 1536, "sampler_name": "deis", "scheduler": "simple", "seed": 0, "steps": 10, "width": 1024}
---

# 图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ImageScaleBy`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Tile_image_size`
- `GetImageSize+`
- `ImageScaleBy`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `easy promptList`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPLoader`
- `easy promptList`
- `KSampler` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `redcraft_ernieRedmix.safetensors`
- `seed` = `0`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ImageScaleBy`、`GetImageSize+`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`easy promptList`、`Seed (rgthree)`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`SaveImage`、`VAELoader`、`VAEDecode`、`CLIPLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
