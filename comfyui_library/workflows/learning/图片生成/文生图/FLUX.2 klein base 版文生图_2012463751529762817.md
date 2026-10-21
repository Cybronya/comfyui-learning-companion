---
key: 图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json
name: FLUX.2 klein base 版文生图_2012463751529762817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json
hash: 7d35a289665276c7
coverage: 0.8125
learned_at: 2026-10-19 22:14:58
nodes: [PrimitiveInt, PrimitiveInt, VAELoader, SamplerCustomAdvanced, CLIPTextEncode, CLIPLoader, CFGGuider, CLIPTextEncode, EmptyFlux2LatentImage, VAEDecode, RandomNoise, KSamplerSelect, Flux2Scheduler, SaveImage, PrimitiveStringMultiline, UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SaveImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAELoader`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`CLIPLoader`、`CFGGuider`、`EmptyFlux2LatentImage`、`VAEDecode`、`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`SaveImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
