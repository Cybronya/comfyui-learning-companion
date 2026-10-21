---
key: 图片生成/文生图/flux2.klein官方文生图工作流_2042509850478907393.json
name: flux2.klein官方文生图工作流_2042509850478907393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux2.klein官方文生图工作流_2042509850478907393.json
hash: de0732a4d855c945
coverage: 0.8125
learned_at: 2026-10-21 02:56:50
nodes: [MarkdownNote, SamplerCustomAdvanced, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, PrimitiveStringMultiline, RandomNoise, CFGGuider, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, CFGGuider, RandomNoise, ConditioningZeroOut, VAEDecode, SaveImage, KSamplerSelect, Flux2Scheduler, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/flux2.klein官方文生图工作流_2042509850478907393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux2.klein官方文生图工作流_2042509850478907393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `RandomNoise`
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SaveImage`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`SamplerCustomAdvanced`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`CFGGuider`、`EmptyFlux2LatentImage`、`VAEDecode`、`Flux2Scheduler`、`KSamplerSelect`、`ConditioningZeroOut`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
