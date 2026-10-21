---
key: 图片生成/图生图/F.2klein 9b白底转家具背景美式现代经典风格_2059573998828216322.json
name: F.2klein 9b白底转家具背景美式现代经典风格_2059573998828216322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein 9b白底转家具背景美式现代经典风格_2059573998828216322.json
hash: fae064e965c1e51f
coverage: 0.862069
learned_at: 2026-10-21 00:39:00
nodes: [JoinStrings, AILab_ColorInput, VAELoader, PainterFluxImageEdit, ReferenceLatent, ReferenceLatent, LoraLoaderModelOnly, KSampler, VAEDecode, PreviewImage, GetImageSize+, CR Text, CLIPLoader, UNETLoader, UNETLoader, Flux2KleinColorAnchor, LoraLoaderModelOnly, CR Text, easy imageDetailTransfer, SaveImage, Image Comparer (rgthree), PreviewImage, ShowText|pysssss, RMBG, LoraLoaderModelOnly, SaveImage, ImageLoader, LayerUtility: ImageScaleByAspectRatio V2, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 244942471959894, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2klein 9b白底转家具背景美式现代经典风格_2059573998828216322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein 9b白底转家具背景美式现代经典风格_2059573998828216322.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `JoinStrings`
- `AILab_ColorInput`
- `VAELoader`
- `PainterFluxImageEdit`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `GetImageSize+`
- `CR Text`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Flux2KleinColorAnchor`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `easy imageDetailTransfer`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ShowText|pysssss`
- `RMBG`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `ImageLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`

## 关键参数

- `seed` = `244942471959894`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`JoinStrings`、`AILab_ColorInput`、`VAELoader`、`PainterFluxImageEdit`、`ReferenceLatent`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`GetImageSize+`、`CR Text`、`CLIPLoader`、`UNETLoader`、`Flux2KleinColorAnchor`、`easy imageDetailTransfer`、`SaveImage`、`RMBG`、`ImageLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ReferenceLatent、Flux2KleinColorAnchor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
