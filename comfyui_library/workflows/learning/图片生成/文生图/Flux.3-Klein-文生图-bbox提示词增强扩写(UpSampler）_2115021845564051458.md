---
key: 图片生成/文生图/Flux.3-Klein-文生图-bbox提示词增强扩写(UpSampler）_2115021845564051458.json
name: Flux.3-Klein-文生图-bbox提示词增强扩写(UpSampler）_2115021845564051458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.3-Klein-文生图-bbox提示词增强扩写(UpSampler）_2115021845564051458.json
hash: 03819049ffa4b91b
coverage: 0.85
learned_at: 2026-10-30 17:54:21
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, VAEDecode, KSampler, CLIPTextEncode, EmptyFlux2LatentImage, PreviewAny, CreateBoundingBoxes, Flux3LayoutPrompt, SaveImage, TextGenerate, CLIPLoader, ComfyNotNode, Switch string [Crystools], PrimitiveBoolean, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, ShowAnything|Mie]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 410274412832257, "steps": 16}
---

# 图片生成/文生图/Flux.3-Klein-文生图-bbox提示词增强扩写(UpSampler）_2115021845564051458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.3-Klein-文生图-bbox提示词增强扩写(UpSampler）_2115021845564051458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `PreviewAny`
- `CreateBoundingBoxes`
- `Flux3LayoutPrompt`
- `SaveImage`
- `TextGenerate`
- `CLIPLoader`
- `ComfyNotNode`
- `Switch string [Crystools]`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `ShowAnything|Mie`

## 关键参数

- `seed` = `410274412832257`
- `steps` = `16`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`EmptyFlux2LatentImage`、`CreateBoundingBoxes`、`Flux3LayoutPrompt`、`SaveImage`、`TextGenerate`、`ComfyNotNode`、`Switch string [Crystools]`、`PrimitiveBoolean`、`ShowAnything|Mie`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、EmptyFlux2LatentImage
