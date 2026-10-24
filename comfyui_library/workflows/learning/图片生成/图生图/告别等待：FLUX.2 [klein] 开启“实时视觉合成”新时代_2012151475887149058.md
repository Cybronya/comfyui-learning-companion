---
key: 图片生成/图生图/告别等待：FLUX.2 [klein] 开启“实时视觉合成”新时代_2012151475887149058.json
name: 告别等待：FLUX.2 [klein] 开启“实时视觉合成”新时代_2012151475887149058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/告别等待：FLUX.2 [klein] 开启“实时视觉合成”新时代_2012151475887149058.json
hash: 45c98f707951dfce
coverage: 1
learned_at: 2026-10-23 12:36:36
nodes: [UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, RandomNoise, CFGGuider, SamplerCustomAdvanced, VAEDecode, VAEEncode, GetImageSize, Flux2Scheduler, EmptyFlux2LatentImage, KSamplerSelect, ImageScaleToTotalPixels, CR Text, SaveImage, CLIPTextEncode, TextCombinerTwo, LoadImage, CR Text, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/告别等待：FLUX.2 [klein] 开启“实时视觉合成”新时代_2012151475887149058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/告别等待：FLUX.2 [klein] 开启“实时视觉合成”新时代_2012151475887149058.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `GetImageSize`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `ImageScaleToTotalPixels`
- `CR Text`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `TextCombinerTwo`
- `LoadImage`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`GetImageSize`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`CR Text`、`SaveImage`、`CLIPTextEncode`、`TextCombinerTwo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
