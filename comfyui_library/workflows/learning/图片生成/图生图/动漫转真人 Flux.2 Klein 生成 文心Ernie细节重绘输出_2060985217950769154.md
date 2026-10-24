---
key: 图片生成/图生图/动漫转真人 Flux.2 Klein 生成 文心Ernie细节重绘输出_2060985217950769154.json
name: 动漫转真人 Flux.2 Klein 生成 文心Ernie细节重绘输出_2060985217950769154
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/动漫转真人 Flux.2 Klein 生成 文心Ernie细节重绘输出_2060985217950769154.json
hash: bd217f1948d73bad
coverage: 0.627119
learned_at: 2026-10-23 12:25:44
nodes: [INTConstant, SetNode, INTConstant, Image Comparer (rgthree), GetNode, GetNode, RandomNoise, EmptyFlux2LatentImage, CFGGuider, PreviewImage, Any Switch (rgthree), SetNode, SetNode, Seed (rgthree), SaveImage, VAEDecode, GetNode, ImageConcanate, SetNode, Fast Groups Muter (rgthree), FloatConstant, SetNode, GetImageSize, GetNode, LazyCache, ConditioningZeroOut, SetNode, SetNode, ImpactSwitch, VAEDecode, ReferenceLatent, VAEEncode, GetNode, SetNode, INTConstant, CLIPLoader, Seed (rgthree), LayerUtility: ImageScaleByAspectRatio V2, GetNode, PreviewImage, Flux2KleinEnhancer, ZML_ImageMemory, Flux2Scheduler, KSamplerSelect, UNETLoader, SamplerCustomAdvanced, VAELoader, UNETLoader, ShowText, easy showAnything, CLIPTextEncode, ConditioningZeroOut, AILab_QwenVL, CLIPLoader, KSampler, LoadImage, CLIPTextEncode, GetNode, ReferenceLatent]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.6, "denoise": 0.4, "sampler_name": "dpm_2", "scheduler": "simple", "seed": 115198972302254, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/动漫转真人 Flux.2 Klein 生成 文心Ernie细节重绘输出_2060985217950769154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/动漫转真人 Flux.2 Klein 生成 文心Ernie细节重绘输出_2060985217950769154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `INTConstant`
- `SetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `PreviewImage`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `Seed (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `GetNode`
- `ImageConcanate`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `FloatConstant`
- `SetNode`
- `GetImageSize`
- `GetNode`
- `LazyCache`
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `ImpactSwitch`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `GetNode`
- `SetNode`
- `INTConstant`
- `CLIPLoader`
- `Seed (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `PreviewImage`
- `Flux2KleinEnhancer`
- `ZML_ImageMemory`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `ShowText`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `AILab_QwenVL`
- `CLIPLoader`
- `KSampler` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ReferenceLatent`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `115198972302254`
- `steps` = `4`
- `cfg` = `1.6`
- `sampler_name` = `dpm_2`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **63%**（37/59）

**有卡**：`INTConstant`、`RandomNoise`、`EmptyFlux2LatentImage`、`CFGGuider`、`Seed (rgthree)`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`FloatConstant`、`GetImageSize`、`LazyCache`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Flux2KleinEnhancer`、`ZML_ImageMemory`、`Flux2Scheduler`、`KSamplerSelect`、`UNETLoader`、`SamplerCustomAdvanced`、`VAELoader`、`ShowText`、`CLIPTextEncode`、`AILab_QwenVL`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
