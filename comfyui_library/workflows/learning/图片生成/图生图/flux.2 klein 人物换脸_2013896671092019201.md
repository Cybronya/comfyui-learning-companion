---
key: 图片生成/图生图/flux.2 klein 人物换脸_2013896671092019201.json
name: flux.2 klein 人物换脸_2013896671092019201
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.2 klein 人物换脸_2013896671092019201.json
hash: beb8a7c54b533ebf
coverage: 0.897959
learned_at: 2026-10-23 11:35:52
nodes: [easy imageRemBg, ACE_ImageFaceCrop, easy positive, CLIPTextEncode, CLIPLoader, ConditioningZeroOut, SamplerCustomAdvanced, CFGGuider, Reroute, Reroute, VAEDecode, RandomNoise, EmptyFlux2LatentImage, GetImageSize, Fast Groups Bypasser (rgthree), AnySwitch, AnySwitch, PreviewImage, KSampler, VAEDecode, ConditioningZeroOut, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, VAEEncode, KSampler, VAEEncode, VAEEncode, ReferenceLatent, VAEDecode, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, Flux2Scheduler, KSamplerSelect, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, VAEEncode, Reroute, LoadImage, LoadImage, VAELoader, UNETLoader, SaveImageAndMetadata_]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 28940567352145, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/flux.2 klein 人物换脸_2013896671092019201.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.2 klein 人物换脸_2013896671092019201.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `easy imageRemBg`
- `ACE_ImageFaceCrop`
- `easy positive`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `Fast Groups Bypasser (rgthree)`
- `AnySwitch`
- `AnySwitch`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `Reroute`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImageAndMetadata_`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `28940567352145`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`easy imageRemBg`、`ACE_ImageFaceCrop`、`easy positive`、`CLIPTextEncode`、`CLIPLoader`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`CFGGuider`、`VAEDecode`、`RandomNoise`、`EmptyFlux2LatentImage`、`GetImageSize`、`AnySwitch`、`KSampler`、`UNETLoader`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`Flux2Scheduler`、`KSamplerSelect`、`LoadImage`、`SaveImageAndMetadata_`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
