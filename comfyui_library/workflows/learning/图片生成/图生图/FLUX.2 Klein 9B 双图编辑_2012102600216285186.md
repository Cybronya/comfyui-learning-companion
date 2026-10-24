---
key: 图片生成/图生图/FLUX.2 Klein 9B 双图编辑_2012102600216285186.json
name: FLUX.2 Klein 9B 双图编辑_2012102600216285186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 9B 双图编辑_2012102600216285186.json
hash: 9ac7885a04b60c71
coverage: 1
learned_at: 2026-10-23 10:54:05
nodes: [Flux2Scheduler, BasicGuider, VAELoader, FluxGuidance, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, UNETLoader, SaveImage, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, EmptyFlux2LatentImage, VAEDecode, Int, CLIPTextEncode, LoadImage, LoadImage, Int, Int, CLIPLoader]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 Klein 9B 双图编辑_2012102600216285186.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 9B 双图编辑_2012102600216285186.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAELoader`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `Int`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `Int`
- `Int`
- `CLIPLoader`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAELoader`、`FluxGuidance`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`UNETLoader`、`SaveImage`、`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`VAEDecode`、`Int`、`CLIPTextEncode`、`LoadImage`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
