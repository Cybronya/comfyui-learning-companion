---
key: 图片生成/图生图/Z_Image_Controlnet_Union_1996610921038495745.json
name: Z_Image_Controlnet_Union_1996610921038495745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z_Image_Controlnet_Union_1996610921038495745.json
hash: 40cfb6e844c50b19
coverage: 0.875
learned_at: 2026-10-23 11:32:51
nodes: [SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, CLIPLoader, VAELoader, LoadImage, PreviewImage, MarkdownNote, EmptySD3LatentImage, ConditioningZeroOut, VAEDecode, ModelPatchLoader, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, ImageScaleBy, KSampler, CLIPTextEncode, SeedVR2LoadDiTModel, SaveImage, AIO_Preprocessor, Image Comparer (rgthree), AIO_Preprocessor, AIO_Preprocessor, QwenImageDiffsynthControlnet]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "simple", "seed": 343687848963159, "steps": 10}
---

# 图片生成/图生图/Z_Image_Controlnet_Union_1996610921038495745.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z_Image_Controlnet_Union_1996610921038495745.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `PreviewImage`
- `MarkdownNote`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ModelPatchLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `ImageScaleBy`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `AIO_Preprocessor`
- `Image Comparer (rgthree)`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`

## 关键参数

- `seed` = `343687848963159`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`VAEDecode`、`ModelPatchLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`ImageScaleBy`、`KSampler`、`CLIPTextEncode`、`SeedVR2LoadDiTModel`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
