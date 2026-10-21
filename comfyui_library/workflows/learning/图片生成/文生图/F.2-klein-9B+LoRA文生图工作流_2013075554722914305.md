---
key: 图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json
name: F.2-klein-9B+LoRA文生图工作流_2013075554722914305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json
hash: d801e6bc2eba8f35
coverage: 0.875
learned_at: 2026-10-19 22:14:56
nodes: [CLIPTextEncode, RandomNoise, KSamplerSelect, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, Flux2Scheduler, CFGGuider, CLIPTextEncode, VAEDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `Flux2Scheduler`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPTextEncode`、`RandomNoise`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`Flux2Scheduler`、`CFGGuider`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect
