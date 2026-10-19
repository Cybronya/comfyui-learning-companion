---
key: 图片生成/文生图/FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505.json
name: FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505.json
hash: 009af0645629ed5e
coverage: 0.857143
learned_at: 2026-10-19 22:00:30
nodes: [BasicGuider, VAEEncode, LoadImage, VAEEncode, ReferenceLatent, FluxGuidance, KSamplerSelect, ReferenceLatent, PrimitiveNode, PrimitiveNode, VAELoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEDecode, ImageScaleToTotalPixels, Note, LoadImage, SaveImage, UNETLoader, MarkdownNote, CLIPLoader, Flux2Scheduler, LoraLoaderModelOnly, CLIPTextEncode, RandomNoise, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `BasicGuider`
- `VAEEncode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`BasicGuider`、`VAEEncode`、`LoadImage`、`ReferenceLatent`、`FluxGuidance`、`KSamplerSelect`、`VAELoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`RandomNoise`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance
