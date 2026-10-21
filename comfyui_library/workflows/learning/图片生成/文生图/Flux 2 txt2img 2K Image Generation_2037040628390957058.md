---
key: 图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json
name: Flux 2 txt2img 2K Image Generation_2037040628390957058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json
hash: af8bfd7ca8d28d3d
coverage: 0.909091
learned_at: 2026-10-21 02:52:02
nodes: [FluxGuidance, KSampler, VAEDecode, ConditioningZeroOut, SaveImage, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, MarkdownNote, EmptyFlux2LatentImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 460356357862874, "steps": 20}
---

# 图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `EmptyFlux2LatentImage`

## 关键参数

- `seed` = `460356357862874`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`FluxGuidance`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyFlux2LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、FluxGuidance
