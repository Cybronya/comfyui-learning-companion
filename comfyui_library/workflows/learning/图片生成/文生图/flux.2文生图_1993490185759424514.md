---
key: 图片生成/文生图/flux.2文生图_1993490185759424514.json
name: flux.2文生图_1993490185759424514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux.2文生图_1993490185759424514.json
hash: 617fe6a41dcd63e5
coverage: 1
learned_at: 2026-10-19 21:33:11
nodes: [RandomNoise, KSamplerSelect, EmptyFlux2LatentImage, FluxGuidance, BasicGuider, SamplerCustomAdvanced, VAEDecode, SaveImage, CLIPTextEncode, VAELoader, CLIPLoader, UNETLoader, Flux2Scheduler, ImpactInt, ImpactInt, RH_Translator]
patterns: []
missing: []
---

# 图片生成/文生图/flux.2文生图_1993490185759424514.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux.2文生图_1993490185759424514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `FluxGuidance`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Flux2Scheduler`
- `ImpactInt`
- `ImpactInt`
- `RH_Translator`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`RandomNoise`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`FluxGuidance`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`Flux2Scheduler`、`ImpactInt`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
