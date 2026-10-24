---
key: 图片生成/图生图/FLUX.2 Klein 4B 双图编辑_2012164713425145858.json
name: FLUX.2 Klein 4B 双图编辑_2012164713425145858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 4B 双图编辑_2012164713425145858.json
hash: e9d79ef716704887
coverage: 1
learned_at: 2026-10-23 10:54:05
nodes: [Flux2Scheduler, BasicGuider, VAELoader, FluxGuidance, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, SaveImage, VAEEncode, ReferenceLatent, ReferenceLatent, EmptyFlux2LatentImage, VAEDecode, UNETLoader, CLIPLoader, LoadImage, VAEEncode, Int, Int, Int, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 Klein 4B 双图编辑_2012164713425145858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 4B 双图编辑_2012164713425145858.json`

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
- `SaveImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `VAEEncode` ★核心
- `Int`
- `Int`
- `Int`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **100%**（22/22）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAELoader`、`FluxGuidance`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`SaveImage`、`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`Int`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
