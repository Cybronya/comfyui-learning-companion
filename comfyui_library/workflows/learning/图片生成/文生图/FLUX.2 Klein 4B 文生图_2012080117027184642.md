---
key: 图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json
name: FLUX.2 Klein 4B 文生图_2012080117027184642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json
hash: dd2be26b96391af1
coverage: 1
learned_at: 2026-10-19 22:14:57
nodes: [BasicGuider, KSamplerSelect, VAELoader, VAEDecode, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, FluxGuidance, CLIPLoader, CLIPTextEncode, UNETLoader, SaveImage, Flux2Scheduler, Int Literal]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `Flux2Scheduler`
- `Int Literal`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAELoader`、`VAEDecode`、`EmptyFlux2LatentImage`、`RandomNoise`、`SamplerCustomAdvanced`、`FluxGuidance`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`SaveImage`、`Flux2Scheduler`、`Int Literal`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
