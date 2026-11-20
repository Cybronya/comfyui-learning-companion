---
key: 平台全量/动漫转真人 Flux.2 Klein 生成 Z-imag写实重绘输出_2005675192120737793.json
name: 动漫转真人 Flux.2 Klein 生成 Z-imag写实重绘输出_2005675192120737793
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/动漫转真人 Flux.2 Klein 生成 Z-imag写实重绘输出_2005675192120737793.json
hash: 72d23eaf02c93579
coverage: 0.681818
learned_at: 2026-11-14 01:46:40
nodes: [INTConstant, SetNode, INTConstant, Image Comparer (rgthree), GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, EmptyFlux2LatentImage, CFGGuider, PreviewImage, Any Switch (rgthree), SetNode, SetNode, Seed (rgthree), GetNode, SaveImage, VAEDecode, GetNode, ImageConcanate, SetNode, Fast Groups Muter (rgthree), FloatConstant, SetNode, GetImageSize, GetNode, LazyCache, ConditioningZeroOut, SetNode, SetNode, ImpactSwitch, LazyCache, VAEDecode, KSampler, VAEEncode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, VAEEncode, GetNode, SetNode, INTConstant, CLIPLoader, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoadImage, CLIPTextEncode, Seed (rgthree), AILab_QwenVL, LayerUtility: ImageScaleByAspectRatio V2, GetNode, PreviewImage, Flux2KleinEnhancer, FluxKontextImageScale, ZML_ImageMemory, Flux2Scheduler, ShowText, LoadImage, KSamplerSelect, CLIPTextEncode, UNETLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1.6, "denoise": 0.4, "sampler_name": "dpm_2", "scheduler": "simple", "seed": 115198972302254, "steps": 10}
---

# 平台全量/动漫转真人 Flux.2 Klein 生成 Z-imag写实重绘输出_2005675192120737793.json

> 来源文件 `comfyui_library/workflows/平台全量/动漫转真人 Flux.2 Klein 生成 Z-imag写实重绘输出_2005675192120737793.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `INTConstant`
- `SetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `PreviewImage`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `Seed (rgthree)`
- `GetNode`
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
- `LazyCache`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `SetNode`
- `INTConstant`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `AILab_QwenVL`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `PreviewImage`
- `Flux2KleinEnhancer`
- `FluxKontextImageScale`
- `ZML_ImageMemory`
- `Flux2Scheduler`
- `ShowText`
- `LoadImage`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `115198972302254`
- `steps` = `10`
- `cfg` = `1.6`
- `sampler_name` = `dpm_2`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **68%**（45/66）

**有卡**：`INTConstant`、`RandomNoise`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`CFGGuider`、`Seed (rgthree)`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`FloatConstant`、`GetImageSize`、`LazyCache`、`ConditioningZeroOut`、`KSampler`、`VAEEncode`、`ReferenceLatent`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`AILab_QwenVL`、`LayerUtility: ImageScaleByAspectRatio V2`、`Flux2KleinEnhancer`、`FluxKontextImageScale`、`ZML_ImageMemory`、`Flux2Scheduler`、`ShowText`、`KSamplerSelect`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
