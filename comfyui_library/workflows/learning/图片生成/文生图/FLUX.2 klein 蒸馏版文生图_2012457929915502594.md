---
key: 图片生成/文生图/FLUX.2 klein 蒸馏版文生图_2012457929915502594.json
name: FLUX.2 klein 蒸馏版文生图_2012457929915502594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 klein 蒸馏版文生图_2012457929915502594.json
hash: 37ffa3ca7bf5a5c5
coverage: 0.8125
learned_at: 2026-10-19 22:14:58
nodes: [SaveImage, PrimitiveInt, PrimitiveInt, Flux2Scheduler, PrimitiveStringMultiline, EmptyFlux2LatentImage, VAELoader, CLIPTextEncode, KSamplerSelect, RandomNoise, ConditioningZeroOut, VAEDecode, SamplerCustomAdvanced, CFGGuider, UNETLoader, CLIPLoader]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 klein 蒸馏版文生图_2012457929915502594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 klein 蒸馏版文生图_2012457929915502594.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `Flux2Scheduler`
- `PrimitiveStringMultiline`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`SaveImage`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`ConditioningZeroOut`、`VAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`UNETLoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
