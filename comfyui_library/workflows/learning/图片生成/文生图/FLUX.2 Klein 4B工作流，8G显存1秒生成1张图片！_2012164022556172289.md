---
key: 图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json
name: FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json
hash: d90b04aa71854f7e
coverage: 0.966667
learned_at: 2026-10-19 22:14:57
nodes: [KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, UNETLoader, CLIPLoader, VAELoader, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, SaveImage, KSamplerSelect, SamplerCustomAdvanced, UNETLoader, CLIPLoader, VAELoader, EmptyFlux2LatentImage, CFGGuider, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, GetImageSize, Flux2Scheduler, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, UNETLoader, CLIPLoader, VAELoader, CFGGuider, ConditioningZeroOut, Flux2Scheduler, EmptyFlux2LatentImage, SaveImage, ImageScaleToTotalPixels, SaveImage, VAEDecode, MarkdownNote, LoadImage, CLIPTextEncode, CLIPTextEncode, RandomNoise, LoadImage, Fast Groups Bypasser (rgthree), VAEEncode, ReferenceLatent, ReferenceLatent, ImageScaleToTotalPixels, VAEEncode, ImageScaleToTotalPixels, LoadImage, CLIPTextEncode, RandomNoise, Label (rgthree), Label (rgthree), RandomNoise]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `SaveImage`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `VAEDecode` ★核心
- `MarkdownNote`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `Label (rgthree)`
- `Label (rgthree)`
- `RandomNoise`

## 知识

覆盖率 **97%**（58/60）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`SaveImage`、`ReferenceLatent`、`VAEEncode`、`ImageScaleToTotalPixels`、`LoadImage`、`CLIPTextEncode`、`RandomNoise`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
