---
key: 图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json
name: Flux.2 Klein 9B满血版文生图_2066862519515435010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json
hash: 74193a1956877f5a
coverage: 1
learned_at: 2026-10-19 23:21:22
nodes: [CLIPLoader, VAELoader, BasicGuider, SamplerCustomAdvanced, RandomNoise, EmptyFlux2LatentImage, KSamplerSelect, FluxGuidance, Flux2Scheduler, UNETLoader, CLIPTextEncode, CompressImages, SaveImage, VAEDecode]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CompressImages`
- `SaveImage`
- `VAEDecode` ★核心

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPLoader`、`VAELoader`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`FluxGuidance`、`Flux2Scheduler`、`UNETLoader`、`CLIPTextEncode`、`CompressImages`、`SaveImage`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
