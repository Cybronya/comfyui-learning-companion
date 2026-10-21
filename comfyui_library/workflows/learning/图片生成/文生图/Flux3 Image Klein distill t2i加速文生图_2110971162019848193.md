---
key: 图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json
name: Flux3 Image Klein distill t2i加速文生图_2110971162019848193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json
hash: a7bec4e30d4a4dd0
coverage: 0.684211
learned_at: 2026-10-21 02:52:15
nodes: [SaveImage, PrimitiveStringMultiline, TextGenerate, UNETLoader, CLIPTextEncode, CLIPLoader, KSampler, VAELoader, PreviewAny, EmptyFlux2LatentImage, CLIPTextEncode, VAEDecode, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, ComfySwitchNode, ComfySwitchNode, Ideogram4PromptBuilderKJ, PreviewAny]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 77472862623513, "steps": 16}
---

# 图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `SaveImage`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `PreviewAny`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `Ideogram4PromptBuilderKJ`
- `PreviewAny`

## 关键参数

- `seed` = `77472862623513`
- `steps` = `16`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（13/19）

**有卡**：`SaveImage`、`TextGenerate`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`KSampler`、`VAELoader`、`EmptyFlux2LatentImage`、`VAEDecode`、`ResolutionSelector`、`Ideogram4PromptBuilderKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、EmptyFlux2LatentImage
