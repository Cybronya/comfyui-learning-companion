---
key: 平台全量/人物精细修复｜人物皮肤、头发、去模糊、并保持人脸特征、黑白转彩色｜flux2 klein 9B +LoRA adonis base +adonis refine_2049330636854398977.json
name: 人物精细修复｜人物皮肤、头发、去模糊、并保持人脸特征、黑白转彩色｜flux2 klein 9B +LoRA adonis base +adonis refine_2049330636854398977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物精细修复｜人物皮肤、头发、去模糊、并保持人脸特征、黑白转彩色｜flux2 klein 9B +LoRA adonis base +adonis refine_2049330636854398977.json
hash: 0e24003ac9d94c35
coverage: 0.7
learned_at: 2026-11-14 01:38:11
nodes: [ReferenceLatent, FastFilmGrain, Image Comparer (rgthree), SharkOptions_Beta, EmptyFlux2LatentImage, ReferenceLatent, Seed (rgthree), ClownsharKSampler_Beta, ClownsharKSampler_Beta, VAEDecode, PreviewImage, VAEEncode, ConditioningZeroOut, LoadImage, Note, LoraLoaderModelOnly, UNETLoader, ClipLoaderGGUF, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, SaveImage, Note, Note, Note, Note, Note, Fast Bypasser (rgthree), ImageScaleToTotalPixelsX, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 9, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.8, "steps": "simple"}
---

# 平台全量/人物精细修复｜人物皮肤、头发、去模糊、并保持人脸特征、黑白转彩色｜flux2 klein 9B +LoRA adonis base +adonis refine_2049330636854398977.json

> 来源文件 `comfyui_library/workflows/平台全量/人物精细修复｜人物皮肤、头发、去模糊、并保持人脸特征、黑白转彩色｜flux2 klein 9B +LoRA adonis base +adonis refine_2049330636854398977.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `ReferenceLatent`
- `FastFilmGrain`
- `Image Comparer (rgthree)`
- `SharkOptions_Beta`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `Seed (rgthree)`
- `ClownsharKSampler_Beta` ★核心
- `ClownsharKSampler_Beta` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LoadImage`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ClipLoaderGGUF`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Fast Bypasser (rgthree)`
- `ImageScaleToTotalPixelsX`
- `PreviewImage`

## 关键参数

- `seed` = `0.8`
- `steps` = `simple`
- `cfg` = `9`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **70%**（21/30）

**有卡**：`ReferenceLatent`、`FastFilmGrain`、`SharkOptions_Beta`、`EmptyFlux2LatentImage`、`Seed (rgthree)`、`ClownsharKSampler_Beta`、`VAEDecode`、`VAEEncode`、`ConditioningZeroOut`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`ClipLoaderGGUF`、`VAELoader`、`CLIPTextEncode`、`SaveImage`、`Fast Bypasser (rgthree)`、`ImageScaleToTotalPixelsX`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ClownsharKSampler_Beta
