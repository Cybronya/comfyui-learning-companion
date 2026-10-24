---
key: 图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json
name: Flux3 Image Klein distill t2i加速图生图_2110971174585978882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json
hash: 73bba0ed458718d3
coverage: 0.761905
learned_at: 2026-10-23 11:01:26
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, KSampler, VAEDecode, SaveImage, ReferenceMultiLatent, MarkdownNote, EmptyFlux2LatentImage, TextGenerate, PrimitiveStringMultiline, BatchImagesNode, ComfySwitchNode, PreviewAny, CLIPTextEncode, UNETLoader, LoadImage, LoadImage, LoadImage, CLIPLoader, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 62872500709123, "steps": 16}
---

# 图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ReferenceMultiLatent`
- `MarkdownNote`
- `EmptyFlux2LatentImage`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `BatchImagesNode`
- `ComfySwitchNode`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `62872500709123`
- `steps` = `16`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`ReferenceMultiLatent`、`EmptyFlux2LatentImage`、`TextGenerate`、`BatchImagesNode`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、EmptyFlux2LatentImage
