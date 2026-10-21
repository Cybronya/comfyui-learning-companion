---
key: 图片生成/文生图/VividMuse Z-Image-Turbo ControlNet_2051502577258377217.json
name: VividMuse Z-Image-Turbo ControlNet_2051502577258377217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo ControlNet_2051502577258377217.json
hash: 8c728403adf9c80f
coverage: 0.822222
learned_at: 2026-10-21 02:55:18
nodes: [ImageScaleBy, GetImageSize+, ImageResize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, SeedVR2LoadVAEModel, ImageResize+, TTP_Image_Assy, Image Comparer (rgthree), PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, UNETLoader, LoadImage, easy promptList, PrimitiveStringMultiline, PreviewImage, VAEDecode, VAEDecode, VAEDecode, PreviewImage, LoadImage, KSamplerAdvanced, VAELoader, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, CLIPTextEncode, easy promptList, ImageResize+, easy imageRemBg, ModelPatchLoader, QwenImageDiffsynthControlnet, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, LoraLoaderModelOnly, KSamplerAdvanced, AIO_Preprocessor, SaveImage, PreviewImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "beta57", "height": 2048, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/VividMuse Z-Image-Turbo ControlNet_2051502577258377217.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo ControlNet_2051502577258377217.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `ImageScaleBy`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `GetImageSize+`
- `SeedVR2LoadVAEModel`
- `ImageResize+`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `easy promptList`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `easy promptList`
- `ImageResize+`
- `easy imageRemBg`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `AIO_Preprocessor`
- `SaveImage`
- `PreviewImage`
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

覆盖率 **82%**（37/45）

**有卡**：`ImageScaleBy`、`GetImageSize+`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`UNETLoader`、`LoadImage`、`easy promptList`、`VAEDecode`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`EmptyLatentImage`、`CLIPTextEncode`、`easy imageRemBg`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`LoraLoaderModelOnly`、`AIO_Preprocessor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
