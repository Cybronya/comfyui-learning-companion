---
key: 图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json
name: flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json
hash: 5762b2e1d4588ca1
coverage: 0.833333
learned_at: 2026-10-19 22:15:39
nodes: [KSamplerSelect, SamplerCustomAdvanced, EmptyFlux2LatentImage, UNETLoader, CLIPLoader, VAELoader, CFGGuider, ConditioningZeroOut, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, ConditioningZeroOut, CLIPTextEncode, CFGGuider, Flux2Scheduler, AddLabel, VAEDecode, VAEDecode, UNETLoader, CLIPLoader, VAELoader, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, EmptyFlux2LatentImage, SaveImage, AddLabel, SamplerCustomAdvanced, PrimitiveStringMultiline, SaveImage, SaveImage, PrimitiveStringMultiline, ImageConcatMulti, RandomNoise, RandomNoise]
patterns: []
missing: []
---

# 图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
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
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `AddLabel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `AddLabel`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`
- `SaveImage`
- `PrimitiveStringMultiline`
- `ImageConcatMulti`
- `RandomNoise`
- `RandomNoise`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`ConditioningZeroOut`、`CLIPTextEncode`、`Flux2Scheduler`、`AddLabel`、`VAEDecode`、`SaveImage`、`ImageConcatMulti`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
