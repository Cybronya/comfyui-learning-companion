---
key: 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169.json
name: Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169.json
hash: 314ad86f63f67d48
coverage: 0.866667
learned_at: 2026-10-19 22:15:01
nodes: [KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, CLIPTextEncode, PrimitiveInt, PrimitiveInt, RandomNoise, CLIPLoader, VAELoader, SaveImage, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
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

## 知识

覆盖率 **87%**（13/15）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SaveImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
