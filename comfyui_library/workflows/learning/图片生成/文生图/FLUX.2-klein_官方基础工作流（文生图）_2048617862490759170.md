---
key: 图片生成/文生图/FLUX.2-klein_官方基础工作流（文生图）_2048617862490759170.json
name: FLUX.2-klein_官方基础工作流（文生图）_2048617862490759170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2-klein_官方基础工作流（文生图）_2048617862490759170.json
hash: 677ac8e317c91a51
coverage: 0.941176
learned_at: 2026-10-21 02:51:49
nodes: [VAELoader, KSamplerSelect, CLIPTextEncode, Int, Int, Flux2Scheduler, CLIPTextEncode, CFGGuider, VAEDecode, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, VAELoader, KSamplerSelect, CLIPTextEncode, Int, Int, Flux2Scheduler, CLIPTextEncode, CFGGuider, VAEDecode, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, CLIPLoader, CLIPLoader, Note, Note, UNETLoader, UNETLoader, CR Prompt Text, CR Prompt Text, SaveImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2-klein_官方基础工作流（文生图）_2048617862490759170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2-klein_官方基础工作流（文生图）_2048617862490759170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `VAELoader`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `SaveImage`
- `SaveImage`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`VAELoader`、`KSamplerSelect`、`CLIPTextEncode`、`Int`、`Flux2Scheduler`、`CFGGuider`、`VAEDecode`、`EmptyFlux2LatentImage`、`RandomNoise`、`SamplerCustomAdvanced`、`CLIPLoader`、`UNETLoader`、`CR Prompt Text`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
