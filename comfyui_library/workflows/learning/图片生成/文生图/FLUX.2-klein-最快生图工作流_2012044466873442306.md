---
key: 图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json
name: FLUX.2-klein-最快生图工作流_2012044466873442306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json
hash: f7ccc5f78aa88b0f
coverage: 0.888889
learned_at: 2026-10-19 22:14:58
nodes: [RandomNoise, VAELoader, VAEEncode, SamplerCustomAdvanced, GetImageSize, EmptyFlux2LatentImage, KSamplerSelect, MarkdownNote, VAEDecode, SaveImage, RandomNoise, SamplerCustomAdvanced, EmptyFlux2LatentImage, KSamplerSelect, VAEDecode, VAELoader, FluxResolutionNode, Flux2Scheduler, SaveImage, Note, Flux2Scheduler, LoadImage, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), PrimitiveNode, CLIPLoader, CLIPLoader, UNETLoader, CLIPTextEncode, ConditioningZeroOut, ConditioningZeroOut, CLIPTextEncode, UNETLoader, CFGGuider, ReferenceLatent, CFGGuider]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `RandomNoise`
- `VAELoader`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `FluxResolutionNode`
- `Flux2Scheduler`
- `SaveImage`
- `Note`
- `Flux2Scheduler`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveNode`
- `CLIPLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CFGGuider`
- `ReferenceLatent`
- `CFGGuider`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`RandomNoise`、`VAELoader`、`VAEEncode`、`SamplerCustomAdvanced`、`GetImageSize`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`VAEDecode`、`SaveImage`、`FluxResolutionNode`、`Flux2Scheduler`、`LoadImage`、`ImageScaleToTotalPixels`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`CFGGuider`、`ReferenceLatent`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
