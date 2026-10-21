---
key: 图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json
name: flux klein9B 工作流 浮云1.19_2013089641938817026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json
hash: a819b5b3091ee7cc
coverage: 0.8125
learned_at: 2026-10-19 22:15:39
nodes: [KSamplerSelect, ConditioningZeroOut, CLIPTextEncode, CFGGuider, Flux2Scheduler, UNETLoader, CLIPLoader, VAELoader, PrimitiveInt, PrimitiveInt, EmptyFlux2LatentImage, SaveImage, SamplerCustomAdvanced, RandomNoise, PrimitiveStringMultiline, VAEDecode]
patterns: []
missing: []
---

# 图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSamplerSelect`、`ConditioningZeroOut`、`CLIPTextEncode`、`CFGGuider`、`Flux2Scheduler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyFlux2LatentImage`、`SaveImage`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
