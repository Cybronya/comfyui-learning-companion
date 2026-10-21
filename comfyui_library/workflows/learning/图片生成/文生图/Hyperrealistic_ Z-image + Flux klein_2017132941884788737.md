---
key: 图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json
name: Hyperrealistic_ Z-image + Flux klein_2017132941884788737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json
hash: ea9c944b131d2683
coverage: 0.914286
learned_at: 2026-10-19 22:15:10
nodes: [ModelSamplingAuraFlow, VAELoader, UNETLoader, ConditioningZeroOut, CLIPTextEncode, EmptySD3LatentImage, KSamplerSelect, CFGGuider, VAELoader, CLIPLoader, UNETLoader, CLIPTextEncode, ReferenceLatent, ReferenceLatent, Flux2Scheduler, SamplerCustomAdvanced, VAEDecode, VAEEncode, GetImageSize, EmptyFlux2LatentImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, MarkdownNote, CLIPLoader, UNETLoader, ColorMatch, CLIPTextEncode, RandomNoise, VAEDecode, ImageSharpen, PreviewImage, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `ModelSamplingAuraFlow`
- `VAELoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ColorMatch`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `ImageSharpen`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`ModelSamplingAuraFlow`、`VAELoader`、`UNETLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSamplerSelect`、`CFGGuider`、`CLIPLoader`、`ReferenceLatent`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEEncode`、`GetImageSize`、`EmptyFlux2LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`ColorMatch`、`RandomNoise`、`ImageSharpen`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerAdvanced
