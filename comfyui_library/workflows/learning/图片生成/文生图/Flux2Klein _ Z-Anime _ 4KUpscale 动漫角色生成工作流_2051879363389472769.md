---
key: 图片生成/文生图/Flux2Klein _ Z-Anime _ 4KUpscale 动漫角色生成工作流_2051879363389472769.json
name: Flux2Klein _ Z-Anime _ 4KUpscale 动漫角色生成工作流_2051879363389472769
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2Klein _ Z-Anime _ 4KUpscale 动漫角色生成工作流_2051879363389472769.json
hash: acdaafd996fb872c
coverage: 0.706897
learned_at: 2026-10-19 22:45:31
nodes: [PrimitiveInt, SamplerCustomAdvanced, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, ImageScaleToTotalPixels, ImageScaleToTotalPixels, KSamplerSelect, ReferenceLatent, VAEEncode, ReferenceLatent, VAEEncode, Note, PrimitiveInt, ImageScaleToTotalPixels, LoadImage, VAEEncode, ReferenceLatent, ReferenceLatent, Reroute, ReferenceLatent, ReferenceLatent, EmptyFlux2LatentImage, MarkdownNote, CFGGuider, Flux2Scheduler, VAEDecode, RandomNoise, UNETLoader, CLIPLoader, VAELoader, Note, ImageScaleBy, GetImageSizeAndCount, CLIPLoader, VAELoader, Note, VAEEncode, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, VAEDecode, UNETLoader, CLIPTextEncode, SetNode, LoraLoaderModelOnly, RTXVideoSuperResolution, PreviewImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, PreviewImage, Image Comparer (rgthree), SaveImage, PreviewImage, Image Comparer (rgthree), PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.35, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Flux2Klein _ Z-Anime _ 4KUpscale 动漫角色生成工作流_2051879363389472769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2Klein _ Z-Anime _ 4KUpscale 动漫角色生成工作流_2051879363389472769.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `Note`
- `PrimitiveInt`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Reroute`
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `MarkdownNote`
- `CFGGuider`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `ImageScaleBy`
- `GetImageSizeAndCount`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `RTXVideoSuperResolution`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **71%**（41/58）

**有卡**：`SamplerCustomAdvanced`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`KSamplerSelect`、`ReferenceLatent`、`VAEEncode`、`LoadImage`、`EmptyFlux2LatentImage`、`CFGGuider`、`Flux2Scheduler`、`VAEDecode`、`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleBy`、`GetImageSizeAndCount`、`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`RTXVideoSuperResolution`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
