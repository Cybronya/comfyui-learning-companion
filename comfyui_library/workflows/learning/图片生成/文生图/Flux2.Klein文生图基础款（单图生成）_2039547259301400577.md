---
key: 图片生成/文生图/Flux2.Klein文生图基础款（单图生成）_2039547259301400577.json
name: Flux2.Klein文生图基础款（单图生成）_2039547259301400577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2.Klein文生图基础款（单图生成）_2039547259301400577.json
hash: ea81d1be02e775c0
coverage: 0.8125
learned_at: 2026-10-21 02:52:13
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, CFGGuider, RandomNoise, KSamplerSelect, PrimitiveInt, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, PrimitiveInt, UNETLoader, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/Flux2.Klein文生图基础款（单图生成）_2039547259301400577.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2.Klein文生图基础款（单图生成）_2039547259301400577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PrimitiveInt`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`UNETLoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
