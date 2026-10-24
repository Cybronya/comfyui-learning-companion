---
key: 图片生成/图生图/Z-image Controlnet Uion 2.1_2000500536866635778.json
name: Z-image Controlnet Uion 2.1_2000500536866635778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Uion 2.1_2000500536866635778.json
hash: 4794e81379602a2d
coverage: 0.846154
learned_at: 2026-10-23 11:30:15
nodes: [VAELoader, CLIPTextEncode, Image Comparer (rgthree), GetImageSize, LoadImage, UpscaleModelLoader, VAEDecode, SaveImage, EmptyLatentImage, PreviewImage, CLIPLoader, ImageScaleToTotalPixels, ImageConcanate, LoraLoaderModelOnly, UNETLoader, ImageUpscaleWithModel, LoadImage, AILab_QwenVL, KSampler, KSampler, ModelPatchLoader, PreviewImage, AIO_Preprocessor, QwenImageDiffsynthControlnet, PrimitiveFloat, ConditioningZeroOut]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.6000000000000001, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 1108699996865968, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Z-image Controlnet Uion 2.1_2000500536866635778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Uion 2.1_2000500536866635778.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `GetImageSize`
- `LoadImage`
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageUpscaleWithModel`
- `LoadImage`
- `AILab_QwenVL`
- `KSampler` ★核心
- `KSampler` ★核心
- `ModelPatchLoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `PrimitiveFloat`
- `ConditioningZeroOut`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `1108699996865968`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`VAELoader`、`CLIPTextEncode`、`GetImageSize`、`LoadImage`、`UpscaleModelLoader`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`CLIPLoader`、`ImageScaleToTotalPixels`、`ImageConcanate`、`LoraLoaderModelOnly`、`UNETLoader`、`ImageUpscaleWithModel`、`AILab_QwenVL`、`KSampler`、`ModelPatchLoader`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
