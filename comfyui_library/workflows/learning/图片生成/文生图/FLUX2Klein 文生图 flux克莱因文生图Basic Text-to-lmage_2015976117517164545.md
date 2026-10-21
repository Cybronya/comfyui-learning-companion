---
key: 图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json
name: FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json
hash: 743c695671b7c364
coverage: 0.944444
learned_at: 2026-10-19 22:15:00
nodes: [KSamplerSelect, VAELoader, CFGGuider, Flux2Scheduler, Seed (rgthree), VAEDecode, SamplerCustomAdvanced, EmptyFlux2LatentImage, RandomNoise, SaveImage, easy int, easy int, CLIPTextEncode, PrimitiveStringMultiline, UNETLoader, CLIPTextEncode, CLIPLoader, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `KSamplerSelect` ★核心
- `VAELoader`
- `CFGGuider`
- `Flux2Scheduler`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SaveImage`
- `easy int`
- `easy int`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **94%**（17/18）

**有卡**：`KSamplerSelect`、`VAELoader`、`CFGGuider`、`Flux2Scheduler`、`Seed (rgthree)`、`VAEDecode`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`RandomNoise`、`SaveImage`、`easy int`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect
