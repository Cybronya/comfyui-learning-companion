---
key: 图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json
name: F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json
hash: 6fb188a58493a0db
coverage: 0.833333
learned_at: 2026-10-23 10:52:37
nodes: [SetNode, VAELoader, DualCLIPLoader, ImageResize+, LoraLoaderModelOnly, easy ifElse, easy ifElse, ReferenceLatent, ConditioningZeroOut, GetNode, ImageResize+, easy mathString, FluxGuidance, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, easy cleanGpuUsed, UNETLoader, LoraLoaderModelOnly, Image Comparer (rgthree), VAEEncode, VAEDecode, TextInput_, KSampler, easy cleanGpuUsed, ApplyFBCacheOnModel, CLIPTextEncode, TextInput_, SaveImage, ImpactInt, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 811514288706639, "steps": 20}
---

# 图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json`

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
- `CLIPTextEncode` ★核心
- `TextInput_`
- `SaveImage`
- `ImpactInt`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `811514288706639`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ImageResize+`、`LoraLoaderModelOnly`、`ReferenceLatent`、`ConditioningZeroOut`、`easy mathString`、`FluxGuidance`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`easy cleanGpuUsed`、`UNETLoader`、`VAEEncode`、`VAEDecode`、`TextInput_`、`KSampler`、`ApplyFBCacheOnModel`、`CLIPTextEncode`、`SaveImage`、`ImpactInt`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
