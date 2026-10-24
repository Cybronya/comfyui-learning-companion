---
key: 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json
name: Klein+Sun_direction_LoRA可控打光_2073950983855628289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json
hash: f7328c41969c4a2c
coverage: 0.966667
learned_at: 2026-10-23 11:04:27
nodes: [UNETLoader, CLIPLoader, VAELoader, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, EmptyFlux2LatentImage, GetImageSize, VAEDecode, Flux2Scheduler, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, ReferenceLatent, LoadImage, ImageResize+, SphereLightNode, SaveImage, VAEEncode, VAEEncode, ImageScaleToTotalPixels, LoraLoaderModelOnly, RandomNoise, SaveImage, Image Comparer (rgthree), CLIPTextEncode, DF_Integer, RHHiddenNodes, easy imageColorMatch]
patterns: []
missing: []
---

# 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `ImageResize+`
- `SphereLightNode`
- `SaveImage`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `DF_Integer`
- `RHHiddenNodes`
- `easy imageColorMatch`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`GetImageSize`、`VAEDecode`、`Flux2Scheduler`、`ReferenceLatent`、`ConditioningZeroOut`、`LoadImage`、`ImageResize+`、`SphereLightNode`、`SaveImage`、`VAEEncode`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`RandomNoise`、`CLIPTextEncode`、`DF_Integer`、`RHHiddenNodes`、`easy imageColorMatch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
