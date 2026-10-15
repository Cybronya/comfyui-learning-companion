---
key: 视频生成/文生视频/flux klein4B 工作流 浮云1.17_2012350472430034946.json
name: flux klein4B 工作流 浮云1.17_2012350472430034946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/flux klein4B 工作流 浮云1.17_2012350472430034946.json
hash: 9b3e390513d7aaff
coverage: 0.8125
learned_at: 2026-10-15 22:47:19
nodes: [KSamplerSelect, SamplerCustomAdvanced, EmptyFlux2LatentImage, UNETLoader, CLIPLoader, VAELoader, CFGGuider, ConditioningZeroOut, CLIPTextEncode, Flux2Scheduler, VAEDecode, PrimitiveInt, PrimitiveInt, RandomNoise, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: []
---

# 视频生成/文生视频/flux klein4B 工作流 浮云1.17_2012350472430034946.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/flux klein4B 工作流 浮云1.17_2012350472430034946.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `SaveImage`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`ConditioningZeroOut`、`CLIPTextEncode`、`Flux2Scheduler`、`VAEDecode`、`RandomNoise`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
