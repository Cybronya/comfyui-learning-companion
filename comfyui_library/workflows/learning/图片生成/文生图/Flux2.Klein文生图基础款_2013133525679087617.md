---
key: 图片生成/文生图/Flux2.Klein文生图基础款_2013133525679087617.json
name: Flux2.Klein文生图基础款_2013133525679087617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2.Klein文生图基础款_2013133525679087617.json
hash: 9c310d61c4e0e6da
coverage: 0.823529
learned_at: 2026-10-19 22:15:09
nodes: [KSamplerSelect, SamplerCustomAdvanced, EmptyFlux2LatentImage, PrimitiveInt, PrimitiveInt, UNETLoader, VAELoader, CFGGuider, ConditioningZeroOut, CLIPTextEncode, Flux2Scheduler, VAEDecode, RandomNoise, CLIPLoader, AddLabel, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/文生图/Flux2.Klein文生图基础款_2013133525679087617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2.Klein文生图基础款_2013133525679087617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `CFGGuider`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `RandomNoise`
- `CLIPLoader`
- `AddLabel`
- `SaveImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`UNETLoader`、`VAELoader`、`CFGGuider`、`ConditioningZeroOut`、`CLIPTextEncode`、`Flux2Scheduler`、`VAEDecode`、`RandomNoise`、`CLIPLoader`、`AddLabel`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
