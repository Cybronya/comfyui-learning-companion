---
key: 图片生成/文生图/Flux.2-Klein 文生图_2012020733546860545.json
name: Flux.2-Klein 文生图_2012020733546860545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2-Klein 文生图_2012020733546860545.json
hash: 30b477ec8304450e
coverage: 0.8125
learned_at: 2026-10-19 22:00:31
nodes: [KSamplerSelect, EmptyFlux2LatentImage, PrimitiveInt, RandomNoise, UNETLoader, CLIPLoader, VAELoader, CFGGuider, ConditioningZeroOut, CLIPTextEncode, Flux2Scheduler, SamplerCustomAdvanced, VAEDecode, SaveImage, PrimitiveInt, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2-Klein 文生图_2012020733546860545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2-Klein 文生图_2012020733546860545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `PrimitiveInt`
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSamplerSelect`、`EmptyFlux2LatentImage`、`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`ConditioningZeroOut`、`CLIPTextEncode`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
