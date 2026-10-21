---
key: 图片生成/文生图/Flux2.Klein基础文生图工作流_2014585003874717698.json
name: Flux2.Klein基础文生图工作流_2014585003874717698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2.Klein基础文生图工作流_2014585003874717698.json
hash: f359525e2a420b69
coverage: 0.823529
learned_at: 2026-10-19 22:15:08
nodes: [KSamplerSelect, SamplerCustomAdvanced, CLIPTextEncode, VAELoader, CLIPTextEncode, PrimitiveInt, PrimitiveInt, VAEDecode, Flux2Scheduler, easy promptList, EmptyFlux2LatentImage, SaveImage, UNETLoader, CLIPLoader, CFGGuider, RandomNoise, Note]
patterns: []
missing: []
---

# 图片生成/文生图/Flux2.Klein基础文生图工作流_2014585003874717698.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2.Klein基础文生图工作流_2014585003874717698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `easy promptList`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CFGGuider`
- `RandomNoise`
- `Note`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`Flux2Scheduler`、`easy promptList`、`EmptyFlux2LatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`CFGGuider`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
