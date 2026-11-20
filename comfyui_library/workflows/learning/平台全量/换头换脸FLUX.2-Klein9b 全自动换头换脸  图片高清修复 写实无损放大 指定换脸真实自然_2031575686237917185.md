---
key: 平台全量/换头换脸FLUX.2-Klein9b 全自动换头换脸  图片高清修复 写实无损放大 指定换脸真实自然_2031575686237917185.json
name: 换头换脸FLUX.2-Klein9b 全自动换头换脸  图片高清修复 写实无损放大 指定换脸真实自然_2031575686237917185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/换头换脸FLUX.2-Klein9b 全自动换头换脸  图片高清修复 写实无损放大 指定换脸真实自然_2031575686237917185.json
hash: 418c72ec3a91afc5
coverage: 0.85
learned_at: 2026-11-14 02:07:36
nodes: [CLIPLoader, VAELoader, VAEDecode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2KleinEditTextEncode_EditUtils, RMBG, PreviewImage, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), PreviewImage, LoadImage, CR Prompt Text, Int, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 838392205768769, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/换头换脸FLUX.2-Klein9b 全自动换头换脸  图片高清修复 写实无损放大 指定换脸真实自然_2031575686237917185.json

> 来源文件 `comfyui_library/workflows/平台全量/换头换脸FLUX.2-Klein9b 全自动换头换脸  图片高清修复 写实无损放大 指定换脸真实自然_2031575686237917185.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2KleinEditTextEncode_EditUtils`
- `RMBG`
- `PreviewImage`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `CR Prompt Text`
- `Int`
- `LoadImage`

## 关键参数

- `seed` = `838392205768769`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`Flux2KleinEditTextEncode_EditUtils`、`RMBG`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`CR Prompt Text`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
