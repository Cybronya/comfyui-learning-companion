---
key: 图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json
name: Flux.2 Klein 9B二次元CG动漫_2025780362521088001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json
hash: 933ced8982c275e8
coverage: 1
learned_at: 2026-10-19 22:29:40
nodes: [Int Literal, FluxGuidance, Flux2Scheduler, KSamplerSelect, BasicGuider, RandomNoise, CLIPLoader, VAELoader, SamplerCustomAdvanced, EmptyFlux2LatentImage, VAEDecode, CompressImages, SaveImage, UNETLoader, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `Int Literal`
- `FluxGuidance`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `CompressImages`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **100%**（15/15）

**有卡**：`Int Literal`、`FluxGuidance`、`Flux2Scheduler`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`VAEDecode`、`CompressImages`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
