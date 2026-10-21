---
key: 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538.json
name: Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538.json
hash: 878f2400f473ff42
coverage: 0.866667
learned_at: 2026-10-19 22:15:01
nodes: [KSamplerSelect, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, CLIPTextEncode, PrimitiveInt, PrimitiveInt, RandomNoise, CLIPLoader, VAELoader, SaveImage, CLIPTextEncode, UNETLoader, CFGGuider, Flux2Scheduler]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CFGGuider`
- `Flux2Scheduler`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SaveImage`、`UNETLoader`、`CFGGuider`、`Flux2Scheduler`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
