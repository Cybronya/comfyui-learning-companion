---
key: 平台全量/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_1964520134234787842.json
name: F.1-Kontext 白天 ⇄ 夜晚（自动切换）_1964520134234787842
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_1964520134234787842.json
hash: fd0e3ae9fb03566e
coverage: 0.833333
learned_at: 2026-11-14 00:24:02
nodes: [SetNode, VAELoader, DualCLIPLoader, ImageResize+, LoraLoaderModelOnly, easy ifElse, easy ifElse, ReferenceLatent, ConditioningZeroOut, GetNode, ImageResize+, easy mathString, FluxGuidance, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, easy cleanGpuUsed, UNETLoader, LoraLoaderModelOnly, Image Comparer (rgthree), VAEEncode, VAEDecode, TextInput_, KSampler, easy cleanGpuUsed, ApplyFBCacheOnModel, LoadImage, CLIPTextEncode, TextInput_, ImpactInt, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 446215039953790, "steps": 20}
---

# 平台全量/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_1964520134234787842.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_1964520134234787842.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `SetNode`
- `VAELoader`
- `DualCLIPLoader`
- `ImageResize+`
- `LoraLoaderModelOnly` ★核心
- `easy ifElse`
- `easy ifElse`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `GetNode`
- `ImageResize+`
- `easy mathString`
- `FluxGuidance`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `TextInput_`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `ApplyFBCacheOnModel`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `ImpactInt`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `446215039953790`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ImageResize+`、`LoraLoaderModelOnly`、`ReferenceLatent`、`ConditioningZeroOut`、`easy mathString`、`FluxGuidance`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`easy cleanGpuUsed`、`UNETLoader`、`VAEEncode`、`VAEDecode`、`TextInput_`、`KSampler`、`ApplyFBCacheOnModel`、`LoadImage`、`CLIPTextEncode`、`ImpactInt`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
