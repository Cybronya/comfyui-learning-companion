---
key: 图片生成/文生图/Flux.2-Klein 文生图-模板_2090689443601666049.json
name: Flux.2-Klein 文生图-模板_2090689443601666049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2-Klein 文生图-模板_2090689443601666049.json
hash: c110ad182dad6d0c
coverage: 0.8125
learned_at: 2026-10-20 00:58:45
nodes: [KSamplerSelect, EmptyFlux2LatentImage, RandomNoise, CFGGuider, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader, CLIPTextEncode, Flux2Scheduler, CLIPTextEncode, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, CLIPLoader, UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2-Klein 文生图-模板_2090689443601666049.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2-Klein 文生图-模板_2090689443601666049.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPLoader`
- `UNETLoader` ★核心

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSamplerSelect`、`EmptyFlux2LatentImage`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`SaveImage`、`VAEDecode`、`VAELoader`、`CLIPTextEncode`、`Flux2Scheduler`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
