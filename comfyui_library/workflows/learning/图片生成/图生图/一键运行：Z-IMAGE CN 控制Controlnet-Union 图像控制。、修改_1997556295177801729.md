---
key: 图片生成/图生图/一键运行：Z-IMAGE CN 控制Controlnet-Union 图像控制。、修改_1997556295177801729.json
name: 一键运行：Z-IMAGE CN 控制Controlnet-Union 图像控制。、修改_1997556295177801729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键运行：Z-IMAGE CN 控制Controlnet-Union 图像控制。、修改_1997556295177801729.json
hash: 27a6b53003d2c304
coverage: 0.84
learned_at: 2026-10-23 11:59:17
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SeedVR2LoadVAEModel, easy stylesSelector, PreviewImage, SeedVR2VideoUpscaler, QwenImageDiffsynthControlnet, ModelPatchLoader, PreviewImage, GetImageSize, PreviewImage, AIO_Preprocessor, StringFunction|pysssss, LoadImage, Note, VAELoader, EmptyLatentImage, LayerFilter: HDREffects, SeedVR2LoadDiTModel, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler (Efficient), SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1200, "sampler_name": "euler", "scheduler": "simple", "seed": 1093593973069323, "steps": 6, "width": 728}
---

# 图片生成/图生图/一键运行：Z-IMAGE CN 控制Controlnet-Union 图像控制。、修改_1997556295177801729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键运行：Z-IMAGE CN 控制Controlnet-Union 图像控制。、修改_1997556295177801729.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Process → Output → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadVAEModel`
- `easy stylesSelector`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `PreviewImage`
- `GetImageSize`
- `PreviewImage`
- `AIO_Preprocessor`
- `StringFunction|pysssss`
- `LoadImage`
- `Note`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `LayerFilter: HDREffects`
- `SeedVR2LoadDiTModel`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler (Efficient)` ★核心
- `SaveImage`

## 关键参数

- `width` = `728`
- `height` = `1200`
- `batch_size` = `1`
- `seed` = `1093593973069323`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`SeedVR2LoadVAEModel`、`easy stylesSelector`、`SeedVR2VideoUpscaler`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`GetImageSize`、`AIO_Preprocessor`、`StringFunction|pysssss`、`LoadImage`、`VAELoader`、`EmptyLatentImage`、`LayerFilter: HDREffects`、`SeedVR2LoadDiTModel`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler (Efficient)`、`SaveImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader
