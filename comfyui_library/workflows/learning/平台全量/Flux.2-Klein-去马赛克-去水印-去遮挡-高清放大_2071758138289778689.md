---
key: 平台全量/Flux.2-Klein-去马赛克-去水印-去遮挡-高清放大_2071758138289778689.json
name: Flux.2-Klein-去马赛克-去水印-去遮挡-高清放大_2071758138289778689
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2-Klein-去马赛克-去水印-去遮挡-高清放大_2071758138289778689.json
hash: 43427771b15ebd09
coverage: 0.944444
learned_at: 2026-11-14 00:28:58
nodes: [VAELoader, CLIPLoader, UNETLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, VAEDecode, VAEEncode, ReferenceLatent, Seed (rgthree), ColorMatch, SaveImage, LoadImage, Image Comparer (rgthree), ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 13757014960812, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2-Klein-去马赛克-去水印-去遮挡-高清放大_2071758138289778689.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2-Klein-去马赛克-去水印-去遮挡-高清放大_2071758138289778689.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `Seed (rgthree)`
- `ColorMatch`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `13757014960812`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`KSampler`、`VAEDecode`、`VAEEncode`、`ReferenceLatent`、`Seed (rgthree)`、`ColorMatch`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
