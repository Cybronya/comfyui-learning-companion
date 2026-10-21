---
key: 图片生成/文生图/Z-Image-Turbo ControlNet_2057628633455484929.json
name: Z-Image-Turbo ControlNet_2057628633455484929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo ControlNet_2057628633455484929.json
hash: 6f3bea56caab557f
coverage: 0.813953
learned_at: 2026-10-19 22:45:47
nodes: [ImageScaleBy, GetImageSize+, ImageResize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, SeedVR2LoadVAEModel, ImageResize+, TTP_Image_Assy, Image Comparer (rgthree), PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, UNETLoader, PreviewImage, VAEDecode, VAEDecode, VAEDecode, PreviewImage, KSamplerAdvanced, VAELoader, CLIPLoader, ConditioningZeroOut, CLIPTextEncode, ImageResize+, easy imageRemBg, ModelPatchLoader, QwenImageDiffsynthControlnet, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, LoraLoaderModelOnly, KSamplerAdvanced, AIO_Preprocessor, SaveImage, PreviewImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, EmptyLatentImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "beta57", "height": 2048, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/Z-Image-Turbo ControlNet_2057628633455484929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo ControlNet_2057628633455484929.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
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
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
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
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`

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

覆盖率 **81%**（35/43）

**有卡**：`ImageScaleBy`、`GetImageSize+`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`UNETLoader`、`VAEDecode`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`easy imageRemBg`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`LoraLoaderModelOnly`、`AIO_Preprocessor`、`LoadImage`、`EmptyLatentImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
