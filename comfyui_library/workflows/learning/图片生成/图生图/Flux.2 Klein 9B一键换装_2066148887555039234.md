---
key: 图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json
name: Flux.2 Klein 9B一键换装_2066148887555039234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json
hash: 98d62f8736c31f00
coverage: 0.866667
learned_at: 2026-10-23 10:58:45
nodes: [SetNode, SetNode, GetNode, GetNode, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, VAEEncode, VAEEncode, Int, SamplerCustomAdvanced, VAELoader, CLIPLoader, RandomNoise, ReferenceLatent, CFGGuider, KSamplerSelect, Flux2Scheduler, ReferenceLatent, CLIPTextEncodeBREAK, EmptyFlux2LatentImage, ImageConcanate, VAEDecode, ImageConcanate, UNETLoader, LoadImage, SaveImage, SaveImage, LoadImage, Int]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `Int`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `RandomNoise`
- `ReferenceLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ReferenceLatent`
- `CLIPTextEncodeBREAK` ★核心
- `EmptyFlux2LatentImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `ImageConcanate`
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `Int`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`ReferenceLatent`、`ConditioningZeroOut`、`VAEEncode`、`Int`、`SamplerCustomAdvanced`、`VAELoader`、`CLIPLoader`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`CLIPTextEncodeBREAK`、`EmptyFlux2LatentImage`、`ImageConcanate`、`VAEDecode`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect
