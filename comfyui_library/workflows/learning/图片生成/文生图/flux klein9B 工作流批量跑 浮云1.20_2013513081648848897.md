---
key: 图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json
name: flux klein9B 工作流批量跑 浮云1.20_2013513081648848897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json
hash: 04f516f23e6e2fad
coverage: 0.791667
learned_at: 2026-10-19 22:15:39
nodes: [KSamplerSelect, CLIPTextEncode, CFGGuider, Flux2Scheduler, UNETLoader, CLIPLoader, VAELoader, PrimitiveInt, PrimitiveInt, SamplerCustomAdvanced, RandomNoise, VAEDecode, EmptyFlux2LatentImage, ConditioningZeroOut, SaveImage, SaveImage, RH_LLMAPI_NODE, PrimitiveStringMultiline, ProcessString, easy showAnything, easy promptLine, SaveImage, SaveImage, easy showAnything]
patterns: []
missing: []
---

# 图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `ConditioningZeroOut`
- `SaveImage`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `PrimitiveStringMultiline`
- `ProcessString`
- `easy showAnything`
- `easy promptLine`
- `SaveImage`
- `SaveImage`
- `easy showAnything`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`KSamplerSelect`、`CLIPTextEncode`、`CFGGuider`、`Flux2Scheduler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`EmptyFlux2LatentImage`、`ConditioningZeroOut`、`SaveImage`、`RH_LLMAPI_NODE`、`ProcessString`、`easy promptLine`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect
