---
key: 图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json
name: FLUX.2 Klein 9B 文生图_2012074303356936193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json
hash: 1639cb0317018d3e
coverage: 1
learned_at: 2026-10-19 22:14:57
nodes: [BasicGuider, KSamplerSelect, VAELoader, VAEDecode, EmptyFlux2LatentImage, RandomNoise, Flux2Scheduler, SaveImage, SamplerCustomAdvanced, FluxGuidance, CLIPLoader, UNETLoader, CLIPTextEncode, Int Literal]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `Flux2Scheduler`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Int Literal`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAELoader`、`VAEDecode`、`EmptyFlux2LatentImage`、`RandomNoise`、`Flux2Scheduler`、`SaveImage`、`SamplerCustomAdvanced`、`FluxGuidance`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`Int Literal`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
