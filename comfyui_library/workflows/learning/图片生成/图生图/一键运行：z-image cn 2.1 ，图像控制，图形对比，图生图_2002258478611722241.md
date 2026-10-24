---
key: 图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json
name: 一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json
hash: 53d0284a9602b231
coverage: 0.85
learned_at: 2026-10-23 11:59:22
nodes: [Image Comparer (rgthree), SaveImage, KSampler (Efficient), ConditioningZeroOut, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, EmptySD3LatentImage, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, LoadImage, LoraLoaderModelOnly, VAELoader, ModelPatchLoader, CLIPLoader, ZImageFunControlnet, PreviewImage, LayerFilter: HDREffects, SaveImage, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 45210796441771, "steps": 9}
---

# 图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Process → Output → Other

**节点**（20 个）：
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler (Efficient)` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ModelPatchLoader`
- `CLIPLoader`
- `ZImageFunControlnet`
- `PreviewImage`
- `LayerFilter: HDREffects`
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `45210796441771`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`SaveImage`、`KSampler (Efficient)`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`LoadImage`、`LoraLoaderModelOnly`、`VAELoader`、`ModelPatchLoader`、`CLIPLoader`、`ZImageFunControlnet`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、ZImageFunControlnet
