---
key: 图片生成/图生图/Flux.2-Klein-图像编辑_2012002471639523329.json
name: Flux.2-Klein-图像编辑_2012002471639523329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Klein-图像编辑_2012002471639523329.json
hash: 4e763279286ac620
coverage: 0.857143
learned_at: 2026-10-23 10:58:50
nodes: [LoadImage, UNETLoader, CLIPLoader, LoadImage, VAELoader, CFGGuider, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, FluxKontextImageScale, VAEEncode, SamplerCustomAdvanced, VAEDecode, Reroute, Reroute, GetImageSize, RandomNoise, KSamplerSelect, Flux2Scheduler, Anything Everywhere, CLIPTextEncode, ReferenceLatent, FluxKontextImageScale, ConditioningZeroOut, EmptyFlux2LatentImage, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2-Klein-图像编辑_2012002471639523329.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Klein-图像编辑_2012002471639523329.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `VAELoader`
- `CFGGuider`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `GetImageSize`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `FluxKontextImageScale`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`VAEEncode`、`ReferenceLatent`、`FluxKontextImageScale`、`SamplerCustomAdvanced`、`VAEDecode`、`GetImageSize`、`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
