---
key: 图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json
name: Flux.2 Klein 9B_fp16文生图_2066061172897574913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json
hash: 9c73b64229177b3f
coverage: 1
learned_at: 2026-10-19 23:21:21
nodes: [BasicGuider, KSamplerSelect, SamplerCustomAdvanced, FluxGuidance, CLIPLoader, VAELoader, Int Literal, VAEDecode, RandomNoise, EmptyFlux2LatentImage, Flux2Scheduler, UNETLoader, CLIPTextEncode, SaveImage, CompressImages]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `CLIPLoader`
- `VAELoader`
- `Int Literal`
- `VAEDecode` ★核心
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CompressImages`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`FluxGuidance`、`CLIPLoader`、`VAELoader`、`Int Literal`、`VAEDecode`、`RandomNoise`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`UNETLoader`、`CLIPTextEncode`、`SaveImage`、`CompressImages`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
